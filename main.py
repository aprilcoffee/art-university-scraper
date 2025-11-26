#!/usr/bin/env python3
"""
Art University Job Scraper - Main CLI.
Uses Selenium by default for JavaScript support.
"""

import argparse
from scraper import ArtScraper
from config.universities import (
    get_all_universities,
    get_high_priority_universities,
    get_media_art_universities,
    get_university_by_name
)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Art University Job Scraper (with Selenium support)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Scrape all universities
  %(prog)s --priority media         # Scrape only 8 media art schools
  %(prog)s --priority high          # Scrape 26 high-priority schools
  %(prog)s --full                   # Force full scrape (ignore change detection)
  %(prog)s --test                   # Test on 3 sample universities
  %(prog)s --university "UdK Berlin"# Scrape specific university
        """
    )

    parser.add_argument(
        '--full',
        action='store_true',
        help='Force full scrape (ignore change detection)'
    )

    parser.add_argument(
        '--priority',
        choices=['media', 'high', 'all'],
        default='all',
        help='Priority level: media (8 schools), high (26 schools), all (51 schools)'
    )

    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode: scrape only 3 sample universities'
    )

    parser.add_argument(
        '--university',
        type=str,
        help='Scrape a specific university by name (partial match supported)'
    )

    parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay in seconds between requests (default: 2.0)'
    )

    parser.add_argument(
        '--database',
        default='art_positions.db',
        help='Path to SQLite database (default: art_positions.db)'
    )

    args = parser.parse_args()

    # Select universities
    if args.test:
        print("TEST MODE: Scraping 3 sample universities")
        test_universities = [
            'Universität der Künste Berlin',
            'Kunsthochschule für Medien Köln',
            'Hochschule für Fernsehen und Film München',
        ]
        universities = [get_university_by_name(name) for name in test_universities]
        universities = [u for u in universities if u]  # Remove None values
    elif args.university:
        # Find university by partial name match
        all_unis = get_all_universities()
        matches = [u for u in all_unis if args.university.lower() in u['name'].lower()]

        if not matches:
            print(f"Error: No university found matching '{args.university}'")
            print("\nAvailable universities:")
            for u in all_unis[:10]:
                print(f"  - {u['name']}")
            print(f"  ... and {len(all_unis) - 10} more")
            return

        if len(matches) > 1:
            print(f"Multiple universities found matching '{args.university}':")
            for u in matches:
                print(f"  - {u['name']}")
            print("\nPlease be more specific.")
            return

        universities = matches
    elif args.priority == 'media':
        universities = get_media_art_universities()
        print(f"Scraping {len(universities)} MEDIA ART focused universities")
    elif args.priority == 'high':
        universities = get_high_priority_universities()
        print(f"Scraping {len(universities)} HIGH PRIORITY universities")
    else:
        universities = get_all_universities()
        print(f"Scraping ALL {len(universities)} universities")

    # Create scraper
    scraper = ArtScraper(db_path=args.database, delay=args.delay)

    try:
        if len(universities) == 1:
            # Single university mode
            university = universities[0]
            print(f"\nScraping: {university['name']}")
            print(f"Website: {university['website']}")
            if university.get('job_page_url'):
                print(f"Job page: {university['job_page_url']}")
            print()

            result = scraper.scrape_university(university, force_scrape=args.full)

            print(f"\nStatus: {result['status']}")
            if result['status'] == 'success':
                print(f"Positions found: {result['positions_found']}")

                if result['positions_found'] > 0:
                    # Show positions
                    positions = scraper.db.get_positions(university_name=university['name'])
                    print(f"\nPositions:")
                    for i, pos in enumerate(positions[:10], 1):
                        print(f"\n  {i}. {pos['title'][:70]}")
                        print(f"     Type: {pos['position_type']}")
                        print(f"     URL: {pos['url'][:80]}")
            else:
                print(f"Error: {result['error']}")
        else:
            # Multiple universities mode
            scraper.scrape_all(force_full_scrape=args.full)

    except KeyboardInterrupt:
        print("\n\nScraping interrupted by user.")
        scraper._print_summary()
    finally:
        scraper.close()


if __name__ == '__main__':
    main()
