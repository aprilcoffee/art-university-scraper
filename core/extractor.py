"""Position extractor for wissenschaftliche and künstlerische Mitarbeiter."""
import re
from datetime import datetime
from typing import List, Optional
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

from .models import Position
from .detector import ContentDetector
from config.search_terms import POSITION_TYPES, EXCLUDE_PATTERNS


class PositionExtractor:
    """Extracts job positions from pages."""

    def __init__(self, university_name: str, base_url: str):
        self.university_name = university_name
        self.base_url = base_url

    def extract_positions(self, soup: BeautifulSoup) -> List[Position]:
        """Extract all positions from a job page."""
        positions = []
        content = ContentDetector.extract_main_content(soup) or soup
        text = content.get_text()
        language = ContentDetector.detect_language(text)
        search_terms = self._get_search_terms(language)

        job_listings = self._find_job_listings(content)

        if job_listings:
            for listing in job_listings:
                position = self._extract_from_listing(listing, language, search_terms)
                if position:
                    positions.append(position)
        else:
            positions.extend(self._extract_from_full_text(content, language, search_terms))

        return positions

    def _get_search_terms(self, language: str):
        """Get search terms based on language."""
        terms = {}
        for pos_type, lang_terms in POSITION_TYPES.items():
            terms[pos_type] = lang_terms.get(language, lang_terms.get('german', []))
        return terms

    def _find_job_listings(self, soup: BeautifulSoup) -> List[Tag]:
        """Find job listing elements."""
        listings = []
        for tag, attrs in [('article', {}),
                          ('div', {'class': re.compile(r'(job|stelle|position)', re.I)}),
                          ('li', {'class': re.compile(r'(job|stelle)', re.I)})]:
            found = soup.find_all(tag, attrs, limit=50)
            if found:
                listings.extend(found)

        return listings if len(listings) >= 2 else soup.find_all('a', href=True, limit=50) if len(soup.find_all('a', href=True)) >= 2 else []

    def _extract_from_listing(self, listing: Tag, language: str, search_terms: dict) -> Optional[Position]:
        """Extract position from listing element."""
        text = listing.get_text().lower()
        position_type = self._match_position_type(text, search_terms)

        if not position_type or self._should_exclude(text):
            return None

        title = self._extract_title(listing)
        url = self._extract_url(listing)

        if not title or not url:
            return None

        return Position(
            university_name=self.university_name,
            title=title,
            url=url,
            position_type=position_type,
            description=self._extract_description(listing),
            language=language,
            deadline=self._extract_deadline(text),
            department=self._extract_department(text),
            found_date=datetime.now().isoformat()
        )

    def _extract_from_full_text(self, content: BeautifulSoup, language: str, search_terms: dict) -> List[Position]:
        """Extract positions from full page text."""
        positions = []
        text = content.get_text().lower()
        position_type = self._match_position_type(text, search_terms)

        if not position_type or self._should_exclude(text):
            return positions

        for link in content.find_all('a', href=True):
            link_text = link.get_text().strip()
            if self._match_position_type(link_text.lower(), search_terms):
                positions.append(Position(
                    university_name=self.university_name,
                    title=link_text[:200],
                    url=self._resolve_url(link.get('href')),
                    position_type=position_type,
                    language=language,
                    found_date=datetime.now().isoformat()
                ))
        return positions

    def _match_position_type(self, text: str, search_terms: dict) -> Optional[str]:
        """Match text to position type."""
        for pos_type, terms in search_terms.items():
            for term in terms:
                if term.lower() in text:
                    return 'wissenschaftliche' if 'wissenschaftliche' in pos_type else 'kuenstlerische'
        return None

    def _should_exclude(self, text: str) -> bool:
        """Check if content should be excluded."""
        return any(pattern.lower() in text for pattern in EXCLUDE_PATTERNS)

    def _extract_title(self, listing: Tag) -> Optional[str]:
        """Extract job title."""
        for tag, attrs in [('h1', {}), ('h2', {}), ('h3', {}), ('h4', {}),
                          ('div', {'class': re.compile(r'title', re.I)}),
                          ('strong', {}), ('b', {})]:
            element = listing.find(tag, attrs)
            if element and len(element.get_text().strip()) > 5:
                return element.get_text().strip()[:200]

        if listing.name == 'a':
            return listing.get_text().strip()[:200]

        first_line = listing.get_text().strip().split('\n')[0]
        return first_line[:200] if len(first_line) > 5 else None

    def _extract_url(self, listing: Tag) -> Optional[str]:
        """Extract job URL."""
        if listing.name == 'a' and listing.get('href'):
            return self._resolve_url(listing.get('href'))
        link = listing.find('a', href=True)
        return self._resolve_url(link.get('href')) if link else None

    def _extract_description(self, listing: Tag) -> Optional[str]:
        """Extract job description."""
        text = listing.get_text().strip()
        return (text[:500] + '...') if len(text) > 500 else text if len(text) > 20 else None

    def _extract_deadline(self, text: str) -> Optional[str]:
        """Extract deadline from text."""
        for pattern in [r'bewerbungsfrist[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
                       r'frist[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})',
                       r'bis[:\s]+(\d{1,2}[\./-]\d{1,2}[\./-]\d{2,4})']:
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
        return href if href.startswith('http') else urljoin(self.base_url, href)
