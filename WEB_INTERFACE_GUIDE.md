# Web Interface Guide

**Tracking 51 institutions** across Germany, Austria, and Switzerland.

## Starting the Web Interface

```bash
python app_v2.py
```

The server will start at: **http://localhost:5002**

## Pages

### 📊 Dashboard (`/`)
- Overview statistics
- Total positions count
- Breakdown by position type (wissenschaftliche/künstlerische)
- Top universities by positions
- Recent scraping activity

### 📋 Positions (`/positions`)
- Browse all job positions
- Filter by:
  - Position type (wissenschaftliche/künstlerische)
  - University
  - Language (German/English)
- View position details
- Export to CSV

### 🏛️ Universities (`/universities`)
- List of all 39 configured institutions
- Filter by country (DE, AT, CH)
- View which universities have job page URLs configured
- Direct links to university websites

### 🤖 Scraper (`/scraper`)
- Start incremental or full scrapes
- Real-time progress tracking
- View scraping results:
  - Changed pages
  - Unchanged pages
  - Failed scrapes
  - New positions found
- Recent scraping logs

## API Endpoints

All API endpoints return JSON.

### Positions
- `GET /api/positions` - Get all positions
  - Query params: `university`, `position_type`, `language`, `limit`
- `GET /api/positions/wissenschaftliche` - Get wissenschaftliche positions
- `GET /api/positions/kuenstlerische` - Get künstlerische positions

### Statistics
- `GET /api/statistics` - Database statistics

### Universities
- `GET /api/universities` - All universities
- `GET /api/universities/{country}` - Universities by country

### Logs
- `GET /api/logs` - Recent scraping logs
  - Query params: `limit` (default: 50)

### Scraping
- `POST /api/scraping/start` - Start scraping
  - Body: `{"force": true/false}`
- `GET /api/scraping/status` - Get scraping status

## Example API Usage

### Get all wissenschaftliche positions
```bash
curl http://localhost:5002/api/positions/wissenschaftliche
```

### Get positions from specific university
```bash
curl "http://localhost:5002/api/positions?university=Universität%20der%20Künste%20Berlin"
```

### Start incremental scrape
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"force": false}' \
  http://localhost:5002/api/scraping/start
```

### Get statistics
```bash
curl http://localhost:5002/api/statistics
```

## Features

### ⚡ Incremental Scraping
- **Default mode**: Only checks pages that have changed
- **10-100x faster** than full scrapes
- Ideal for daily/regular checks

### 🔄 Full Scraping
- **Force mode**: Scrapes all universities regardless of changes
- Use for first run or when you want complete refresh
- Takes 5-10 minutes for all 39 universities

### 📊 Real-time Progress
- Live progress bar during scraping
- Shows current university being scraped
- Updates statistics in real-time
- Displays results when complete

### 🎨 Clean Interface
- Modern, responsive design
- Easy navigation
- Clear visual indicators
- No external dependencies (pure CSS)

## Troubleshooting

### Port already in use
If port 5002 is taken, edit `app_v2.py` line 179:
```python
app.run(debug=True, host='0.0.0.0', port=5003)  # Change port
```

### Templates not found
Make sure you're running from the project root directory:
```bash
cd /path/to/art-university-scraper
python app_v2.py
```

### Database errors
Ensure database is initialized:
```bash
python main_v2.py --stats  # This will create DB if needed
```

## Integration with CLI

The web interface and CLI use the same database, so you can:
1. Run scrapes via CLI: `python main_v2.py --full`
2. View results via web interface
3. Or vice versa!

Both systems are fully compatible.

## Production Deployment

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5002 app_v2:app
```

Or use Docker (create `Dockerfile`):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "app_v2:app"]
```

## Security Notes

- The interface has no authentication by default
- Do not expose to public internet without adding auth
- Use behind nginx/apache with auth for production
- Consider adding rate limiting for API endpoints
