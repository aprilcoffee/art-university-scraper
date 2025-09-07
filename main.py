#!/usr/bin/env python3
"""
Main script for the Art University Job Scraper
"""

import argparse
import sys
import time
from datetime import datetime

from scraper import ArtUniversityScraper
from database import DatabaseManager
from config import UNIVERSITIES_BY_COUNTRY, UNIVERSITIES

def main():
    parser = argparse.ArgumentParser(description='Art University Job Scraper')
    parser.add_argument('--mode', choices=['scrape', 'web', 'test'], default='web',
                       help='Mode to run: scrape (command line), web (web interface), test (test run)')
    parser.add_argument('--universities', nargs='+', help='Specific universities to scrape')
    parser.add_argument('--terms', nargs='+', help='Specific terms to search for')
    parser.add_argument('--output', help='Output file for results')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.mode == 'web':
        print("Starting web interface...")
        print("Open your browser and go to: http://localhost:5002")
        print("Press Ctrl+C to stop the server")
        
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5002)
        
    elif args.mode == 'scrape':
        print("Starting command line scraping...")
        scraper = ArtUniversityScraper()
        
        try:
            if args.universities:
                # Scrape specific universities
                universities_to_scrape = []
                all_universities = UNIVERSITIES
                
                for uni_name in args.universities:
                    for uni in all_universities:
                        if uni_name.lower() in uni['name'].lower():
                            universities_to_scrape.append(uni)
                            break
                
                if not universities_to_scrape:
                    print(f"No universities found matching: {args.universities}")
                    return
                
                print(f"Scraping {len(universities_to_scrape)} specific universities...")
                results = {}
                
                for university in universities_to_scrape:
                    print(f"Scraping {university['name']}...")
                    positions_found = scraper.scrape_university(university)
                    results[university['name']] = positions_found
                    print(f"Found {positions_found} positions")
                    time.sleep(2)
                
            elif args.terms:
                # Search for specific terms
                print(f"Searching for terms: {args.terms}")
                results = scraper.search_specific_terms(terms=args.terms)
                
            else:
                # Scrape all universities
                print("Scraping all universities...")
                results = scraper.scrape_all_universities()
            
            # Display results
            print("\n" + "="*50)
            print("SCRAPING RESULTS")
            print("="*50)
            
            total_positions = 0
            for university, count in results.items():
                print(f"{university}: {count} positions")
                total_positions += count
            
            print(f"\nTotal positions found: {total_positions}")
            
            # Save results if output file specified
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(f"Art University Scraping Results - {datetime.now()}\n")
                    f.write("="*50 + "\n")
                    for university, count in results.items():
                        f.write(f"{university}: {count} positions\n")
                    f.write(f"\nTotal positions found: {total_positions}\n")
                print(f"Results saved to: {args.output}")
            
        except KeyboardInterrupt:
            print("\nScraping interrupted by user")
        except Exception as e:
            print(f"Error during scraping: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
        finally:
            scraper.close_selenium()
    
    elif args.mode == 'test':
        print("Running test mode...")
        scraper = ArtUniversityScraper()
        
        # Test with a few universities
        test_universities = UNIVERSITIES[:3]  # Test first 3 universities
        
        print(f"Testing with {len(test_universities)} universities...")
        results = {}
        
        for university in test_universities:
            print(f"Testing {university['name']}...")
            try:
                positions_found = scraper.scrape_university(university)
                results[university['name']] = positions_found
                print(f"✓ Found {positions_found} positions")
            except Exception as e:
                print(f"✗ Error: {e}")
                results[university['name']] = 0
        
        print("\nTest Results:")
        for university, count in results.items():
            print(f"  {university}: {count} positions")
        
        scraper.close_selenium()

if __name__ == '__main__':
    main()