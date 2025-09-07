"""
Configuration file for the Art University Job Scraper
"""

# Search terms for different types of positions
SEARCH_TERMS = {
    'german': {
        'media_art': ['Medienkunst', 'Digitale Kunst', 'Neue Medien', 'Kunst und Medien', 'Medienkunst', 'Digitale Medien'],
        'digital_art': ['Digitale Kunst', 'Computerkunst', 'Generative Kunst', 'Algorithmische Kunst', 'Digitale Bildende Kunst'],
        'ai_art': ['KI-Kunst', 'Künstliche Intelligenz Kunst', 'Machine Learning Kunst', 'AI Art', 'KI in der Kunst', 'Algorithmische Kunst'],
        'artistic_research_phd': [
            'Artistic Research', 'Künstlerische Forschung', 'Practice-based PhD', 'Praxis-basierte Promotion',
            'Artistic PhD', 'Künstlerische Promotion', 'Forschung in der Kunst', 'Kunst als Forschung',
            'Doktorat in Kunst', 'Promotion Kunst', 'Künstlerische Doktorarbeit', 'Forschungsprojekt Kunst'
        ],
        'academic_positions': [
            'Künstlerische Mitarbeiter', 'Wissenschaftliche Mitarbeiter', 'Künstlerische Mitarbeiterin',
            'Wissenschaftliche Mitarbeiterin', 'Künstlerischer Mitarbeiter', 'Wissenschaftlicher Mitarbeiter',
            'Künstlerische Mitarbeiter/in', 'Wissenschaftliche Mitarbeiter/in', 'Mitarbeiter Kunst',
            'Mitarbeiter Forschung', 'Künstlerische Assistenz', 'Wissenschaftliche Assistenz',
            'Künstlerische Hilfskraft', 'Wissenschaftliche Hilfskraft', 'Kunstwissenschaftliche Mitarbeiter'
        ],
        'phd': [
            'Promotion', 'Doktorand', 'PhD', 'Doktorarbeit', 'Doktorat', 'Doktorandenstelle',
            'Promotionsstelle', 'Doktorandenprogramm', 'Graduate School', 'Graduiertenschule',
            'Doktorandenkolleg', 'Promotionsprogramm', 'Doktorandenausbildung'
        ],
        'jobs': [
            'Stellenausschreibung', 'Stelle', 'Job', 'Position', 'Bewerbung', 'Stellenangebot',
            'Ausschreibung', 'Stellenmarkt', 'Karriere', 'Arbeitsplatz', 'Vakanz',
            'Stellenausschreibung Kunst', 'Stellenausschreibung Forschung'
        ]
    },
    'english': {
        'media_art': ['Media Art', 'Digital Art', 'New Media', 'Art and Technology', 'Media Arts', 'Digital Media'],
        'digital_art': ['Digital Art', 'Computer Art', 'Generative Art', 'Algorithmic Art', 'Digital Fine Arts'],
        'ai_art': ['AI Art', 'Artificial Intelligence Art', 'Machine Learning Art', 'Neural Art', 'AI in Art', 'Algorithmic Art'],
        'artistic_research_phd': [
            'Artistic Research', 'Practice-based PhD', 'Artistic PhD', 'Research in Art', 'Art as Research',
            'Doctorate in Art', 'PhD in Art', 'Artistic Doctorate', 'Research Project Art', 'Creative Research',
            'Practice-led Research', 'Artistic Practice Research', 'Studio-based Research'
        ],
        'academic_positions': [
            'Artistic Assistant', 'Research Assistant', 'Academic Assistant', 'Artistic Staff',
            'Research Staff', 'Academic Staff', 'Artistic Collaborator', 'Research Collaborator',
            'Artistic Associate', 'Research Associate', 'Artistic Fellow', 'Research Fellow',
            'Artistic Coordinator', 'Research Coordinator', 'Artistic Technician', 'Research Technician'
        ],
        'phd': [
            'PhD', 'Doctorate', 'Doctoral', 'Graduate Studies', 'PhD Position', 'Doctoral Position',
            'PhD Program', 'Doctoral Program', 'Graduate Program', 'PhD Student', 'Doctoral Student',
            'PhD Candidate', 'Doctoral Candidate', 'Graduate Student', 'Research Student'
        ],
        'jobs': [
            'Job Opening', 'Position', 'Vacancy', 'Employment', 'Career', 'Job Opportunity',
            'Academic Position', 'Research Position', 'Art Position', 'Faculty Position',
            'Staff Position', 'Academic Job', 'Research Job', 'Art Job'
        ]
    }
}

# University data extracted from CSV
UNIVERSITIES = [
    {
        'name': 'Alanus Hochschule für Kunst und Gesellschaft',
        'city': 'Alfter',
        'country': 'Germany',
        'website': 'https://www.alanus.edu',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Kunsthochschule Berlin-Weißensee',
        'city': 'Berlin',
        'country': 'Germany',
        'website': 'https://www.kh-berlin.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Universität der Künste Berlin',
        'city': 'Berlin',
        'country': 'Germany',
        'website': 'https://www.udk-berlin.de',
        'has_phd': False,
        'alternative': 'Graduate School',
        'phd_url': 'https://www.udk-berlin.de/en/research/graduate-school/'
    },
    {
        'name': 'Hochschule für Bildende Künste Braunschweig',
        'city': 'Braunschweig',
        'country': 'Germany',
        'website': 'https://www.hbk-bs.de',
        'has_phd': True,
        'phd_url': 'https://www.hbk-bs.de/hochschule/forschung-entwicklung/'
    },
    {
        'name': 'Hochschule für Künste Bremen',
        'city': 'Bremen',
        'country': 'Germany',
        'website': 'https://www.hfk-bremen.de',
        'has_phd': True,
        'phd_url': 'https://artisticphd-hfkbremen.net'
    },
    {
        'name': 'Hochschule für Bildende Künste Dresden',
        'city': 'Dresden',
        'country': 'Germany',
        'website': 'https://www.hfbk-dresden.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Kunstakademie Düsseldorf',
        'city': 'Düsseldorf',
        'country': 'Germany',
        'website': 'https://www.kunstakademie-duesseldorf.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Folkwang Universität der Künste',
        'city': 'Essen',
        'country': 'Germany',
        'website': 'https://www.folkwang-uni.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Hochschule der bildenden Künste Essen',
        'city': 'Essen',
        'country': 'Germany',
        'website': 'https://www.hbk-essen.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Staatliche Hochschule für Bildende Künste – Städelschule',
        'city': 'Frankfurt am Main',
        'country': 'Germany',
        'website': 'https://www.staedelschule.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Burg Giebichenstein Kunsthochschule Halle',
        'city': 'Halle (Saale)',
        'country': 'Germany',
        'website': 'https://www.burg-halle.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Hochschule für bildende Künste Hamburg',
        'city': 'Hamburg',
        'country': 'Germany',
        'website': 'https://www.hfbk-hamburg.de',
        'has_phd': True,
        'phd_url': 'https://www.hfbk-hamburg.de/en/studium/promotion-der-hfbk-hamburg/'
    },
    {
        'name': 'Staatliche Akademie der Bildenden Künste Karlsruhe',
        'city': 'Karlsruhe',
        'country': 'Germany',
        'website': 'https://www.karlsruhe.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Staatliche Hochschule für Gestaltung Karlsruhe',
        'city': 'Karlsruhe',
        'country': 'Germany',
        'website': 'https://www.hfg-karlsruhe.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Kunsthochschule Kassel',
        'city': 'Kassel',
        'country': 'Germany',
        'website': 'https://www.kunsthochschule-kassel.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Muthesius Kunsthochschule',
        'city': 'Kiel',
        'country': 'Germany',
        'website': 'https://www.muthesius-kunsthochschule.de',
        'has_phd': True,
        'phd_url': 'https://en.muthesius-kunsthochschule.de/phds/'
    },
    {
        'name': 'Kunsthochschule für Medien Köln',
        'city': 'Köln',
        'country': 'Germany',
        'website': 'https://www.khm.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Hochschule für Grafik und Buchkunst Leipzig',
        'city': 'Leipzig',
        'country': 'Germany',
        'website': 'https://www.hgb-leipzig.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Kunsthochschule Mainz',
        'city': 'Mainz',
        'country': 'Germany',
        'website': 'https://www.kunsthochschule-mainz.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Akademie der Bildenden Künste München',
        'city': 'München',
        'country': 'Germany',
        'website': 'https://www.adbk.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Kunstakademie Münster',
        'city': 'Münster',
        'country': 'Germany',
        'website': 'https://www.kunstakademie-muenster.de',
        'has_phd': False,
        'alternative': 'PhD'
    },
    {
        'name': 'Akademie der Bildenden Künste Nürnberg',
        'city': 'Nürnberg',
        'country': 'Germany',
        'website': 'https://www.adbk-nuernberg.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Hochschule für Gestaltung Offenbach am Main',
        'city': 'Offenbach am Main',
        'country': 'Germany',
        'website': 'https://www.hfg-offenbach.de',
        'has_phd': True,
        'phd_url': 'https://www.hfg-offenbach.de/en/pages/phd#doctorate'
    },
    {
        'name': 'Hochschule für Künste im Sozialen Ottersberg',
        'city': 'Ottersberg',
        'country': 'Germany',
        'website': 'https://www.hks-ottersberg.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Staatliche Kunstschule für Textilindustrie Plauen',
        'city': 'Plauen',
        'country': 'Germany',
        'website': 'https://www.kunstschule-plauen.de',
        'has_phd': False,
        'alternative': None
    },
    {
        'name': 'Hochschule der Bildenden Künste Saar',
        'city': 'Saarbrücken',
        'country': 'Germany',
        'website': 'https://www.hbksaar.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Staatliche Akademie der Bildenden Künste Stuttgart',
        'city': 'Stuttgart',
        'country': 'Germany',
        'website': 'https://www.abk-stuttgart.de',
        'has_phd': False,
        'alternative': 'Dr.phil'
    },
    {
        'name': 'Bauhaus-Universität Weimar',
        'city': 'Weimar',
        'country': 'Germany',
        'website': 'https://www.uni-weimar.de',
        'has_phd': True,
        'phd_url': 'https://www.uni-weimar.de/en/art-and-design/studies/doctorate-at-the-faculty-of-art-and-design/degree-programmes/degree-programme-phd/'
    },
    {
        'name': 'Universität für angewandte Kunst Wien',
        'city': 'Wien',
        'country': 'Austria',
        'website': 'https://www.dieangewandte.at',
        'has_phd': True,
        'alternative': 'PhD in Art'
    },
    {
        'name': 'Kunstuniversität Linz',
        'city': 'Linz',
        'country': 'Austria',
        'website': 'https://www.kunstuni-linz.at',
        'has_phd': True,
        'phd_url': 'https://www.kunstuni-linz.at/PhD-Programme-Intro.14861+M52087573ab0.0.html'
    },
    {
        'name': 'Kunstuniversität Graz',
        'city': 'Graz',
        'country': 'Austria',
        'website': 'https://www.kug.ac.at',
        'has_phd': True,
        'phd_url': 'https://doctorartium.kug.ac.at/'
    }
]

# Additional major international art universities
INTERNATIONAL_UNIVERSITIES = [
    {
        'name': 'Royal College of Art',
        'city': 'London',
        'country': 'UK',
        'website': 'https://www.rca.ac.uk',
        'has_phd': True,
        'phd_url': 'https://www.rca.ac.uk/research/'
    },
    {
        'name': 'Central Saint Martins',
        'city': 'London',
        'country': 'UK',
        'website': 'https://www.arts.ac.uk/csm',
        'has_phd': True,
        'phd_url': 'https://www.arts.ac.uk/csm/research'
    },
    {
        'name': 'Parsons School of Design',
        'city': 'New York',
        'country': 'USA',
        'website': 'https://www.newschool.edu/parsons',
        'has_phd': True,
        'phd_url': 'https://www.newschool.edu/parsons/phd-design'
    },
    {
        'name': 'Rhode Island School of Design',
        'city': 'Providence',
        'country': 'USA',
        'website': 'https://www.risd.edu',
        'has_phd': True,
        'phd_url': 'https://www.risd.edu/academics/graduate-studies'
    },
    {
        'name': 'California Institute of the Arts',
        'city': 'Valencia',
        'country': 'USA',
        'website': 'https://www.calarts.edu',
        'has_phd': True,
        'phd_url': 'https://www.calarts.edu/academics/graduate-programs'
    }
]

# Scraping configuration
SCRAPING_CONFIG = {
    'request_delay': 2,  # seconds between requests
    'timeout': 30,  # request timeout in seconds
    'max_retries': 3,
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'headers': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5,de;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
}

# Database configuration
DATABASE_CONFIG = {
    'db_path': 'art_positions.db',
    'tables': {
        'positions': 'CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, university TEXT, position_type TEXT, title TEXT, description TEXT, url TEXT, language TEXT, date_found TEXT, status TEXT)',
        'universities': 'CREATE TABLE IF NOT EXISTS universities (id INTEGER PRIMARY KEY, name TEXT, city TEXT, country TEXT, website TEXT, has_phd BOOLEAN, last_scraped TEXT)'
    }
}