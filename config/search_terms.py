"""
Focused search terms for academic positions at art universities.
Only searches for wissenschaftliche and künstlerische Mitarbeiter positions.
"""

# Core position types we're looking for
POSITION_TYPES = {
    'wissenschaftliche_mitarbeiter': {
        'german': [
            'wissenschaftliche mitarbeiter',
            'wissenschaftliche mitarbeiterin',
            'wissenschaftlicher mitarbeiter',
            'wiss. mitarbeiter',
            'wiss. mitarbeiterin',
            'wissenschaftliche/r mitarbeiter/in',
            'research assistant',
            'research associate',
            'wissenschaftliche hilfskraft',
            'forschungsmitarbeiter',
        ],
        'english': [
            'research assistant',
            'research associate',
            'scientific staff',
            'academic staff',
            'research fellow',
        ]
    },
    'kuenstlerische_mitarbeiter': {
        'german': [
            'künstlerische mitarbeiter',
            'künstlerische mitarbeiterin',
            'künstlerischer mitarbeiter',
            'künst. mitarbeiter',
            'künst. mitarbeiterin',
            'künstlerische/r mitarbeiter/in',
            'künstlerische hilfskraft',
        ],
        'english': [
            'artistic staff',
            'artistic assistant',
            'artistic associate',
            'creative assistant',
        ]
    }
}

# Common job listing page indicators
JOB_PAGE_INDICATORS = {
    'german': [
        'stellenangebote',
        'stellenausschreibung',
        'stellenausschreibungen',
        'offene stellen',
        'karriere',
        'jobs',
        'stellenanzeigen',
        'ausschreibungen',
    ],
    'english': [
        'job openings',
        'job opportunities',
        'careers',
        'vacancies',
        'open positions',
        'employment',
        'jobs',
    ]
}

# Patterns to exclude (non-position content)
EXCLUDE_PATTERNS = [
    'exhibition',
    'ausstellung',
    'veranstaltung',
    'event',
    'katalog',
    'catalogue',
    'publikation',
    'publication',
    'workshop',
    'seminar',
    'studiengang',
    'degree program',
    'bachelor',
    'master',
]
