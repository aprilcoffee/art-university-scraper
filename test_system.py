#!/usr/bin/env python3
"""
Comprehensive unit tests for Art University Job Scraper
Tests all functions and components to ensure they work properly
"""

import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch, MagicMock
import json

# Import the modules to test
from database import DatabaseManager
from scraper import ArtUniversityScraper
from app import app
from config import UNIVERSITIES, SEARCH_TERMS, SCRAPING_CONFIG, UNIVERSITIES_BY_COUNTRY
from utils import PositionBuilder, URLResolver, TextProcessor, SearchHelper, DatabaseHelper


class TestDatabaseManager(unittest.TestCase):
    """Test DatabaseManager functionality"""
    
    def setUp(self):
        """Set up test database"""
        self.test_db_path = tempfile.mktemp(suffix='.db')
        self.db = DatabaseManager(self.test_db_path)
    
    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.test_db_path):
            os.unlink(self.test_db_path)
    
    def test_database_initialization(self):
        """Test database initialization"""
        self.assertTrue(os.path.exists(self.test_db_path))
        
        # Check if tables exist
        with sqlite3.connect(self.test_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            self.assertIn('positions', tables)
            self.assertIn('universities', tables)
            self.assertIn('search_logs', tables)
    
    def test_add_position(self):
        """Test adding positions to database"""
        position_data = {
            'university': 'Test University',
            'title': 'Test Position',
            'description': 'Test Description',
            'url': 'https://test.com',
            'language': 'english',
            'date_found': '2024-01-01',
            'status': 'active',
            'category': 'job',
            'department': 'Test Department',
            'position_level': 'entry',
            'employment_details': 'Full-time'
        }
        
        result = self.db.add_position(position_data)
        self.assertTrue(result)
        
        # Check if position was added
        positions = self.db.get_positions()
        self.assertEqual(len(positions), 1)
        self.assertEqual(positions[0]['title'], 'Test Position')
    
    def test_get_positions(self):
        """Test retrieving positions"""
        # Add test positions
        test_positions = [
            {
                'university': 'Test University 1',
                'title': 'PhD Position',
                'description': 'PhD Description',
                'url': 'https://test1.com',
                'language': 'english',
                'date_found': '2024-01-01',
                'status': 'active',
                'category': 'phd',
                'department': None,
                'position_level': None,
                'employment_details': None
            },
            {
                'university': 'Test University 2',
                'title': 'Job Position',
                'description': 'Job Description',
                'url': 'https://test2.com',
                'language': 'german',
                'date_found': '2024-01-02',
                'status': 'active',
                'category': 'job',
                'department': None,
                'position_level': None,
                'employment_details': None
            }
        ]
        
        for pos in test_positions:
            self.db.add_position(pos)
        
        # Test get all positions
        all_positions = self.db.get_positions()
        self.assertEqual(len(all_positions), 2)
        
        # Test get PhD positions
        phd_positions = self.db.get_phd_positions()
        self.assertEqual(len(phd_positions), 1)
        self.assertEqual(phd_positions[0]['category'], 'phd')
        
        # Test get job positions
        job_positions = self.db.get_job_positions()
        self.assertEqual(len(job_positions), 1)
        self.assertEqual(job_positions[0]['category'], 'job')
    
    def test_search_positions(self):
        """Test searching positions"""
        # Add test position
        position_data = {
            'university': 'Test University',
            'title': 'Design Mitarbeiter Position',
            'description': 'Looking for design mitarbeiter',
            'url': 'https://test.com',
            'language': 'german',
            'date_found': '2024-01-01',
            'status': 'active',
            'category': 'job',
            'department': None,
            'position_level': None,
            'employment_details': None
        }
        
        self.db.add_position(position_data)
        
        # Test search
        results = self.db.search_positions('design')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Design Mitarbeiter Position')
        
        # Test search with filters
        results = self.db.search_positions('mitarbeiter', 'job')
        self.assertEqual(len(results), 1)
    
    def test_get_statistics(self):
        """Test getting database statistics"""
        # Add test positions
        test_positions = [
            {'university': 'Test Uni 1', 'title': 'PhD 1', 'description': 'PhD', 'url': 'https://test1.com', 'language': 'english', 'date_found': '2024-01-01', 'status': 'active', 'category': 'phd', 'department': None, 'position_level': None, 'employment_details': None},
            {'university': 'Test Uni 2', 'title': 'Job 1', 'description': 'Job', 'url': 'https://test2.com', 'language': 'german', 'date_found': '2024-01-02', 'status': 'active', 'category': 'job', 'department': None, 'position_level': None, 'employment_details': None},
            {'university': 'Test Uni 3', 'title': 'Job 2', 'description': 'Job', 'url': 'https://test3.com', 'language': 'english', 'date_found': '2024-01-03', 'status': 'active', 'category': 'job', 'department': None, 'position_level': None, 'employment_details': None}
        ]
        
        for pos in test_positions:
            self.db.add_position(pos)
        
        stats = self.db.get_statistics()
        
        self.assertEqual(stats['total_positions'], 3)
        self.assertEqual(stats['position_types']['phd'], 1)
        self.assertEqual(stats['position_types']['job'], 2)
        self.assertEqual(stats['languages']['english'], 2)
        self.assertEqual(stats['languages']['german'], 1)


class TestConfiguration(unittest.TestCase):
    """Test configuration validity"""
    
    def test_universities_configuration(self):
        """Test universities configuration"""
        self.assertGreater(len(UNIVERSITIES), 0, "No universities configured")
        
        # Check required fields
        required_fields = ['name', 'country', 'website', 'city']
        for uni in UNIVERSITIES:
            for field in required_fields:
                self.assertIn(field, uni, f"Missing field {field} in university: {uni.get('name', 'unknown')}")
        
        # Check if all universities in UNIVERSITIES_BY_COUNTRY are in UNIVERSITIES
        all_country_unis = []
        for country, unis in UNIVERSITIES_BY_COUNTRY.items():
            all_country_unis.extend(unis)
        
        for uni_name in all_country_unis:
            self.assertTrue(
                any(uni_name == uni['name'] for uni in UNIVERSITIES),
                f"University {uni_name} in UNIVERSITIES_BY_COUNTRY but not in UNIVERSITIES"
            )
    
    def test_search_terms_configuration(self):
        """Test search terms configuration"""
        self.assertIn('german', SEARCH_TERMS, "German search terms missing")
        self.assertIn('english', SEARCH_TERMS, "English search terms missing")
        
        # Check German terms
        german_terms = SEARCH_TERMS['german']
        self.assertIn('phd_programs', german_terms, "German PhD terms missing")
        self.assertIn('job_offers', german_terms, "German job terms missing")
        
        # Check English terms
        english_terms = SEARCH_TERMS['english']
        self.assertIn('phd_programs', english_terms, "English PhD terms missing")
        self.assertIn('job_offers', english_terms, "English job terms missing")
        
        # Check for design terms
        german_design_terms = [term for term in german_terms['job_offers']['mitarbeiter_stelle'] if 'design' in term]
        english_design_terms = [term for term in english_terms['job_offers']['artistic_staff'] if 'design' in term]
        
        self.assertGreater(len(german_design_terms), 0, "No German design terms found")
        self.assertGreater(len(english_design_terms), 0, "No English design terms found")
    
    def test_key_universities_present(self):
        """Test that key universities are present"""
        key_universities = [
            'Köln International School of Design (KISD)',
            'Technische Universität Berlin',
            'Technische Universität München',
            'RWTH Aachen',
            'Universität der Künste Berlin',
            'Royal College of Art',
            'Parsons School of Design'
        ]
        
        for uni_name in key_universities:
            self.assertTrue(
                any(uni_name.lower() in uni['name'].lower() for uni in UNIVERSITIES),
                f"Key university {uni_name} not found"
            )


class TestUtils(unittest.TestCase):
    """Test utility functions"""
    
    def test_position_builder(self):
        """Test PositionBuilder class"""
        builder = PositionBuilder('Test University', 'english', 'https://test.com')
        
        position = (builder
                   .set_basic_info('job', 'Test Position', 'Test Description', 'https://test.com')
                   .set_category('job_offer')
                   .build())
        
        self.assertEqual(position['university'], 'Test University')
        self.assertEqual(position['title'], 'Test Position')
        self.assertEqual(position['description'], 'Test Description')
        self.assertEqual(position['category'], 'job')
        self.assertEqual(position['language'], 'english')
        self.assertEqual(position['status'], 'active')
    
    def test_text_processor(self):
        """Test TextProcessor class"""
        processor = TextProcessor()
        
        # Test clean job title
        dirty_title = "  Test Job Title  \n  "
        clean_title = processor.clean_job_title(dirty_title)
        self.assertEqual(clean_title, "Test Job Title")
        
        # Test clean description
        dirty_desc = "Test description with   multiple   spaces"
        clean_desc = processor.clean_description(dirty_desc)
        self.assertEqual(clean_desc, "Test description with multiple spaces")
    
    def test_search_helper(self):
        """Test SearchHelper class"""
        # Test language detection
        german_text = "Wir suchen einen mitarbeiter"
        detected_lang = SearchHelper.detect_language(german_text)
        self.assertEqual(detected_lang, 'german')
        
        english_text = "We are looking for a staff member"
        detected_lang = SearchHelper.detect_language(english_text)
        self.assertEqual(detected_lang, 'english')
        
        # Test term search
        text = "We have PhD programs and job positions available"
        terms = ['phd', 'job', 'position']
        found_terms = SearchHelper.search_for_terms(text, terms)
        self.assertIn('phd', found_terms)
        self.assertIn('job', found_terms)
        self.assertIn('position', found_terms)


class TestFlaskApp(unittest.TestCase):
    """Test Flask application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
    
    def test_main_page(self):
        """Test main page loads"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_api_positions(self):
        """Test positions API"""
        response = self.app.get('/api/positions')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_api_phd_positions(self):
        """Test PhD positions API"""
        response = self.app.get('/api/phd-positions')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_api_job_positions(self):
        """Test job positions API"""
        response = self.app.get('/api/job-positions')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_api_search_positions(self):
        """Test search positions API"""
        # Test with search term
        response = self.app.get('/api/search-positions?search_term=mitarbeiter')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        
        # Test without search term (should return 400)
        response = self.app.get('/api/search-positions')
        self.assertEqual(response.status_code, 400)
    
    def test_api_statistics(self):
        """Test statistics API"""
        response = self.app.get('/api/statistics')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIn('total_positions', data)
        self.assertIn('position_types', data)
        self.assertIn('languages', data)
    
    def test_api_universities(self):
        """Test universities API"""
        response = self.app.get('/api/universities')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
    
    def test_api_universities_by_country(self):
        """Test universities by country API"""
        response = self.app.get('/api/universities-by-country')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('germany', data)
        self.assertIn('usa', data)


class TestScraper(unittest.TestCase):
    """Test scraper functionality"""
    
    @patch('scraper.requests.Session')
    def test_scraper_initialization(self, mock_session):
        """Test scraper initialization"""
        scraper = ArtUniversityScraper()
        self.assertIsNotNone(scraper.db)
        self.assertIsNotNone(scraper.session)
    
    def test_search_specific_terms_empty(self):
        """Test search_specific_terms with empty inputs"""
        scraper = ArtUniversityScraper()
        
        # Test with empty inputs
        results = scraper.search_specific_terms([], [])
        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), 0)
    
    def test_extract_text_content(self):
        """Test text content extraction"""
        scraper = ArtUniversityScraper()
        
        # Mock BeautifulSoup object
        mock_soup = MagicMock()
        mock_soup.get_text.return_value = "Test content with   multiple   spaces"
        
        # Remove script and style elements
        mock_soup.return_value = []
        
        text = scraper.extract_text_content(mock_soup)
        self.assertIsInstance(text, str)
    
    def test_detect_language(self):
        """Test language detection"""
        scraper = ArtUniversityScraper()
        
        # Test German text
        german_text = "Wir suchen einen mitarbeiter für unsere abteilung"
        lang = scraper._detect_language(german_text)
        self.assertEqual(lang, 'german')
        
        # Test English text
        english_text = "We are looking for a staff member for our department"
        lang = scraper._detect_language(english_text)
        self.assertEqual(lang, 'english')


class TestIntegration(unittest.TestCase):
    """Test integration between components"""
    
    def setUp(self):
        """Set up test database"""
        self.test_db_path = tempfile.mktemp(suffix='.db')
        self.db = DatabaseManager(self.test_db_path)
    
    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.test_db_path):
            os.unlink(self.test_db_path)
    
    def test_end_to_end_workflow(self):
        """Test complete workflow from scraping to API"""
        # Test adding position
        position_data = {
            'university': 'Test University',
            'title': 'Test Position',
            'description': 'Test Description',
            'url': 'https://test.com',
            'language': 'english',
            'date_found': '2024-01-01',
            'status': 'active',
            'category': 'job',
            'department': None,
            'position_level': None,
            'employment_details': None
        }
        
        # Add position
        result = self.db.add_position(position_data)
        self.assertTrue(result)
        
        # Test API retrieval
        app_client = app.test_client()
        response = app_client.get('/api/positions')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Position')
        
        # Test search API
        response = app_client.get('/api/search-positions?search_term=test')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertEqual(len(data), 1)
    
    def test_data_consistency(self):
        """Test data consistency across different operations"""
        # Add test positions
        test_positions = [
            {'university': 'Test Uni 1', 'title': 'PhD 1', 'description': 'PhD', 'url': 'https://test1.com', 'language': 'english', 'date_found': '2024-01-01', 'status': 'active', 'category': 'phd', 'department': None, 'position_level': None, 'employment_details': None},
            {'university': 'Test Uni 2', 'title': 'Job 1', 'description': 'Job', 'url': 'https://test2.com', 'language': 'german', 'date_found': '2024-01-02', 'status': 'active', 'category': 'job', 'department': None, 'position_level': None, 'employment_details': None}
        ]
        
        for pos in test_positions:
            self.db.add_position(pos)
        
        # Test consistency
        total_positions = len(self.db.get_positions())
        phd_positions = len(self.db.get_phd_positions())
        job_positions = len(self.db.get_job_positions())
        
        self.assertEqual(total_positions, phd_positions + job_positions)
        self.assertEqual(total_positions, 2)
        self.assertEqual(phd_positions, 1)
        self.assertEqual(job_positions, 1)


def run_tests():
    """Run all tests"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestDatabaseManager,
        TestConfiguration,
        TestUtils,
        TestFlaskApp,
        TestScraper,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=== RUNNING COMPREHENSIVE UNIT TESTS ===")
    success = run_tests()
    
    if success:
        print("\n🎯 ALL TESTS PASSED! SYSTEM IS WORKING CORRECTLY!")
    else:
        print("\n❌ SOME TESTS FAILED! CHECK THE OUTPUT ABOVE.")