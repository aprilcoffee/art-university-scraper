"""
Utility functions for the Art University Job Scraper
Consolidates repeated patterns and common operations
"""

import time
import json
from typing import Dict, List, Optional, Any
from bs4 import BeautifulSoup
from config import SEARCH_TERMS, DEPARTMENTS, ACADEMIC_POSITIONS, EMPLOYMENT_DETAILS


class PositionBuilder:
    """Builder class for creating position objects with consistent structure"""
    
    def __init__(self, university_name: str, language: str, url: str):
        self.university_name = university_name
        self.language = language
        self.url = url
        self.position_data = {
            'university': university_name,
            'language': language,
            'date_found': time.strftime('%Y-%m-%d'),
            'status': 'active'
        }
    
    def set_basic_info(self, position_type: str, title: str, description: str = '', url: str = None) -> 'PositionBuilder':
        """Set basic position information"""
        self.position_data.update({
            'position_type': position_type,
            'title': title,
            'description': description,
            'url': url or self.url
        })
        return self
    
    def set_category(self, category: str) -> 'PositionBuilder':
        """Set position category (phd_program or job_offer)"""
        self.position_data['position_category'] = category
        return self
    
    def add_metadata(self, soup: BeautifulSoup, text_content: str) -> 'PositionBuilder':
        """Add metadata like department, position level, employment details"""
        self.position_data.update({
            'department': self._extract_department(text_content),
            'position_level': self._classify_academic_position(
                self.position_data.get('title', ''), 
                self.position_data.get('description', '')
            ),
            'employment_details': self._extract_employment_details(text_content)
        })
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build and return the position dictionary"""
        return self.position_data.copy()
    
    def _extract_department(self, text_content: str) -> Optional[str]:
        """Extract department from text content"""
        departments = DEPARTMENTS.get(self.language, [])
        
        for dept in departments:
            if dept.lower() in text_content.lower():
                return dept
        return None
    
    def _classify_academic_position(self, title: str, description: str) -> str:
        """Classify academic position level"""
        text = f"{title} {description}".lower()
        positions = ACADEMIC_POSITIONS.get(self.language, {})
        
        for position_type, keywords in positions.items():
            if any(keyword.lower() in text for keyword in keywords):
                return position_type
        return 'unknown'
    
    def _extract_employment_details(self, text_content: str) -> Dict[str, str]:
        """Extract employment details from text"""
        details = {}
        employment_details = EMPLOYMENT_DETAILS.get(self.language, {})
        
        # Extract deadline
        deadline_patterns = employment_details.get('deadline', [])
        for pattern in deadline_patterns:
            if pattern.lower() in text_content.lower():
                deadline_text = self._extract_date_near_keyword(text_content, pattern)
                if deadline_text:
                    details['deadline'] = deadline_text
                    break
        
        # Extract employment type
        employment_types = employment_details.get('employment_type', [])
        for emp_type in employment_types:
            if emp_type.lower() in text_content.lower():
                details['employment_type'] = emp_type
                break
        
        # Extract salary information
        salary_patterns = employment_details.get('salary', [])
        for pattern in salary_patterns:
            if pattern.lower() in text_content.lower():
                salary_text = self._extract_salary_near_keyword(text_content, pattern)
                if salary_text:
                    details['salary'] = salary_text
                    break
        
        return details
    
    def _extract_date_near_keyword(self, text: str, keyword: str) -> Optional[str]:
        """Extract date information near a keyword"""
        import re
        
        keyword_pos = text.lower().find(keyword.lower())
        if keyword_pos == -1:
            return None
        
        # Extract text around the keyword (±200 characters)
        start = max(0, keyword_pos - 200)
        end = min(len(text), keyword_pos + 200)
        context = text[start:end]
        
        # Look for date patterns
        date_patterns = [
            r'\d{1,2}\.\d{1,2}\.\d{4}',  # DD.MM.YYYY
            r'\d{1,2}/\d{1,2}/\d{4}',    # DD/MM/YYYY
            r'\d{4}-\d{1,2}-\d{1,2}',    # YYYY-MM-DD
            r'\d{1,2}\.\s*\w+\s*\d{4}',  # DD. Month YYYY
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group()
        
        return None
    
    def _extract_salary_near_keyword(self, text: str, keyword: str) -> Optional[str]:
        """Extract salary information near a keyword"""
        import re
        
        keyword_pos = text.lower().find(keyword.lower())
        if keyword_pos == -1:
            return None
        
        # Extract text around the keyword (±100 characters)
        start = max(0, keyword_pos - 100)
        end = min(len(text), keyword_pos + 100)
        context = text[start:end]
        
        # Look for salary patterns
        salary_patterns = [
            r'TV-L\s*\d+',  # TV-L 13
            r'TVöD\s*\d+',  # TVöD 13
            r'Entgeltgruppe\s*\d+',  # Entgeltgruppe 13
            r'\d+\s*€',     # 3000 €
            r'\d+\.\d+\s*€', # 3.000 €
        ]
        
        for pattern in salary_patterns:
            match = re.search(pattern, context, re.IGNORECASE)
            if match:
                return match.group()
        
        return None


class URLResolver:
    """Utility class for resolving and converting URLs"""
    
    @staticmethod
    def make_full_url(href: str, current_url: str) -> str:
        """Convert relative URL to full URL"""
        if not href:
            return None
        
        # If it's already a full URL, return it
        if href.startswith(('http://', 'https://')):
            return href
        
        # Parse the current URL to get the base URL
        from urllib.parse import urljoin, urlparse
        
        # Use urljoin to properly combine URLs
        full_url = urljoin(current_url, href)
        
        # Validate that the URL is properly formed
        parsed = urlparse(full_url)
        if parsed.netloc:  # Has a domain
            return full_url
        
        return href
    
    @staticmethod
    def find_specific_url(soup: BeautifulSoup, university_name: str, current_url: str, url_type: str) -> Optional[str]:
        """Find specific URL for PhD programs or job postings"""
        if url_type == 'phd':
            return URLResolver._find_phd_program_url(soup, university_name, current_url)
        elif url_type == 'job':
            return URLResolver._find_job_posting_url(soup, university_name, current_url)
        return None
    
    @staticmethod
    def _find_phd_program_url(soup: BeautifulSoup, university_name: str, current_url: str) -> Optional[str]:
        """Find the specific PhD program URL"""
        # Look for PhD-related links
        phd_links = soup.find_all('a', href=True)
        
        for link in phd_links:
            href = link.get('href', '').lower()
            link_text = link.get_text().lower()
            
            # Check for PhD-related keywords in URL or text
            phd_keywords = [
                'phd', 'promotion', 'doktorand', 'doktorat', 'graduate', 'graduiertenschule',
                'doktorandenprogramm', 'promotionsprogramm', 'research', 'forschung'
            ]
            
            if any(keyword in href or keyword in link_text for keyword in phd_keywords):
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        # Look for PhD program sections
        phd_sections = soup.find_all(['section', 'div'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['phd', 'promotion', 'doktorand', 'graduate', 'research']))
        
        for section in phd_sections:
            section_links = section.find_all('a', href=True)
            for link in section_links:
                href = link.get('href', '')
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        return None
    
    @staticmethod
    def _find_job_posting_url(soup: BeautifulSoup, university_name: str, current_url: str) -> Optional[str]:
        """Find the specific job posting URL"""
        # Look for job-related links
        job_links = soup.find_all('a', href=True)
        
        for link in job_links:
            href = link.get('href', '').lower()
            link_text = link.get_text().lower()
            
            # Check for job-related keywords in URL or text
            job_keywords = [
                'stellenausschreibung', 'job', 'position', 'vacancy', 'career', 'karriere',
                'mitarbeiter', 'bewerbung', 'application', 'stellen', 'jobs'
            ]
            
            if any(keyword in href or keyword in link_text for keyword in job_keywords):
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        # Look for job posting sections
        job_sections = soup.find_all(['section', 'div'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['job', 'stellen', 'karriere', 'career', 'mitarbeiter']))
        
        for section in job_sections:
            section_links = section.find_all('a', href=True)
            for link in section_links:
                href = link.get('href', '')
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        return None


class TextProcessor:
    """Utility class for text processing operations"""
    
    @staticmethod
    def clean_job_title(title: str) -> str:
        """Clean and format job title"""
        if not title:
            return ""
        
        # Remove extra whitespace
        title = ' '.join(title.split())
        
        # Remove common prefixes/suffixes
        prefixes_to_remove = ['Stellenausschreibung:', 'Job:', 'Position:', 'Vacancy:']
        suffixes_to_remove = ['- Bewerbung', '- Application', '- Job', '- Position']
        
        for prefix in prefixes_to_remove:
            if title.startswith(prefix):
                title = title[len(prefix):].strip()
        
        for suffix in suffixes_to_remove:
            if title.endswith(suffix):
                title = title[:-len(suffix)].strip()
        
        # Limit length
        if len(title) > 100:
            title = title[:97] + "..."
        
        return title
    
    @staticmethod
    def clean_phd_title(title: str) -> str:
        """Clean and format PhD title"""
        if not title:
            return ""
        
        # Remove extra whitespace
        title = ' '.join(title.split())
        
        # Remove common prefixes
        prefixes_to_remove = ['PhD Program:', 'Doktorandenprogramm:', 'Promotionsprogramm:']
        
        for prefix in prefixes_to_remove:
            if title.startswith(prefix):
                title = title[len(prefix):].strip()
        
        # Limit length
        if len(title) > 120:
            title = title[:117] + "..."
        
        return title
    
    @staticmethod
    def clean_description(description: str) -> str:
        """Clean and format description text"""
        if not description:
            return ""
        
        # Remove extra whitespace and newlines
        description = ' '.join(description.split())
        
        # Limit length
        if len(description) > 500:
            description = description[:497] + "..."
        
        return description
    
    @staticmethod
    def is_job_title(text: str, found_terms: List[str]) -> bool:
        """Check if text looks like a job title"""
        if not text or len(text) > 150:
            return False
        
        # Check if it contains job-related terms
        job_indicators = [
            'mitarbeiter', 'assistant', 'coordinator', 'manager', 'director',
            'professor', 'lecturer', 'researcher', 'specialist', 'technician'
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in job_indicators)
    
    @staticmethod
    def is_phd_title(text: str, found_terms: List[str]) -> bool:
        """Check if text looks like a PhD title"""
        if not text or len(text) > 200:
            return False
        
        # Check if it contains PhD-related terms
        phd_indicators = [
            'phd', 'promotion', 'doktorand', 'doktorat', 'graduate',
            'doctorate', 'doctoral', 'research', 'forschung'
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in phd_indicators)


class DatabaseHelper:
    """Utility class for database operations"""
    
    @staticmethod
    def prepare_position_for_db(position_data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare position data for database insertion"""
        # Convert employment_details dict to JSON string
        if 'employment_details' in position_data and position_data['employment_details']:
            position_data['employment_details'] = json.dumps(position_data['employment_details'])
        
        return position_data
    
    @staticmethod
    def get_position_fields() -> List[str]:
        """Get list of position table fields"""
        return [
            'university', 'position_type', 'title', 'description', 'url', 
            'language', 'date_found', 'status', 'position_category', 
            'department', 'position_level', 'employment_details'
        ]


class SearchHelper:
    """Utility class for search operations"""
    
    @staticmethod
    def search_for_terms(text_content: str, terms: List[str]) -> List[str]:
        """Search for terms in text content"""
        found_terms = []
        text_lower = text_content.lower()
        
        for term in terms:
            if term.lower() in text_lower:
                found_terms.append(term)
        
        return found_terms
    
    @staticmethod
    def detect_language(text_content: str) -> str:
        """Detect language of text content"""
        text_lower = text_content.lower()
        
        # German indicators
        german_indicators = [
            'der', 'die', 'das', 'und', 'für', 'mit', 'von', 'zu', 'auf', 'in', 'an',
            'stellenausschreibung', 'bewerbung', 'promotion', 'doktorand', 'mitarbeiter',
            'wissenschaftliche', 'künstlerische', 'hochschule', 'universität', 'fakultät'
        ]
        
        # English indicators
        english_indicators = [
            'the', 'and', 'for', 'with', 'from', 'to', 'in', 'on', 'at',
            'job', 'position', 'vacancy', 'application', 'phd', 'graduate',
            'university', 'college', 'faculty', 'department', 'research'
        ]
        
        german_count = sum(1 for indicator in german_indicators if indicator in text_lower)
        english_count = sum(1 for indicator in english_indicators if indicator in text_lower)
        
        if german_count > english_count:
            return 'german'
        elif english_count > german_count:
            return 'english'
        else:
            return 'mixed'