"""Configuration package for art university scraper."""

from .universities import get_all_universities, get_universities_by_country, get_university_by_name
from .search_terms import POSITION_TYPES, JOB_PAGE_INDICATORS, EXCLUDE_PATTERNS

__all__ = [
    'get_all_universities',
    'get_universities_by_country',
    'get_university_by_name',
    'POSITION_TYPES',
    'JOB_PAGE_INDICATORS',
    'EXCLUDE_PATTERNS',
]
