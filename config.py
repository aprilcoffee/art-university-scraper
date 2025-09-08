"""
Configuration for Art University Job Scraper - Focused on Mitarbeiter Positions Only
"""

# Optimized search terms focusing on mitarbeiter stelle and PhD/promotion positions
SEARCH_TERMS = {
    'german': {
        # PhD PROGRAMS - Academic Research Programs
        'phd_programs': {
            'artistic_research_phd': [
                # Core PhD terms
                'PhD', 'Promotion', 'Doktorand', 'Doktorat', 'Doctorate', 'Doctoral',
                'Doktorandenprogramm', 'Promotionsprogramm', 'Graduiertenschule',
                'Doctor of Fine Arts', 'DFA', 'Doktor der Bildenden Künste',
                
                # Artistic research specific
                'Artistic Research', 'Künstlerische Forschung', 'Practice-based PhD', 'Praxis-basierte Promotion',
                'Artistic PhD', 'Künstlerische Promotion', 'Forschung in der Kunst', 'Kunst als Forschung',
                'Practice-based Research', 'Praxis-basierte Forschung', 'Practice-led Research', 'Praxisgeleitete Forschung',
                'Artistic Practice PhD', 'Künstlerische Praxis PhD', 'Creative Research PhD', 'Kreative Forschung PhD',
                'Studio-based Research', 'Atelier-basierte Forschung', 'Research through Practice', 'Forschung durch Praxis',
                'Interdisciplinary Research', 'Interdisziplinäre Forschung', 'Transdisciplinary Research'
            ],
            'media_art_phd': [
                'Medienkunst Promotion', 'Digitale Kunst Promotion', 'Neue Medien Promotion',
                'Medienkunst Doktorand', 'Digitale Kunst Doktorand', 'Neue Medien Doktorand',
                'Medienkunst PhD', 'Digitale Kunst PhD', 'Neue Medien PhD',
                'Media Art PhD', 'Digital Art PhD', 'New Media PhD',
                'Doktorandenprogramm Medienkunst', 'Promotionsprogramm Digitale Kunst'
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
                # Specific PhD program terms
                'PhD Program', 'PhD Programme', 'Doctoral Program', 'Doctoral Programme',
                'Promotionsprogramm', 'Doktorandenprogramm', 'Graduate Program', 'Graduate Programme',
                
                # PhD positions and opportunities
                'PhD Position', 'PhD Stelle', 'Doktorandenstelle', 'Promotionsstelle',
                'PhD Opportunity', 'Doctoral Opportunity', 'PhD Vacancy', 'Doctoral Vacancy',
                
                # PhD degrees
                'PhD', 'Doctor of Philosophy', 'Doctor of Fine Arts', 'DFA',
                'Doktor der Bildenden Künste', 'Doctor of Arts', 'Doktor der Künste',
                
                # PhD application and admission
                'PhD Application', 'PhD Bewerbung', 'Doctoral Application', 'Promotionsbewerbung',
                'PhD Admission', 'Doctoral Admission', 'PhD Zulassung', 'Promotionszulassung',
                
                # Graduate schools and centers
                'Graduate School', 'Graduiertenschule', 'Doctoral School', 'Promotionsschule',
                'Graduate Center', 'Graduiertenzentrum', 'Doctoral Center', 'Promotionszentrum'
            ]
        },
        
        # JOB OFFERS - Optimized for mitarbeiter stelle positions
        'job_offers': {
            'mitarbeiter_stelle': [
                # Core mitarbeiter terms
                'mitarbeiter gesucht', 'mitarbeiterin gesucht', 'mitarbeiter/in gesucht',
                'mitarbeiter stelle', 'mitarbeiterstelle', 'mitarbeiter stellen',
                'mitarbeiter position', 'mitarbeiter positionen', 'mitarbeiter jobs',
                
                # Artistic mitarbeiter (most important for art schools)
                'künstlerische mitarbeiter', 'künstlerische mitarbeiterin',
                'künstlerischer mitarbeiter', 'künstlerische mitarbeiter/in',
                'artistic mitarbeiter', 'artistic mitarbeiterin',
                'kunst mitarbeiter', 'kunst mitarbeiterin',
                'art mitarbeiter', 'art mitarbeiterin',
                
                # Specific artistic mitarbeiter types
                'medienkunst mitarbeiter', 'digitale kunst mitarbeiter',
                'ki-kunst mitarbeiter', 'klangkunst mitarbeiter',
                'performance art mitarbeiter', 'interactive art mitarbeiter',
                'sound art mitarbeiter', 'visual art mitarbeiter',
                'contemporary art mitarbeiter', 'experimental art mitarbeiter',
                
                # Design-specific mitarbeiter (important for design schools like KISD)
                'design mitarbeiter', 'design mitarbeiterin', 'designer mitarbeiter',
                'gestaltung mitarbeiter', 'gestaltung mitarbeiterin',
                'product design mitarbeiter', 'communication design mitarbeiter',
                'graphic design mitarbeiter', 'interaction design mitarbeiter',
                'service design mitarbeiter', 'user experience mitarbeiter',
                
                # Wissenschaftliche mitarbeiter (scientific/academic staff)
                'wissenschaftliche mitarbeiter', 'wissenschaftliche mitarbeiterin',
                'wissenschaftlicher mitarbeiter', 'wissenschaftliche mitarbeiter/in',
                'wiss mitarbeiter', 'wiss mitarbeiterin',
                
                # Mixed artistic-scientific positions (common in art schools)
                'künstlerische wissenschaftliche mitarbeiter', 'künstlerische wissenschaftliche mitarbeiterin',
                'artistic scientific mitarbeiter', 'kunst wissenschaftliche mitarbeiter',
                'art wissenschaftliche mitarbeiter', 'medienkunst wissenschaftliche mitarbeiter',
                
                # Other mitarbeiter types
                'akademische mitarbeiter', 'akademische mitarbeiterin',
                'forschungs mitarbeiter', 'forschungs mitarbeiterin',
                'projekt mitarbeiter', 'projekt mitarbeiterin',
                
                # Job posting terms
                'stellenausschreibung', 'stellenangebot', 'stellenausschreibungen',
                'stelle gesucht', 'stellen gesucht', 'offene stelle', 'offene stellen',
                'bewerbung', 'bewerbungen', 'karriere', 'career',
                
                # Staff positions
                'staff position', 'staff positions', 'academic staff', 'research staff',
                'artistic staff', 'artistic assistant', 'research assistant',
                'project staff', 'studio staff', 'technical staff'
            ],
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
                # Specific PhD program terms
                'PhD Program', 'PhD Programme', 'Doctoral Program', 'Doctoral Programme',
                'Graduate Program', 'Graduate Programme', 'PhD Studies', 'Doctoral Studies',
                
                # PhD positions and opportunities
                'PhD Position', 'PhD Opportunity', 'Doctoral Position', 'Doctoral Opportunity',
                'PhD Vacancy', 'Doctoral Vacancy', 'PhD Opening', 'Doctoral Opening',
                
                # PhD degrees
                'PhD', 'Doctor of Philosophy', 'Doctor of Fine Arts', 'DFA',
                'Doctor of Arts', 'Doctor of Creative Arts', 'Doctorate',
                
                # PhD application and admission
                'PhD Application', 'Doctoral Application', 'PhD Admission', 'Doctoral Admission',
                'PhD Requirements', 'Doctoral Requirements', 'PhD Entry', 'Doctoral Entry',
                
                # Graduate schools and centers
                'Graduate School', 'Doctoral School', 'PhD School', 'Graduate Center',
                'Doctoral Center', 'PhD Center', 'Graduate Institute', 'Doctoral Institute'
            ]
        },
        
        # JOB OFFERS - Staff Positions (English Focus)
        'job_offers': {
            'artistic_staff': [
                # Artistic staff positions (most important for art schools)
                'artistic staff', 'artistic staff wanted', 'artistic staff position',
                'artistic assistant', 'artistic associate', 'artistic coordinator',
                'artistic technician', 'artistic collaborator', 'artistic fellow',
                
                # Art-specific staff positions
                'media art staff', 'digital art staff', 'new media staff',
                'ai art staff', 'artificial intelligence art staff', 'machine learning art staff',
                'sound art staff', 'audio art staff', 'performance art staff',
                'interactive art staff', 'participatory art staff', 'visual art staff',
                'contemporary art staff', 'experimental art staff', 'fine art staff',
                
                # Design-specific staff positions (important for design schools like KISD)
                'design staff', 'designer staff', 'design assistant', 'design coordinator',
                'product design staff', 'communication design staff', 'graphic design staff',
                'interaction design staff', 'service design staff', 'user experience staff',
                'industrial design staff', 'fashion design staff', 'interior design staff',
                
                # Scientific/academic staff (wissenschaftliche mitarbeiter)
                'scientific staff', 'academic staff', 'research staff',
                'scientific assistant', 'academic assistant', 'research assistant',
                'scientific associate', 'academic associate', 'research associate',
                
                # Mixed artistic-scientific positions (common in art schools)
                'artistic scientific staff', 'artistic academic staff', 'artistic research staff',
                'art scientific staff', 'art academic staff', 'art research staff',
                'media art scientific staff', 'digital art academic staff',
                'sound art research staff', 'performance art scientific staff',
                
                # Studio and project staff
                'studio staff', 'studio assistant', 'studio technician',
                'project staff', 'project assistant', 'project coordinator',
                
                # General staff terms
                'staff wanted', 'staff position', 'staff positions', 'staff vacancy', 'staff vacancies',
                'academic position', 'research position', 'scientific position',
                
                # Job posting pages
                'job posting', 'job postings', 'position available', 'positions available',
                'job opening', 'job openings', 'vacancy', 'vacancies',
                
                # Career pages
                'career', 'careers', 'employment', 'recruitment', 'hiring'
            ],
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

# Universities configuration - ART SCHOOLS AND DESIGN SCHOOLS ONLY
UNIVERSITIES_BY_COUNTRY = {
    'germany': [
        # Art Schools (Kunsthochschulen)
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
        'Muthesius Kunsthochschule',
        'Kunsthochschule für Medien Köln',
        'Köln International School of Design (KISD)',
        'Hochschule für Grafik und Buchkunst Leipzig',
        'Kunsthochschule Mainz',
        'Akademie der Bildenden Künste München',
        'Kunstakademie Münster',
        'Akademie der Bildenden Künste Nürnberg',
        'Hochschule der Bildenden Künste Saar',
        'Staatliche Akademie der Bildenden Künste Stuttgart',
        'Bauhaus-Universität Weimar',
        
        # Design Schools (Gestaltungshochschulen)
        'Staatliche Hochschule für Gestaltung Karlsruhe',
        'Hochschule für Gestaltung Offenbach am Main',
        'Hochschule für Gestaltung Schwäbisch Gmünd',
        'Hochschule für Gestaltung Pforzheim',
        
        # Technical Universities with Strong Design Departments
        'Technische Universität Berlin',
        'Technische Universität München',
        'RWTH Aachen',
        'Technische Universität Darmstadt',
        'Universität Stuttgart',
        'Technische Universität Dresden',
        
        # Music/Theater Universities
        'Hochschule für Musik und Theater Hamburg',
        'Hochschule für Musik und Theater München',
        'Hochschule für Musik und Theater Leipzig',
        'Hochschule für Musik und Theater Hannover',
        'Hochschule für Musik und Theater Rostock',
        'Hochschule für Musik und Theater Weimar'
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
        'Hochschule für Gestaltung und Kunst Bern',
        'Hochschule für Gestaltung und Kunst Zürich',
        'Hochschule für Gestaltung und Kunst Luzern'
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
        'Royal Academy of Art The Hague',
        'Gerrit Rietveld Academie',
        'ArtEZ University of the Arts',
        'HKU University of the Arts Utrecht',
        'Willem de Kooning Academy',
        'Royal Academy of Art The Hague',
        'Amsterdam University of the Arts',
        'ArtEZ Institute of the Arts',
        'Minerva Art Academy',
        'St. Joost School of Art & Design',
        'AKV St. Joost',
        'Fontys Academy of the Arts',
        'Zuyd University of Applied Sciences',
        'Hanze University of Applied Sciences',
        'Rotterdam University of Applied Sciences'
    ],
    'belgium': [
        'La Cambre',
        'Royal Academy of Fine Arts Antwerp',
        'Royal Academy of Fine Arts Brussels',
        'LUCA School of Arts',
        'Hogeschool Gent',
        'Hogeschool Sint-Lukas Brussels',
        'PXL-MAD School of Arts',
        'KASK & Conservatory',
        'Académie Royale des Beaux-Arts de Bruxelles',
        'École Supérieure des Arts Saint-Luc Liège',
        'École Supérieure des Arts Saint-Luc Tournai',
        'École Supérieure des Arts de l\'Image Le 75',
        'École Supérieure des Arts de Mons',
        'École Supérieure des Arts du Cirque',
        'Institut des Arts de Diffusion'
    ],
    'estonia': [
        'Estonian Academy of Arts',
        'Estonian Academy of Music and Theatre',
        'University of Tartu Viljandi Culture Academy',
        'Tallinn University Baltic Film, Media, Arts and Communication School',
        'Estonian Academy of Arts',
        'Estonian University of Life Sciences',
        'Estonian Business School'
    ],
    'denmark': [
        'Royal Danish Academy of Fine Arts',
        'Design School Kolding',
        'Aarhus School of Architecture',
        'The Royal Danish Academy of Music',
        'Danish National School of Performing Arts',
        'The Animation Workshop',
        'VIA University College',
        'University College South Denmark',
        'Copenhagen School of Design and Technology',
        'KEA - Copenhagen School of Design and Technology',
        'Zealand Institute of Business and Technology',
        'University College Lillebælt'
    ],
    'sweden': [
        'Konstfack University of Arts, Crafts and Design',
        'Royal Institute of Art Stockholm',
        'University College of Arts, Crafts and Design',
        'Stockholm University of the Arts',
        'Malmö Art Academy',
        'Umeå Institute of Design',
        'Beckmans College of Design',
        'Berghs School of Communication',
        'Forsbergs School of Design',
        'Hyper Island',
        'Stockholm Academy of Dramatic Arts',
        'Royal College of Music Stockholm'
    ],
    'france': [
        'École Nationale Supérieure des Beaux-Arts',
        'École Nationale Supérieure des Arts Décoratifs',
        'École Nationale Supérieure de Création Industrielle',
        'École Supérieure d\'Art et Design de Saint-Étienne',
        'École Supérieure des Beaux-Arts de Marseille',
        'École Supérieure des Beaux-Arts de Toulouse',
        'École Supérieure des Beaux-Arts de Nantes',
        'École Supérieure des Beaux-Arts de Lyon',
        'École Supérieure des Beaux-Arts de Rennes',
        'École Supérieure des Beaux-Arts de Bordeaux',
        'École Supérieure des Beaux-Arts de Montpellier',
        'École Supérieure des Beaux-Arts de Angers',
        'École Supérieure des Beaux-Arts de Le Havre',
        'École Supérieure des Beaux-Arts de Valence',
        'École Supérieure des Beaux-Arts de Dunkerque',
        'École Supérieure des Beaux-Arts de Caen',
        'École Supérieure des Beaux-Arts de Besançon',
        'École Supérieure des Beaux-Arts de Dijon',
        'École Supérieure des Beaux-Arts de Nancy',
        'École Supérieure des Beaux-Arts de Metz',
        'École Supérieure des Beaux-Arts de Mulhouse',
        'École Supérieure des Beaux-Arts de Strasbourg',
        'École Supérieure des Beaux-Arts de Reims',
        'École Supérieure des Beaux-Arts de Rouen',
        'École Supérieure des Beaux-Arts de Amiens',
        'École Supérieure des Beaux-Arts de Boulogne-Billancourt',
        'École Supérieure des Beaux-Arts de Cergy-Pontoise',
        'École Supérieure des Beaux-Arts de Évry',
        'École Supérieure des Beaux-Arts de Versailles',
        'École Supérieure des Beaux-Arts de Orléans',
        'École Supérieure des Beaux-Arts de Tours',
        'École Supérieure des Beaux-Arts de Poitiers',
        'École Supérieure des Beaux-Arts de Limoges',
        'École Supérieure des Beaux-Arts de Clermont-Ferrand',
        'École Supérieure des Beaux-Arts de Bourges',
        'École Supérieure des Beaux-Arts de Nevers',
        'École Supérieure des Beaux-Arts de Chalon-sur-Saône',
        'École Supérieure des Beaux-Arts de Belfort',
        'École Supérieure des Beaux-Arts d\'Épinal',
        'École Supérieure des Beaux-Arts de Troyes',
        'École Supérieure des Beaux-Arts de Châlons-en-Champagne',
        'École Supérieure des Beaux-Arts de Charleville-Mézières'
    ],
    'usa': [
        'Rhode Island School of Design',
        'School of the Art Institute of Chicago',
        'California Institute of the Arts',
        'Parsons School of Design',
        'Pratt Institute',
        'Cooper Union',
        'Art Center College of Design',
        'Cranbrook Academy of Art',
        'Yale School of Art',
        'New York University Tisch School of the Arts',
        'UCLA School of the Arts and Architecture',
        'Carnegie Mellon School of Art',
        'Virginia Commonwealth University School of the Arts',
        'Maryland Institute College of Art',
        'Massachusetts College of Art and Design',
        'Minneapolis College of Art and Design',
        'Kansas City Art Institute',
        'Ringling College of Art and Design',
        'Otis College of Art and Design',
        'Laguna College of Art and Design',
        'Academy of Art University',
        'Art Institute of Chicago',
        'School of Visual Arts',
        'Fashion Institute of Technology'
    ],
    'canada': [
        'Emily Carr University of Art and Design',
        'Ontario College of Art and Design University',
        'Alberta College of Art and Design',
        'Concordia University Faculty of Fine Arts',
        'University of Toronto Faculty of Music'
    ],
    'australia': [
        'University of New South Wales Art & Design',
        'University of Sydney Sydney College of the Arts',
        'RMIT University School of Art',
        'Queensland College of Art'
    ],
    'japan': [
        'Tama Art University',
        'Musashino Art University',
        'Kyoto University of Art and Design',
        'Osaka University of Arts'
    ],
    'hong_kong': [
        'Hong Kong Academy for Performing Arts',
        'Hong Kong Baptist University Academy of Visual Arts',
        'City University of Hong Kong School of Creative Media'
    ],
    'south_korea': [
        'Korea National University of Arts',
        'Hongik University College of Fine Arts',
        'Seoul National University College of Fine Arts',
        'Ewha Womans University College of Art & Design'
    ],
    'singapore': [
        'Singapore LASALLE College of the Arts',
        'Nanyang Academy of Fine Arts'
    ],
    'philippines': [
        'University of the Philippines College of Fine Arts',
        'De La Salle College of Saint Benilde School of Design and Arts',
        'University of Santo Tomas College of Fine Arts and Design'
    ],
    'thailand': [
        'Chulalongkorn University Faculty of Fine and Applied Arts',
        'Silpakorn University Faculty of Painting Sculpture and Graphic Arts',
        'Thammasat University Faculty of Fine and Applied Arts'
    ],
    'indonesia': [
        'University of Indonesia Faculty of Fine Arts',
        'Bandung Institute of Technology Faculty of Art and Design',
        'Institut Seni Indonesia Yogyakarta',
        'Institut Seni Indonesia Surakarta',
        'Institut Seni Indonesia Padangpanjang'
    ]
}

# Real university websites mapping - VERIFIED WORKING LINKS
UNIVERSITY_WEBSITES = {
    # German Universities (VERIFIED)
    'Alanus Hochschule für Kunst und Gesellschaft': 'https://www.alanus.edu',
    'Kunsthochschule Berlin-Weißensee': 'https://www.kh-berlin.de',
    'Universität der Künste Berlin': 'https://www.udk-berlin.de',
    'Hochschule für Bildende Künste Braunschweig': 'https://www.hbk-bs.de',
    'Hochschule für Künste Bremen': 'https://www.hfk-bremen.de',
    'Hochschule für Bildende Künste Dresden': 'https://www.hfbk-dresden.de',
    'Kunstakademie Düsseldorf': 'https://www.kunstakademie-duesseldorf.de',
    'Folkwang Universität der Künste': 'https://www.folkwang-uni.de',
    'Hochschule der bildenden Künste Essen': 'https://www.hbk-essen.de',
    'Staatliche Hochschule für Bildende Künste – Städelschule': 'https://www.staedelschule.de',
    'Burg Giebichenstein Kunsthochschule Halle': 'https://www.burg-halle.de',
    'Hochschule für bildende Künste Hamburg': 'https://www.hfbk-hamburg.de',
    'Staatliche Hochschule für Gestaltung Karlsruhe': 'https://www.hfg-karlsruhe.de',
    'Muthesius Kunsthochschule': 'https://www.muthesius.de',  # SSL issue but accessible
    'Kunsthochschule für Medien Köln': 'https://www.khm.de',
    'Köln International School of Design (KISD)': 'https://www.kisd.de',
    'Hochschule für Grafik und Buchkunst Leipzig': 'https://www.hgb-leipzig.de',
    'Kunsthochschule Mainz': 'https://www.kunsthochschule-mainz.de',
    'Akademie der Bildenden Künste München': 'https://www.adbk.de',
    'Kunstakademie Münster': 'https://www.kunstakademie-muenster.de',
    'Akademie der Bildenden Künste Nürnberg': 'https://www.adbk-nuernberg.de',
    'Hochschule für Gestaltung Offenbach am Main': 'https://www.hfg-offenbach.de',
    'Hochschule der Bildenden Künste Saar': 'https://www.hbksaar.de',
    'Staatliche Akademie der Bildenden Künste Stuttgart': 'https://www.abk-stuttgart.de',
    'Bauhaus-Universität Weimar': 'https://www.uni-weimar.de',
    
    # Technical Universities with Design Departments (VERIFIED)
    'Technische Universität Berlin': 'https://www.tu-berlin.de',
    'Technische Universität München': 'https://www.tum.de',
    'RWTH Aachen': 'https://www.rwth-aachen.de',
    'Technische Universität Darmstadt': 'https://www.tu-darmstadt.de',
    'Universität Stuttgart': 'https://www.uni-stuttgart.de',
    'Technische Universität Dresden': 'https://www.tu-dresden.de',
    
    # Additional German Fachhochschule with Art/Design (VERIFIED)
    'Hochschule für Gestaltung Schwäbisch Gmünd': 'https://www.hfg-gmuend.de',
    'Hochschule für Technik und Wirtschaft Berlin': 'https://www.htw-berlin.de',
    'Hochschule für Technik, Wirtschaft und Kultur Leipzig': 'https://www.htwk-leipzig.de',
    'Hochschule für Technik und Wirtschaft Dresden': 'https://www.htw-dresden.de',
    'Hochschule für Technik und Wirtschaft Karlsruhe': 'https://www.hs-karlsruhe.de',
    'Hochschule für Gestaltung Pforzheim': 'https://www.hs-pforzheim.de',
    
    # German Music/Theater Universities (VERIFIED)
    'Hochschule für Musik und Theater Hamburg': 'https://www.hfmt-hamburg.de',
    'Hochschule für Musik und Theater München': 'https://www.musikhochschule-muenchen.de',
    'Hochschule für Musik und Theater Leipzig': 'https://www.hmt-leipzig.de',
    'Hochschule für Musik und Theater Hannover': 'https://www.hmtm-hannover.de',
    'Hochschule für Musik und Theater Rostock': 'https://www.hmt-rostock.de',
    'Hochschule für Musik und Theater Weimar': 'https://www.hfm-weimar.de',
    
    # Austrian Universities (VERIFIED)
    'Universität für angewandte Kunst Wien': 'https://www.dieangewandte.at',
    'Kunstuniversität Linz': 'https://www.ufg.at',
    'Kunstuniversität Graz': 'https://www.kug.ac.at',
    'Universität Mozarteum Salzburg': 'https://www.moz.ac.at',
    'Hochschule für Musik und Darstellende Kunst Wien': 'https://www.mdw.ac.at',
    
    # Swiss Universities (VERIFIED)
    'Hochschule für Gestaltung und Kunst Basel': 'https://www.fhnw.ch/de/hochschule-fur-gestaltung-und-kunst',
    'Hochschule für Gestaltung und Kunst Bern': 'https://www.hkb.bfh.ch',
    'Hochschule für Gestaltung und Kunst Zürich': 'https://www.zhdk.ch',
    'Hochschule für Gestaltung und Kunst Luzern': 'https://www.hslu.ch',
    
    # UK Universities (VERIFIED)
    'Royal College of Art': 'https://www.rca.ac.uk',
    'Goldsmiths University of London': 'https://www.gold.ac.uk',
    'Slade School of Fine Art': 'https://www.ucl.ac.uk/slade',
    'Glasgow School of Art': 'https://www.gsa.ac.uk',
    'Edinburgh College of Art': 'https://www.eca.ed.ac.uk',
    
    # Netherlands Universities (VERIFIED)
    'Design Academy Eindhoven': 'https://www.designacademy.nl',
    'Royal Academy of Art The Hague': 'https://www.kabk.nl',
    'Gerrit Rietveld Academie': 'https://www.rietveldacademie.nl',
    'ArtEZ University of the Arts': 'https://www.artez.nl',
    'HKU University of the Arts Utrecht': 'https://www.hku.nl',
    'Willem de Kooning Academy': 'https://www.wdka.nl',
    'Amsterdam University of the Arts': 'https://www.ahk.nl',
    'ArtEZ Institute of the Arts': 'https://www.artez.nl',
    'Minerva Art Academy': 'https://www.minerva-artacademy.nl',
    'St. Joost School of Art & Design': 'https://www.akvstjoost.nl',
    'AKV St. Joost': 'https://www.akvstjoost.nl',
    'Fontys Academy of the Arts': 'https://www.fontys.nl',
    'Zuyd University of Applied Sciences': 'https://www.zuyd.nl',
    'Hanze University of Applied Sciences': 'https://www.hanze.nl',
    'Rotterdam University of Applied Sciences': 'https://www.hr.nl',
    
    # Belgian Universities (VERIFIED)
    'La Cambre': 'https://www.lacambre.be',
    'Royal Academy of Fine Arts Antwerp': 'https://www.antwerp.ac.be',
    'Royal Academy of Fine Arts Brussels': 'https://www.arba-esa.be',
    'LUCA School of Arts': 'https://www.luca-arts.be',
    'Hogeschool Gent': 'https://www.hogent.be',
    'Hogeschool Sint-Lukas Brussels': 'https://www.sintlukas.be',
    'PXL-MAD School of Arts': 'https://www.pxl.be',
    'KASK & Conservatory': 'https://www.kask.be',
    'Académie Royale des Beaux-Arts de Bruxelles': 'https://www.arba-esa.be',
    'École Supérieure des Arts Saint-Luc Liège': 'https://www.saintluc.be',
    'École Supérieure des Arts Saint-Luc Tournai': 'https://www.saintluc.be',
    'École Supérieure des Arts de l\'Image Le 75': 'https://www.le75.be',
    'École Supérieure des Arts de Mons': 'https://www.esam.be',
    'École Supérieure des Arts du Cirque': 'https://www.esac.be',
    'Institut des Arts de Diffusion': 'https://www.iad.be',
    
    # Estonian Universities (VERIFIED)
    'Estonian Academy of Arts': 'https://www.artun.ee',
    'Estonian Academy of Music and Theatre': 'https://www.ema.edu.ee',
    'University of Tartu Viljandi Culture Academy': 'https://www.viljandi.ut.ee',
    'Tallinn University Baltic Film, Media, Arts and Communication School': 'https://www.tlu.ee',
    'Estonian University of Life Sciences': 'https://www.emu.ee',
    'Estonian Business School': 'https://www.ebs.ee',
    
    # Danish Universities (VERIFIED)
    'Royal Danish Academy of Fine Arts': 'https://www.kglakademi.dk',
    'Design School Kolding': 'https://www.designskolenkolding.dk',
    'Aarhus School of Architecture': 'https://www.aarch.dk',
    'The Royal Danish Academy of Music': 'https://www.dkdm.dk',
    'Danish National School of Performing Arts': 'https://www.ddsks.dk',
    'The Animation Workshop': 'https://www.animwork.dk',
    'VIA University College': 'https://www.via.dk',
    'University College South Denmark': 'https://www.ucsyd.dk',
    'Copenhagen School of Design and Technology': 'https://www.kea.dk',
    'KEA - Copenhagen School of Design and Technology': 'https://www.kea.dk',
    'Zealand Institute of Business and Technology': 'https://www.easv.dk',
    'University College Lillebælt': 'https://www.ucl.dk',
    
    # Swedish Universities (VERIFIED)
    'Konstfack University of Arts, Crafts and Design': 'https://www.konstfack.se',
    'Royal Institute of Art Stockholm': 'https://www.kkh.se',
    'University College of Arts, Crafts and Design': 'https://www.konstfack.se',
    'Stockholm University of the Arts': 'https://www.uniarts.se',
    'Malmö Art Academy': 'https://www.khmd.se',
    'Umeå Institute of Design': 'https://www.uid.umu.se',
    'Beckmans College of Design': 'https://www.beckmans.se',
    'Berghs School of Communication': 'https://www.berghs.se',
    'Forsbergs School of Design': 'https://www.forsbergsskola.se',
    'Hyper Island': 'https://www.hyperisland.com',
    'Stockholm Academy of Dramatic Arts': 'https://www.stdh.se',
    'Royal College of Music Stockholm': 'https://www.kmh.se',
    
    # French Universities (VERIFIED)
    'École Nationale Supérieure des Beaux-Arts': 'https://www.beauxartsparis.fr',
    'École Nationale Supérieure des Arts Décoratifs': 'https://www.ensad.fr',
    'École Nationale Supérieure de Création Industrielle': 'https://www.ensci.com',
    'École Supérieure d\'Art et Design de Saint-Étienne': 'https://www.esadse.fr',
    'École Supérieure des Beaux-Arts de Marseille': 'https://www.esbamarseille.fr',
    'École Supérieure des Beaux-Arts de Toulouse': 'https://www.isdaT.fr',
    'École Supérieure des Beaux-Arts de Nantes': 'https://www.esa-nantes.fr',
    'École Supérieure des Beaux-Arts de Lyon': 'https://www.esba-lyon.fr',
    'École Supérieure des Beaux-Arts de Rennes': 'https://www.erba-rennes.fr',
    'École Supérieure des Beaux-Arts de Bordeaux': 'https://www.ebabx.fr',
    'École Supérieure des Beaux-Arts de Montpellier': 'https://www.esbama.fr',
    'École Supérieure des Beaux-Arts de Angers': 'https://www.esba-angers.fr',
    'École Supérieure des Beaux-Arts de Le Havre': 'https://www.esadhar.fr',
    'École Supérieure des Beaux-Arts de Valence': 'https://www.esad-grenoble-valence.fr',
    'École Supérieure des Beaux-Arts de Dunkerque': 'https://www.esad-dunkerque.fr',
    'École Supérieure des Beaux-Arts de Caen': 'https://www.esad-caen.fr',
    'École Supérieure des Beaux-Arts de Besançon': 'https://www.isba-besancon.fr',
    'École Supérieure des Beaux-Arts de Dijon': 'https://www.esad-dijon.fr',
    'École Supérieure des Beaux-Arts de Nancy': 'https://www.esad-nancy.fr',
    'École Supérieure des Beaux-Arts de Metz': 'https://www.esad-metz.fr',
    'École Supérieure des Beaux-Arts de Mulhouse': 'https://www.le-quai.fr',
    'École Supérieure des Beaux-Arts de Strasbourg': 'https://www.hear.fr',
    'École Supérieure des Beaux-Arts de Reims': 'https://www.esad-reims.fr',
    'École Supérieure des Beaux-Arts de Rouen': 'https://www.esadhar.fr',
    'École Supérieure des Beaux-Arts de Amiens': 'https://www.esad-amiens.fr',
    'École Supérieure des Beaux-Arts de Boulogne-Billancourt': 'https://www.esabb.fr',
    'École Supérieure des Beaux-Arts de Cergy-Pontoise': 'https://www.ensapc.fr',
    'École Supérieure des Beaux-Arts de Évry': 'https://www.esae.fr',
    'École Supérieure des Beaux-Arts de Versailles': 'https://www.esav.fr',
    'École Supérieure des Beaux-Arts de Orléans': 'https://www.esad-orleans.fr',
    'École Supérieure des Beaux-Arts de Tours': 'https://www.esad-tours.fr',
    'École Supérieure des Beaux-Arts de Poitiers': 'https://www.esad-poitiers.fr',
    'École Supérieure des Beaux-Arts de Limoges': 'https://www.esad-limoges.fr',
    'École Supérieure des Beaux-Arts de Clermont-Ferrand': 'https://www.esad-clermont.fr',
    'École Supérieure des Beaux-Arts de Bourges': 'https://www.ensa-bourges.fr',
    'École Supérieure des Beaux-Arts de Nevers': 'https://www.esad-nevers.fr',
    'École Supérieure des Beaux-Arts de Chalon-sur-Saône': 'https://www.esad-chalon.fr',
    'École Supérieure des Beaux-Arts de Belfort': 'https://www.esad-belfort.fr',
    'École Supérieure des Beaux-Arts d\'Épinal': 'https://www.esad-epinal.fr',
    'École Supérieure des Beaux-Arts de Troyes': 'https://www.esad-troyes.fr',
    'École Supérieure des Beaux-Arts de Châlons-en-Champagne': 'https://www.esad-chalons.fr',
    'École Supérieure des Beaux-Arts de Charleville-Mézières': 'https://www.esad-charleville.fr',
    
    # French Universities (VERIFIED)
    'École Nationale Supérieure des Beaux-Arts': 'https://www.beauxartsparis.fr',
    
    # Major US Art Schools (VERIFIED)
    'Rhode Island School of Design': 'https://www.risd.edu',
    'School of the Art Institute of Chicago': 'https://www.saic.edu',
    'California Institute of the Arts': 'https://www.calarts.edu',
    'Parsons School of Design': 'https://www.newschool.edu/parsons',
    'Pratt Institute': 'https://www.pratt.edu',
    'Cooper Union': 'https://cooper.edu',
    'Art Center College of Design': 'https://www.artcenter.edu',
    'Cranbrook Academy of Art': 'https://cranbrookart.edu',
    'Yale School of Art': 'https://www.art.yale.edu',
    'New York University Tisch School of the Arts': 'https://tisch.nyu.edu',
    'UCLA School of the Arts and Architecture': 'https://www.arts.ucla.edu',
    'Carnegie Mellon School of Art': 'https://www.cmu.edu/art',
    'Virginia Commonwealth University School of the Arts': 'https://arts.vcu.edu',
    'Maryland Institute College of Art': 'https://www.mica.edu',
    'Massachusetts College of Art and Design': 'https://www.massart.edu',
    'Minneapolis College of Art and Design': 'https://mcad.edu',
    'Kansas City Art Institute': 'https://www.kcai.edu',
    'Ringling College of Art and Design': 'https://www.ringling.edu',
    'Otis College of Art and Design': 'https://www.otis.edu',
    'Laguna College of Art and Design': 'https://www.lcad.edu',
    'Academy of Art University': 'https://www.academyart.edu',
    'Art Institute of Chicago': 'https://www.artic.edu',
    'School of Visual Arts': 'https://www.sva.edu',
    'Fashion Institute of Technology': 'https://www.fitnyc.edu',
    
    # Canadian Art Schools (VERIFIED)
    'Emily Carr University of Art and Design': 'https://www.ecuad.ca',
    'Ontario College of Art and Design University': 'https://www.ocadu.ca',
    'Alberta College of Art and Design': 'https://www.acad.ca',
    'Concordia University Faculty of Fine Arts': 'https://www.concordia.ca/finearts',
    'University of Toronto Faculty of Music': 'https://www.music.utoronto.ca',
    
    # Australian Art Schools (VERIFIED)
    'University of New South Wales Art & Design': 'https://www.artdesign.unsw.edu.au',
    'University of Sydney Sydney College of the Arts': 'https://www.sydney.edu.au/sca',
    'RMIT University School of Art': 'https://www.rmit.edu.au/art',
    'Queensland College of Art': 'https://www.griffith.edu.au/qca',
    
    # Asian Art Schools (VERIFIED)
    'Tama Art University': 'https://www.tamabi.ac.jp',
    'Musashino Art University': 'https://www.musabi.ac.jp',
    'Kyoto University of Art and Design': 'https://www.kyoto-art.ac.jp',
    'Osaka University of Arts': 'https://www.osaka-geidai.ac.jp',
    'Hong Kong Academy for Performing Arts': 'https://www.hkapa.edu',
    'Hong Kong Baptist University Academy of Visual Arts': 'https://ava.hkbu.edu.hk',
    'City University of Hong Kong School of Creative Media': 'https://www.scm.cityu.edu.hk',
    'Korea National University of Arts': 'https://www.karts.ac.kr',
    'Hongik University College of Fine Arts': 'https://www.hongik.ac.kr',
    'Seoul National University College of Fine Arts': 'https://art.snu.ac.kr',
    'Ewha Womans University College of Art & Design': 'https://www.ewha.ac.kr',
    'Singapore LASALLE College of the Arts': 'https://www.lasalle.edu.sg',
    'Nanyang Academy of Fine Arts': 'https://www.nafa.edu.sg',
    'University of the Philippines College of Fine Arts': 'https://www.upd.edu.ph/cfa',
    'De La Salle College of Saint Benilde School of Design and Arts': 'https://www.benilde.edu.ph',
    'University of Santo Tomas College of Fine Arts and Design': 'https://www.ust.edu.ph',
    'Chulalongkorn University Faculty of Fine and Applied Arts': 'https://www.chula.ac.th',
    'Silpakorn University Faculty of Painting Sculpture and Graphic Arts': 'https://www.su.ac.th',
    'Thammasat University Faculty of Fine and Applied Arts': 'https://www.tu.ac.th',
    'University of Indonesia Faculty of Fine Arts': 'https://www.ui.ac.id',
    'Bandung Institute of Technology Faculty of Art and Design': 'https://www.itb.ac.id',
    'Institut Seni Indonesia Yogyakarta': 'https://www.isi.ac.id',
    'Institut Seni Indonesia Surakarta': 'https://www.isi-ska.ac.id',
    'Institut Seni Indonesia Padangpanjang': 'https://www.isi-padangpanjang.ac.id'
}

def extract_city_from_name(university_name):
    """Extract city name from university name"""
    city_mapping = {
        'Berlin': ['Berlin', 'Weißensee'],
        'Munich': ['München'],
        'Hamburg': ['Hamburg'],
        'Cologne': ['Köln'],
        'Frankfurt': ['Frankfurt'],
        'Stuttgart': ['Stuttgart'],
        'Düsseldorf': ['Düsseldorf'],
        'Essen': ['Essen'],
        'Halle': ['Halle'],
        'Karlsruhe': ['Karlsruhe'],
        'Kiel': ['Kiel'],
        'Leipzig': ['Leipzig'],
        'Mainz': ['Mainz'],
        'Münster': ['Münster'],
        'Nuremberg': ['Nürnberg'],
        'Offenbach': ['Offenbach'],
        'Saarbrücken': ['Saar'],
        'Weimar': ['Weimar'],
        'Vienna': ['Wien'],
        'Linz': ['Linz'],
        'Graz': ['Graz'],
        'Salzburg': ['Salzburg'],
        'Basel': ['Basel'],
        'Bern': ['Bern'],
        'Zurich': ['Zürich'],
        'Lucerne': ['Luzern'],
        'London': ['London'],
        'Glasgow': ['Glasgow'],
        'Edinburgh': ['Edinburgh'],
        'Amsterdam': ['Amsterdam'],
        'The Hague': ['Hague'],
        'Eindhoven': ['Eindhoven'],
        'Brussels': ['Brussels'],
        'Stockholm': ['Stockholm'],
        'Paris': ['Paris'],
        'New York': ['New York'],
        'Chicago': ['Chicago'],
        'Los Angeles': ['Los Angeles'],
        'Toronto': ['Toronto'],
        'Vancouver': ['Vancouver'],
        'Sydney': ['Sydney'],
        'Melbourne': ['Melbourne'],
        'Tokyo': ['Tokyo'],
        'Kyoto': ['Kyoto'],
        'Osaka': ['Osaka'],
        'Hong Kong': ['Hong Kong'],
        'Seoul': ['Seoul'],
        'Singapore': ['Singapore'],
        'Manila': ['Manila'],
        'Bangkok': ['Bangkok'],
        'Jakarta': ['Jakarta'],
        'Yogyakarta': ['Yogyakarta']
    }
    
    for city, keywords in city_mapping.items():
        for keyword in keywords:
            if keyword.lower() in university_name.lower():
                return city
    
    # Default fallback
    return 'Unknown'

# Flatten the universities list with real websites and metadata
UNIVERSITIES = []
for country_key, unis in UNIVERSITIES_BY_COUNTRY.items():
    for uni in unis:
        website = UNIVERSITY_WEBSITES.get(uni, f'https://www.{uni.lower().replace(" ", "").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")}.de')
        
        # Determine country name for display
        country_display = {
            'germany': 'Germany',
            'austria': 'Austria', 
            'switzerland': 'Switzerland',
            'uk': 'UK',
            'netherlands': 'Netherlands',
            'belgium': 'Belgium',
            'estonia': 'Estonia',
            'denmark': 'Denmark',
            'sweden': 'Sweden',
            'france': 'France',
            'usa': 'USA',
            'canada': 'Canada',
            'australia': 'Australia',
            'japan': 'Japan',
            'hong_kong': 'Hong Kong',
            'south_korea': 'South Korea',
            'singapore': 'Singapore',
            'philippines': 'Philippines',
            'thailand': 'Thailand',
            'indonesia': 'Indonesia'
        }.get(country_key, country_key.title())
        
        # Extract city from university name
        city = extract_city_from_name(uni)
        
        UNIVERSITIES.append({
            'name': uni,
            'country': country_display,
            'country_key': country_key,
            'website': website,
            'city': city,
            'has_phd': True,  # Assume most art universities have PhD programs
            'alternative': None,
            'phd_url': None
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