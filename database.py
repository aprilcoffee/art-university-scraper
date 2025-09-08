"""
Database management for the Art University Job Scraper
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging
from utils import DatabaseHelper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, db_path: str = "art_positions.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create positions table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS positions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        university TEXT NOT NULL,
                        title TEXT NOT NULL,
                        description TEXT,
                        url TEXT NOT NULL,
                        language TEXT NOT NULL,
                        date_found TEXT NOT NULL,
                        status TEXT DEFAULT 'active',
                        category TEXT NOT NULL,
                        department TEXT,
                        position_level TEXT,
                        employment_details TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create universities table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS universities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        city TEXT NOT NULL,
                        country TEXT NOT NULL,
                        website TEXT NOT NULL,
                        has_phd BOOLEAN NOT NULL,
                        last_scraped TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create search_logs table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS search_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        university TEXT NOT NULL,
                        search_term TEXT NOT NULL,
                        results_count INTEGER DEFAULT 0,
                        search_date TEXT NOT NULL,
                        status TEXT DEFAULT 'success'
                    )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
                
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            raise
    
    def add_position(self, position_data: Dict) -> bool:
        """Add a new position to the database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if position already exists
                cursor.execute('''
                    SELECT id FROM positions 
                    WHERE university = ? AND title = ? AND url = ?
                ''', (position_data['university'], position_data['title'], position_data['url']))
                
                if cursor.fetchone():
                    logger.info(f"Position already exists: {position_data['title']}")
                    return False
                
                # Prepare position data for database insertion
                prepared_data = DatabaseHelper.prepare_position_for_db(position_data)
                
                # Get field names and values
                fields = DatabaseHelper.get_position_fields()
                values = [prepared_data.get(field) for field in fields]
                
                cursor.execute(f'''
                    INSERT INTO positions ({', '.join(fields)})
                    VALUES ({', '.join(['?' for _ in fields])})
                ''', values)
                
                conn.commit()
                logger.info(f"Added new position: {position_data['title']}")
                return True
                
        except Exception as e:
            logger.error(f"Error adding position: {e}")
            return False
    
    def get_positions(self, filters: Optional[Dict] = None) -> List[Dict]:
        """Retrieve positions with optional filters"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = "SELECT * FROM positions WHERE 1=1"
                params = []
                
                if filters:
                    if 'university' in filters:
                        query += " AND university LIKE ?"
                        params.append(f"%{filters['university']}%")
                    
                    if 'category' in filters:
                        query += " AND category = ?"
                        params.append(filters['category'])
                    
                    if 'language' in filters:
                        query += " AND language = ?"
                        params.append(filters['language'])
                    
                    if 'status' in filters:
                        query += " AND status = ?"
                        params.append(filters['status'])
                    
                    if 'search_term' in filters:
                        query += " AND (title LIKE ? OR description LIKE ?)"
                        search_term = f"%{filters['search_term']}%"
                        params.extend([search_term, search_term])
                    
                
                query += " ORDER BY created_at DESC"
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Error retrieving positions: {e}")
            return []
    
    def search_positions(self, search_term: str, position_type: str = None, university: str = None) -> List[Dict]:
        """Search for positions with specific terms"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = """
                    SELECT * FROM positions 
                    WHERE (title LIKE ? OR description LIKE ?)
                """
                params = [f"%{search_term}%", f"%{search_term}%"]
                
                if position_type:
                    query += " AND category = ?"
                    params.append(position_type)
                
                if university:
                    query += " AND university LIKE ?"
                    params.append(f"%{university}%")
                
                query += " ORDER BY created_at DESC"
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Error searching positions: {e}")
            return []
    
    def get_phd_positions(self, university: str = None, search_term: str = None) -> List[Dict]:
        """Get PhD positions with optional filters"""
        filters = {'category': 'phd'}
        if university:
            filters['university'] = university
        if search_term:
            filters['search_term'] = search_term
        return self.get_positions(filters)
    
    def get_job_positions(self, university: str = None, search_term: str = None) -> List[Dict]:
        """Get job positions with optional filters"""
        filters = {'category': 'job'}
        if university:
            filters['university'] = university
        if search_term:
            filters['search_term'] = search_term
        return self.get_positions(filters)
    
    def update_university_scrape_time(self, university_name: str):
        """Update the last scraped time for a university"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    UPDATE universities 
                    SET last_scraped = ? 
                    WHERE name = ?
                ''', (datetime.now().isoformat(), university_name))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error updating university scrape time: {e}")
    
    def log_search(self, university: str, search_term: str, results_count: int, status: str = 'success'):
        """Log a search operation"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO search_logs (university, search_term, results_count, search_date, status)
                    VALUES (?, ?, ?, ?, ?)
                ''', (university, search_term, results_count, datetime.now().isoformat(), status))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error logging search: {e}")
    
    def get_statistics(self) -> Dict:
        """Get database statistics"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Count positions by category
                cursor.execute('SELECT category, COUNT(*) FROM positions GROUP BY category')
                position_types = dict(cursor.fetchall())
                
                # Count positions by language
                cursor.execute('SELECT language, COUNT(*) FROM positions GROUP BY language')
                languages = dict(cursor.fetchall())
                
                # Count positions by university
                cursor.execute('SELECT university, COUNT(*) FROM positions GROUP BY university ORDER BY COUNT(*) DESC LIMIT 10')
                top_universities = dict(cursor.fetchall())
                
                # Total positions
                cursor.execute('SELECT COUNT(*) FROM positions')
                total_positions = cursor.fetchone()[0]
                
                return {
                    'total_positions': total_positions,
                    'position_types': position_types,
                    'languages': languages,
                    'top_universities': top_universities
                }
                
        except Exception as e:
            logger.error(f"Error getting statistics: {e}")
            return {}
    
    def clear_old_positions(self, days_old: int = 30):
        """Remove positions older than specified days"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    DELETE FROM positions 
                    WHERE created_at < datetime('now', '-? days')
                ''', (days_old,))
                
                deleted_count = cursor.rowcount
                conn.commit()
                
                logger.info(f"Cleared {deleted_count} old positions")
                return deleted_count
                
        except Exception as e:
            logger.error(f"Error clearing old positions: {e}")
            return 0