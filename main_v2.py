#!/usr/bin/env python3
"""
Art University Job Scraper - Main Entry Point

Incremental scraper for wissenschaftliche and künstlerische Mitarbeiter positions
at German-speaking art universities.

Usage:
    python main_v2.py                    # Incremental scrape (checks for changes)
    python main_v2.py --full             # Full scrape (force re-scrape everything)
    python main_v2.py --stats            # Show database statistics
    python main_v2.py --logs             # Show recent scraping logs
    python main_v2.py --export FILE      # Export positions to CSV
"""

import argparse
import csv
import sys
from datetime import datetime

from scraper_v2 import IncrementalScraper
from core.database import DatabaseManager
from config.universities import (
    get_all_universities,
    get_high_priority_universities,
    get_media_art_universities
)


def scrape(args):
    """Run the scraper."""
    # Select universities based on priority
    if hasattr(args, 'priority'):
        if args.priority == 'media':
            universities = get_media_art_universities()
            print(f"Scraping {len(universities)} MEDIA ART focused universities")
        elif args.priority == 'high':
            universities = get_high_priority_universities()
            print(f"Scraping {len(universities)} HIGH PRIORITY universities (media/design focus)")
        else:
            universities = get_all_universities()
    else:
        universities = get_all_universities()

    scraper = IncrementalScraper(
        db_path=args.database,
        use_selenium=args.selenium,
        delay=args.delay
    )

    try:
        # Scrape selected universities
        if universities != get_all_universities():
            # Custom university list
            for i, university in enumerate(universities, 1):
                print(f"[{i}/{len(universities)}] {university['name']}...", end=' ')
                result = scraper.scrape_university(university, force_scrape=args.full)

                if result['status'] == 'success':
                    if result['changed']:
                        print(f"✓ Changed - {result['positions_found']} positions")
                        scraper.stats['universities_changed'] += 1
                    else:
                        print("✓ No changes")
                        scraper.stats['universities_unchanged'] += 1
                else:
                    print(f"✗ Failed - {result['error']}")
                    scraper.stats['universities_failed'] += 1

                scraper.stats['universities_checked'] += 1
                scraper.stats['new_positions'] += result.get('positions_found', 0)

                if i < len(universities):
                    import time
                    time.sleep(scraper.delay)

            scraper._print_summary()
        else:
            # Standard scrape all
            scraper.scrape_all(force_full_scrape=args.full)
    except KeyboardInterrupt:
        print("\n\nScraping interrupted by user.")
        scraper._print_summary()
    finally:
        scraper.close()


def show_stats(args):
    """Show database statistics."""
    db = DatabaseManager(args.database)
    stats = db.get_statistics()

    print("\n" + "="*60)
    print("DATABASE STATISTICS")
    print("="*60)
    print(f"Total active positions: {stats['total_positions']}")

    if stats['by_type']:
        print("\nPositions by type:")
        for pos_type, count in stats['by_type'].items():
            print(f"  {pos_type:25s} {count:5d}")

    if stats['top_universities']:
        print("\nTop universities by positions:")
        for uni, count in list(stats['top_universities'].items())[:10]:
            print(f"  {uni:50s} {count:3d}")

    print(f"\nScraping activity (last 7 days): {stats['recent_scrapes']} scrapes")
    print("="*60 + "\n")


def show_logs(args):
    """Show recent scraping logs."""
    db = DatabaseManager(args.database)
    logs = db.get_recent_logs(limit=args.limit)

    print("\n" + "="*60)
    print(f"RECENT SCRAPING LOGS (last {len(logs)})")
    print("="*60)

    for log in logs:
        timestamp = log['timestamp'][:19]  # Remove microseconds
        status_symbol = {
            'success': '✓',
            'failed': '✗',
            'unchanged': '○'
        }.get(log['status'], '?')

        print(f"{status_symbol} {timestamp} | {log['university_name']:40s} | "
              f"{log['status']:10s} | {log['message']}")

    print("="*60 + "\n")


def export_positions(args):
    """Export positions to CSV."""
    db = DatabaseManager(args.database)
    positions = db.get_positions(active_only=True)

    if not positions:
        print("No positions to export.")
        return

    # Determine output file
    if args.output:
        filename = args.output
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'positions_{timestamp}.csv'

    # Write CSV
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'university_name', 'position_type', 'title', 'url',
            'language', 'deadline', 'department', 'found_date'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

        writer.writeheader()
        for position in positions:
            writer.writerow(position)

    print(f"\nExported {len(positions)} positions to {filename}\n")


def list_universities(args):
    """List all configured universities."""
    universities = get_all_universities()

    print("\n" + "="*60)
    print(f"CONFIGURED UNIVERSITIES ({len(universities)})")
    print("="*60)

    # Group by country
    by_country = {}
    for uni in universities:
        country = uni['country']
        if country not in by_country:
            by_country[country] = []
        by_country[country].append(uni)

    for country in sorted(by_country.keys()):
        unis = by_country[country]
        print(f"\n{country} ({len(unis)} universities):")
        for uni in sorted(unis, key=lambda x: x['name']):
            job_page = "✓" if uni.get('job_page_url') else "○"
            print(f"  {job_page} {uni['name']}")

    print("\n" + "="*60)
    print("Legend: ✓ = Job page URL configured, ○ = Will be discovered")
    print("="*60 + "\n")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Art University Job Scraper - Incremental scraping system',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Incremental scrape (only changed pages)
  %(prog)s --full             # Full scrape (force all universities)
  %(prog)s --stats            # Show statistics
  %(prog)s --logs --limit 100 # Show last 100 log entries
  %(prog)s --export jobs.csv  # Export positions to CSV
  %(prog)s --list             # List all universities
        """
    )

    # Main mode arguments
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--full',
        action='store_true',
        help='Force full scrape of all universities (ignore change detection)'
    )
    mode_group.add_argument(
        '--stats',
        action='store_true',
        help='Show database statistics'
    )
    mode_group.add_argument(
        '--logs',
        action='store_true',
        help='Show recent scraping logs'
    )
    mode_group.add_argument(
        '--export',
        metavar='FILE',
        help='Export positions to CSV file'
    )
    mode_group.add_argument(
        '--list',
        action='store_true',
        help='List all configured universities'
    )

    # Scraping options
    parser.add_argument(
        '--database',
        default='art_positions.db',
        help='Path to SQLite database (default: art_positions.db)'
    )
    parser.add_argument(
        '--selenium',
        action='store_true',
        help='Use Selenium for all requests (slower but works with JavaScript)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay in seconds between requests (default: 2.0)'
    )
    parser.add_argument(
        '--priority',
        choices=['media', 'high', 'all'],
        default='all',
        help='Priority level: media (8 media art schools), high (26 media/design schools), all (51 schools)'
    )

    # Display options
    parser.add_argument(
        '--limit',
        type=int,
        default=50,
        help='Limit number of log entries to show (default: 50)'
    )
    parser.add_argument(
        '--output',
        '-o',
        metavar='FILE',
        help='Output file for export (default: positions_TIMESTAMP.csv)'
    )

    args = parser.parse_args()

    # Route to appropriate function
    if args.stats:
        show_stats(args)
    elif args.logs:
        show_logs(args)
    elif args.export:
        args.output = args.export
        export_positions(args)
    elif args.list:
        list_universities(args)
    else:
        # Default: run scraper
        scrape(args)


if __name__ == '__main__':
    main()
