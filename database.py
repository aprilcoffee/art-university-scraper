"""
Database management for the Art University Job Scraper
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging

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
                        position_type TEXT NOT NULL,
                        title TEXT NOT NULL,
                        description TEXT,
                        url TEXT NOT NULL,
                        language TEXT NOT NULL,
                        date_found TEXT NOT NULL,
                        status TEXT DEFAULT 'active',
                        position_category TEXT,
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
                
                # Convert employment_details dict to JSON string
                employment_details_json = None
                if 'employment_details' in position_data and position_data['employment_details']:
                    import json
                    employment_details_json = json.dumps(position_data['employment_details'])
                
                cursor.execute('''
                    INSERT INTO positions (university, position_type, title, description, url, language, date_found, status, 
                                         position_category, department, position_level, employment_details)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    position_data['university'],
                    position_data['position_type'],
                    position_data['title'],
                    position_data['description'],
                    position_data['url'],
                    position_data['language'],
                    position_data['date_found'],
                    position_data.get('status', 'active'),
                    position_data.get('position_category'),
                    position_data.get('department'),
                    position_data.get('position_level'),
                    employment_details_json
                ))
                
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
                    
                    if 'position_type' in filters:
                        query += " AND position_type = ?"
                        params.append(filters['position_type'])
                    
                    if 'language' in filters:
                        query += " AND language = ?"
                        params.append(filters['language'])
                    
                    if 'status' in filters:
                        query += " AND status = ?"
                        params.append(filters['status'])
                
                query += " ORDER BY created_at DESC"
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Error retrieving positions: {e}")
            return []
    
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
                
                # Count positions by type
                cursor.execute('SELECT position_type, COUNT(*) FROM positions GROUP BY position_type')
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
                    WHERE created_at < datetime('now', '-{} days')
                '''.format(days_old))
                
                deleted_count = cursor.rowcount
                conn.commit()
                
                logger.info(f"Cleared {deleted_count} old positions")
                return deleted_count
                
        except Exception as e:
            logger.error(f"Error clearing old positions: {e}")
            return 0