# Art University Job Scraper

Scrapes job postings (Stellenausschreibungen) from 51 German-speaking art universities. Focuses on **wissenschaftliche Mitarbeiter** and **künstlerische Mitarbeiter** positions.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python main.py

# Test mode (3 universities)
python main.py --test
```

## Features

- ✅ **51 art universities** across Germany, Austria, Switzerland
- ✅ **Selenium support** for JavaScript-loaded Stellenausschreibung pages
- ✅ **Smart extraction** from various page structures (lists, tables, PDFs, links)
- ✅ **Flexible keywords** - wissenschaftliche, künstlerische, mitarbeiter, stelle, etc.
- ✅ **Incremental scraping** - only updates when pages change
- ✅ **SQLite database** with full export capabilities

## Installation

```bash
# Install dependencies (requires Chrome browser)
pip install -r requirements.txt

# Run the scraper
python main.py
```

## Usage

**Scrape all universities:**
```bash
python main.py
```

**Scrape media art schools (8 universities):**
```bash
python main.py --priority media
```

**Scrape high-priority schools (26 universities):**
```bash
python main.py --priority high
```

**Force full re-scrape:**
```bash
python main.py --full
```

**Scrape specific university:**
```bash
python main.py --university "UdK Berlin"
```

**Test mode (3 universities):**
```bash
python main.py --test
```

## Universities (51 total)

**Germany (39):** UdK Berlin, Bauhaus Weimar, KHM Köln, HfG Karlsruhe, Filmuni Babelsberg, HFF München, and more

**Austria (7):** Angewandte Wien, Kunstuni Linz, Mozarteum Salzburg, and more

**Switzerland (5):** ZHdK, HKB Bern, HGK Basel, and more

Full list in `config/universities.py`

## How It Works

1. **Finds job pages** - Automatically discovers Stellenausschreibung pages
2. **Renders with Selenium** - Handles JavaScript-loaded content
3. **Extracts positions** - Uses 4 strategies:
   - Structured listings (divs, articles, lists)
   - Job links with keywords
   - PDF job postings
   - Table-based listings
4. **Flexible matching** - Finds variations:
   - German: wissenschaftliche, künstlerische, mitarbeiter, stelle, ausschreibung, position
   - English: research assistant, artistic staff, etc.
   - Abbreviations: wiss., künst.
5. **Classifies positions** - wissenschaftliche, kuenstlerische, or other
6. **Stores in database** - SQLite with full metadata

## Project Structure

```
art-university-scraper/
├── main.py                  # Main CLI entry point
├── scraper.py              # Scraper logic
├── config/
│   ├── universities.py     # 51 universities
│   └── search_terms.py     # Job keywords
├── core/
│   ├── database.py         # SQLite operations
│   ├── fetcher.py          # HTTP + Selenium
│   ├── extractor.py        # Position extraction
│   ├── detector.py         # Content detection
│   └── models.py           # Data models
└── art_positions.db        # Results database
```

## Configuration

**Adjust scraping speed:**
```bash
python main.py --delay 3.0
```

**Custom database:**
```bash
python main.py --database my_jobs.db
```

## Performance

- ~3-5 seconds per university (Selenium)
- ~3-4 minutes for all 51 universities

## Recent Results

Real scraping results:
- **Bauhaus-Universität Weimar**: 16 positions
- **Universität für angewandte Kunst Wien**: 16 positions
- **Filmuniversität Babelsberg**: 4 positions
- **Hochschule für Gestaltung und Kunst Basel**: 4 positions
- **HTWK Leipzig**: 3 positions
- **Hochschule der Künste Bern**: 2 positions
- **HTW Berlin**: 1 position

## Troubleshooting

**ChromeDriver not found:**
```bash
brew install chromedriver  # macOS
```

**Selenium timeout:**
- Increase delay: `--delay 5.0`
- Check internet connection

**No positions found:**
- Normal if university has no open positions currently
- Try `--full` to force re-scrape

## Recent Improvements

1. ✅ **Selenium by default** - Handles JavaScript-loaded Stellenausschreibung pages
2. ✅ **Improved extraction** - 4 strategies for different page structures
3. ✅ **Flexible keywords** - Catches more position variations
4. ✅ **Better results** - Successfully extracts from universities that previously returned 0 results

## License

MIT - For educational and research purposes
