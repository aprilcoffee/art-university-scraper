"""
Art University Job Scraper.

Features:
- Uses Selenium to handle JavaScript-loaded content
- Flexible position extraction with keyword matching
- Handles various page structures
"""

import time
from datetime import datetime
from typing import List, Dict, Optional

from core.database import DatabaseManager
from core.fetcher import PageFetcher
from core.detector import ContentDetector
from core.extractor import PositionExtractor
from core.models import UniversityJobPage, ScrapingLog
from config.universities import get_all_universities
from config.search_terms import JOB_PAGE_INDICATORS


class ArtScraper:
    """Art university scraper with JavaScript support."""

    def __init__(self, db_path='art_positions.db', delay=2):
        """
        Initialize scraper.

        Args:
            db_path: Path to SQLite database
            delay: Delay in seconds between requests
        """
        self.db = DatabaseManager(db_path)
        # Use Selenium by default for better JavaScript handling
        self.fetcher = PageFetcher(use_selenium=True)
        self.detector = ContentDetector()
        self.delay = delay
        self.stats = {
            'universities_checked': 0,
            'universities_changed': 0,
            'universities_unchanged': 0,
            'universities_failed': 0,
            'new_positions': 0,
        }

    def scrape_all(self, force_full_scrape: bool = False) -> Dict:
        """
        Scrape all universities.

        Args:
            force_full_scrape: Force full scrape even if content hasn't changed

        Returns:
            Statistics dictionary
        """
        universities = get_all_universities()
        total = len(universities)

        print(f"\nStarting improved incremental scrape of {total} universities...")
        print(f"Using Selenium for JavaScript support")
        print(f"Force full scrape: {force_full_scrape}\n")

        for i, university in enumerate(universities, 1):
            print(f"[{i}/{total}] {university['name']}...", end=' ', flush=True)

            result = self.scrape_university(university, force_full_scrape)

            if result['status'] == 'success':
                if result['changed']:
                    print(f"✓ Changed - {result['positions_found']} positions")
                    self.stats['universities_changed'] += 1
                else:
                    print("✓ No changes")
                    self.stats['universities_unchanged'] += 1
            else:
                print(f"✗ Failed - {result['error']}")
                self.stats['universities_failed'] += 1

            self.stats['universities_checked'] += 1
            self.stats['new_positions'] += result.get('positions_found', 0)

            # Delay between universities
            if i < total:
                time.sleep(self.delay)

        self._print_summary()
        return self.stats

    def scrape_university(
        self,
        university: Dict,
        force_scrape: bool = False
    ) -> Dict:
        """
        Scrape a single university.

        Args:
            university: University configuration dict
            force_scrape: Force scrape even if content hasn't changed

        Returns:
            Result dictionary with status, changed, positions_found, error
        """
        university_name = university['name']
        timestamp = datetime.now().isoformat()

        # Step 1: Get or find job page URL
        job_page_url = university.get('job_page_url')

        if not job_page_url:
            # Try to find job page
            job_page_url = self._find_job_page(university)

            if not job_page_url:
                error = "Could not find job page"
                self._log_failure(university_name, error, timestamp)
                return {
                    'status': 'failed',
                    'changed': False,
                    'positions_found': 0,
                    'error': error
                }

        # Step 2: Fetch job page
        soup = self.fetcher.fetch(job_page_url)

        if not soup:
            error = "Failed to fetch job page"
            self._log_failure(university_name, error, timestamp)
            return {
                'status': 'failed',
                'changed': False,
                'positions_found': 0,
                'error': error
            }

        # Step 3: Check if content has changed
        new_hash = self.detector.compute_content_hash(soup)
        stored_info = self.db.get_job_page_info(university_name)

        content_changed = True
        if stored_info and not force_scrape:
            old_hash = stored_info['content_hash']
            content_changed = self.detector.has_content_changed(old_hash, new_hash)

        # Step 4: If changed (or forced), extract positions
        positions_found = 0

        if content_changed or force_scrape:
            # Extract positions
            extractor = PositionExtractor(university_name, job_page_url)
            positions = extractor.extract_positions(soup)

            # Save positions to database
            for position in positions:
                if self.db.add_position(position):
                    positions_found += 1

            # Update job page tracking
            job_page = UniversityJobPage(
                university_name=university_name,
                job_page_url=job_page_url,
                content_hash=new_hash,
                last_scraped=timestamp,
                last_modified=timestamp if content_changed else stored_info.get('last_modified', timestamp),
                positions_count=positions_found,
                is_active=True,
            )
            self.db.update_job_page(job_page)

            # Log success
            self._log_success(university_name, positions_found, timestamp)

            return {
                'status': 'success',
                'changed': True,
                'positions_found': positions_found,
                'error': None
            }
        else:
            # Content unchanged - just update last_scraped
            if stored_info:
                job_page = UniversityJobPage(
                    university_name=university_name,
                    job_page_url=job_page_url,
                    content_hash=new_hash,
                    last_scraped=timestamp,
                    last_modified=stored_info['last_modified'],
                    positions_count=stored_info['positions_count'],
                    is_active=True,
                )
                self.db.update_job_page(job_page)

            # Log unchanged
            log = ScrapingLog(
                university_name=university_name,
                status='unchanged',
                message='Content unchanged since last scrape',
                timestamp=timestamp,
                positions_found=0,
            )
            self.db.add_log(log)

            return {
                'status': 'success',
                'changed': False,
                'positions_found': 0,
                'error': None
            }

    def _find_job_page(self, university: Dict) -> Optional[str]:
        """
        Find the job/career page URL for a university.

        Args:
            university: University configuration dict

        Returns:
            Job page URL or None
        """
        base_url = university['website']

        # Get job page indicators (German and English)
        indicators = (
            JOB_PAGE_INDICATORS['german'] +
            JOB_PAGE_INDICATORS['english']
        )

        # Try to find job page
        job_url = self.fetcher.find_job_page_url(base_url, indicators)

        return job_url

    def _log_success(self, university_name: str, positions_found: int, timestamp: str):
        """Log successful scrape."""
        log = ScrapingLog(
            university_name=university_name,
            status='success',
            message=f'Found {positions_found} positions',
            timestamp=timestamp,
            positions_found=positions_found,
        )
        self.db.add_log(log)

    def _log_failure(self, university_name: str, error: str, timestamp: str):
        """Log failed scrape."""
        log = ScrapingLog(
            university_name=university_name,
            status='failed',
            message=error,
            timestamp=timestamp,
            positions_found=0,
        )
        self.db.add_log(log)

    def _print_summary(self):
        """Print scraping summary."""
        print("\n" + "="*60)
        print("SCRAPING SUMMARY")
        print("="*60)
        print(f"Universities checked:  {self.stats['universities_checked']}")
        print(f"  - Changed:           {self.stats['universities_changed']}")
        print(f"  - Unchanged:         {self.stats['universities_unchanged']}")
        print(f"  - Failed:            {self.stats['universities_failed']}")
        print(f"\nNew positions found:   {self.stats['new_positions']}")
        print("="*60)

        # Database statistics
        db_stats = self.db.get_statistics()
        print("\nDATABASE STATISTICS")
        print("="*60)
        print(f"Total positions:       {db_stats['total_positions']}")
        if db_stats['by_type']:
            print("\nBy type:")
            for pos_type, count in db_stats['by_type'].items():
                print(f"  - {pos_type:20s} {count}")
        print("="*60 + "\n")

    def close(self):
        """Clean up resources."""
        self.fetcher.close()


def main():
    """Main entry point for testing."""
    scraper = ArtScraper(delay=2)

    try:
        print("Running art scraper with Selenium support...")
        scraper.scrape_all(force_full_scrape=True)
    finally:
        scraper.close()


if __name__ == '__main__':
    main()
