#!/usr/bin/env python3
"""
Setup script for the Art University Job Scraper
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements: {e}")
        return False

def check_chrome():
    """Check if Chrome is installed"""
    print("Checking for Chrome browser...")
    try:
        # Try to find Chrome executable
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
            "/usr/bin/google-chrome",  # Linux
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",  # Windows
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"  # Windows 32-bit
        ]
        
        for path in chrome_paths:
            if os.path.exists(path):
                print("✓ Chrome browser found")
                return True
        
        print("⚠ Chrome browser not found. Please install Google Chrome for full functionality.")
        return False
    except Exception as e:
        print(f"✗ Error checking Chrome: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    directories = ["logs", "exports", "data"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created directory: {directory}")
        else:
            print(f"✓ Directory exists: {directory}")

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    required_modules = [
        "requests",
        "beautifulsoup4",
        "selenium",
        "pandas",
        "flask",
        "flask_cors"
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            if module == "beautifulsoup4":
                __import__("bs4")
            elif module == "flask_cors":
                __import__("flask_cors")
            else:
                __import__(module)
            print(f"✓ {module}")
        except ImportError:
            print(f"✗ {module}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\nFailed to import: {', '.join(failed_imports)}")
        return False
    
    print("✓ All imports successful")
    return True

def main():
    print("=" * 50)
    print("Art University Job Scraper Setup")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        print("\nSetup failed: Could not install requirements")
        return False
    
    # Check Chrome
    check_chrome()
    
    # Create directories
    create_directories()
    
    # Test imports
    if not test_imports():
        print("\nSetup failed: Import errors")
        return False
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("=" * 50)
    print("\nTo start the web interface:")
    print("  python main.py --mode web")
    print("\nThen open your browser to: http://localhost:5000")
    print("\nFor command line usage:")
    print("  python main.py --mode scrape")
    print("  python main.py --mode test")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)