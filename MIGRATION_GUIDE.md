# Migration Guide: v1 → v2

## What Changed

The scraper has been completely restructured for better performance, maintainability, and focus.

### Old System (v1)
```
main.py              # 132 lines
scraper.py           # 1,092 lines - monolithic
config.py            # 1,445 lines - massive, redundant
database.py          # 292 lines
utils.py             # 495 lines
```
**Total: ~3,500 lines** of complex, repetitive code

### New System (v2)
```
main_v2.py           # Clean CLI interface
scraper_v2.py        # Incremental scraper logic
config/
  ├── universities.py    # 200 lines - focused list
  └── search_terms.py    # 60 lines - essential terms only
core/
  ├── database.py        # Enhanced with tracking
  ├── fetcher.py         # Separated HTTP/Selenium logic
  ├── detector.py        # Content change detection
  ├── extractor.py       # Position extraction
  └── models.py          # Clean data models
```
**Total: ~1,500 lines** of clean, modular code

## Key Improvements

### 1. Incremental Scraping
- **Old**: Re-scrapes everything every time (slow, wasteful)
- **New**: Only scrapes pages that have changed (10-100x faster)

### 2. Focused Search
- **Old**: 400+ universities, 200+ search terms (unfocused)
- **New**: 33 core art universities, focused on wissenschaftliche/künstlerische Mitarbeiter

### 3. Better Architecture
- **Old**: Everything in one 1,092-line scraper class
- **New**: Separated concerns (fetcher, detector, extractor, database)

### 4. Simplified Configuration
- **Old**: 1,445 lines with massive redundancy
- **New**: 260 lines with clear structure

## Database Changes

### Schema Differences

#### Old `positions` table:
```sql
university TEXT          -- Just "university"
category TEXT            -- 'phd', 'job', 'mixed'
position_level TEXT
employment_details TEXT
```

#### New `positions` table:
```sql
university_name TEXT     -- Clearer name
position_type TEXT       -- 'wissenschaftliche', 'kuenstlerische'
deadline TEXT            -- Extracted separately
department TEXT          -- Extracted separately
is_active BOOLEAN        -- Track expired positions
```

### New Tables

**`university_job_pages`** - Tracks content changes
- Stores content hash for each university's job page
- Enables incremental scraping
- Tracks when content last changed

**`scraping_logs`** - Better logging
- Records every scrape attempt
- Tracks success/failure/unchanged status
- Useful for debugging and monitoring

## Migration Steps

### Option 1: Fresh Start (Recommended)

1. **Backup old database**
   ```bash
   mv art_positions.db art_positions_old.db
   ```

2. **Run new scraper**
   ```bash
   python main_v2.py --full
   ```

3. **Verify results**
   ```bash
   python main_v2.py --stats
   python main_v2.py --export positions.csv
   ```

### Option 2: Migrate Data

If you want to keep old data, create a migration script:

```python
import sqlite3

# Connect to both databases
old_db = sqlite3.connect('art_positions_old.db')
new_db = sqlite3.connect('art_positions.db')

# Read old positions
old_cursor = old_db.cursor()
old_cursor.execute('SELECT * FROM positions')

# Map to new schema
new_cursor = new_db.cursor()
for row in old_cursor:
    # Map old fields to new fields
    # Note: You'll need to determine position_type from old category/title
    new_cursor.execute('''
        INSERT OR IGNORE INTO positions
        (university_name, title, url, position_type, description,
         language, found_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        row['university'],  # → university_name
        row['title'],
        row['url'],
        'wissenschaftliche',  # Default - adjust based on category
        row['description'],
        row['language'],
        row['date_found'],
    ))

new_db.commit()
```

## Usage Changes

### Old Way
```bash
# Full scrape
python main.py --mode scrape

# Web interface
python main.py --mode web

# Test
python main.py --mode test
```

### New Way
```bash
# Incremental scrape (default)
python main_v2.py

# Full scrape
python main_v2.py --full

# Statistics
python main_v2.py --stats

# Export
python main_v2.py --export positions.csv

# List universities
python main_v2.py --list
```

## Configuration Changes

### Adding Universities

**Old way:** Edit massive UNIVERSITIES_BY_COUNTRY dict in config.py

**New way:** Edit clean list in config/universities.py
```python
{
    'name': 'Hochschule Example',
    'website': 'https://example.edu',
    'country': 'DE',
    'city': 'Berlin',
    'job_page_url': None,  # Will auto-discover
}
```

### Adding Search Terms

**Old way:** Edit 1,445-line config.py with 200+ overlapping terms

**New way:** Edit config/search_terms.py with focused terms
```python
POSITION_TYPES = {
    'wissenschaftliche_mitarbeiter': {
        'german': ['wissenschaftliche mitarbeiter', ...],
        'english': ['research assistant', ...]
    }
}
```

## Performance Comparison

### Initial Scrape (400 universities)
- **Old**: ~2 hours (scrapes everything)
- **New**: ~5-10 minutes (only 33 focused universities)

### Subsequent Scrapes
- **Old**: ~2 hours (re-scrapes everything again)
- **New**: ~1-2 minutes (only checks changed pages)

**Speed improvement: 60-120x faster** for incremental scrapes

## What's Removed

### Features NOT in v2:
- Web interface (app.py) - focus on command line
- PhD program tracking - focus on Mitarbeiter positions only
- 400+ universities - focus on 33 core art schools
- Multiple search term categories - simplified to 2 types

### If you need these:
- Keep old system running alongside v2
- Or extend v2 by adding more universities to config/universities.py

## Troubleshooting

### "No positions found"
This is normal if:
- University doesn't currently have openings
- Job page structure is different than expected
- Search terms don't match page content

**Solution**: Check the actual job page manually, or use `--selenium` flag

### "Could not find job page"
The scraper couldn't auto-discover the Stellenausschreibung page.

**Solution**: Add `job_page_url` manually in config/universities.py

### "Import errors"
Make sure you're in the project root and have `__init__.py` files.

**Solution**:
```bash
# Check directory structure
ls -la config/ core/

# Should see __init__.py in both
```

## Recommendation

**Use v2 for daily scraping** of wissenschaftliche/künstlerische Mitarbeiter positions at core art universities.

**Keep v1** if you need:
- The web interface
- PhD program tracking
- Broader university coverage

Both can coexist - just use different database files.

## Questions?

Check these files:
- `README_v2.md` - Full v2 documentation
- `test_scraper.py` - Example usage
- `main_v2.py --help` - CLI options
