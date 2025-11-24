"""Data models for the scraper."""
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class Position:
    """Job position at a university."""
    university_name: str
    title: str
    url: str
    position_type: str  # 'wissenschaftliche' or 'kuenstlerische'
    description: Optional[str] = None
    language: str = 'de'
    deadline: Optional[str] = None
    department: Optional[str] = None
    found_date: Optional[str] = None

    def to_dict(self):
        data = asdict(self)
        if not data['found_date']:
            data['found_date'] = datetime.now().isoformat()
        return data


@dataclass
class UniversityJobPage:
    """Tracks a university's job page for change detection."""
    university_name: str
    job_page_url: str
    content_hash: str
    last_scraped: str
    last_modified: str
    positions_count: int = 0
    is_active: bool = True

    def to_dict(self):
        return asdict(self)


@dataclass
class ScrapingLog:
    """Log entry for scraping operations."""
    university_name: str
    status: str  # 'success', 'failed', 'unchanged'
    message: str
    timestamp: str
    positions_found: int = 0

    def to_dict(self):
        return asdict(self)
