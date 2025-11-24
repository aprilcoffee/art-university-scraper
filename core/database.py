"""
Database manager for the art university job scraper.
Supports incremental scraping with content change tracking.
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
from .models import Position, UniversityJobPage, ScrapingLog


class DatabaseManager:
    """Manages SQLite database operations for the scraper."""

    def __init__(self, db_path='art_positions.db'):
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        """Get database connection."""
        return sqlite3.connect(self.db_path)

    def init_database(self):
        """Initialize database schema."""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Positions table - stores found job positions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS positions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                position_type TEXT NOT NULL,
                description TEXT,
                language TEXT DEFAULT 'de',
                deadline TEXT,
                department TEXT,
                found_date TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # University job pages table - tracks page content changes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS university_job_pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL UNIQUE,
                job_page_url TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                last_scraped TEXT NOT NULL,
                last_modified TEXT NOT NULL,
                positions_count INTEGER DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Scraping logs table - tracks scraping operations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scraping_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                university_name TEXT NOT NULL,
                status TEXT NOT NULL,
                message TEXT,
                positions_found INTEGER DEFAULT 0,
                timestamp TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create indexes for better performance
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_positions_university ON positions(university_name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_positions_type ON positions(position_type)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_positions_active ON positions(is_active)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_job_pages_university ON university_job_pages(university_name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_logs_university ON scraping_logs(university_name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_logs_timestamp ON scraping_logs(timestamp)')

        conn.commit()
        conn.close()

    def add_position(self, position: Position) -> bool:
        """Add a new position to the database. Returns True if added, False if duplicate."""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            data = position.to_dict()
            cursor.execute('''
                INSERT INTO positions
                (university_name, title, url, position_type, description,
                 language, deadline, department, found_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['university_name'],
                data['title'],
                data['url'],
                data['position_type'],
                data['description'],
                data['language'],
                data['deadline'],
                data['department'],
                data['found_date'],
            ))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Duplicate URL
            return False
        finally:
            conn.close()

    def update_job_page(self, job_page: UniversityJobPage):
        """Update or insert university job page tracking info."""
        conn = self.get_connection()
        cursor = conn.cursor()

        data = job_page.to_dict()
        cursor.execute('''
            INSERT OR REPLACE INTO university_job_pages
            (university_name, job_page_url, content_hash, last_scraped,
             last_modified, positions_count, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['university_name'],
            data['job_page_url'],
            data['content_hash'],
            data['last_scraped'],
            data['last_modified'],
            data['positions_count'],
            data['is_active'],
        ))

        conn.commit()
        conn.close()

    def get_job_page_info(self, university_name: str) -> Optional[Dict]:
        """Get job page tracking info for a university."""
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM university_job_pages
            WHERE university_name = ?
        ''', (university_name,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)
        return None

    def add_log(self, log: ScrapingLog):
        """Add a scraping log entry."""
        conn = self.get_connection()
        cursor = conn.cursor()

        data = log.to_dict()
        cursor.execute('''
            INSERT INTO scraping_logs
            (university_name, status, message, positions_found, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['university_name'],
            data['status'],
            data['message'],
            data['positions_found'],
            data['timestamp'],
        ))

        conn.commit()
        conn.close()

    def get_positions(
        self,
        university_name: Optional[str] = None,
        position_type: Optional[str] = None,
        active_only: bool = True,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """Get positions with optional filters."""
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = 'SELECT * FROM positions WHERE 1=1'
        params = []

        if university_name:
            query += ' AND university_name = ?'
            params.append(university_name)

        if position_type:
            query += ' AND position_type = ?'
            params.append(position_type)

        if active_only:
            query += ' AND is_active = 1'

        query += ' ORDER BY found_date DESC'

        if limit:
            query += ' LIMIT ?'
            params.append(limit)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_statistics(self) -> Dict:
        """Get database statistics."""
        conn = self.get_connection()
        cursor = conn.cursor()

        stats = {}

        # Total positions
        cursor.execute('SELECT COUNT(*) FROM positions WHERE is_active = 1')
        stats['total_positions'] = cursor.fetchone()[0]

        # Positions by type
        cursor.execute('''
            SELECT position_type, COUNT(*)
            FROM positions
            WHERE is_active = 1
            GROUP BY position_type
        ''')
        stats['by_type'] = dict(cursor.fetchall())

        # Positions by university
        cursor.execute('''
            SELECT university_name, COUNT(*)
            FROM positions
            WHERE is_active = 1
            GROUP BY university_name
            ORDER BY COUNT(*) DESC
            LIMIT 10
        ''')
        stats['top_universities'] = dict(cursor.fetchall())

        # Recent scraping activity
        cursor.execute('''
            SELECT COUNT(*)
            FROM scraping_logs
            WHERE timestamp > datetime('now', '-7 days')
        ''')
        stats['recent_scrapes'] = cursor.fetchone()[0]

        conn.close()
        return stats

    def mark_position_inactive(self, url: str):
        """Mark a position as inactive (e.g., expired)."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE positions
            SET is_active = 0
            WHERE url = ?
        ''', (url,))

        conn.commit()
        conn.close()

    def get_recent_logs(self, limit: int = 50) -> List[Dict]:
        """Get recent scraping logs."""
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM scraping_logs
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]
