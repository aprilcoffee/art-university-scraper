"""
Position extractor for German art university job pages.
Handles various page structures with flexible keyword matching.
"""
import re
from datetime import datetime
from typing import List, Optional
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

from .models import Position
from .detector import ContentDetector
from config.search_terms import POSITION_TYPES, EXCLUDE_PATTERNS


class PositionExtractor:
    """Extractor that handles various page structures."""

    def __init__(self, university_name: str, base_url: str):
        self.university_name = university_name
        self.base_url = base_url

    def extract_positions(self, soup: BeautifulSoup) -> List[Position]:
        """Extract all positions from a job page using multiple strategies."""
        positions = []
        content = ContentDetector.extract_main_content(soup) or soup
        text = content.get_text()
        language = ContentDetector.detect_language(text)

        # Strategy 1: Look for structured job listing containers
        positions.extend(self._extract_from_structured_listings(content, language))

        # Strategy 2: Look for links with job keywords
        if not positions:
            positions.extend(self._extract_from_job_links(content, language))

        # Strategy 3: Look for PDF job postings
        if not positions:
            positions.extend(self._extract_from_pdfs(content, language))

        # Strategy 4: Extract from tables (some universities use tables)
        if not positions:
            positions.extend(self._extract_from_tables(content, language))

        # Deduplicate by URL
        seen_urls = set()
        unique_positions = []
        for pos in positions:
            if pos.url not in seen_urls:
                seen_urls.add(pos.url)
                unique_positions.append(pos)

        return unique_positions

    def _extract_from_structured_listings(self, content: BeautifulSoup, language: str) -> List[Position]:
        """Extract from structured job listing containers."""
        positions = []

        # Look for various job listing patterns
        patterns = [
            ('div', {'class': re.compile(r'(job|stelle|position|vacancy).*list.*row', re.I)}),
            ('div', {'class': re.compile(r'job.*item', re.I)}),
            ('article', {'class': re.compile(r'job|position|stelle', re.I)}),
            ('li', {'class': re.compile(r'job|position|stelle', re.I)}),
        ]

        for tag_name, attrs in patterns:
            elements = content.find_all(tag_name, attrs, limit=50)
            for elem in elements:
                position = self._extract_from_element(elem, language)
                if position:
                    positions.append(position)

        return positions

    def _extract_from_element(self, element: Tag, language: str) -> Optional[Position]:
        """Extract position info from a single element."""
        text = element.get_text().strip()
        text_lower = text.lower()

        # Check if contains job keywords (more flexible)
        if not self._contains_job_keywords(text_lower):
            return None

        # Check for exclusion patterns
        if self._should_exclude(text_lower):
            return None

        # Extract title
        title = self._extract_title_from_element(element)
        if not title or len(title) < 10:
            return None

        # Extract URL
        url = self._extract_url_from_element(element)
        if not url:
            # If no direct URL, use the base page URL
            url = self.base_url

        # Determine position type
        position_type = self._determine_position_type(text_lower)

        return Position(
            university_name=self.university_name,
            title=title,
            url=url,
            position_type=position_type or 'other',
            description=self._extract_description(element),
            language=language,
            deadline=self._extract_deadline(text),
            department=self._extract_department(text),
            found_date=datetime.now().isoformat()
        )

    def _extract_from_job_links(self, content: BeautifulSoup, language: str) -> List[Position]:
        """Extract positions from links that contain job keywords."""
        positions = []

        for link in content.find_all('a', href=True):
            link_text = link.get_text().strip()
            link_href = link.get('href', '')

            # Skip very short links
            if len(link_text) < 10:
                continue

            combined_text = (link_text + ' ' + link_href).lower()

            # Check for job keywords
            if not self._contains_job_keywords(combined_text):
                continue

            # Check for exclusion patterns
            if self._should_exclude(combined_text):
                continue

            # Determine position type
            position_type = self._determine_position_type(combined_text)

            # Create position
            url = self._resolve_url(link_href)

            positions.append(Position(
                university_name=self.university_name,
                title=link_text[:200],
                url=url,
                position_type=position_type or 'other',
                language=language,
                found_date=datetime.now().isoformat()
            ))

        return positions

    def _extract_from_pdfs(self, content: BeautifulSoup, language: str) -> List[Position]:
        """Extract job positions from PDF links."""
        positions = []

        for link in content.find_all('a', href=re.compile(r'\.pdf$', re.I)):
            link_text = link.get_text().strip()
            combined_text = (link_text + ' ' + link.get('href', '')).lower()

            # Check for job keywords
            if not self._contains_job_keywords(combined_text):
                continue

            # Check for exclusion patterns
            if self._should_exclude(combined_text):
                continue

            position_type = self._determine_position_type(combined_text)

            positions.append(Position(
                university_name=self.university_name,
                title=link_text[:200] if link_text else 'Job posting (PDF)',
                url=self._resolve_url(link.get('href')),
                position_type=position_type or 'other',
                language=language,
                found_date=datetime.now().isoformat()
            ))

        return positions

    def _extract_from_tables(self, content: BeautifulSoup, language: str) -> List[Position]:
        """Extract positions from tables."""
        positions = []

        for table in content.find_all('table'):
            table_text = table.get_text().lower()

            if not self._contains_job_keywords(table_text):
                continue

            # Extract rows
            for row in table.find_all('tr'):
                row_text = row.get_text().strip()
                row_text_lower = row_text.lower()

                if len(row_text) < 20:
                    continue

                if not self._contains_job_keywords(row_text_lower):
                    continue

                if self._should_exclude(row_text_lower):
                    continue

                # Try to find a link in the row
                link = row.find('a', href=True)
                url = self._resolve_url(link.get('href')) if link else self.base_url

                position_type = self._determine_position_type(row_text_lower)

                # Try to extract title from first cell or link
                title = link.get_text().strip() if link else None
                if not title:
                    cells = row.find_all(['td', 'th'])
                    if cells:
                        title = cells[0].get_text().strip()

                if title and len(title) >= 10:
                    positions.append(Position(
                        university_name=self.university_name,
                        title=title[:200],
                        url=url,
                        position_type=position_type or 'other',
                        language=language,
                        found_date=datetime.now().isoformat()
                    ))

        return positions

    def _contains_job_keywords(self, text: str) -> bool:
        """Check if text contains any job-related keywords (flexible)."""
        keywords = [
            # German
            'mitarbeiter', 'wissenschaftliche', 'künstlerische', 'stelle',
            'ausschreibung', 'position', 'besetzung', 'teilzeit', 'vollzeit',
            'befristet', 'entgeltgruppe', 'tv-l', 'wiss.', 'künst.',
            'lehrkraft', 'dozent', 'professor', 'assistent',
            # English
            'position', 'staff', 'assistant', 'associate', 'researcher',
            'lecturer', 'professor', 'employment', 'vacancy'
        ]

        text_lower = text.lower()
        return any(keyword in text_lower for keyword in keywords)

    def _determine_position_type(self, text: str) -> Optional[str]:
        """Determine if position is wissenschaftliche or kuenstlerische."""
        text_lower = text.lower()

        # Check for wissenschaftliche
        wiss_keywords = ['wissenschaftliche', 'wiss.', 'research', 'forschung']
        if any(kw in text_lower for kw in wiss_keywords):
            return 'wissenschaftliche'

        # Check for künstlerische
        kunst_keywords = ['künstlerische', 'künst.', 'artistic', 'kunst']
        if any(kw in text_lower for kw in kunst_keywords):
            return 'kuenstlerische'

        return 'other'

    def _should_exclude(self, text: str) -> bool:
        """Check if content should be excluded."""
        return any(pattern.lower() in text for pattern in EXCLUDE_PATTERNS)

    def _extract_title_from_element(self, element: Tag) -> Optional[str]:
        """Extract title from element."""
        # Try to find title in headers
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5']:
            header = element.find(tag)
            if header:
                title = header.get_text().strip()
                if len(title) >= 10:
                    return title[:200]

        # Try div with 'title' class
        title_div = element.find(['div', 'span'], class_=re.compile(r'title', re.I))
        if title_div:
            title = title_div.get_text().strip()
            if len(title) >= 10:
                return title[:200]

        # Try first line of text
        text_lines = element.get_text().strip().split('\n')
        for line in text_lines:
            line = line.strip()
            if len(line) >= 10:
                return line[:200]

        return None

    def _extract_url_from_element(self, element: Tag) -> Optional[str]:
        """Extract URL from element."""
        # Check if element itself is a link
        if element.name == 'a' and element.get('href'):
            return self._resolve_url(element.get('href'))

        # Find first link in element
        link = element.find('a', href=True)
        if link:
            return self._resolve_url(link.get('href'))

        # Check for data-url or data-link attributes
        for attr in ['data-url', 'data-link', 'data-href']:
            if element.get(attr):
                return self._resolve_url(element.get(attr))

        return None

    def _extract_description(self, element: Tag) -> Optional[str]:
        """Extract job description."""
        text = element.get_text().strip()
        return (text[:500] + '...') if len(text) > 500 else text if len(text) > 20 else None

    def _extract_deadline(self, text: str) -> Optional[str]:
        """Extract deadline from text."""
        patterns = [
            r'bewerbungsfrist[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
            r'frist[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
            r'bis[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
            r'deadline[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.I)
            if match:
                return match.group(1)
        return None

    def _extract_department(self, text: str) -> Optional[str]:
        """Extract department from text."""
        match = re.search(r'(fakultät|faculty|department|institut)[:\s]+([a-zäöüß\s]+)', text, re.I)
        if match:
            dept = match.group(2).strip()
            return dept[:100] if len(dept) > 3 else None
        return None

    def _resolve_url(self, href: str) -> str:
        """Resolve relative URLs."""
        if not href:
            return self.base_url
        return href if href.startswith('http') else urljoin(self.base_url, href)
