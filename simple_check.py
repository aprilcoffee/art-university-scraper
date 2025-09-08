#!/usr/bin/env python3
import requests
from config import UNIVERSITY_WEBSITES

print("Testing links...")

# Test first 5 links
count = 0
for uni, url in list(UNIVERSITY_WEBSITES.items())[:5]:
    try:
        response = requests.get(url, timeout=5)
        print(f"✅ {uni}: {response.status_code}")
    except Exception as e:
        print(f"❌ {uni}: {e}")
    count += 1

print(f"Tested {count} links")