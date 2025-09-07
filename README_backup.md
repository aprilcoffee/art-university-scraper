# Art University Job Scraper

A comprehensive web scraping system designed to find art and media art positions at universities worldwide, with a focus on German and Austrian institutions. The system searches for PhD programs, job positions, and opportunities in media art, digital art, and AI art.

## Features

### 🎨 **Comprehensive Coverage**
- **30+ German Art Universities** from the provided CSV list
- **5+ International Universities** (UK, USA)
- **Multiple Languages** (German, English)
- **Various Position Types** (PhD, Jobs, Media Art, Digital Art, AI Art)

### 🔍 **Advanced Search Capabilities**
- **Media Art** positions and programs
- **Digital Art** opportunities
- **AI Art** and artificial intelligence in art
- **PhD Programs** in art and design
- **Job Positions** (Stellenausschreibungen)

### 🌐 **Interactive Web Interface**
- **Real-time Dashboard** with statistics and charts
- **Position Browser** with advanced filtering
- **University Directory** with detailed information
- **Scraper Control Panel** for monitoring progress
- **Export Functionality** (CSV format)

### 🤖 **Intelligent Scraping**
- **Selenium WebDriver** for JavaScript-heavy sites
- **BeautifulSoup** for HTML parsing
- **Smart Content Detection** (German vs English)
- **Rate Limiting** and respectful scraping
- **Error Handling** and retry mechanisms

## Installation

### Prerequisites
- Python 3.8+
- Chrome browser (for Selenium)
- Internet connection

### Setup
1. **Clone or download** the project files
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py --mode web
   ```

4. **Open your browser** and go to: `http://localhost:5000`

## Usage

### Web Interface (Recommended)
```bash
python main.py --mode web
```
- Open `http://localhost:5000` in your browser
- Use the dashboard to monitor scraping progress
- Browse positions with advanced filters
- Export results to CSV

### Command Line Scraping
```bash
# Scrape all universities
python main.py --mode scrape

# Scrape specific universities
python main.py --mode scrape --universities "Universität der Künste Berlin" "Bauhaus-Universität Weimar"

# Search for specific terms
python main.py --mode scrape --terms "media art" "digital art" "AI art"

# Save results to file
python main.py --mode scrape --output results.txt
```

### Test Mode
```bash
python main.py --mode test
```
Tests the scraper with a few universities to ensure everything works.

## University Coverage

### German Universities (30+)
- **Universität der Künste Berlin** (Graduate School)
- **Bauhaus-Universität Weimar** (PhD Programs)
- **Hochschule für Künste Bremen** (Artistic PhD)
- **Muthesius Kunsthochschule** (PhD Programs)
- **Hochschule für Gestaltung Offenbach** (PhD Programs)
- And many more...

### International Universities (5+)
- **Royal College of Art** (London, UK)
- **Central Saint Martins** (London, UK)
- **Parsons School of Design** (New York, USA)
- **Rhode Island School of Design** (USA)
- **California Institute of the Arts** (USA)

### Austrian Universities
- **Universität für angewandte Kunst Wien**
- **Kunstuniversität Linz**
- **Kunstuniversität Graz**

## Search Terms

### German Terms
- **Medienkunst** (Media Art)
- **Digitale Kunst** (Digital Art)
- **Neue Medien** (New Media)
- **KI-Kunst** (AI Art)
- **Promotion** (PhD)
- **Stellenausschreibung** (Job Posting)

### English Terms
- **Media Art**
- **Digital Art**
- **Computer Art**
- **AI Art**
- **Artificial Intelligence Art**
- **PhD Programs**
- **Job Openings**

## Web Interface Features

### 📊 Dashboard
- Real-time statistics
- Position type distribution charts
- Language breakdown
- Recent positions overview

### 🔍 Position Browser
- Advanced filtering (university, type, language, status)
- Search functionality
- Detailed position information
- Export to CSV

### 🏛️ University Directory
- Complete university list
- PhD program availability
- Direct website links
- Individual university scraping

### 🕷️ Scraper Control
- Start/stop scraping processes
- Real-time progress monitoring
- Specific term searches
- Scraping logs

## Database

The system uses SQLite database with the following tables:
- **positions**: Scraped job positions and PhD opportunities
- **universities**: University information and metadata
- **search_logs**: Scraping activity logs

## Configuration

Key configuration options in `config.py`:
- **Search terms** for different languages and categories
- **University data** with websites and PhD availability
- **Scraping settings** (delays, timeouts, retries)
- **Database configuration**

## Technical Details

### Architecture
- **Flask** web framework
- **SQLite** database
- **Selenium** for dynamic content
- **BeautifulSoup** for HTML parsing
- **Bootstrap** for responsive UI

### Scraping Strategy
1. **Respectful scraping** with delays between requests
2. **Multiple content detection** methods
3. **JavaScript rendering** for complex sites
4. **Error handling** and retry mechanisms
5. **Content deduplication**

## Troubleshooting

### Common Issues
1. **Chrome driver issues**: Ensure Chrome browser is installed
2. **Network timeouts**: Check internet connection
3. **Permission errors**: Run with appropriate permissions
4. **Memory issues**: Reduce concurrent scraping

### Debug Mode
```bash
python main.py --mode scrape --verbose
```

## Contributing

To add new universities or search terms:
1. Edit `config.py`
2. Add university data to `UNIVERSITIES` or `INTERNATIONAL_UNIVERSITIES`
3. Update search terms in `SEARCH_TERMS`
4. Test with `--mode test`

## License

This project is for educational and research purposes. Please respect the terms of service of the websites being scraped.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Run in test mode to identify problems
3. Check the scraping logs in the web interface

---

**Built with ❤️ for the art and media art community**