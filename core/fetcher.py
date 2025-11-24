"""Page fetcher with HTTP and Selenium support."""
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageFetcher:
    """Fetches web pages."""

    def __init__(self, use_selenium=False, timeout=30):
        self.use_selenium = use_selenium
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch(self, url: str, force_selenium=False):
        """Fetch page and return BeautifulSoup object."""
        if not force_selenium and not self.use_selenium:
            soup = self._fetch_http(url)
            if soup:
                return soup
        return self._fetch_selenium(url)

    def _fetch_http(self, url: str):
        """Fetch via HTTP."""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            for tag in soup(['script', 'style', 'noscript']):
                tag.decompose()
            return soup
        except requests.RequestException as e:
            print(f"HTTP failed for {url}: {e}")
            return None

    def _fetch_selenium(self, url: str):
        """Fetch via Selenium."""
        driver = None
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(self.timeout)
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            for tag in soup(['script', 'style', 'noscript']):
                tag.decompose()
            return soup
        except Exception as e:
            print(f"Selenium failed for {url}: {e}")
            return None
        finally:
            if driver:
                driver.quit()

    def find_job_page_url(self, base_url: str, indicators: list):
        """Find job page URL from university website."""
        soup = self.fetch(base_url)
        if not soup:
            return None

        for link in soup.find_all('a', href=True):
            href = link.get('href', '').lower()
            text = link.get_text().lower()

            for indicator in indicators:
                if indicator.lower() in href or indicator.lower() in text:
                    if href.startswith('http'):
                        return link['href']
                    elif href.startswith('/'):
                        from urllib.parse import urljoin
                        return urljoin(base_url, href)
        return None

    def close(self):
        self.session.close()
