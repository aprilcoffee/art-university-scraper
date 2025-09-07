"""
Web scraper for art university job positions and PhD opportunities
"""

import requests
from bs4 import BeautifulSoup
import time
import logging
from typing import List, Dict, Optional, Set
from urllib.parse import urljoin, urlparse
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from config import UNIVERSITIES_BY_COUNTRY, UNIVERSITIES, SEARCH_TERMS, SCRAPING_CONFIG
from database import DatabaseManager
from utils import PositionBuilder, URLResolver, TextProcessor, SearchHelper, DatabaseHelper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ArtUniversityScraper:
    def __init__(self):
        self.db = DatabaseManager()
        self.session = requests.Session()
        self.session.headers.update(SCRAPING_CONFIG['headers'])
        self.session.headers['User-Agent'] = SCRAPING_CONFIG['user_agent']
        self.driver = None
        self.setup_selenium()
    
    def setup_selenium(self):
        """Setup Selenium WebDriver for JavaScript-heavy sites"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument(f'--user-agent={SCRAPING_CONFIG["user_agent"]}')
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            logger.info("Selenium WebDriver initialized successfully")
            
        except Exception as e:
            logger.error(f"Error setting up Selenium: {e}")
            self.driver = None
    
    def close_selenium(self):
        """Close Selenium WebDriver"""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def make_request(self, url: str, use_selenium: bool = False) -> Optional[BeautifulSoup]:
        """Make HTTP request and return BeautifulSoup object"""
        try:
            if use_selenium and self.driver:
                return self._scrape_with_selenium(url)
            else:
                response = self.session.get(url, timeout=SCRAPING_CONFIG['timeout'])
                response.raise_for_status()
                return BeautifulSoup(response.content, 'html.parser')
                
        except Exception as e:
            logger.error(f"Error making request to {url}: {e}")
            return None
    
    def _scrape_with_selenium(self, url: str) -> Optional[BeautifulSoup]:
        """Scrape page using Selenium for JavaScript-heavy content"""
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Wait a bit for dynamic content to load
            time.sleep(2)
            
            html = self.driver.page_source
            return BeautifulSoup(html, 'html.parser')
            
        except TimeoutException:
            logger.error(f"Timeout loading page: {url}")
            return None
        except Exception as e:
            logger.error(f"Error scraping with Selenium: {e}")
            return None
    
    def extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract clean text content from BeautifulSoup object"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def find_job_related_links(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Find links that might contain job postings"""
        job_keywords = [
            'stellenausschreibung', 'stelle', 'job', 'position', 'bewerbung',
            'career', 'employment', 'vacancy', 'opening', 'phd', 'promotion',
            'doctorate', 'graduate', 'research', 'karriere', 'stellenmarkt'
        ]
        
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            text = link.get_text().lower()
            
            # Check if link text or href contains job-related keywords
            if any(keyword in text or keyword in href.lower() for keyword in job_keywords):
                full_url = urljoin(base_url, href)
                links.append(full_url)
        
        return list(set(links))  # Remove duplicates
    
    def search_for_terms(self, text: str, terms: List[str]) -> List[str]:
        """Search for specific terms in text and return matches"""
        return SearchHelper.search_for_terms(text, terms)
    
    def extract_positions_from_page(self, soup: BeautifulSoup, url: str, university_name: str) -> List[Dict]:
        """Extract position information from a page"""
        positions = []
        text_content = self.extract_text_content(soup)
        
        # Enhanced language detection
        language = self._detect_language(text_content)
        
        # Search for both PhD programs and job positions
        phd_positions = self._extract_phd_programs(soup, text_content, language, university_name, url)
        job_positions = self._extract_job_offers(soup, text_content, language, university_name, url)
        
        # Also search for general job opportunities (mitarbeiter positions)
        general_job_positions = self._extract_general_job_opportunities_from_page(soup, text_content, language, university_name, url)
        
        positions.extend(phd_positions)
        positions.extend(job_positions)
        positions.extend(general_job_positions)
        
        return positions
    
    def _extract_phd_programs(self, soup: BeautifulSoup, text_content: str, language: str, university_name: str, url: str) -> List[Dict]:
        """Extract PhD program information"""
        positions = []
        
        # Search through PhD program categories
        for category, terms in SEARCH_TERMS[language]['phd_programs'].items():
            found_terms = self.search_for_terms(text_content, terms)
            
            if found_terms:
                position_info = self._extract_position_details(soup, found_terms, category, 'phd')
                
                for info in position_info:
                    # Get the specific PhD program URL if available
                    phd_url = info.get('url', url)
                    if not phd_url or phd_url == url:
                        phd_url = URLResolver.find_specific_url(soup, university_name, url, 'phd')
                    
                    # Create position using builder pattern
                    position = (PositionBuilder(university_name, language, url)
                               .set_basic_info(category, 
                                              info.get('title', f"{category.replace('_', ' ').title()} PhD Program"),
                                              info.get('description', ''),
                                              phd_url)
                               .set_category('phd_program')
                               .add_metadata(soup, text_content)
                               .build())
                    positions.append(position)
        
        return positions
    
    def _extract_job_offers(self, soup: BeautifulSoup, text_content: str, language: str, university_name: str, url: str) -> List[Dict]:
        """Extract job offer information"""
        positions = []
        
        # Search through job offer categories
        for category, terms in SEARCH_TERMS[language]['job_offers'].items():
            found_terms = self.search_for_terms(text_content, terms)
            
            if found_terms:
                position_info = self._extract_position_details(soup, found_terms, category, 'job')
                
                for info in position_info:
                    # Get the specific job posting URL if available
                    job_url = info.get('url', url)
                    if not job_url or job_url == url:
                        job_url = URLResolver.find_specific_url(soup, university_name, url, 'job')
                    
                    # Create position using builder pattern
                    position = (PositionBuilder(university_name, language, url)
                               .set_basic_info(category,
                                              info.get('title', f"{category.replace('_', ' ').title()} Position"),
                                              info.get('description', ''),
                                              job_url)
                               .set_category('job_offer')
                               .add_metadata(soup, text_content)
                               .build())
                    positions.append(position)
        
        return positions
    
    def _extract_general_job_opportunities_from_page(self, soup: BeautifulSoup, text_content: str, language: str, university_name: str, url: str) -> List[Dict]:
        """Extract general job opportunities from the entire page"""
        positions = []
        
        # Search through general job terms
        general_job_terms = SEARCH_TERMS[language]['job_offers']['general_jobs']
        found_terms = self.search_for_terms(text_content, general_job_terms)
        
        if found_terms:
            # Look for general job opportunities in the page
            general_jobs = self._extract_general_job_opportunities(soup, found_terms, url)
            
            for job_info in general_jobs:
                position = (PositionBuilder(university_name, language, url)
                           .set_basic_info('general_jobs',
                                          job_info.get('title', 'General Job Opportunity'),
                                          job_info.get('description', ''),
                                          job_info.get('url', url))
                           .set_category('job_offer')
                           .add_metadata(soup, text_content)
                           .build())
                positions.append(position)
        
        return positions[:5]  # Limit to 5 general job opportunities per page
    
    def _detect_language(self, text_content: str) -> str:
        """Enhanced language detection"""
        return SearchHelper.detect_language(text_content)
    
    def _extract_position_details(self, soup: BeautifulSoup, found_terms: List[str], category: str, position_type: str) -> List[Dict]:
        """Extract detailed position information with improved title extraction"""
        positions = []
        
        if position_type == 'phd':
            positions = self._extract_phd_details(soup, found_terms, category)
        elif position_type == 'job':
            positions = self._extract_job_details(soup, found_terms, category)
        
        # If no specific positions found, create generic position
        if not positions:
            positions.append({
                'title': f"{category.replace('_', ' ').title()} Opportunity",
                'description': f"Found {category.replace('_', ' ')} related content"
            })
        
        return positions
    
    def _extract_phd_details(self, soup: BeautifulSoup, found_terms: List[str], category: str) -> List[Dict]:
        """Extract PhD program details"""
        positions = []
        
        # Look for PhD-specific headings and content
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        for heading in headings:
            heading_text = heading.get_text().strip()
            
            # Check if heading contains PhD-related terms
            if any(term.lower() in heading_text.lower() for term in found_terms):
                description = self._find_description_near_heading(heading)
                
                # Clean up the title to be more concise
                clean_title = self._clean_phd_title(heading_text)
                
                positions.append({
                    'title': clean_title,
                    'description': description
                })
        
        return positions[:3]  # Limit to 3 PhD programs per page
    
    def _extract_job_details(self, soup: BeautifulSoup, found_terms: List[str], category: str) -> List[Dict]:
        """Extract job offer details with improved title extraction"""
        positions = []
        
        # Look for job posting patterns with art/academic-focused search terms
        job_elements = soup.find_all(['div', 'section', 'article', 'li'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['job', 'position', 'stelle', 'ausschreibung', 'bewerbung', 'mitarbeiter',
                                                            'vacancy', 'employment', 'career', 'coordinator', 'manager', 'director',
                                                            'specialist', 'curator', 'educator', 'freelance', 'contract', 'temporary']))
        
        for element in job_elements:
            element_text = element.get_text().strip()
            
            # Skip inactive job postings
            if self._is_inactive_job_posting(element_text):
                continue
            
            if any(term.lower() in element_text.lower() for term in found_terms):
                # Try to extract a clean job title
                job_title = self._extract_job_title(element, found_terms)
                
                if job_title:
                    # Try to find the specific job posting URL
                    job_url = self._find_specific_job_url(element, url)
                    
                    positions.append({
                        'title': job_title,
                        'description': self._clean_job_description(element_text),
                        'url': job_url
                    })
        
        # Also look in headings for job titles
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        for heading in headings:
            heading_text = heading.get_text().strip()
            
            # Skip inactive job postings
            if self._is_inactive_job_posting(heading_text):
                continue
            
            if any(term.lower() in heading_text.lower() for term in found_terms):
                # Check if this looks like a job title
                if self._is_job_title(heading_text, found_terms):
                    description = self._find_description_near_heading(heading)
                    
                    # Try to find the specific job posting URL
                    job_url = self._find_specific_job_url(heading, url)
                    
                    positions.append({
                        'title': self._clean_job_title(heading_text),
                        'description': description,
                        'url': job_url
                    })
        
        # Also look for general job opportunities in broader contexts
        general_jobs = self._extract_general_job_opportunities(soup, found_terms, url)
        positions.extend(general_jobs)
        
        return positions[:8]  # Limit to 8 job positions per page (increased for better coverage)
    
    def _is_inactive_job_posting(self, text: str) -> bool:
        """Check if this is an inactive job posting"""
        inactive_indicators = [
            'aktuelle stellenausschreibungen',
            'current job postings',
            'archiv',
            'archive',
            'abgeschlossen',
            'completed',
            'beendet',
            'ended',
            'vergangen',
            'past',
            'nicht mehr aktiv',
            'no longer active',
            'ausgelaufen',
            'expired',
            'bewerbungsfrist abgelaufen',
            'application deadline passed'
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in inactive_indicators)
    
    def _is_non_position_content(self, text: str) -> bool:
        """Check if this content is not about job positions (exhibitions, research catalogues, etc.)"""
        non_position_indicators = [
            'exhibition', 'ausstellung', 'expo', 'show', 'schau',
            'research catalogue', 'forschungsverzeichnis', 'research catalog',
            'publication', 'publikation', 'book', 'buch', 'journal', 'zeitschrift',
            'event', 'veranstaltung', 'conference', 'konferenz', 'symposium',
            'gallery', 'galerie', 'museum', 'collection', 'sammlung',
            'student work', 'studentenarbeit', 'student project', 'studentenprojekt',
            'graduation', 'absolvent', 'alumni', 'alumnus',
            'news', 'nachrichten', 'announcement', 'ankündigung',
            'program', 'programm', 'course', 'kurs', 'workshop',
            'visit', 'besuch', 'opening', 'eröffnung', 'closing', 'schließung'
        ]
        
        text_lower = text.lower()
        
        # If the text contains multiple non-position indicators, it's likely not a job posting
        non_position_count = sum(1 for indicator in non_position_indicators if indicator in text_lower)
        
        # Also check for specific patterns that indicate non-position content
        non_position_patterns = [
            r'exhibition.*opening',
            r'research.*catalogue',
            r'student.*work',
            r'graduation.*show',
            r'publication.*release',
            r'event.*announcement'
        ]
        
        import re
        pattern_matches = sum(1 for pattern in non_position_patterns if re.search(pattern, text_lower))
        
        # Consider it non-position content if it has multiple indicators or pattern matches
        return non_position_count >= 2 or pattern_matches >= 1
    
    def _extract_general_job_opportunities(self, soup: BeautifulSoup, found_terms: List[str], current_url: str) -> List[Dict]:
        """Extract general job opportunities from broader page content"""
        positions = []
        
        # Look for job-related sections and pages (more specific job-focused terms)
        job_sections = soup.find_all(['section', 'div', 'article'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['karriere', 'career', 'jobs', 'stellen', 'positions',
                                                            'mitarbeiter', 'bewerbung', 'application', 'ausschreibung', 'vacancy',
                                                            'lehre', 'teaching', 'employment', 'recruitment']))
        
        for section in job_sections:
            section_text = section.get_text().strip()
            
            # Skip inactive sections
            if self._is_inactive_job_posting(section_text):
                continue
            
            # Skip non-position content like exhibitions, research catalogues, etc.
            if self._is_non_position_content(section_text):
                continue
            
            # Look for job listings within the section
            job_listings = section.find_all(['li', 'div', 'p'], 
                                         string=lambda text: text and any(term.lower() in text.lower() for term in found_terms))
            
            for listing in job_listings:
                listing_text = listing.get_text().strip()
                
                if any(term.lower() in listing_text.lower() for term in found_terms):
                    # Try to extract job title from the listing
                    job_title = self._extract_job_title_from_listing(listing)
                    
                    if job_title:
                        # Try to find the specific job URL
                        job_url = self._find_specific_job_url(listing, url)
                        
                        positions.append({
                            'title': job_title,
                            'description': self._clean_job_description(listing_text),
                            'url': job_url
                        })
        
        # Look for job-related links (art/academic focused)
        job_links = soup.find_all('a', href=lambda x: x and any(word in x.lower() for word in 
                                                             ['karriere', 'career', 'jobs', 'stellen', 'positions',
                                                              'mitarbeiter', 'bewerbung', 'application', 'kunst', 'art',
                                                              'forschung', 'research', 'lehre', 'teaching']))
        
        for link in job_links:
            link_text = link.get_text().strip()
            
            if any(term.lower() in link_text.lower() for term in found_terms):
                # Get the full URL for the job link
                job_url = self._make_full_url(link.get('href', ''), url)
                
                positions.append({
                    'title': self._clean_job_title(link_text),
                    'description': f"Job opportunity link: {job_url}",
                    'url': job_url
                })
        
        return positions[:3]  # Limit to 3 additional general job opportunities
    
    def _extract_job_title_from_listing(self, listing_element) -> str:
        """Extract job title from a job listing element"""
        # Look for the most prominent text in the listing
        title_element = listing_element.find(['strong', 'b', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        if title_element:
            title_text = title_element.get_text().strip()
            if self._is_job_title(title_text, []):
                return self._clean_job_title(title_text)
        
        # If no title element found, use the first line of the listing
        listing_text = listing_element.get_text().strip()
        first_line = listing_text.split('\n')[0].strip()
        
        if len(first_line) < 100 and self._is_job_title(first_line, []):
            return self._clean_job_title(first_line)
        
        return None
    
    def _find_phd_program_url(self, soup: BeautifulSoup, university_name: str, current_url: str) -> str:
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
                # Make sure it's a full URL
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        # Look for PhD program sections
        phd_sections = soup.find_all(['section', 'div'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['phd', 'promotion', 'doktorand', 'graduate', 'research']))
        
        for section in phd_sections:
            # Look for links within the section
            section_links = section.find_all('a', href=True)
            for link in section_links:
                href = link.get('href', '')
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        return None
    
    def _find_job_posting_url(self, soup: BeautifulSoup, university_name: str, current_url: str) -> str:
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
                # Make sure it's a full URL
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        # Look for job posting sections
        job_sections = soup.find_all(['section', 'div'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['job', 'stellen', 'karriere', 'career', 'mitarbeiter']))
        
        for section in job_sections:
            # Look for links within the section
            section_links = section.find_all('a', href=True)
            for link in section_links:
                href = link.get('href', '')
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        return None
    
    
    def _find_specific_job_url(self, element, current_url: str) -> str:
        """Find the specific URL for a job posting within an element"""
        # Look for links within the element
        links = element.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            link_text = link.get_text().lower()
            
            # Check if this looks like a job posting link
            job_indicators = [
                'stellenausschreibung', 'job', 'position', 'vacancy', 'bewerbung',
                'application', 'mitarbeiter', 'stellen', 'karriere', 'career'
            ]
            
            if any(indicator in href.lower() or indicator in link_text for indicator in job_indicators):
                full_url = URLResolver.make_full_url(href, current_url)
                if full_url:
                    return full_url
        
        # Look for links in parent elements
        parent = element.parent
        if parent:
            parent_links = parent.find_all('a', href=True)
            for link in parent_links:
                href = link.get('href', '')
                link_text = link.get_text().lower()
                
                if any(indicator in href.lower() or indicator in link_text for indicator in job_indicators):
                    full_url = URLResolver.make_full_url(href, current_url)
                    if full_url:
                        return full_url
        
        return None
    
    
    
    
    
    
    def _extract_job_title(self, element, found_terms: List[str]) -> str:
        """Extract job title from element with improved accuracy"""
        # Look for title within the element
        title_element = element.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'b'])
        
        if title_element:
            title_text = title_element.get_text().strip()
            if self._is_job_title(title_text, found_terms):
                return self._clean_job_title(title_text)
        
        # Look for job title patterns in the text
        element_text = element.get_text().strip()
        sentences = element_text.split('.')
        
        for sentence in sentences:
            sentence = sentence.strip()
            if self._is_job_title(sentence, found_terms):
                return self._clean_job_title(sentence)
        
        return None
    
    def _is_job_title(self, text: str, found_terms: List[str]) -> bool:
        """Check if text looks like a job title"""
        text_lower = text.lower()
        
        # Must contain at least one found term
        if not any(term.lower() in text_lower for term in found_terms):
            return False
        
        # Job title indicators
        job_indicators = [
            'mitarbeiter', 'stelle', 'position', 'job', 'assistant', 'staff', 'fellow',
            'coordinator', 'technician', 'collaborator', 'associate'
        ]
        
        # PhD indicators (should not be job titles)
        phd_indicators = [
            'phd', 'promotion', 'doktorand', 'doctorate', 'doctoral', 'graduate program'
        ]
        
        # Check for job indicators
        has_job_indicator = any(indicator in text_lower for indicator in job_indicators)
        
        # Check for PhD indicators (exclude these from job titles)
        has_phd_indicator = any(indicator in text_lower for indicator in phd_indicators)
        
        # Length check (job titles are usually shorter)
        is_reasonable_length = len(text) < 100
        
        return has_job_indicator and not has_phd_indicator and is_reasonable_length
    
    def _clean_job_title(self, title: str) -> str:
        """Clean and format job title"""
        return TextProcessor.clean_job_title(title)
    
    def _clean_phd_title(self, title: str) -> str:
        """Clean and format PhD program title"""
        return TextProcessor.clean_phd_title(title)
    
    def _clean_job_description(self, description: str) -> str:
        """Clean job description text"""
        return TextProcessor.clean_description(description)
    
    def _extract_academic_positions(self, soup: BeautifulSoup, found_terms: List[str]) -> List[Dict]:
        """Extract academic position details"""
        positions = []
        
        # Look for specific patterns in text
        text_content = soup.get_text()
        
        # Search for position titles in paragraphs
        paragraphs = soup.find_all(['p', 'div', 'span'])
        
        for para in paragraphs:
            para_text = para.get_text().strip()
            
            # Check if paragraph contains academic position terms
            if any(term.lower() in para_text.lower() for term in found_terms):
                # Extract the sentence containing the term
                sentences = para_text.split('.')
                for sentence in sentences:
                    sentence = sentence.strip()
                    if any(term.lower() in sentence.lower() for term in found_terms):
                        positions.append({
                            'title': sentence[:100] + '...' if len(sentence) > 100 else sentence,
                            'description': para_text[:300] + '...' if len(para_text) > 300 else para_text
                        })
                        break
        
        return positions[:5]  # Limit to 5 positions per page
    
    def _extract_job_postings(self, soup: BeautifulSoup, found_terms: List[str]) -> List[Dict]:
        """Extract job posting details"""
        positions = []
        
        # Look for job posting patterns
        job_elements = soup.find_all(['div', 'section', 'article'], 
                                   class_=lambda x: x and any(word in x.lower() for word in 
                                                           ['job', 'position', 'stelle', 'ausschreibung', 'bewerbung']))
        
        for element in job_elements:
            element_text = element.get_text().strip()
            
            if any(term.lower() in element_text.lower() for term in found_terms):
                # Try to find a title within this element
                title_element = element.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                title = title_element.get_text().strip() if title_element else element_text[:100] + '...'
                
                positions.append({
                    'title': title,
                    'description': element_text[:300] + '...' if len(element_text) > 300 else element_text
                })
        
        return positions[:5]  # Limit to 5 positions per page
    
    def _find_description_near_heading(self, heading) -> str:
        """Find description text near a heading"""
        description = ""
        
        # Look in the next sibling elements
        current = heading.next_sibling
        while current and len(description) < 500:  # Limit description length
            if hasattr(current, 'get_text'):
                text = current.get_text().strip()
                if text:
                    description += text + " "
            current = current.next_sibling
        
        return description.strip()
    
    def scrape_university(self, university: Dict) -> int:
        """Scrape a single university for positions"""
        university_name = university['name']
        website = university['website']
        
        logger.info(f"Scraping {university_name}...")
        
        try:
            # First, try to scrape the main website
            soup = self.make_request(website)
            if not soup:
                logger.warning(f"Could not access main website for {university_name}")
                return 0
            
            positions_found = 0
            
            # Extract positions from main page
            positions = self.extract_positions_from_page(soup, website, university_name)
            for position in positions:
                if self.db.add_position(position):
                    positions_found += 1
            
            # Find and scrape job-related pages
            job_links = self.find_job_related_links(soup, website)
            
            for link in job_links[:5]:  # Limit to first 5 job-related links
                try:
                    time.sleep(SCRAPING_CONFIG['request_delay'])
                    
                    # Use Selenium for complex pages
                    use_selenium = 'career' in link.lower() or 'job' in link.lower()
                    link_soup = self.make_request(link, use_selenium=use_selenium)
                    
                    if link_soup:
                        link_positions = self.extract_positions_from_page(link_soup, link, university_name)
                        for position in link_positions:
                            if self.db.add_position(position):
                                positions_found += 1
                
                except Exception as e:
                    logger.error(f"Error scraping link {link}: {e}")
                    continue
            
            # Update university scrape time
            self.db.update_university_scrape_time(university_name)
            
            # Log search results
            self.db.log_search(university_name, "general_search", positions_found)
            
            logger.info(f"Found {positions_found} positions at {university_name}")
            return positions_found
            
        except Exception as e:
            logger.error(f"Error scraping {university_name}: {e}")
            self.db.log_search(university_name, "general_search", 0, "error")
            return 0
    
    def scrape_all_universities(self) -> Dict[str, int]:
        """Scrape all universities and return results summary"""
        all_universities = UNIVERSITIES  # This now includes all universities from all countries
        results = {}
        total_positions = 0
        
        logger.info(f"Starting to scrape {len(all_universities)} universities...")
        
        for i, university in enumerate(all_universities, 1):
            logger.info(f"Progress: {i}/{len(all_universities)}")
            
            positions_found = self.scrape_university(university)
            results[university['name']] = positions_found
            total_positions += positions_found
            
            # Add delay between universities
            time.sleep(SCRAPING_CONFIG['request_delay'] * 2)
        
        logger.info(f"Scraping completed. Total positions found: {total_positions}")
        return results
    
    def scrape_by_country(self, country: str) -> Dict[str, int]:
        """Scrape universities from a specific country/region"""
        if country not in UNIVERSITIES_BY_COUNTRY:
            logger.error(f"Unknown country: {country}")
            return {}
        
        universities = UNIVERSITIES_BY_COUNTRY[country]
        results = {}
        total_positions = 0
        
        logger.info(f"Starting to scrape {len(universities)} universities from {country}...")
        
        for i, university in enumerate(universities, 1):
            logger.info(f"Progress: {i}/{len(universities)}")
            
            positions_found = self.scrape_university(university)
            results[university['name']] = positions_found
            total_positions += positions_found
            
            # Add delay between universities
            time.sleep(SCRAPING_CONFIG['request_delay'] * 2)
        
        logger.info(f"Scraping completed for {country}. Total positions found: {total_positions}")
        return results
    
    def search_specific_terms(self, universities: List[str] = None, terms: List[str] = None) -> Dict[str, int]:
        """Search for specific terms across universities"""
        if not terms:
            terms = [
                # Mitarbeiter positions (German)
                'künstlerische mitarbeiter', 'wissenschaftliche mitarbeiter',
                'media art mitarbeiter', 'ai art mitarbeiter', 'artistic research mitarbeiter',
                'medienkunst mitarbeiter', 'ki-kunst mitarbeiter', 'klangkunst mitarbeiter',
                'performance art mitarbeiter', 'interactive art mitarbeiter',
                
                # PhD programs (German)
                'media art phd', 'ai art phd', 'artistic research phd',
                'medienkunst promotion', 'ki-kunst promotion', 'klangkunst promotion',
                'practice-based phd', 'künstlerische forschung', 'praxis-basierte forschung',
                'practice-led research', 'artistic practice phd', 'creative research phd',
                'dfa', 'doctor of fine arts',
                'studio-based research', 'research through practice', 'practice as research',
                
                # Staff positions (English)
                'artistic staff', 'research staff', 'academic staff',
                'media art staff', 'ai art staff', 'artistic research staff',
                
                # PhD programs (English)
                'media art phd', 'ai art phd', 'artistic research phd',
                'practice-based phd', 'creative research phd', 'practice-led research',
                'artistic practice phd', 'research through practice', 'practice as research',
                'dfa', 'doctor of fine arts',
                'studio-based research', 'creative practice phd', 'interdisciplinary research'
            ]
        
        if not universities:
            universities = [uni['name'] for uni in UNIVERSITIES]
        
        results = {}
        
        for university_name in universities:
            logger.info(f"Searching specific terms in {university_name}...")
            
            # Find university data
            university_data = None
            for uni in UNIVERSITIES:
                if uni['name'] == university_name:
                    university_data = uni
                    break
            
            if not university_data:
                continue
            
            try:
                soup = self.make_request(university_data['website'])
                if not soup:
                    continue
                
                text_content = self.extract_text_content(soup)
                positions_found = 0
                
                # Enhanced search for academic positions with consolidated types
                for term in terms:
                    if term.lower() in text_content.lower():
                        # Skip if this appears to be non-position content
                        if self._is_non_position_content(text_content):
                            continue
                            
                        # Determine position type based on term
                        position_type = 'specific_search'
                        
                        # Media Art positions
                        if 'media art' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'media_art_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'media_art_phd'
                            else:
                                position_type = 'media_art_jobs'
                        
                        # AI Art positions
                        elif 'ai art' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'ai_art_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'ai_art_phd'
                            else:
                                position_type = 'ai_art_jobs'
                        
                        # Sound Art positions
                        elif 'sound art' in term.lower() or 'klangkunst' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'sound_art_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'sound_art_phd'
                            else:
                                position_type = 'sound_art_jobs'
                        
                        # Performance Art positions
                        elif 'performance art' in term.lower() or 'aufführungskunst' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'performance_art_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'performance_art_phd'
                            else:
                                position_type = 'performance_art_jobs'
                        
                        # Interactive Art positions
                        elif 'interactive art' in term.lower() or 'interaktive kunst' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'interactive_art_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'interactive_art_phd'
                            else:
                                position_type = 'interactive_art_jobs'
                        
                        # Artistic Research positions
                        elif 'artistic research' in term.lower() or 'künstlerische forschung' in term.lower():
                            if 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                                position_type = 'artistic_research_jobs'
                            elif 'phd' in term.lower() or 'promotion' in term.lower():
                                position_type = 'artistic_research_phd'
                            else:
                                position_type = 'artistic_research_jobs'
                        
                        # General academic positions
                        elif 'mitarbeiter' in term.lower() or 'assistant' in term.lower():
                            position_type = 'academic_jobs'
                        elif 'phd' in term.lower() or 'promotion' in term.lower():
                            position_type = 'general_phd'
                        else:
                            # Check if it's a general job term (focused on mitarbeiter positions)
                            general_job_indicators = [
                                'stelle', 'position', 'job', 'vacancy', 'employment', 'career',
                                'mitarbeiter', 'assistant', 'assistent', 'coordinator', 'manager',
                                'curator', 'educator', 'freelance', 'contract', 'temporary',
                                'part-time', 'full-time', 'kunst', 'art', 'forschung', 'research'
                            ]
                            if any(indicator in term.lower() for indicator in general_job_indicators):
                                position_type = 'general_jobs'
                            else:
                                position_type = 'general_jobs'  # Default to general jobs for unmatched terms
                        
                        # Determine position category based on position type
                        position_category = 'job_offer' if '_jobs' in position_type else 'phd_program'
                        
                        position = {
                            'university': university_name,
                            'position_type': position_type,
                            'title': f"Position related to: {term}",
                            'description': f"Found content related to {term}",
                            'url': university_data['website'],
                            'language': self._detect_language(text_content),
                            'date_found': time.strftime('%Y-%m-%d'),
                            'status': 'active',
                            'position_category': position_category
                        }
                        
                        if self.db.add_position(position):
                            positions_found += 1
                
                results[university_name] = positions_found
                self.db.log_search(university_name, f"specific_search_{'_'.join(terms)}", positions_found)
                
            except Exception as e:
                logger.error(f"Error searching {university_name}: {e}")
                results[university_name] = 0
        
        return results
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        self.close_selenium()