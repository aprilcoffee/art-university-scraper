#!/usr/bin/env python3
"""
Data cleaning script for Art University Job Scraper
Cleans the database to focus only on PhD and job positions
"""

import sqlite3
import re
from typing import List, Dict, Set
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCleaner:
    def __init__(self, db_path: str = "art_positions.db"):
        self.db_path = db_path
        
        # Define non-position content indicators
        self.non_position_indicators = {
            'exhibition_terms': [
                'exhibition', 'ausstellung', 'expo', 'show', 'schau', 'display', 'zeigen', 'präsentieren',
                'stellen aus', 'put on display', 'ausstellen', 'exhibit', 'exhibiting', 'klasse knapp',
                'klasse reisch', 'student exhibition', 'studentenausstellung', 'student show', 'studentenschau'
            ],
            'student_work_terms': [
                'student work', 'studentenarbeit', 'student project', 'studentenprojekt',
                'student exhibition', 'studentenausstellung', 'student show', 'studentenschau',
                'alumni', 'alumnus', 'absolvent', 'graduate', 'graduation', 'klasse', 'class',
                'studierende gestalten', 'students create', 'studierende ausstellung'
            ],
            'events_terms': [
                'event', 'veranstaltung', 'conference', 'konferenz', 'symposium',
                'workshop', 'seminar', 'vortrag', 'lecture', 'talk', 'visit', 'besuch',
                'opening', 'eröffnung', 'closing', 'schließung', 'kooperation', 'cooperation',
                'collaboration', 'zusammenarbeit', 'küchengespräche', 'kitchen conversations'
            ],
            'publications_terms': [
                'publication', 'publikation', 'book', 'buch', 'journal', 'zeitschrift',
                'research catalogue', 'forschungsverzeichnis', 'research catalog',
                'catalogue', 'katalog', 'verzeichnis', 'directory'
            ],
            'cultural_terms': [
                'gallery', 'galerie', 'museum', 'collection', 'sammlung',
                'cultural', 'kulturell', 'cultural institution', 'kultureinrichtung'
            ],
            'news_terms': [
                'news', 'nachrichten', 'announcement', 'ankündigung', 'meldung',
                'press release', 'pressemitteilung', 'press', 'presse'
            ],
            'academic_programs_terms': [
                'program', 'programm', 'course', 'kurs', 'studium', 'study',
                'curriculum', 'lehrplan', 'syllabus', 'bewerbung', 'application',
                'bewerbungsprozess', 'application process', 'zulassung', 'admission'
            ],
            'construction_terms': [
                'baustelle', 'construction site', 'demokratie', 'democracy',
                'wasserstoff', 'hydrogen', 'tankstellen', 'fuel stations'
            ],
            'practice_terms': [
                'praxispartner', 'practice partner', 'praxis', 'practice',
                'vaude', 'visual exchange', 'kunstprojekt', 'art project'
            ],
            'administrative_terms': [
                'interne meldestelle', 'internal reporting office', 'hinweisgeberschutz',
                'whistleblower protection', 'justiziariat', 'legal department',
                'fakultät', 'faculty', 'darstellende kunst', 'performing arts'
            ]
        }
        
        # Define valid position indicators
        self.valid_position_indicators = {
            'phd_terms': [
                'phd', 'promotion', 'doktorand', 'doktorat', 'doctorate', 'doctoral',
                'graduate program', 'graduiertenschule', 'doktorandenprogramm',
                'promotionsprogramm', 'research', 'forschung', 'artistic research',
                'künstlerische forschung', 'practice-based phd', 'praxis-basierte forschung',
                'practice-led research', 'artistic practice phd', 'creative research phd',
                'dfa', 'doctor of fine arts', 'studio-based research', 'research through practice',
                'practice as research', 'creative practice phd', 'interdisciplinary research'
            ],
            'job_terms': [
                'mitarbeiter', 'assistant', 'assistent', 'staff', 'fellow', 'coordinator',
                'technician', 'collaborator', 'associate', 'manager', 'director',
                'specialist', 'curator', 'educator', 'freelance', 'contract', 'temporary',
                'part-time', 'full-time', 'stellenausschreibung', 'job', 'position',
                'vacancy', 'employment', 'career', 'karriere', 'bewerbung', 'application',
                'stellen', 'jobs', 'stellenangebote', 'job offers', 'academic staff',
                'research staff', 'artistic staff', 'media art', 'ai art', 'sound art',
                'klangkunst', 'performance art', 'aufführungskunst', 'interactive art',
                'interaktive kunst', 'medienkunst', 'ki-kunst'
            ]
        }
    
    def is_non_position_content(self, text: str) -> bool:
        """Check if content is not about job positions"""
        text_lower = text.lower()
        
        # Count non-position indicators
        non_position_count = 0
        for category, terms in self.non_position_indicators.items():
            for term in terms:
                if term in text_lower:
                    non_position_count += 1
        
        # Check for specific problematic patterns
        problematic_patterns = [
            r'ausstellung.*student', r'student.*ausstellung', r'exhibition.*student',
            r'klasse.*stellen', r'class.*display', r'alumni.*stellen', r'graduate.*show',
            r'stellen.*aus', r'display.*work', r'show.*work', r'exhibit.*work',
            r'kooperation.*mit', r'cooperation.*with', r'zusammenarbeit.*mit',
            r'exhibition.*opening', r'research.*catalogue', r'graduation.*show',
            r'publication.*release', r'event.*announcement', r'bewerbung.*guide',
            r'application.*process', r'zulassung.*überblick', r'admission.*overview'
        ]
        
        pattern_matches = sum(1 for pattern in problematic_patterns if re.search(pattern, text_lower))
        
        # Consider it non-position content if it has multiple indicators or pattern matches
        return non_position_count >= 2 or pattern_matches >= 1
    
    def is_valid_position_content(self, text: str) -> bool:
        """Check if content is about valid job positions or PhD programs"""
        text_lower = text.lower()
        
        # Check for valid position indicators
        valid_count = 0
        for category, terms in self.valid_position_indicators.items():
            for term in terms:
                if term in text_lower:
                    valid_count += 1
        
        # Must have at least one valid position indicator
        return valid_count >= 1
    
    def clean_title(self, title: str) -> str:
        """Clean and normalize position titles"""
        if not title:
            return ""
        
        # Remove common prefixes/suffixes that don't add value
        title = re.sub(r'^(job opportunity link:|found.*related content|position related to:)', '', title, flags=re.IGNORECASE)
        title = re.sub(r'\s+', ' ', title).strip()
        
        # Truncate very long titles
        if len(title) > 200:
            title = title[:197] + "..."
        
        return title
    
    def clean_description(self, description: str) -> str:
        """Clean and normalize position descriptions"""
        if not description:
            return ""
        
        # Remove HTML-like content and excessive whitespace
        description = re.sub(r'<[^>]+>', '', description)
        description = re.sub(r'\s+', ' ', description).strip()
        
        # Truncate very long descriptions
        if len(description) > 1000:
            description = description[:997] + "..."
        
        return description
    
    def categorize_position(self, title: str, description: str) -> str:
        """Categorize position as PhD or Job"""
        text = f"{title} {description}".lower()
        
        # Check for PhD indicators
        phd_indicators = self.valid_position_indicators['phd_terms']
        if any(indicator in text for indicator in phd_indicators):
            return 'phd'
        
        # Check for job indicators
        job_indicators = self.valid_position_indicators['job_terms']
        if any(indicator in text for indicator in job_indicators):
            return 'job'
        
        # Default to job if unclear
        return 'job'
    
    def clean_database(self) -> Dict[str, int]:
        """Clean the database and return statistics"""
        stats = {
            'total_before': 0,
            'removed_non_positions': 0,
            'removed_duplicates': 0,
            'cleaned_positions': 0,
            'phd_positions': 0,
            'job_positions': 0,
            'total_after': 0
        }
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get total count before cleaning
                cursor.execute("SELECT COUNT(*) FROM positions")
                stats['total_before'] = cursor.fetchone()[0]
                
                logger.info(f"Starting data cleaning. Total positions before: {stats['total_before']}")
                
                # Get all positions
                cursor.execute("SELECT id, title, description, position_type FROM positions")
                positions = cursor.fetchall()
                
                # Track positions to keep
                positions_to_keep = []
                seen_titles = set()
                
                for pos_id, title, description, position_type in positions:
                    # Clean title and description
                    clean_title = self.clean_title(title)
                    clean_description = self.clean_description(description)
                    
                    # Skip if content is not about positions
                    full_text = f"{clean_title} {clean_description}"
                    if self.is_non_position_content(full_text):
                        stats['removed_non_positions'] += 1
                        continue
                    
                    # Skip if not valid position content
                    if not self.is_valid_position_content(full_text):
                        stats['removed_non_positions'] += 1
                        continue
                    
                    # Skip duplicates based on title similarity
                    title_key = clean_title.lower().strip()
                    if title_key in seen_titles:
                        stats['removed_duplicates'] += 1
                        continue
                    seen_titles.add(title_key)
                    
                    # Categorize position
                    category = self.categorize_position(clean_title, clean_description)
                    
                    # Update position
                    cursor.execute("""
                        UPDATE positions 
                        SET title = ?, description = ?, position_type = ?, position_category = ?
                        WHERE id = ?
                    """, (clean_title, clean_description, category, category, pos_id))
                    
                    positions_to_keep.append(pos_id)
                    stats['cleaned_positions'] += 1
                    
                    if category == 'phd':
                        stats['phd_positions'] += 1
                    else:
                        stats['job_positions'] += 1
                
                # Remove positions that weren't kept
                if positions_to_keep:
                    placeholders = ','.join(['?' for _ in positions_to_keep])
                    cursor.execute(f"DELETE FROM positions WHERE id NOT IN ({placeholders})", positions_to_keep)
                else:
                    cursor.execute("DELETE FROM positions")
                
                # Get final count
                cursor.execute("SELECT COUNT(*) FROM positions")
                stats['total_after'] = cursor.fetchone()[0]
                
                conn.commit()
                
                logger.info("Data cleaning completed successfully")
                logger.info(f"Statistics: {stats}")
                
                return stats
                
        except Exception as e:
            logger.error(f"Error cleaning database: {e}")
            raise
    
    def create_clean_position_types(self):
        """Create clean position type categories"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Update position types to be cleaner
                cursor.execute("UPDATE positions SET position_type = 'phd' WHERE position_type IN ('general_phd', 'artistic_research_phd')")
                cursor.execute("UPDATE positions SET position_type = 'job' WHERE position_type IN ('general_jobs', 'academic_staff')")
                
                conn.commit()
                logger.info("Position types updated successfully")
                
        except Exception as e:
            logger.error(f"Error updating position types: {e}")
            raise

def main():
    """Main function to run data cleaning"""
    cleaner = DataCleaner()
    
    print("Starting data cleaning process...")
    print("This will:")
    print("1. Remove non-position content (exhibitions, student work, etc.)")
    print("2. Remove duplicate positions")
    print("3. Clean and normalize titles and descriptions")
    print("4. Categorize positions as 'phd' or 'job'")
    print("5. Update position types")
    print()
    
    # Auto-proceed with cleaning
    print("Proceeding with data cleaning...")
    
    try:
        # Clean the database
        stats = cleaner.clean_database()
        
        # Update position types
        cleaner.create_clean_position_types()
        
        print("\nData cleaning completed successfully!")
        print(f"Total positions before: {stats['total_before']}")
        print(f"Total positions after: {stats['total_after']}")
        print(f"Removed non-positions: {stats['removed_non_positions']}")
        print(f"Removed duplicates: {stats['removed_duplicates']}")
        print(f"Cleaned positions: {stats['cleaned_positions']}")
        print(f"PhD positions: {stats['phd_positions']}")
        print(f"Job positions: {stats['job_positions']}")
        
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        logger.error(f"Data cleaning failed: {e}")

if __name__ == "__main__":
    main()