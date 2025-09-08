"""
Flask web application for the Art University Job Scraper
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
from datetime import datetime
import threading
import time

from database import DatabaseManager
from scraper import ArtUniversityScraper
from config import UNIVERSITIES_BY_COUNTRY, UNIVERSITIES

app = Flask(__name__)
CORS(app)

# Global variables
db = DatabaseManager()
scraper = None
scraping_status = {'running': False, 'progress': 0, 'total': 0, 'current': '', 'results': {}}

@app.route('/')
def index():
    """Main dashboard page"""
    stats = db.get_statistics()
    return render_template('index.html', stats=stats)

@app.route('/api/positions')
def get_positions():
    """API endpoint to get positions with optional filters"""
    filters = {}
    
    if request.args.get('university'):
        filters['university'] = request.args.get('university')
    
    if request.args.get('category'):
        filters['category'] = request.args.get('category')
    
    if request.args.get('language'):
        filters['language'] = request.args.get('language')
    
    if request.args.get('status'):
        filters['status'] = request.args.get('status')
    
    if request.args.get('search_term'):
        filters['search_term'] = request.args.get('search_term')
    
    positions = db.get_positions(filters)
    return jsonify(positions)

@app.route('/api/phd-positions')
def get_phd_positions():
    """API endpoint to get PhD positions with optional filters"""
    university = request.args.get('university')
    search_term = request.args.get('search_term')
    
    positions = db.get_phd_positions(university, search_term)
    return jsonify(positions)

@app.route('/api/job-positions')
def get_job_positions():
    """API endpoint to get job positions with optional filters"""
    university = request.args.get('university')
    search_term = request.args.get('search_term')
    
    positions = db.get_job_positions(university, search_term)
    return jsonify(positions)

@app.route('/api/search-positions')
def search_positions():
    """API endpoint to search for positions with specific terms"""
    search_term = request.args.get('search_term')
    category = request.args.get('category')
    university = request.args.get('university')
    
    if not search_term:
        return jsonify({'error': 'search_term parameter is required'}), 400
    
    positions = db.search_positions(search_term, category, university)
    return jsonify(positions)

@app.route('/api/universities')
def get_universities():
    """API endpoint to get list of universities"""
    return jsonify(UNIVERSITIES)

@app.route('/api/universities-by-country')
def get_universities_by_country():
    """API endpoint to get universities organized by country"""
    return jsonify(UNIVERSITIES_BY_COUNTRY)

@app.route('/api/universities/<country>')
def get_universities_by_country_specific(country):
    """API endpoint to get universities from a specific country"""
    if country in UNIVERSITIES_BY_COUNTRY:
        return jsonify(UNIVERSITIES_BY_COUNTRY[country])
    else:
        return jsonify({'error': 'Country not found'}), 404

@app.route('/api/statistics')
def get_statistics():
    """API endpoint to get database statistics"""
    stats = db.get_statistics()
    return jsonify(stats)

@app.route('/api/start-scraping', methods=['POST'])
def start_scraping():
    """Start the scraping process"""
    global scraper, scraping_status
    
    if scraping_status['running']:
        return jsonify({'error': 'Scraping is already running'}), 400
    
    try:
        scraper = ArtUniversityScraper()
        scraping_status['running'] = True
        scraping_status['progress'] = 0
        scraping_status['total'] = len(UNIVERSITIES)
        scraping_status['current'] = ''
        scraping_status['results'] = {}
        
        # Start scraping in a separate thread
        thread = threading.Thread(target=run_scraping)
        thread.daemon = True
        thread.start()
        
        return jsonify({'message': 'Scraping started successfully'})
        
    except Exception as e:
        scraping_status['running'] = False
        return jsonify({'error': str(e)}), 500

@app.route('/api/scraping-status')
def get_scraping_status():
    """Get current scraping status"""
    return jsonify(scraping_status)

@app.route('/api/search-specific', methods=['POST'])
def search_specific():
    """Search for specific terms"""
    global scraper
    
    data = request.get_json()
    terms = data.get('terms', [])
    universities = data.get('universities', [])
    
    if not scraper:
        scraper = ArtUniversityScraper()
    
    try:
        results = scraper.search_specific_terms(universities, terms)
        return jsonify({'results': results})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search-phd-specific', methods=['POST'])
def search_phd_specific():
    """Search specifically for PhD programs"""
    global scraper
    
    data = request.get_json()
    universities = data.get('universities', [])
    
    # Focus on PhD-specific terms
    phd_terms = [
        'media art phd', 'ai art phd', 'artistic research phd',
        'medienkunst promotion', 'ki-kunst promotion', 'klangkunst promotion',
        'practice-based phd', 'künstlerische forschung', 'praxis-basierte forschung',
        'practice-led research', 'artistic practice phd', 'creative research phd',
        'dfa', 'doctor of fine arts', 'studio-based research', 
        'research through practice', 'practice as research',
        'creative practice phd', 'interdisciplinary research'
    ]
    
    if not scraper:
        scraper = ArtUniversityScraper()
    
    try:
        results = scraper.search_specific_terms(universities, phd_terms)
        return jsonify({'results': results})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search-jobs-specific', methods=['POST'])
def search_jobs_specific():
    """Search specifically for job positions"""
    global scraper
    
    data = request.get_json()
    universities = data.get('universities', [])
    
    # Focus on job-specific terms
    job_terms = [
        'künstlerische mitarbeiter', 'wissenschaftliche mitarbeiter',
        'media art mitarbeiter', 'ai art mitarbeiter', 'artistic research mitarbeiter',
        'medienkunst mitarbeiter', 'ki-kunst mitarbeiter', 'klangkunst mitarbeiter',
        'performance art mitarbeiter', 'interactive art mitarbeiter',
        'artistic staff', 'research staff', 'academic staff',
        'media art staff', 'ai art staff', 'artistic research staff',
        'sound art staff', 'performance art staff', 'interactive art staff'
    ]
    
    if not scraper:
        scraper = ArtUniversityScraper()
    
    try:
        results = scraper.search_specific_terms(universities, job_terms)
        return jsonify({'results': results})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear-old-positions', methods=['POST'])
def clear_old_positions():
    """Clear positions older than specified days"""
    data = request.get_json()
    days = data.get('days', 30)
    
    try:
        deleted_count = db.clear_old_positions(days)
        return jsonify({'deleted_count': deleted_count})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def run_scraping():
    """Run the scraping process in a separate thread"""
    global scraping_status, scraper
    
    try:
        all_universities = UNIVERSITIES
        
        for i, university in enumerate(all_universities):
            if not scraping_status['running']:
                break
                
            scraping_status['current'] = university['name']
            scraping_status['progress'] = i + 1
            
            positions_found = scraper.scrape_university(university)
            scraping_status['results'][university['name']] = positions_found
            
            time.sleep(1)  # Small delay for UI updates
        
        scraping_status['running'] = False
        scraping_status['current'] = 'Completed'
        
    except Exception as e:
        scraping_status['running'] = False
        scraping_status['current'] = f'Error: {str(e)}'

@app.route('/positions')
def positions_page():
    """Positions listing page"""
    return render_template('positions.html')

@app.route('/universities')
def universities_page():
    """Universities listing page"""
    return render_template('universities.html', universities_by_country=UNIVERSITIES_BY_COUNTRY)

@app.route('/map')
def map_page():
    """Interactive map page"""
    return render_template('map.html')

@app.route('/scraper')
def scraper_page():
    """Scraper control page"""
    return render_template('scraper.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)