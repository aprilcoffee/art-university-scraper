#!/usr/bin/env python3
"""
Quick test of the new scraper with one university.
"""

from scraper_v2 import IncrementalScraper
from config.universities import get_university_by_name

def test_single_university():
    """Test scraping a single university."""
    # Use UdK Berlin as test (has known job page URL)
    scraper = IncrementalScraper(delay=1)

    university = get_university_by_name('Universität der Künste Berlin')

    if not university:
        print("Test university not found!")
        return

    print(f"Testing with: {university['name']}")
    print(f"Website: {university['website']}")
    print(f"Job page: {university.get('job_page_url', 'Not configured')}")
    print("\nStarting scrape...\n")

    result = scraper.scrape_university(university, force_scrape=True)

    print(f"\nResult: {result}")

    if result['status'] == 'success':
        print("\n✓ Test successful!")
        if result['positions_found'] > 0:
            print(f"  Found {result['positions_found']} positions")

            # Show positions
            positions = scraper.db.get_positions(university_name=university['name'])
            print(f"\n  Positions:")
            for pos in positions[:5]:  # Show first 5
                print(f"    - {pos['title'][:60]}")
                print(f"      Type: {pos['position_type']}")
                print(f"      URL: {pos['url'][:80]}")
                print()
        else:
            print("  No positions found (page might not have any currently)")
    else:
        print(f"\n✗ Test failed: {result['error']}")

    scraper.close()


if __name__ == '__main__':
    test_single_university()
