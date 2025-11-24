"""Flask web interface for Art University Job Scraper v2."""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import threading
from datetime import datetime

from core.database import DatabaseManager
from scraper_v2 import IncrementalScraper
from config.universities import get_all_universities, get_universities_by_country

app = Flask(__name__)
CORS(app)

db = DatabaseManager()
scraper = None
scraping_status = {'running': False, 'progress': 0, 'total': 0, 'current': '', 'changed': 0, 'unchanged': 0, 'failed': 0, 'new_positions': 0}


@app.route('/')
def index():
    """Main dashboard."""
    stats = db.get_statistics()
    return render_template('index_v2.html', stats=stats)


@app.route('/positions')
def positions_page():
    """Positions browser page."""
    return render_template('positions_v2.html')


@app.route('/universities')
def universities_page():
    """Universities page."""
    universities = get_all_universities()
    return render_template('universities_v2.html', universities=universities)


@app.route('/scraper')
def scraper_page():
    """Scraper control page."""
    return render_template('scraper_v2.html')


# API Routes
@app.route('/api/positions')
def api_get_positions():
    """Get positions with filters."""
    university = request.args.get('university')
    position_type = request.args.get('position_type')
    language = request.args.get('language')
    limit = request.args.get('limit', type=int)

    positions = db.get_positions(
        university_name=university,
        position_type=position_type,
        active_only=True,
        limit=limit
    )
    return jsonify(positions)


@app.route('/api/positions/wissenschaftliche')
def api_wissenschaftliche():
    """Get wissenschaftliche Mitarbeiter positions."""
    positions = db.get_positions(position_type='wissenschaftliche', active_only=True)
    return jsonify(positions)


@app.route('/api/positions/kuenstlerische')
def api_kuenstlerische():
    """Get künstlerische Mitarbeiter positions."""
    positions = db.get_positions(position_type='kuenstlerische', active_only=True)
    return jsonify(positions)


@app.route('/api/statistics')
def api_statistics():
    """Get database statistics."""
    return jsonify(db.get_statistics())


@app.route('/api/universities')
def api_universities():
    """Get all universities."""
    return jsonify(get_all_universities())


@app.route('/api/universities/<country>')
def api_universities_country(country):
    """Get universities by country."""
    unis = get_universities_by_country(country.upper())
    return jsonify(unis)


@app.route('/api/logs')
def api_logs():
    """Get recent scraping logs."""
    limit = request.args.get('limit', 50, type=int)
    logs = db.get_recent_logs(limit)
    return jsonify(logs)


@app.route('/api/scraping/start', methods=['POST'])
def api_start_scraping():
    """Start scraping process."""
    global scraper, scraping_status

    if scraping_status['running']:
        return jsonify({'error': 'Scraping already running'}), 400

    force = request.json.get('force', False) if request.json else False

    try:
        scraper = IncrementalScraper(delay=2)
        scraping_status = {
            'running': True,
            'progress': 0,
            'total': len(get_all_universities()),
            'current': '',
            'changed': 0,
            'unchanged': 0,
            'failed': 0,
            'new_positions': 0
        }

        thread = threading.Thread(target=run_scraping, args=(force,))
        thread.daemon = True
        thread.start()

        return jsonify({'message': 'Scraping started'})
    except Exception as e:
        scraping_status['running'] = False
        return jsonify({'error': str(e)}), 500


@app.route('/api/scraping/status')
def api_scraping_status():
    """Get scraping status."""
    return jsonify(scraping_status)


def run_scraping(force=False):
    """Run scraping in background thread."""
    global scraper, scraping_status

    universities = get_all_universities()

    for i, university in enumerate(universities, 1):
        if not scraping_status['running']:
            break

        scraping_status['progress'] = i
        scraping_status['current'] = university['name']

        result = scraper.scrape_university(university, force_scrape=force)

        if result['status'] == 'success':
            if result['changed']:
                scraping_status['changed'] += 1
                scraping_status['new_positions'] += result.get('positions_found', 0)
            else:
                scraping_status['unchanged'] += 1
        else:
            scraping_status['failed'] += 1

    scraping_status['running'] = False
    scraping_status['current'] = 'Complete'
    scraper.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
