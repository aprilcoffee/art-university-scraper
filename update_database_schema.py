#!/usr/bin/env python3
"""
Update database schema to remove position_type and simplify structure
"""

import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_database_schema():
    """Update database schema to remove position_type and simplify"""
    try:
        with sqlite3.connect("art_positions.db") as conn:
            cursor = conn.cursor()
            
            # Create new simplified positions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS positions_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    university TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    url TEXT NOT NULL,
                    language TEXT NOT NULL,
                    date_found TEXT NOT NULL,
                    status TEXT DEFAULT 'active',
                    category TEXT NOT NULL,  -- 'phd' or 'job'
                    department TEXT,
                    position_level TEXT,
                    employment_details TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Copy data from old table to new table
            cursor.execute('''
                INSERT INTO positions_new (
                    id, university, title, description, url, language, 
                    date_found, status, category, department, position_level, 
                    employment_details, created_at
                )
                SELECT 
                    id, university, title, description, url, language,
                    date_found, status, position_type as category, department, 
                    position_level, employment_details, created_at
                FROM positions
            ''')
            
            # Drop old table
            cursor.execute('DROP TABLE positions')
            
            # Rename new table
            cursor.execute('ALTER TABLE positions_new RENAME TO positions')
            
            conn.commit()
            logger.info("Database schema updated successfully")
            
            # Verify the update
            cursor.execute("SELECT COUNT(*) FROM positions")
            count = cursor.fetchone()[0]
            logger.info(f"Total positions after schema update: {count}")
            
            cursor.execute("SELECT category, COUNT(*) FROM positions GROUP BY category")
            categories = cursor.fetchall()
            logger.info(f"Categories: {categories}")
            
    except Exception as e:
        logger.error(f"Error updating database schema: {e}")
        raise

if __name__ == "__main__":
    update_database_schema()