"""
Configuration for Art University Job Scraper - Focused on Mitarbeiter Positions Only
"""

# Simplified search terms focusing only on mitarbeiter positions
SEARCH_TERMS = {
    'german': {
        # PhD PROGRAMS - Academic Research Programs (Flexible Language Support)
        'phd_programs': {
            'media_art_phd': [
                'Medienkunst Promotion', 'Digitale Kunst Promotion', 'Neue Medien Promotion',
                'Medienkunst Doktorand', 'Digitale Kunst Doktorand', 'Neue Medien Doktorand',
                'Medienkunst PhD', 'Digitale Kunst PhD', 'Neue Medien PhD',
                'Media Art PhD', 'Digital Art PhD', 'New Media PhD',
                'Doktorandenprogramm Medienkunst', 'Promotionsprogramm Digitale Kunst',
                'Media Art Doctoral', 'Digital Art Doctoral', 'New Media Doctoral'
            ],
            'ai_art_phd': [
                'KI-Kunst Promotion', 'Künstliche Intelligenz Kunst Promotion', 'AI Art Promotion',
                'KI-Kunst Doktorand', 'AI Art Doktorand', 'Machine Learning Kunst Doktorand',
                'KI-Kunst PhD', 'AI Art PhD', 'Machine Learning Kunst PhD',
                'AI Art Doctoral', 'Machine Learning Art PhD', 'Artificial Intelligence Art PhD',
                'Doktorandenprogramm KI-Kunst', 'Promotionsprogramm AI Art'
            ],
            'artistic_research_phd': [
                # Core artistic research terms
                'Artistic Research', 'Künstlerische Forschung', 'Practice-based PhD', 'Praxis-basierte Promotion',
                'Artistic PhD', 'Künstlerische Promotion', 'Forschung in der Kunst', 'Kunst als Forschung',
                'Doktorat in Kunst', 'Promotion Kunst', 'Künstlerische Doktorarbeit', 'Forschungsprojekt Kunst',
                'Doktorandenprogramm Kunst', 'Promotionsprogramm Kunstforschung',
                
                # Practice-based research variations
                'Practice-based Research', 'Praxis-basierte Forschung', 'Practice-led Research', 'Praxisgeleitete Forschung',
                'Practice-as-Research', 'Praxis-als-Forschung', 'Practice-oriented Research', 'Praxisorientierte Forschung',
                'Practice-informed Research', 'Praxisinformierte Forschung', 'Practice-driven Research', 'Praxisgetriebene Forschung',
                
                # Artistic practice variations
                'Artistic Practice PhD', 'Künstlerische Praxis PhD', 'Artistic Practice Research', 'Künstlerische Praxis Forschung',
                'Practice-based Doctoral', 'Praxis-basierte Promotion', 'Practice-led Doctoral', 'Praxisgeleitete Promotion',
                'Artistic Practice Doctoral', 'Künstlerische Praxis Promotion', 'Creative Practice PhD', 'Kreative Praxis PhD',
                
                # Research through practice
                'Research through Practice', 'Forschung durch Praxis', 'Research by Practice', 'Forschung durch Praxis',
                'Practice as Research', 'Praxis als Forschung', 'Research in Practice', 'Forschung in der Praxis',
                'Practice-based Inquiry', 'Praxis-basierte Untersuchung', 'Practice-based Investigation', 'Praxis-basierte Untersuchung',
                
                # Creative research variations
                'Creative Research PhD', 'Kreative Forschung PhD', 'Creative Research', 'Kreative Forschung',
                'Creative Practice Research', 'Kreative Praxis Forschung', 'Creative Inquiry', 'Kreative Untersuchung',
                'Creative Investigation', 'Kreative Untersuchung', 'Creative Scholarship', 'Kreative Wissenschaft',
                
                # Alternative PhD degree names
                'DFA', 'Doctor of Fine Arts', 'Doktor der Bildenden Künste', 'Doctor of Arts', 'Doktor der Künste',
                
                # Studio-based research
                'Studio-based Research', 'Atelier-basierte Forschung', 'Studio Practice PhD', 'Atelier-Praxis PhD',
                'Studio-led Research', 'Ateliergeleitete Forschung', 'Studio Research', 'Atelier-Forschung',
                'Workshop-based Research', 'Werkstatt-basierte Forschung', 'Workshop Research', 'Werkstatt-Forschung',
                
                # Interdisciplinary research
                'Interdisciplinary Research', 'Interdisziplinäre Forschung', 'Transdisciplinary Research', 'Transdisziplinäre Forschung',
                'Cross-disciplinary Research', 'Überdisziplinäre Forschung', 'Multi-disciplinary Research', 'Multidisziplinäre Forschung',
                
                # Specific research methodologies
                'Action Research', 'Handlungsforschung', 'Participatory Research', 'Partizipative Forschung',
                'Collaborative Research', 'Kollaborative Forschung', 'Community-based Research', 'Gemeinschaftsbasierte Forschung',
                'Applied Research', 'Angewandte Forschung', 'Experimental Research', 'Experimentelle Forschung',
                
                # Research centers and programs
                'Research Center', 'Forschungszentrum', 'Research Institute', 'Forschungsinstitut',
                'Graduate Research', 'Graduiertenforschung', 'Postgraduate Research', 'Postgraduiertenforschung',
                'Advanced Research', 'Fortgeschrittene Forschung', 'Independent Research', 'Unabhängige Forschung'
            ],
            'sound_art_phd': [
                'Klangkunst Promotion', 'Sound Art Promotion', 'Audio Art Promotion',
                'Klangkunst Doktorand', 'Sound Art Doktorand', 'Audio Art Doktorand',
                'Klangkunst PhD', 'Sound Art PhD', 'Audio Art PhD',
                'Sound Art Doctoral', 'Audio Art Doctoral', 'Music Technology PhD',
                'Doktorandenprogramm Klangkunst', 'Promotionsprogramm Sound Art'
            ],
            'performance_art_phd': [
                'Performance Art Promotion', 'Aufführungskunst Promotion', 'Live Art Promotion',
                'Performance Art Doktorand', 'Aufführungskunst Doktorand', 'Live Art Doktorand',
                'Performance Art PhD', 'Aufführungskunst PhD', 'Live Art PhD',
                'Performance Art Doctoral', 'Live Art Doctoral', 'Theatre PhD',
                'Doktorandenprogramm Performance', 'Promotionsprogramm Live Art'
            ],
            'interactive_art_phd': [
                'Interaktive Kunst Promotion', 'Interactive Art Promotion', 'Partizipative Kunst Promotion',
                'Interaktive Kunst Doktorand', 'Interactive Art Doktorand', 'Partizipative Kunst Doktorand',
                'Interaktive Kunst PhD', 'Interactive Art PhD', 'Partizipative Kunst PhD',
                'Interactive Art Doctoral', 'Participatory Art PhD', 'Digital Interaction PhD',
                'Doktorandenprogramm Interaktion', 'Promotionsprogramm Interactive Art'
            ],
            'general_phd': [
                # Traditional German terms
                'Promotion', 'Doktorand', 'PhD', 'Doktorarbeit', 'Doktorat', 'Doktorandenstelle',
                'Promotionsstelle', 'Doktorandenprogramm', 'Graduate School', 'Graduiertenschule',
                'Doktorandenkolleg', 'Promotionsprogramm', 'Doktorandenausbildung',
                
                # English terms
                'Doctoral', 'Doctorate', 'Graduate Program', 'Research Program',
                'PhD Program', 'Doctoral Program', 'Graduate Studies',
                
                # Alternative PhD degree names
                'DFA', 'Doctor of Fine Arts', 'Doktor der Bildenden Künste', 'Doctor of Arts', 'Doktor der Künste',
                
                # Research-focused terms
                'Research Studies', 'Advanced Studies', 'Postgraduate Studies', 'Graduate Research',
                'Research Training', 'Research Education', 'Research Development', 'Research Mentoring',
                
                # Program variations
                'Graduate School', 'Research School', 'Doctoral School', 'PhD School',
                'Graduate Center', 'Research Center', 'Doctoral Center', 'PhD Center',
                'Graduate Institute', 'Research Institute', 'Doctoral Institute', 'PhD Institute',
                
                # Specific to art universities
                'Artistic Research', 'Creative Research', 'Practice-based Research', 'Studio Research',
                'Fine Arts Research', 'Visual Arts Research', 'Performing Arts Research',
                'Digital Arts Research', 'Media Arts Research', 'Contemporary Arts Research',
                
                # International variations
                'Candidature', 'Candidacy', 'Dissertation', 'Thesis', 'Final Project',
                'Research Project', 'Creative Project', 'Artistic Project', 'Practice Project'
            ]
        },
        
        # JOB OFFERS - Flexible Language Support for Staff Positions
        'job_offers': {
            'academic_staff': [
                # German terms
                'Künstlerische Mitarbeiter', 'Wissenschaftliche Mitarbeiter', 
                'Künstlerische Mitarbeiterin', 'Wissenschaftliche Mitarbeiterin',
                'Künstlerischer Mitarbeiter', 'Wissenschaftlicher Mitarbeiter',
                'Künstlerische Mitarbeiter/in', 'Wissenschaftliche Mitarbeiter/in',
                
                # Art-specific mitarbeiter positions (German)
                'Medienkunst Mitarbeiter', 'Digitale Kunst Mitarbeiter', 'Neue Medien Mitarbeiter',
                'KI-Kunst Mitarbeiter', 'Künstliche Intelligenz Kunst Mitarbeiter', 'AI Art Mitarbeiter',
                'Klangkunst Mitarbeiter', 'Sound Art Mitarbeiter', 'Audio Art Mitarbeiter',
                'Performance Art Mitarbeiter', 'Aufführungskunst Mitarbeiter', 'Live Art Mitarbeiter',
                'Interaktive Kunst Mitarbeiter', 'Interactive Art Mitarbeiter', 'Partizipative Kunst Mitarbeiter',
                'Künstlerische Forschung Mitarbeiter', 'Artistic Research Mitarbeiter',
                
                # Research and academic mitarbeiter (German)
                'Künstlerische Mitarbeiter Forschung', 'Wissenschaftliche Mitarbeiter Kunstforschung',
                'Forschung in der Kunst Mitarbeiter', 'Kunst als Forschung Mitarbeiter',
                'Kunstwissenschaftliche Mitarbeiter', 'Mitarbeiter Kunst', 'Mitarbeiter Forschung',
                
                # Support positions (German)
                'Künstlerische Assistenz', 'Wissenschaftliche Assistenz',
                'Künstlerische Hilfskraft', 'Wissenschaftliche Hilfskraft',
                'Forschungsassistent', 'Forschungsassistentin',
                'Projektmitarbeiter', 'Ateliermitarbeiter',
                
                # English terms
                'Artistic Staff', 'Research Staff', 'Academic Staff',
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant',
                'Artistic Associate', 'Research Associate', 'Academic Associate',
                
                # Art-specific staff positions (English)
                'Media Art Staff', 'Digital Art Staff', 'New Media Staff',
                'AI Art Staff', 'Artificial Intelligence Art Staff', 'Machine Learning Art Staff',
                'Sound Art Staff', 'Audio Art Staff', 'Performance Art Staff',
                'Interactive Art Staff', 'Participatory Art Staff',
                'Artistic Research Staff', 'Practice-based Research Staff',
                
                # Research and academic staff (English)
                'Research Staff Art', 'Academic Staff Art', 'Research Associate Art',
                'Art Research Staff', 'Creative Research Staff',
                
                # Support positions (English)
                'Project Staff', 'Studio Staff', 'Technical Staff',
                
                # Job posting terms (Multi-language)
                'Stellenausschreibung', 'Stelle', 'Stellenangebot', 'Ausschreibung', 'Vakanz',
                'Job Opening', 'Position Available', 'Vacancy', 'Employment Opportunity',
                'Staff Position', 'Academic Position', 'Research Position'
            ]
        }
    },
    
    'english': {
        # PhD PROGRAMS - Academic Research Programs (English Focus)
        'phd_programs': {
            'media_art_phd': [
                'Media Art PhD', 'Digital Art PhD', 'New Media PhD',
                'Media Art Doctoral', 'Digital Art Doctoral', 'New Media Doctoral',
                'Media Art Graduate Program', 'Digital Art Graduate Program',
                'New Media Graduate Program', 'Media Art Research Program'
            ],
            'ai_art_phd': [
                'AI Art PhD', 'Artificial Intelligence Art PhD', 'Machine Learning Art PhD',
                'AI Art Doctoral', 'Machine Learning Art Doctoral', 'Artificial Intelligence Art Doctoral',
                'AI Art Graduate Program', 'Machine Learning Art Graduate Program',
                'Artificial Intelligence Art Graduate Program', 'AI Art Research Program'
            ],
            'artistic_research_phd': [
                # Core artistic research terms
                'Artistic Research PhD', 'Practice-based PhD', 'Practice-based Research PhD',
                'Artistic Practice PhD', 'Creative Research PhD', 'Artistic Research Doctoral',
                'Practice-based Doctoral', 'Artistic Research Graduate Program',
                'Practice-based Graduate Program', 'Creative Research Graduate Program',
                
                # Practice-based research variations
                'Practice-led Research', 'Practice-as-Research', 'Practice-oriented Research',
                'Practice-informed Research', 'Practice-driven Research', 'Practice-based Inquiry',
                'Practice-based Investigation', 'Practice-based Study', 'Practice-based Scholarship',
                
                # Artistic practice variations
                'Artistic Practice Research', 'Creative Practice PhD', 'Artistic Practice Doctoral',
                'Practice-led Doctoral', 'Creative Practice Doctoral', 'Artistic Practice Graduate Program',
                'Creative Practice Graduate Program', 'Practice-led Graduate Program',
                
                # Research through practice
                'Research through Practice', 'Research by Practice', 'Practice as Research',
                'Research in Practice', 'Practice-based Inquiry', 'Practice-based Investigation',
                'Research through Art', 'Art as Research', 'Research through Creative Practice',
                
                # Creative research variations
                'Creative Research', 'Creative Practice Research', 'Creative Inquiry',
                'Creative Investigation', 'Creative Scholarship', 'Creative Study',
                'Creative Research Program', 'Creative Practice Program', 'Creative Inquiry Program',
                
                # Alternative PhD degree names
                'DFA', 'Doctor of Fine Arts', 'Doctor of Arts', 'Doctor of Creative Arts',
                
                # Studio-based research
                'Studio-based Research', 'Studio Practice PhD', 'Studio-led Research',
                'Studio Research', 'Workshop-based Research', 'Workshop Research',
                'Studio-based Doctoral', 'Studio Practice Doctoral', 'Workshop-based Doctoral',
                
                # Interdisciplinary research
                'Interdisciplinary Research', 'Transdisciplinary Research', 'Cross-disciplinary Research',
                'Multi-disciplinary Research', 'Interdisciplinary PhD', 'Transdisciplinary PhD',
                'Cross-disciplinary PhD', 'Multi-disciplinary PhD',
                
                # Specific research methodologies
                'Action Research', 'Participatory Research', 'Collaborative Research',
                'Community-based Research', 'Applied Research', 'Experimental Research',
                'Qualitative Research', 'Mixed Methods Research', 'Case Study Research',
                
                # Research centers and programs
                'Research Center', 'Research Institute', 'Graduate Research',
                'Postgraduate Research', 'Advanced Research', 'Independent Research',
                'Research Program', 'Research Studies', 'Research Training',
                
                # Specific to art universities
                'Fine Arts Research', 'Visual Arts Research', 'Performing Arts Research',
                'Digital Arts Research', 'Media Arts Research', 'Contemporary Arts Research',
                'Experimental Arts Research', 'Critical Arts Research', 'Theoretical Arts Research'
            ],
            'sound_art_phd': [
                'Sound Art PhD', 'Audio Art PhD', 'Music Technology PhD',
                'Sound Art Doctoral', 'Audio Art Doctoral', 'Music Technology Doctoral',
                'Sound Art Graduate Program', 'Audio Art Graduate Program',
                'Music Technology Graduate Program', 'Sound Art Research Program'
            ],
            'performance_art_phd': [
                'Performance Art PhD', 'Live Art PhD', 'Theatre PhD',
                'Performance Art Doctoral', 'Live Art Doctoral', 'Theatre Doctoral',
                'Performance Art Graduate Program', 'Live Art Graduate Program',
                'Theatre Graduate Program', 'Performance Art Research Program'
            ],
            'interactive_art_phd': [
                'Interactive Art PhD', 'Participatory Art PhD', 'Digital Interaction PhD',
                'Interactive Art Doctoral', 'Participatory Art Doctoral', 'Digital Interaction Doctoral',
                'Interactive Art Graduate Program', 'Participatory Art Graduate Program',
                'Digital Interaction Graduate Program', 'Interactive Art Research Program'
            ],
            'general_phd': [
                # Traditional English terms
                'PhD', 'Doctoral', 'Doctorate', 'Graduate Program', 'Research Program',
                'PhD Program', 'Doctoral Program', 'Graduate Studies', 'Graduate School',
                'Research Studies', 'Advanced Studies', 'Postgraduate Program',
                
                # Alternative PhD degree names
                'DFA', 'Doctor of Fine Arts', 'Doctor of Arts', 'Doctor of Creative Arts',
                
                # Research-focused terms
                'Research Studies', 'Advanced Studies', 'Postgraduate Studies', 'Graduate Research',
                'Research Training', 'Research Education', 'Research Development', 'Research Mentoring',
                
                # Program variations
                'Graduate School', 'Research School', 'Doctoral School', 'PhD School',
                'Graduate Center', 'Research Center', 'Doctoral Center', 'PhD Center',
                'Graduate Institute', 'Research Institute', 'Doctoral Institute', 'PhD Institute',
                
                # Specific to art universities
                'Artistic Research', 'Creative Research', 'Practice-based Research', 'Studio Research',
                'Fine Arts Research', 'Visual Arts Research', 'Performing Arts Research',
                'Digital Arts Research', 'Media Arts Research', 'Contemporary Arts Research',
                
                # International variations
                'Candidature', 'Candidacy', 'Dissertation', 'Thesis', 'Final Project',
                'Research Project', 'Creative Project', 'Artistic Project', 'Practice Project',
                
                # Additional art-specific terms
                'Art Research', 'Creative Studies', 'Artistic Studies', 'Creative Arts Research',
                'Visual Studies', 'Performance Studies', 'Media Studies', 'Digital Studies',
                'Contemporary Studies', 'Critical Studies', 'Theoretical Studies', 'Experimental Studies'
            ]
        },
        
        # JOB OFFERS - Staff Positions (English Focus)
        'job_offers': {
            'academic_staff': [
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

# Department names for extraction
DEPARTMENTS = {
    'german': [
        'Kunsthochschule', 'Kunstakademie', 'Hochschule für Bildende Künste',
        'Fakultät für Kunst', 'Fakultät für Design', 'Fakultät für Medien',
        'Institut für Kunst', 'Institut für Design', 'Institut für Medien',
        'Fachbereich Kunst', 'Fachbereich Design', 'Fachbereich Medien',
        'Studiengang Kunst', 'Studiengang Design', 'Studiengang Medien',
        'Kunstwissenschaft', 'Medienwissenschaft', 'Designwissenschaft',
        'Digitale Kunst', 'Neue Medien', 'Interaktive Medien',
        'Fotografie', 'Malerei', 'Skulptur', 'Grafik', 'Illustration',
        'Kommunikationsdesign', 'Produktdesign', 'Mode', 'Textil',
        'Architektur', 'Innenarchitektur', 'Landschaftsarchitektur',
        'Kunstgeschichte', 'Kunstpädagogik', 'Kunsttherapie',
        'Forschungsinstitut', 'Forschungszentrum', 'Graduiertenschule',
        'Künstliche Intelligenz', 'KI', 'Artificial Intelligence', 'AI', 'Machine Learning',
        'Maschinelles Lernen', 'Deep Learning', 'Neuronale Netze', 'Neural Networks',
        'Algorithmic Art', 'Algorithmische Kunst', 'Generative AI', 'Generative Kunst',
        'AI Art', 'KI-Kunst', 'Computational Creativity', 'Computational Arts',
        'Creative AI', 'Kreative KI', 'AI Tools', 'KI-Tools',
        'Informatik', 'Computer Science', 'Software Engineering', 'Programmierung',
        'Digitale Technologien', 'Medieninformatik', 'Computational Arts',
        'Creative Coding', 'Generative Design', 'Algorithmic Design',
        'Musik', 'Musikwissenschaft', 'Komposition', 'Sound Design', 'Klangkunst',
        'Audio Engineering', 'Tontechnik', 'Audioproduktion', 'Musikproduktion',
        'Elektronische Musik', 'Elektroakustik', 'Akustik', 'Sound Art',
        'Medienkunst', 'Digital Art', 'Electronic Art', 'Cyber Art',
        'Net Art', 'Internet Art', 'Web Art', 'Software Art',
        'Generative Art', 'Algorithmic Art', 'Computational Art',
        'Interactive Art', 'Participatory Art', 'Installation Art',
        'Video Art', 'Digital Video', 'Experimental Film', 'Animation',
        'Performance Art', 'Live Art', 'Body Art', 'Conceptual Art'
    ],
    'english': [
        'Art School', 'Academy of Art', 'College of Art', 'University of Art',
        'Faculty of Art', 'Faculty of Design', 'Faculty of Media',
        'Institute of Art', 'Institute of Design', 'Institute of Media',
        'Department of Art', 'Department of Design', 'Department of Media',
        'Program in Art', 'Program in Design', 'Program in Media',
        'Art Studies', 'Media Studies', 'Design Studies',
        'Digital Art', 'New Media', 'Interactive Media',
        'Photography', 'Painting', 'Sculpture', 'Graphics', 'Illustration',
        'Communication Design', 'Product Design', 'Fashion', 'Textile',
        'Architecture', 'Interior Architecture', 'Landscape Architecture',
        'Art History', 'Art Education', 'Art Therapy',
        'Research Institute', 'Research Center', 'Graduate School',
        'Artificial Intelligence', 'AI', 'Machine Learning',
        'Deep Learning', 'Neural Networks',
        'Algorithmic Art', 'Generative AI', 'Generative Art',
        'AI Art', 'Computational Creativity', 'Computational Arts',
        'Creative AI', 'AI Tools',
        'Computer Science', 'Software Engineering', 'Programming',
        'Digital Technologies', 'Media Informatics', 'Computational Arts',
        'Creative Coding', 'Generative Design', 'Algorithmic Design',
        'Music', 'Music Studies', 'Composition', 'Sound Design', 'Sound Art',
        'Audio Engineering', 'Audio Production', 'Music Production',
        'Electronic Music', 'Electroacoustics', 'Acoustics',
        'Media Art', 'Digital Art', 'Electronic Art', 'Cyber Art',
        'Net Art', 'Internet Art', 'Web Art', 'Software Art',
        'Generative Art', 'Algorithmic Art', 'Computational Art',
        'Interactive Art', 'Participatory Art', 'Installation Art',
        'Video Art', 'Digital Video', 'Experimental Film', 'Animation',
        'Performance Art', 'Live Art', 'Body Art', 'Conceptual Art'
    ]
}

# Academic position classifications
ACADEMIC_POSITIONS = {
    'german': {
        'professor': ['Professor', 'Professorin', 'W2 Professor', 'W3 Professor', 'Universitätsprofessor'],
        'lecturer': ['Dozent', 'Dozentin', 'Lehrbeauftragter', 'Lehrbeauftragte', 'Lektor', 'Lektorin'],
        'researcher': ['Wissenschaftliche Mitarbeiter', 'Wissenschaftliche Mitarbeiterin', 'Forschungsassistent', 'Forschungsassistentin'],
        'artistic_staff': ['Künstlerische Mitarbeiter', 'Künstlerische Mitarbeiterin', 'Künstlerische Assistenz'],
        'phd_student': ['Doktorand', 'Doktorandin', 'Promovend', 'Promovendin'],
        'postdoc': ['Postdoc', 'Postdoktorand', 'Postdoktorandin', 'Postdoktorand/in']
    },
    'english': {
        'professor': ['Professor', 'Full Professor', 'Associate Professor', 'Assistant Professor'],
        'lecturer': ['Lecturer', 'Senior Lecturer', 'Reader', 'Teaching Fellow'],
        'researcher': ['Research Assistant', 'Research Associate', 'Research Fellow', 'Research Officer'],
        'artistic_staff': ['Artistic Assistant', 'Studio Assistant', 'Technical Assistant'],
        'phd_student': ['PhD Student', 'Graduate Student', 'Doctoral Student', 'PhD Candidate'],
        'postdoc': ['Postdoc', 'Postdoctoral Researcher', 'Postdoctoral Fellow']
    }
}

# Employment details detection patterns
EMPLOYMENT_DETAILS = {
    'german': {
        'deadline': ['Bewerbungsfrist', 'Einsendeschluss', 'Deadline', 'bis zum', 'bis spätestens'],
        'employment_type': ['Vollzeit', 'Teilzeit', 'befristet', 'unbefristet', 'Werkvertrag'],
        'salary': ['Entgeltgruppe', 'Gehalt', 'Vergütung', 'Besoldung', 'TV-L', 'TVöD'],
        'requirements': ['Voraussetzungen', 'Qualifikation', 'Studium', 'Abschluss', 'Erfahrung']
    },
    'english': {
        'deadline': ['Application Deadline', 'Deadline', 'Closing Date', 'Due Date', 'Apply by'],
        'employment_type': ['Full-time', 'Part-time', 'Temporary', 'Permanent', 'Contract'],
        'salary': ['Salary', 'Compensation', 'Pay', 'Wage', 'Remuneration'],
        'requirements': ['Requirements', 'Qualifications', 'Education', 'Experience', 'Skills']
    }
}

# Scraping configuration
SCRAPING_CONFIG = {
    'max_pages_per_university': 3,
    'delay_between_requests': 2,
    'timeout': 30,
    'max_retries': 3,
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}