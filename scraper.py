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

from config import UNIVERSITIES, INTERNATIONAL_UNIVERSITIES, SEARCH_TERMS, SCRAPING_CONFIG
from database import DatabaseManager

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
        found_terms = []
        text_lower = text.lower()
        
        for term in terms:
            if term.lower() in text_lower:
                found_terms.append(term)
        
        return found_terms
    
    def extract_positions_from_page(self, soup: BeautifulSoup, url: str, university_name: str) -> List[Dict]:
        """Extract position information from a page"""
        positions = []
        text_content = self.extract_text_content(soup)
        
        # Enhanced language detection
        language = self._detect_language(text_content)
        
        # Search for different types of positions - now including artistic research and academic positions
        search_categories = ['media_art', 'digital_art', 'ai_art', 'artistic_research_phd', 'academic_positions', 'phd', 'jobs']
        
        for category in search_categories:
            terms = SEARCH_TERMS[language][category]
            found_terms = self.search_for_terms(text_content, terms)
            
            if found_terms:
                # Try to extract position titles and descriptions
                position_info = self._extract_position_details(soup, found_terms, category)
                
                for info in position_info:
                    position = {
                        'university': university_name,
                        'position_type': category,
                        'title': info.get('title', f"{category.replace('_', ' ').title()} Position"),
                        'description': info.get('description', ''),
                        'url': url,
                        'language': language,
                        'date_found': time.strftime('%Y-%m-%d'),
                        'status': 'active'
                    }
                    positions.append(position)
        
        return positions
    
    def _detect_language(self, text_content: str) -> str:
        """Enhanced language detection"""
        text_lower = text_content.lower()
        
        # German indicators
        german_indicators = [
            'der', 'die', 'das', 'und', 'für', 'mit', 'von', 'zu', 'auf', 'in', 'an',
            'stellenausschreibung', 'bewerbung', 'promotion', 'doktorand', 'mitarbeiter',
            'künstlerische', 'wissenschaftliche', 'forschung', 'kunst', 'hochschule',
            'universität', 'studium', 'semester', 'bewerbungsfrist', 'zulassung'
        ]
        
        # English indicators
        english_indicators = [
            'the', 'and', 'for', 'with', 'from', 'to', 'on', 'in', 'at', 'of',
            'job opening', 'position', 'vacancy', 'employment', 'career', 'application',
            'artistic', 'research', 'art', 'university', 'study', 'semester',
            'application deadline', 'admission', 'graduate', 'doctoral'
        ]
        
        german_count = sum(1 for indicator in german_indicators if indicator in text_lower)
        english_count = sum(1 for indicator in english_indicators if indicator in text_lower)
        
        # If German indicators are significantly more present, classify as German
        if german_count > english_count * 1.5:
            return 'german'
        elif english_count > german_count * 1.5:
            return 'english'
        else:
            # Mixed content - try to determine primary language
            return 'german' if german_count >= english_count else 'english'
    
    def _extract_position_details(self, soup: BeautifulSoup, found_terms: List[str], category: str) -> List[Dict]:
        """Extract detailed position information"""
        positions = []
        
        # Look for headings that might contain position titles
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        for heading in headings:
            heading_text = heading.get_text().strip()
            
            # Check if heading contains any of the found terms
            if any(term.lower() in heading_text.lower() for term in found_terms):
                # Try to find description in nearby content
                description = self._find_description_near_heading(heading)
                
                positions.append({
                    'title': heading_text,
                    'description': description
                })
        
        # Look for specific academic position patterns
        if category in ['academic_positions', 'artistic_research_phd']:
            academic_positions = self._extract_academic_positions(soup, found_terms)
            positions.extend(academic_positions)
        
        # Look for job posting patterns
        if category == 'jobs':
            job_positions = self._extract_job_postings(soup, found_terms)
            positions.extend(job_positions)
        
        # If no specific positions found, create generic position
        if not positions:
            positions.append({
                'title': f"{category.replace('_', ' ').title()} Opportunity",
                'description': f"Found {category.replace('_', ' ')} related content"
            })
        
        return positions
    
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
        all_universities = UNIVERSITIES + INTERNATIONAL_UNIVERSITIES
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
    
    def search_specific_terms(self, universities: List[str] = None, terms: List[str] = None) -> Dict[str, int]:
        """Search for specific terms across universities"""
        if not terms:
            terms = [
                'artistic research', 'künstlerische mitarbeiter', 'wissenschaftliche mitarbeiter',
                'practice-based PhD', 'media art', 'digital art', 'AI art', 'artificial intelligence'
            ]
        
        if not universities:
            universities = [uni['name'] for uni in UNIVERSITIES + INTERNATIONAL_UNIVERSITIES]
        
        results = {}
        
        for university_name in universities:
            logger.info(f"Searching specific terms in {university_name}...")
            
            # Find university data
            university_data = None
            for uni in UNIVERSITIES + INTERNATIONAL_UNIVERSITIES:
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
                
                # Enhanced search for academic positions
                academic_terms = [
                    'künstlerische mitarbeiter', 'wissenschaftliche mitarbeiter', 'artistic research',
                    'practice-based PhD', 'artistic PhD', 'künstlerische forschung'
                ]
                
                for term in terms:
                    if term.lower() in text_content.lower():
                        # Determine position type based on term
                        position_type = 'specific_search'
                        if any(academic_term in term.lower() for academic_term in academic_terms):
                            if 'mitarbeiter' in term.lower():
                                position_type = 'academic_positions'
                            elif 'research' in term.lower() or 'phd' in term.lower():
                                position_type = 'artistic_research_phd'
                        
                        position = {
                            'university': university_name,
                            'position_type': position_type,
                            'title': f"Position related to: {term}",
                            'description': f"Found content related to {term}",
                            'url': university_data['website'],
                            'language': self._detect_language(text_content),
                            'date_found': time.strftime('%Y-%m-%d'),
                            'status': 'active'
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