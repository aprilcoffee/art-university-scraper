"""Content change detection using hashing."""
import hashlib
import re
from bs4 import BeautifulSoup


class ContentDetector:
    """Detects content changes via hash comparison."""

    @staticmethod
    def compute_content_hash(soup: BeautifulSoup) -> str:
        """Compute SHA256 hash of page content."""
        if not soup:
            return ""

        soup_copy = BeautifulSoup(str(soup), 'html.parser')

        # Remove dynamic elements
        for tag in soup_copy.find_all(['script', 'style', 'noscript', 'iframe', 'nav', 'header', 'footer']):
            tag.decompose()

        text = soup_copy.get_text(separator=' ', strip=True).lower()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\d{2}:\d{2}:\d{2}', '', text)
        text = re.sub(r'(stand|aktualisiert):\s*\d{2}\.\d{2}\.\d{4}', '', text, flags=re.I)

        for phrase in ['heute', 'gestern', r'vor \d+ (tag|tagen)', 'last updated']:
            text = re.sub(phrase, '', text, flags=re.I)

        return hashlib.sha256(text.strip().encode('utf-8')).hexdigest()

    @staticmethod
    def has_content_changed(old_hash: str, new_hash: str) -> bool:
        """Check if content changed based on hash."""
        return not old_hash or not new_hash or old_hash != new_hash

    @staticmethod
    def detect_language(text: str) -> str:
        """Simple German vs English detection."""
        text_lower = text.lower()
        german_words = ['und', 'der', 'die', 'das', 'für', 'mit', 'stellenausschreibung']
        english_words = ['and', 'the', 'for', 'with', 'job', 'position']

        german_count = sum(1 for w in german_words if w in text_lower)
        english_count = sum(1 for w in english_words if w in text_lower)

        return 'de' if german_count >= english_count else 'en'

    @staticmethod
    def extract_main_content(soup: BeautifulSoup) -> BeautifulSoup:
        """Extract main content area from page."""
        if not soup:
            return None

        for selector in [{'id': 'main'}, {'id': 'content'}, {'role': 'main'},
                        {'class': re.compile(r'(main|content)', re.I)}]:
            content = soup.find(**selector)
            if content:
                return content

        return soup
