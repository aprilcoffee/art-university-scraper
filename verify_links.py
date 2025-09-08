#!/usr/bin/env python3
"""
University Link Verification Script
"""

import requests
import time
from config import UNIVERSITY_WEBSITES, UNIVERSITIES_BY_COUNTRY

def verify_link(url, timeout=10):
    """Verify if a URL is accessible"""
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        return {
            'status': response.status_code,
            'accessible': response.status_code == 200,
            'final_url': response.url,
            'error': None
        }
    except requests.exceptions.RequestException as e:
        return {
            'status': None,
            'accessible': False,
            'final_url': None,
            'error': str(e)
        }

def main():
    print("🔍 Verifying University Links...")
    print("=" * 60)
    
    working_links = []
    broken_links = []
    
    for university, url in UNIVERSITY_WEBSITES.items():
        print(f"Checking: {university}")
        print(f"URL: {url}")
        
        result = verify_link(url)
        
        if result['accessible']:
            print(f"✅ Status: {result['status']} - WORKING")
            working_links.append((university, url, result['final_url']))
        else:
            print(f"❌ Status: {result['status']} - BROKEN")
            print(f"Error: {result['error']}")
            broken_links.append((university, url, result['error']))
        
        print("-" * 40)
        time.sleep(1)  # Be respectful to servers
    
    print("\n📊 SUMMARY")
    print("=" * 60)
    print(f"✅ Working links: {len(working_links)}")
    print(f"❌ Broken links: {len(broken_links)}")
    
    if broken_links:
        print("\n🔧 BROKEN LINKS TO FIX:")
        for uni, url, error in broken_links:
            print(f"- {uni}: {url} ({error})")
    
    # Save results
    with open('link_verification_results.txt', 'w') as f:
        f.write("University Link Verification Results\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Working links: {len(working_links)}\n")
        f.write(f"Broken links: {len(broken_links)}\n\n")
        
        f.write("WORKING LINKS:\n")
        for uni, url, final_url in working_links:
            f.write(f"✅ {uni}: {url} -> {final_url}\n")
        
        f.write("\nBROKEN LINKS:\n")
        for uni, url, error in broken_links:
            f.write(f"❌ {uni}: {url} ({error})\n")
    
    print(f"\n📄 Results saved to: link_verification_results.txt")

if __name__ == "__main__":
    main()