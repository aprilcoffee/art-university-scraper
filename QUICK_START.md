# Quick Start Guide

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create initial database (optional - will auto-create)
python main_v2.py --stats
```

## Usage Options

### 1️⃣ Web Interface (Recommended)

```bash
python app_v2.py
```

Open **http://localhost:5002**

**Use for:**
- Visual dashboard
- Browsing positions
- Monitoring scrapes in real-time
- Viewing statistics

---

### 2️⃣ Command Line

```bash
# Quick scrape (only changed pages, all 51 schools)
python main_v2.py

# 🔥 RECOMMENDED: Media/design priority (26 schools)
python main_v2.py --priority high

# ⚡ FASTEST: Media art only (8 schools)
python main_v2.py --priority media

# First time / full scrape
python main_v2.py --full

# View statistics
python main_v2.py --stats

# View logs
python main_v2.py --logs

# List universities
python main_v2.py --list

# Export to CSV
python main_v2.py --export positions.csv
```

**Use for:**
- Scheduled tasks (cron jobs)
- Quick checks
- Automated scripts
- Exporting data

---

## What This System Does

### Searches For
- **Wissenschaftliche Mitarbeiter** (Research/Academic staff)
- **Künstlerische Mitarbeiter** (Artistic staff)

### Where It Searches
- **51 institutions** across Germany, Austria, Switzerland
- **25 Art Schools** (Kunsthochschulen)
- **9 Fachhochschulen** with design/art programs
- **2 Film Schools**
- **3 Music/Theater Schools** with art programs
- **12 Universities** in Austria & Switzerland

### How It Works
1. **First run**: Finds job pages, scrapes all positions
2. **Next runs**: Only scrapes pages that changed (10-100x faster!)
3. **Detection**: Uses content hashing to detect changes
4. **Storage**: SQLite database with incremental tracking

---

## File Overview

### Core Files
- `main_v2.py` - Command line interface
- `app_v2.py` - Web interface
- `scraper_v2.py` - Incremental scraper logic

### Configuration
- `config/universities.py` - 39 institutions
- `config/search_terms.py` - Position keywords

### Core Modules
- `core/database.py` - Database operations
- `core/fetcher.py` - Page fetching
- `core/detector.py` - Change detection
- `core/extractor.py` - Position extraction
- `core/models.py` - Data models

### Data
- `art_positions.db` - SQLite database

---

## Priority Levels 🔥

The system now prioritizes by **media art and design focus**:

| Priority | Schools | Time | Use When |
|----------|---------|------|----------|
| `--priority media` | 8 | 1-2 min | Daily checks, media art only |
| `--priority high` | 26 | 2-3 min | **Recommended** for regular use |
| Default (all) | 51 | 2-3 min | Complete DACH coverage |

**Example:**
```bash
# Daily: Check top media art schools only
python main_v2.py --priority media

# Weekly: Check all media/design schools
python main_v2.py --priority high

# Monthly: Full comprehensive scan
python main_v2.py --full
```

See [PRIORITY_SYSTEM.md](PRIORITY_SYSTEM.md) for details.

## Common Tasks

### Run Daily Scrape (Recommended)
```bash
python main_v2.py --priority high
```
Takes ~2-3 minutes (only changed pages, top 26 schools).

### Check What's New
```bash
python main_v2.py --logs --limit 20
```

### Export All Positions
```bash
python main_v2.py --export
```

### View in Browser
```bash
python app_v2.py
# Visit http://localhost:5002
```

---

## Tips

### ⚡ Speed
- Incremental mode is 10-100x faster than full scrape
- Use `--full` only for first run or when suspicious

### 🔧 Troubleshooting
- **No positions found?** This is normal - not all universities have openings
- **Errors fetching pages?** Some sites block bots - try `--selenium` flag
- **Database errors?** Delete `art_positions.db` and re-run

### 📅 Automation
Add to crontab for daily scrapes:
```bash
# Run every day at 9 AM
0 9 * * * cd /path/to/scraper && python main_v2.py
```

### 🎯 Focus
If you only want specific universities, edit `config/universities.py`.

---

## Documentation

- `README_v2.md` - Full documentation
- `WEB_INTERFACE_GUIDE.md` - Web interface details
- `MIGRATION_GUIDE.md` - Migrating from v1
- `OPTIMIZATION_SUMMARY.md` - Code optimization details
- `INTERFACE_UPDATE_SUMMARY.md` - Web interface changes

---

## System Requirements

- Python 3.8+
- Chrome/Chromium (for Selenium fallback)
- 50MB disk space
- Internet connection

---

## Support

### Check Status
```bash
python main_v2.py --stats
```

### View Logs
```bash
python main_v2.py --logs
```

### Test Single University
```bash
python test_scraper.py
```

---

## That's It!

You're ready to scrape! Start with:

```bash
python main_v2.py --full
```

Then check results:

```bash
python app_v2.py  # Open http://localhost:5002
```

Subsequent runs will be much faster:

```bash
python main_v2.py  # 1-2 minutes instead of 10
```
