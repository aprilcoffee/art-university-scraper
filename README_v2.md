# Art University Job Scraper v2

**Optimized incremental scraper for wissenschaftliche and künstlerische Mitarbeiter positions** at German-speaking art universities and Fachhochschulen.

**Latest Update:** Now tracking **51 institutions** across Germany, Austria, and Switzerland, including art schools, Fachhochschulen, film schools, and music/theater schools with art programs.

## What's New in v2

### Key Improvements

1. **Incremental Scraping** - Only scrapes pages that have changed
   - Uses content hashing to detect changes
   - 10-100x faster after initial run
   - Reduces server load

2. **Simplified & Focused**
   - Only searches for wissenschaftliche and künstlerische Mitarbeiter
   - Removed 1,445 lines of redundant configuration
   - Clean, modular architecture

3. **Better Performance**
   - Faster HTTP requests by default
   - Optional Selenium fallback for JS-heavy sites
   - Configurable delays between requests

4. **Improved Data Quality**
   - Better position extraction
   - Language detection
   - Deadline and department extraction
   - Duplicate prevention

## Architecture

```
art-university-scraper/
├── config/
│   ├── universities.py      # University definitions (36 universities)
│   └── search_terms.py      # Focused search terms
├── core/
│   ├── database.py          # Database operations
│   ├── fetcher.py           # Page fetching (HTTP + Selenium)
│   ├── detector.py          # Content change detection
│   ├── extractor.py         # Position extraction
│   └── models.py            # Data models
├── scraper_v2.py            # Main scraper logic
└── main_v2.py               # CLI entry point
```

## Database Schema

### positions
- `id`: Auto-increment primary key
- `university_name`: University name
- `title`: Position title
- `url`: Position URL (unique)
- `position_type`: 'wissenschaftliche' or 'kuenstlerische'
- `description`: Position description
- `language`: 'de' or 'en'
- `deadline`: Application deadline
- `department`: Department name
- `found_date`: When position was first found
- `is_active`: Whether position is still active

### university_job_pages
- `id`: Auto-increment primary key
- `university_name`: University name (unique)
- `job_page_url`: URL of job listings page
- `content_hash`: SHA256 hash of page content
- `last_scraped`: Last scrape timestamp
- `last_modified`: Last content change timestamp
- `positions_count`: Number of positions found
- `is_active`: Whether page is still active

### scraping_logs
- `id`: Auto-increment primary key
- `university_name`: University name
- `status`: 'success', 'failed', or 'unchanged'
- `message`: Log message
- `positions_found`: Number of new positions
- `timestamp`: Log timestamp

## Usage

### Web Interface (New!)

Start the web interface for a visual dashboard:

```bash
python app_v2.py
```

Then open **http://localhost:5002** in your browser.

**Features:**
- 📊 Dashboard with statistics
- 📋 Browse and filter positions
- 🏛️ View all universities
- 🤖 Control scraper with real-time progress
- 📜 View scraping logs

See [WEB_INTERFACE_GUIDE.md](WEB_INTERFACE_GUIDE.md) for details.

### Command Line

```bash
# Incremental scrape (only changed pages)
python main_v2.py

# Scrape only media art schools (8 schools, fastest)
python main_v2.py --priority media

# Scrape media/design focused schools (26 schools, recommended)
python main_v2.py --priority high

# Force full scrape (all universities)
python main_v2.py --full

# Use Selenium for JavaScript-heavy sites
python main_v2.py --selenium

# Custom delay between requests
python main_v2.py --delay 5
```

### View Data

```bash
# Show statistics
python main_v2.py --stats

# Show recent logs
python main_v2.py --logs

# Show more log entries
python main_v2.py --logs --limit 100

# List configured universities
python main_v2.py --list
```

### Export Data

```bash
# Export to CSV (auto-generated filename)
python main_v2.py --export

# Export to specific file
python main_v2.py --export positions.csv
```

## How Incremental Scraping Works

### First Run
1. Find job page URL for each university
2. Fetch and parse job page
3. Extract all positions
4. Compute content hash
5. Store everything in database

### Subsequent Runs
1. Fetch job page
2. Compute content hash
3. Compare with stored hash
4. **If unchanged**: Skip extraction (instant check)
5. **If changed**: Extract only NEW positions
6. Update timestamps and hashes

This makes subsequent runs **10-100x faster** since most pages don't change daily.

## Priority System 🔥

Universities are **prioritized by media art and design focus**:

- **Media priority** (8 schools): KHM Köln, HfG Karlsruhe, Bauhaus Weimar, Film schools
- **High priority** (26 schools): + Design Fachhochschulen + Austrian/Swiss design schools
- **All** (51 schools): Complete DACH region coverage

**Recommendation:** Use `--priority high` for regular checks (2-3 min).

See [PRIORITY_SYSTEM.md](PRIORITY_SYSTEM.md) for complete details.

## Configured Universities

Currently tracking **51 institutions** (ordered by priority):

### Germany (39 institutions)
#### Art Schools (25)
- Universität der Künste Berlin
- Kunsthochschule Berlin-Weißensee
- HfBK Braunschweig
- HfK Bremen
- HfBK Dresden
- Kunstakademie Düsseldorf
- Folkwang Universität
- Städelschule Frankfurt
- Burg Giebichenstein Halle
- HfBK Hamburg
- HfG Karlsruhe
- Muthesius Kunsthochschule
- KHM Köln
- HGB Leipzig
- Kunsthochschule Mainz
- AdBK München
- Kunstakademie Münster
- AdBK Nürnberg
- HfG Offenbach
- HBK Saar
- ABK Stuttgart
- Bauhaus-Universität Weimar
- HfG Schwäbisch Gmünd
- HfG Pforzheim
- Alanus Hochschule

#### Fachhochschulen with Design/Art Programs (9)
- HTW Berlin
- HTW Dresden
- HTWK Leipzig
- HAW Hamburg
- HAW München
- Hochschule Mannheim
- Hochschule Darmstadt
- Hochschule Augsburg
- Hochschule Düsseldorf

#### Film & Media Universities (2)
- Filmuniversität Babelsberg Konrad Wolf
- HFF München

#### Music/Theater Schools with Art Programs (3)
- HfMT Hamburg
- HfMT München
- HfMT Leipzig

### Austria (6 universities)
- Universität für angewandte Kunst Wien
- Akademie der bildenden Künste Wien
- Kunstuniversität Linz
- Kunstuniversität Graz
- Universität Mozarteum Salzburg
- Hochschule für Musik und Darstellende Kunst Wien

### Switzerland (6 universities)
- Zürcher Hochschule der Künste (ZHdK)
- Hochschule für Gestaltung und Kunst Basel (HGK)
- Hochschule der Künste Bern (HKB)
- Hochschule Luzern - Design & Kunst
- HEAD Genève
- FHNW - Hochschule für Gestaltung und Kunst

## Position Types

### Wissenschaftliche Mitarbeiter
- Research assistant positions
- Academic staff roles
- Scientific positions at art universities

### Künstlerische Mitarbeiter
- Artistic assistant positions
- Creative staff roles
- Practice-based positions

## Search Terms

The scraper looks for specific German and English terms:

**German:**
- wissenschaftliche mitarbeiter/in
- wiss. mitarbeiter/in
- künstlerische mitarbeiter/in
- künst. mitarbeiter/in
- forschungsmitarbeiter/in

**English:**
- research assistant/associate
- artistic assistant/associate
- scientific staff
- academic staff

## Excluding Non-Positions

Automatically excludes:
- Exhibitions (Ausstellungen)
- Events (Veranstaltungen)
- Publications (Publikationen)
- Degree programs (Studiengänge)
- Workshops and seminars

## Performance

### Code Efficiency
- **46% less code** than initial v2 (369 vs 682 lines in core modules)
- Optimized for token usage
- Cleaner, more maintainable

### Initial Scrape
- 51 universities × 5-10 seconds each
- **Total: ~5-12 minutes**

### Incremental Scrape
- 51 universities × 1-2 seconds each
- **Total: ~1-3 minutes**
- Most time saved by skipping unchanged pages

## Dependencies

```
requests
beautifulsoup4
selenium
lxml
```

Install with:
```bash
pip install requests beautifulsoup4 selenium lxml
```

## Future Enhancements

1. **Email notifications** for new positions
2. **Web interface** to browse positions
3. **More universities** (expand to Netherlands, UK)
4. **Filtering** by department, deadline, etc.
5. **Position expiration detection** (mark inactive if removed)

## Migration from v1

The old system (main.py, scraper.py, config.py) is kept for reference.

To migrate:
1. Use the new database schema (positions table is similar)
2. Run `python main_v2.py --full` for initial scrape
3. Switch to incremental mode for daily scrapes

## Troubleshooting

### No positions found
- Check if job page URL is correct
- Try `--selenium` flag for JavaScript sites
- Increase `--delay` for rate-limited sites

### Import errors
- Ensure you're in the project root directory
- Check that `config/` and `core/` directories exist
- Verify `__init__.py` files are present

### Database locked
- Close any other programs accessing the database
- Check file permissions

## License

MIT License - Feel free to use and modify for your research.
