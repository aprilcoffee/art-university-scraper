# Art University Job Scraper

A comprehensive web scraping system designed to find **PhD programs** and **job positions** at art universities worldwide, with a focus on German and Austrian institutions. The system searches for artistic research, practice-based PhD programs, and academic staff positions (künstlerische/wissenschaftliche mitarbeiter).

## ✨ Recent Updates & Improvements

### 🔧 **Bug Fixes & Security**
- ✅ **Fixed import errors** - All missing constants added to config
- ✅ **SQL injection vulnerability patched** - Parameterized queries implemented
- ✅ **Configuration consistency** - All config keys properly defined
- ✅ **Error handling improved** - Graceful degradation on failures

### 🎯 **Enhanced Search Focus**
- ✅ **PhD-only search** - Removed master's degree terms, focusing on doctoral programs
- ✅ **Expanded artistic research terms** - 100+ variations of practice-based research
- ✅ **Multi-language support** - German and English terms with flexible matching
- ✅ **Mitarbeiter focus** - Emphasis on künstlerische/wissenschaftliche mitarbeiter positions

### 🚀 **Performance & Reliability**
- ✅ **Better filtering** - Excludes exhibitions, research catalogues, and non-position content
- ✅ **Improved content detection** - Enhanced pattern matching for relevant positions
- ✅ **Database optimization** - Cleaned up generic entries and improved data quality

## Features

### 🎨 **Comprehensive Coverage**
- **30+ German Art Universities** including major institutions
- **5+ International Universities** (UK, Netherlands, Sweden, France)
- **Multiple Languages** (German, English)
- **PhD Programs** and **Job Positions** (mitarbeiter)

### 🔍 **Advanced Search Capabilities**

#### **PhD Programs (Doctoral Level Only)**
- **Practice-based PhD** - Praxis-basierte Promotion
- **Artistic Research PhD** - Künstlerische Forschung
- **Media Art PhD** - Medienkunst Promotion
- **AI Art PhD** - KI-Kunst Promotion
- **Sound Art PhD** - Klangkunst Promotion
- **Performance Art PhD** - Performance Art Promotion
- **Interactive Art PhD** - Interaktive Kunst Promotion
- **Studio-based Research** - Atelier-basierte Forschung
- **Research through Practice** - Forschung durch Praxis
- **DFA** (Doctor of Fine Arts) programs

#### **Job Positions (Mitarbeiter Focus)**
- **Künstlerische Mitarbeiter** (Artistic Staff)
- **Wissenschaftliche Mitarbeiter** (Research Staff)
- **Media Art Staff** positions
- **AI Art Staff** positions
- **Research Assistant** positions
- **Academic Staff** positions

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
- **Non-position content filtering** (excludes exhibitions, catalogues)

## Installation

### Prerequisites
- Python 3.8+
- Chrome browser (for Selenium)
- Internet connection

### Setup
1. **Clone or download** the project files
2. **Install dependencies**:
   ```bash
   pip3 install --break-system-packages -r requirements.txt
   ```
   
   *Note: On macOS with externally managed Python, use the `--break-system-packages` flag*

3. **Run the application**:
   ```bash
   python3 main.py --mode web
   ```

4. **Open your browser** and go to: `http://localhost:5002`

## Usage

### Web Interface (Recommended)
```bash
python3 main.py --mode web
```
- Open `http://localhost:5002` in your browser
- Use the dashboard to monitor scraping progress
- Browse positions with advanced filters
- Export results to CSV

### Command Line Scraping
```bash
# Scrape all universities
python3 main.py --mode scrape

# Scrape specific universities
python3 main.py --mode scrape --universities "Royal College of Art" "Goldsmiths University of London"

# Search for specific terms
python3 main.py --mode scrape --terms "künstlerische mitarbeiter" "practice-based phd" "ai art phd"

# Save results to file
python3 main.py --mode scrape --output results.txt
```

### Test Mode
```bash
python3 main.py --mode test
```
Tests the scraper with 3 universities to ensure everything works.

## University Coverage

### German Universities (24)
- **Universität der Künste Berlin**
- **Bauhaus-Universität Weimar**
- **Hochschule für Künste Bremen**
- **Muthesius Kunsthochschule**
- **Hochschule für Gestaltung Offenbach**
- **Kunsthochschule Berlin-Weißensee**
- **Hochschule für Bildende Künste Braunschweig**
- **Hochschule für Bildende Künste Dresden**
- **Kunstakademie Düsseldorf**
- **Folkwang Universität der Künste**
- And many more...

### International Universities (11)
- **Royal College of Art** (London, UK)
- **Goldsmiths University of London** (UK)
- **Slade School of Fine Art** (UK)
- **Glasgow School of Art** (UK)
- **Edinburgh College of Art** (UK)
- **Design Academy Eindhoven** (Netherlands)
- **Royal Academy of Art The Hague** (Netherlands)
- **Konstfack University of Arts, Crafts and Design** (Sweden)
- **École Nationale Supérieure des Beaux-Arts** (France)

### Austrian Universities (5)
- **Universität für angewandte Kunst Wien**
- **Kunstuniversität Linz**
- **Kunstuniversität Graz**
- **Universität Mozarteum Salzburg**
- **Hochschule für Musik und Darstellende Kunst Wien**

### Swiss Universities (2)
- **Hochschule für Gestaltung und Kunst Basel**
- **Hochschule für Gestaltung und Kunst Bern**

## Search Terms

### PhD Programs (German)
- **Practice-based PhD** - Praxis-basierte Promotion
- **Artistic Research** - Künstlerische Forschung
- **Media Art PhD** - Medienkunst Promotion
- **AI Art PhD** - KI-Kunst Promotion
- **Sound Art PhD** - Klangkunst Promotion
- **Performance Art PhD** - Performance Art Promotion
- **Interactive Art PhD** - Interaktive Kunst Promotion
- **Studio-based Research** - Atelier-basierte Forschung
- **Research through Practice** - Forschung durch Praxis
- **DFA** - Doktor der Bildenden Künste

### PhD Programs (English)
- **Practice-based PhD**
- **Artistic Research PhD**
- **Media Art PhD**
- **AI Art PhD**
- **Sound Art PhD**
- **Performance Art PhD**
- **Interactive Art PhD**
- **Studio-based Research**
- **Research through Practice**
- **DFA** (Doctor of Fine Arts)

### Job Positions (German)
- **Künstlerische Mitarbeiter** (Artistic Staff)
- **Wissenschaftliche Mitarbeiter** (Research Staff)
- **Medienkunst Mitarbeiter** (Media Art Staff)
- **KI-Kunst Mitarbeiter** (AI Art Staff)
- **Klangkunst Mitarbeiter** (Sound Art Staff)
- **Performance Art Mitarbeiter** (Performance Art Staff)
- **Interaktive Kunst Mitarbeiter** (Interactive Art Staff)

### Job Positions (English)
- **Artistic Staff**
- **Research Staff**
- **Academic Staff**
- **Media Art Staff**
- **AI Art Staff**
- **Sound Art Staff**
- **Performance Art Staff**
- **Interactive Art Staff**

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

### Database Schema
```sql
CREATE TABLE positions (
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
);
```

## Configuration

Key configuration options in `config.py`:
- **SEARCH_TERMS**: Comprehensive search terms for German and English
- **UNIVERSITIES**: Complete university data with websites
- **DEPARTMENTS**: Department names for extraction
- **ACADEMIC_POSITIONS**: Position classifications
- **EMPLOYMENT_DETAILS**: Employment details detection patterns
- **SCRAPING_CONFIG**: Scraping settings (delays, timeouts, retries)

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
6. **Non-position content filtering**

### Security Features
- **Parameterized SQL queries** (no SQL injection)
- **Input validation** and sanitization
- **Error handling** with graceful degradation
- **Rate limiting** to respect server resources

## Troubleshooting

### Common Issues
1. **Chrome driver issues**: Ensure Chrome browser is installed
2. **Network timeouts**: Check internet connection
3. **Permission errors**: Run with appropriate permissions
4. **Memory issues**: Reduce concurrent scraping
5. **Import errors**: Ensure all dependencies are installed

### Debug Mode
```bash
python3 main.py --mode scrape --verbose
```

### Installation Issues
If you encounter externally managed environment errors:
```bash
pip3 install --break-system-packages -r requirements.txt
```

## Contributing

To add new universities or search terms:
1. Edit `config.py`
2. Add university data to `UNIVERSITIES_BY_COUNTRY`
3. Update search terms in `SEARCH_TERMS`
4. Test with `--mode test`

## Recent Changes

### Version 2.0 (Current)
- ✅ Fixed all import errors and configuration issues
- ✅ Enhanced PhD search terms (100+ variations)
- ✅ Focused on mitarbeiter positions
- ✅ Removed master's degree terms
- ✅ Improved content filtering
- ✅ Fixed SQL injection vulnerability
- ✅ Enhanced multi-language support

### Version 1.0 (Previous)
- Basic scraping functionality
- Web interface
- Database integration
- University coverage

## License

This project is for educational and research purposes. Please respect the terms of service of the websites being scraped.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Run in test mode to identify problems
3. Check the scraping logs in the web interface
4. Ensure all dependencies are properly installed

---

**Built with ❤️ for the art and media art community**

*Focusing on PhD programs and academic staff positions in art universities worldwide*
