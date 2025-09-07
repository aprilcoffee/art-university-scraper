"""
Configuration for Art University Job Scraper - Focused on Mitarbeiter Positions Only
"""

# Simplified search terms focusing only on mitarbeiter positions
SEARCH_TERMS = {
    'german': {
        # PhD PROGRAMS - Disabled to focus only on job positions (mitarbeiter)
        'phd_programs': {
            # Empty - focusing only on job positions (mitarbeiter)
        },
        
        # JOB OFFERS - Focus on Mitarbeiter Positions Only
        'job_offers': {
            'mitarbeiter_positions': [
                # Core mitarbeiter terms
                'Künstlerische Mitarbeiter', 'Wissenschaftliche Mitarbeiter', 
                'Künstlerische Mitarbeiterin', 'Wissenschaftliche Mitarbeiterin',
                'Künstlerischer Mitarbeiter', 'Wissenschaftlicher Mitarbeiter',
                'Künstlerische Mitarbeiter/in', 'Wissenschaftliche Mitarbeiter/in',
                
                # Art-specific mitarbeiter positions
                'Medienkunst Mitarbeiter', 'Digitale Kunst Mitarbeiter', 'Neue Medien Mitarbeiter',
                'KI-Kunst Mitarbeiter', 'Künstliche Intelligenz Kunst Mitarbeiter', 'AI Art Mitarbeiter',
                'Klangkunst Mitarbeiter', 'Sound Art Mitarbeiter', 'Audio Art Mitarbeiter',
                'Performance Art Mitarbeiter', 'Aufführungskunst Mitarbeiter', 'Live Art Mitarbeiter',
                'Interaktive Kunst Mitarbeiter', 'Interactive Art Mitarbeiter', 'Partizipative Kunst Mitarbeiter',
                'Künstlerische Forschung Mitarbeiter', 'Artistic Research Mitarbeiter',
                
                # Research and academic mitarbeiter
                'Künstlerische Mitarbeiter Forschung', 'Wissenschaftliche Mitarbeiter Kunstforschung',
                'Forschung in der Kunst Mitarbeiter', 'Kunst als Forschung Mitarbeiter',
                'Kunstwissenschaftliche Mitarbeiter', 'Mitarbeiter Kunst', 'Mitarbeiter Forschung',
                
                # Support positions
                'Künstlerische Assistenz', 'Wissenschaftliche Assistenz',
                'Künstlerische Hilfskraft', 'Wissenschaftliche Hilfskraft',
                'Forschungsassistent', 'Forschungsassistentin',
                'Projektmitarbeiter', 'Ateliermitarbeiter',
                
                # Job posting terms
                'Stellenausschreibung', 'Stelle', 'Stellenangebot', 'Ausschreibung', 'Vakanz'
            ]
        }
    },
    
    'english': {
        # PhD PROGRAMS - Disabled to focus only on job positions
        'phd_programs': {
            # Empty - focusing only on job positions
        },
        
        # JOB OFFERS - Focus on Staff Positions Only
        'job_offers': {
            'staff_positions': [
                # Core staff terms
                'Artistic Staff', 'Research Staff', 'Academic Staff',
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant',
                'Artistic Associate', 'Research Associate', 'Academic Associate',
                
                # Art-specific staff positions
                'Media Art Staff', 'Digital Art Staff', 'New Media Staff',
                'AI Art Staff', 'Artificial Intelligence Art Staff', 'Machine Learning Art Staff',
                'Sound Art Staff', 'Audio Art Staff', 'Performance Art Staff',
                'Interactive Art Staff', 'Participatory Art Staff',
                'Artistic Research Staff', 'Practice-based Research Staff',
                
                # Research and academic staff
                'Research Staff Art', 'Academic Staff Art', 'Research Associate Art',
                'Art Research Staff', 'Creative Research Staff',
                
                # Support positions
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant',
                'Project Staff', 'Studio Staff', 'Technical Staff',
                
                # Job posting terms
                'Job Opening', 'Position Available', 'Vacancy', 'Employment Opportunity',
                'Staff Position', 'Academic Position', 'Research Position'
            ]
        }
    }
}

# Universities configuration (keeping the same)
UNIVERSITIES_BY_COUNTRY = {
    'germany': [
        'Alanus Hochschule für Kunst und Gesellschaft',
        'Kunsthochschule Berlin-Weißensee',
        'Universität der Künste Berlin',
        'Hochschule für Bildende Künste Braunschweig',
        'Hochschule für Künste Bremen',
        'Hochschule für Bildende Künste Dresden',
        'Kunstakademie Düsseldorf',
        'Folkwang Universität der Künste',
        'Hochschule der bildenden Künste Essen',
        'Staatliche Hochschule für Bildende Künste – Städelschule',
        'Burg Giebichenstein Kunsthochschule Halle',
        'Hochschule für bildende Künste Hamburg',
        'Staatliche Hochschule für Gestaltung Karlsruhe',
        'Muthesius Kunsthochschule',
        'Kunsthochschule für Medien Köln',
        'Hochschule für Grafik und Buchkunst Leipzig',
        'Kunsthochschule Mainz',
        'Akademie der Bildenden Künste München',
        'Kunstakademie Münster',
        'Akademie der Bildenden Künste Nürnberg',
        'Hochschule für Gestaltung Offenbach am Main',
        'Hochschule der Bildenden Künste Saar',
        'Staatliche Akademie der Bildenden Künste Stuttgart',
        'Bauhaus-Universität Weimar'
    ],
    'austria': [
        'Universität für angewandte Kunst Wien',
        'Kunstuniversität Linz',
        'Kunstuniversität Graz',
        'Universität Mozarteum Salzburg',
        'Hochschule für Musik und Darstellende Kunst Wien'
    ],
    'switzerland': [
        'Hochschule für Gestaltung und Kunst Basel',
        'Hochschule für Gestaltung und Kunst Bern'
    ],
    'uk': [
        'Royal College of Art',
        'Goldsmiths University of London',
        'Slade School of Fine Art',
        'Glasgow School of Art',
        'Edinburgh College of Art'
    ],
    'netherlands': [
        'Design Academy Eindhoven',
        'Royal Academy of Art The Hague'
    ],
    'sweden': [
        'Konstfack University of Arts, Crafts and Design'
    ],
    'france': [
        'École Nationale Supérieure des Beaux-Arts'
    ]
}

# Flatten the universities list
UNIVERSITIES = []
for country, unis in UNIVERSITIES_BY_COUNTRY.items():
    for uni in unis:
        UNIVERSITIES.append({
            'name': uni,
            'country': country,
            'website': f'https://{uni.lower().replace(" ", "").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")}.de' if country == 'germany' else f'https://{uni.lower().replace(" ", "").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")}.com'
        })

# Scraping configuration
SCRAPING_CONFIG = {
    'max_pages_per_university': 3,
    'delay_between_requests': 2,
    'timeout': 30,
    'max_retries': 3,
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}