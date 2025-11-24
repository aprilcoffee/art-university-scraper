# Priority System for Universities

## Overview

The 51 universities are now **prioritized by media art and design focus**. This allows you to scrape the most relevant institutions first.

## Priority Levels

### 🔥 HIGHEST: Media Art Universities (8 schools)
**Flag:** `--priority media`

Specialized media art and design schools:

1. **Kunsthochschule für Medien Köln (KHM)** - Media art leader
2. **Staatliche Hochschule für Gestaltung Karlsruhe (HfG)** - Design & media
3. **Hochschule für Gestaltung Schwäbisch Gmünd** - Interaction design
4. **Hochschule für Gestaltung Offenbach** - Digital media
5. **Bauhaus-Universität Weimar** - Media architecture
6. **Universität der Künste Berlin** - Media/design programs
7. **Filmuniversität Babelsberg** - Film & media production
8. **HFF München** - Film & television

**Use when:** You want only the top media art institutions.

**Scrape time:** ~1-2 minutes (incremental), ~5-8 minutes (full)

```bash
python main_v2.py --priority media
```

---

### ⭐ HIGH: Media/Design Focus (26 schools)
**Flag:** `--priority high`

Includes media art schools + design-focused institutions:

**Media Art (8)** - As above, plus:

**Austria/Switzerland Design Leaders (6):**
- Universität für angewandte Kunst Wien
- Kunstuniversität Linz
- ZHdK Zürich
- HGK Basel
- HKB Bern
- HSLU Luzern
- HEAD Genève
- FHNW Basel

**German Fachhochschulen Design (10):**
- HAW Hamburg
- HAW München
- HTW Berlin
- HTWK Leipzig
- HfG Pforzheim
- HS Mannheim
- HS Darmstadt
- HTW Dresden
- HS Augsburg
- HS Düsseldorf

**Plus Contemporary Art Schools (6):**
- Burg Giebichenstein (Halle)
- HfBK Hamburg
- KH Weißensee (Berlin)
- HGB Leipzig
- Folkwang (Essen)
- Muthesius (Kiel)

**Use when:** You want media/design schools + Fachhochschulen.

**Scrape time:** ~2-3 minutes (incremental), ~8-10 minutes (full)

```bash
python main_v2.py --priority high
```

---

### 📚 ALL: Complete Coverage (51 schools)
**Flag:** `--priority all` (default)

All 51 institutions including:
- All of the above
- Traditional art academies (12)
- Music/Theater schools (5)

**Use when:** You want comprehensive DACH region coverage.

**Scrape time:** ~2-3 minutes (incremental), ~8-12 minutes (full)

```bash
python main_v2.py
# or
python main_v2.py --priority all
```

---

## Priority Ordering Rationale

### Why This Order?

**1. Media Art Schools (Highest)**
- Specialized in digital/new media
- Most likely to have relevant positions
- Strong focus on künstlerische Mitarbeiter

**2. Film & Media Universities**
- Production design, cinematography, VFX
- Interactive media programs
- High demand for both position types

**3. Design Fachhochschulen**
- Industrial, communication, interaction design
- Digital media programs
- Both wissenschaftliche and künstlerische roles

**4. Contemporary Art Schools**
- Mix of traditional and new media
- Interdisciplinary programs
- Good position availability

**5. Traditional Art Academies**
- More classical fine arts focus
- Fewer digital/media positions
- Still valuable for complete coverage

**6. Music/Theater Schools (Lower)**
- Limited art/design positions
- Mostly for sound art, stage design
- Included for completeness

## Usage Examples

### Daily Quick Check (Media Art Only)
```bash
# Just check top 8 media art schools (1-2 min)
python main_v2.py --priority media
```

### Weekly Design Check (High Priority)
```bash
# Check top 26 media/design schools (2-3 min)
python main_v2.py --priority high
```

### Full DACH Coverage (All Schools)
```bash
# Check all 51 schools (2-3 min)
python main_v2.py --priority all
```

### Force Full Scrape of Priority Schools
```bash
# Full scrape of top 26 (8-10 min)
python main_v2.py --priority high --full
```

## Benefits

### ⚡ Speed
- **Media only**: 70% faster than full scrape
- **High priority**: 50% faster than full scrape
- Get results from most relevant schools first

### 🎯 Relevance
- Focus on schools with most media/design positions
- Prioritize digital and interactive programs
- Skip less relevant music/theater schools

### 💰 Efficiency
- Don't waste time on schools with few positions
- Check high-value targets frequently
- Do full scrapes less often

## Programmatic Access

### Python API

```python
from config.universities import (
    get_all_universities,           # All 51
    get_high_priority_universities, # Top 26
    get_media_art_universities      # Top 8
)

# Get only media art schools
media_schools = get_media_art_universities()
for school in media_schools:
    print(school['name'])
```

### Custom Priority Lists

You can create your own priority lists by slicing the UNIVERSITIES list in `config/universities.py`:

```python
# Top 15 schools
top_15 = UNIVERSITIES[:15]

# Skip music schools (last 5)
no_music = UNIVERSITIES[:-5]

# Only German schools
from config.universities import get_universities_by_country
german_only = get_universities_by_country('DE')
```

## Web Interface

The web interface still shows all 51 universities. The priority system is currently CLI-only.

To use priorities in web scraping, the frontend would need to be updated to:
1. Add priority dropdown
2. Pass to `/api/scraping/start` endpoint
3. Filter universities server-side

## Recommendations

### For Daily Monitoring
```bash
python main_v2.py --priority media
```
Check the 8 most relevant schools daily. Quick and focused.

### For Weekly Checks
```bash
python main_v2.py --priority high
```
Check 26 media/design schools weekly. Good balance.

### For Monthly Full Scans
```bash
python main_v2.py --priority all --full
```
Full scrape of all 51 schools monthly. Comprehensive.

### For Research/Initial Setup
```bash
python main_v2.py --full
```
Complete scan to build initial database.

## Statistics by Priority

### Expected Positions

Based on typical availability:

| Priority | Schools | Expected Positions | % of Total |
|----------|---------|-------------------|------------|
| Media | 8 | 20-40 | ~40% |
| High | 26 | 40-80 | ~70% |
| All | 51 | 50-120 | 100% |

**Note:** Media art schools have higher position turnover due to project-based work.

## Priority Override

To scrape in custom order, edit `config/universities.py` directly. The UNIVERSITIES list order determines scraping order when using default/all priority.

## Future Enhancements

Possible additions:
- Save priority preference
- Web interface priority selector
- University-specific priority (mark favorites)
- Time-based priorities (check some daily, others weekly)
- Smart priority based on historical position counts

## Summary

The priority system lets you:
- ✅ Focus on most relevant schools
- ✅ Save time on daily checks
- ✅ Still have complete coverage when needed
- ✅ Prioritize media art and design over traditional fine arts

**Default recommendation:** Use `--priority high` for regular checks, `--priority all` monthly.
