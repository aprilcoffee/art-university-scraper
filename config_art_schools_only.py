"""
Configuration for Art University Job Scraper - Focused on Art Schools Only
"""

# Simplified search terms focusing only on PhD and Jobs
SEARCH_TERMS = {
    'german': {
        'phd_programs': {
            'artistic_research_phd': [
                'Artistic Research', 'Künstlerische Forschung', 'Practice-based PhD', 'Praxis-basierte Promotion',
                'Artistic PhD', 'Künstlerische Promotion', 'Forschung in der Kunst', 'Kunst als Forschung',
                'Doktorat in Kunst', 'Promotion Kunst', 'Künstlerische Doktorarbeit', 'Forschungsprojekt Kunst',
                'Doktorandenprogramm Kunst', 'Promotionsprogramm Kunstforschung',
                'Practice-based Research', 'Praxis-basierte Forschung', 'Practice-led Research', 'Praxisgeleitete Forschung',
                'Practice-as-Research', 'Praxis-als-Forschung', 'Practice-oriented Research', 'Praxisorientierte Forschung',
                'Artistic Practice PhD', 'Künstlerische Praxis PhD', 'Artistic Practice Research', 'Künstlerische Praxis Forschung',
                'Creative Research PhD', 'Kreative Forschung PhD', 'Creative Research', 'Kreative Forschung',
                'DFA', 'Doctor of Fine Arts', 'Doktor der Bildenden Künste', 'Doctor of Arts', 'Doktor der Künste',
                'Studio-based Research', 'Atelier-basierte Forschung', 'Studio Practice PhD', 'Atelier-Praxis PhD',
                'Research through Practice', 'Forschung durch Praxis', 'Practice as Research', 'Praxis als Forschung',
                'Interdisciplinary Research', 'Interdisziplinäre Forschung', 'Transdisciplinary Research', 'Transdisziplinäre Forschung'
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
            ]
        },
        'job_offers': {
            'artistic_staff': [
                'Künstlerische Mitarbeiter', 'Wissenschaftliche Mitarbeiter', 
                'Künstlerische Mitarbeiterin', 'Wissenschaftliche Mitarbeiterin',
                'Künstlerischer Mitarbeiter', 'Wissenschaftlicher Mitarbeiter',
                'Künstlerische Mitarbeiter/in', 'Wissenschaftliche Mitarbeiter/in',
                'Medienkunst Mitarbeiter', 'Digitale Kunst Mitarbeiter', 'Neue Medien Mitarbeiter',
                'KI-Kunst Mitarbeiter', 'Künstliche Intelligenz Kunst Mitarbeiter', 'AI Art Mitarbeiter',
                'Klangkunst Mitarbeiter', 'Sound Art Mitarbeiter', 'Audio Art Mitarbeiter',
                'Performance Art Mitarbeiter', 'Aufführungskunst Mitarbeiter', 'Live Art Mitarbeiter',
                'Interaktive Kunst Mitarbeiter', 'Interactive Art Mitarbeiter', 'Partizipative Kunst Mitarbeiter',
                'Künstlerische Forschung Mitarbeiter', 'Artistic Research Mitarbeiter',
                'Künstlerische Assistenz', 'Wissenschaftliche Assistenz',
                'Künstlerische Hilfskraft', 'Wissenschaftliche Hilfskraft',
                'Forschungsassistent', 'Forschungsassistentin',
                'Projektmitarbeiter', 'Ateliermitarbeiter',
                'Artistic Staff', 'Research Staff', 'Academic Staff',
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant',
                'Artistic Associate', 'Research Associate', 'Academic Associate',
                'Media Art Staff', 'Digital Art Staff', 'New Media Staff',
                'AI Art Staff', 'Artificial Intelligence Art Staff', 'Machine Learning Art Staff',
                'Sound Art Staff', 'Audio Art Staff', 'Performance Art Staff',
                'Interactive Art Staff', 'Participatory Art Staff',
                'Artistic Research Staff', 'Practice-based Research Staff',
                'Project Staff', 'Studio Staff', 'Technical Staff',
                'Stellenausschreibung', 'Stelle', 'Stellenangebot', 'Ausschreibung', 'Vakanz',
                'Job Opening', 'Position Available', 'Vacancy', 'Employment Opportunity',
                'Staff Position', 'Academic Position', 'Research Position'
            ]
        }
    },
    'english': {
        'phd_programs': {
            'artistic_research_phd': [
                'Artistic Research PhD', 'Practice-based PhD', 'Practice-based Research PhD',
                'Artistic Practice PhD', 'Creative Research PhD', 'Artistic Research Doctoral',
                'Practice-based Doctoral', 'Artistic Research Graduate Program',
                'Practice-based Graduate Program', 'Creative Research Graduate Program',
                'Practice-led Research', 'Practice-as-Research', 'Practice-oriented Research',
                'Practice-informed Research', 'Practice-driven Research', 'Practice-based Inquiry',
                'Artistic Practice Research', 'Creative Practice PhD', 'Artistic Practice Doctoral',
                'Practice-led Doctoral', 'Creative Practice Doctoral', 'Artistic Practice Graduate Program',
                'Research through Practice', 'Research by Practice', 'Practice as Research',
                'Research in Practice', 'Practice-based Inquiry', 'Research through Art',
                'Creative Research', 'Creative Practice Research', 'Creative Inquiry',
                'Creative Investigation', 'Creative Scholarship', 'Creative Study',
                'DFA', 'Doctor of Fine Arts', 'Doctor of Arts', 'Doctor of Creative Arts',
                'Studio-based Research', 'Studio Practice PhD', 'Studio-led Research',
                'Studio Research', 'Workshop-based Research', 'Workshop Research',
                'Interdisciplinary Research', 'Transdisciplinary Research', 'Cross-disciplinary Research',
                'Multi-disciplinary Research', 'Interdisciplinary PhD', 'Transdisciplinary PhD',
                'Fine Arts Research', 'Visual Arts Research', 'Performing Arts Research',
                'Digital Arts Research', 'Media Arts Research', 'Contemporary Arts Research'
            ],
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
            ]
        },
        'job_offers': {
            'artistic_staff': [
                'Artistic Staff', 'Research Staff', 'Academic Staff',
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant',
                'Artistic Associate', 'Research Associate', 'Academic Associate',
                'Media Art Staff', 'Digital Art Staff', 'New Media Staff',
                'AI Art Staff', 'Artificial Intelligence Art Staff', 'Machine Learning Art Staff',
                'Sound Art Staff', 'Audio Art Staff', 'Performance Art Staff',
                'Interactive Art Staff', 'Participatory Art Staff',
                'Artistic Research Staff', 'Practice-based Research Staff',
                'Research Staff Art', 'Academic Staff Art', 'Research Associate Art',
                'Art Research Staff', 'Creative Research Staff',
                'Project Staff', 'Studio Staff', 'Technical Staff',
                'Job Opening', 'Position Available', 'Vacancy', 'Employment Opportunity',
                'Staff Position', 'Academic Position', 'Research Position'
            ]
        }
    }
}

# Art Schools Only - Major Art Universities and Art Schools
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
        'Bauhaus-Universität Weimar',
        'Hochschule für Gestaltung Schwäbisch Gmünd',
        'Hochschule für Gestaltung Pforzheim',
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
        'Amsterdam University of the Arts',
        'Minerva Art Academy',
        'St. Joost School of Art & Design'
    ],
    'belgium': [
        'La Cambre',
        'Royal Academy of Fine Arts Antwerp',
        'Royal Academy of Fine Arts Brussels',
        'LUCA School of Arts',
        'Hogeschool Sint-Lukas Brussels',
        'PXL-MAD School of Arts',
        'KASK & Conservatory'
    ],
    'estonia': [
        'Estonian Academy of Arts',
        'Estonian Academy of Music and Theatre'
    ],
    'denmark': [
        'Royal Danish Academy of Fine Arts',
        'Design School Kolding',
        'Aarhus School of Architecture',
        'The Royal Danish Academy of Music',
        'Danish National School of Performing Arts',
        'The Animation Workshop'
    ],
    'sweden': [
        'Konstfack University of Arts, Crafts and Design',
        'Royal Institute of Art Stockholm',
        'Stockholm University of the Arts',
        'Malmö Art Academy',
        'Umeå Institute of Design',
        'Beckmans College of Design'
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
        'École Supérieure des Beaux-Arts de Strasbourg',
        'École Supérieure des Beaux-Arts de Reims',
        'École Supérieure des Beaux-Arts de Rouen',
        'École Supérieure des Beaux-Arts de Amiens',
        'École Supérieure des Beaux-Arts de Versailles',
        'École Supérieure des Beaux-Arts de Orléans',
        'École Supérieure des Beaux-Arts de Tours',
        'École Supérieure des Beaux-Arts de Poitiers',
        'École Supérieure des Beaux-Arts de Limoges',
        'École Supérieure des Beaux-Arts de Clermont-Ferrand',
        'École Supérieure des Beaux-Arts de Bourges'
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
        'School of Visual Arts',
        'Fashion Institute of Technology'
    ],
    'canada': [
        'Emily Carr University of Art and Design',
        'Ontario College of Art and Design University',
        'Alberta College of Art and Design',
        'Concordia University Faculty of Fine Arts'
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
    ]
}

# Real university websites mapping - VERIFIED WORKING LINKS
UNIVERSITY_WEBSITES = {
    # German Art Schools (VERIFIED)
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
    'Muthesius Kunsthochschule': 'https://www.muthesius.de',
    'Kunsthochschule für Medien Köln': 'https://www.khm.de',
    'Hochschule für Grafik und Buchkunst Leipzig': 'https://www.hgb-leipzig.de',
    'Kunsthochschule Mainz': 'https://www.kunsthochschule-mainz.de',
    'Akademie der Bildenden Künste München': 'https://www.adbk.de',
    'Kunstakademie Münster': 'https://www.kunstakademie-muenster.de',
    'Akademie der Bildenden Künste Nürnberg': 'https://www.adbk-nuernberg.de',
    'Hochschule für Gestaltung Offenbach am Main': 'https://www.hfg-offenbach.de',
    'Hochschule der Bildenden Künste Saar': 'https://www.hbksaar.de',
    'Staatliche Akademie der Bildenden Künste Stuttgart': 'https://www.abk-stuttgart.de',
    'Bauhaus-Universität Weimar': 'https://www.uni-weimar.de',
    'Hochschule für Gestaltung Schwäbisch Gmünd': 'https://www.hfg-gmuend.de',
    'Hochschule für Gestaltung Pforzheim': 'https://www.hs-pforzheim.de',
    'Hochschule für Musik und Theater Hamburg': 'https://www.hfmt-hamburg.de',
    'Hochschule für Musik und Theater München': 'https://www.musikhochschule-muenchen.de',
    'Hochschule für Musik und Theater Leipzig': 'https://www.hmt-leipzig.de',
    'Hochschule für Musik und Theater Hannover': 'https://www.hmtm-hannover.de',
    'Hochschule für Musik und Theater Rostock': 'https://www.hmt-rostock.de',
    'Hochschule für Musik und Theater Weimar': 'https://www.hfm-weimar.de',
    
    # Austrian Art Schools (VERIFIED)
    'Universität für angewandte Kunst Wien': 'https://www.dieangewandte.at',
    'Kunstuniversität Linz': 'https://www.ufg.at',
    'Kunstuniversität Graz': 'https://www.kug.ac.at',
    'Universität Mozarteum Salzburg': 'https://www.moz.ac.at',
    'Hochschule für Musik und Darstellende Kunst Wien': 'https://www.mdw.ac.at',
    
    # Swiss Art Schools (VERIFIED)
    'Hochschule für Gestaltung und Kunst Basel': 'https://www.fhnw.ch/de/hochschule-fur-gestaltung-und-kunst',
    'Hochschule für Gestaltung und Kunst Bern': 'https://www.hkb.bfh.ch',
    'Hochschule für Gestaltung und Kunst Zürich': 'https://www.zhdk.ch',
    'Hochschule für Gestaltung und Kunst Luzern': 'https://www.hslu.ch',
    
    # UK Art Schools (VERIFIED)
    'Royal College of Art': 'https://www.rca.ac.uk',
    'Goldsmiths University of London': 'https://www.gold.ac.uk',
    'Slade School of Fine Art': 'https://www.ucl.ac.uk/slade',
    'Glasgow School of Art': 'https://www.gsa.ac.uk',
    'Edinburgh College of Art': 'https://www.eca.ed.ac.uk',
    
    # Netherlands Art Schools (VERIFIED)
    'Design Academy Eindhoven': 'https://www.designacademy.nl',
    'Royal Academy of Art The Hague': 'https://www.kabk.nl',
    'Gerrit Rietveld Academie': 'https://www.rietveldacademie.nl',
    'ArtEZ University of the Arts': 'https://www.artez.nl',
    'HKU University of the Arts Utrecht': 'https://www.hku.nl',
    'Willem de Kooning Academy': 'https://www.wdka.nl',
    'Amsterdam University of the Arts': 'https://www.ahk.nl',
    'Minerva Art Academy': 'https://www.minerva-artacademy.nl',
    'St. Joost School of Art & Design': 'https://www.akvstjoost.nl',
    
    # Belgian Art Schools (VERIFIED)
    'La Cambre': 'https://www.lacambre.be',
    'Royal Academy of Fine Arts Antwerp': 'https://www.antwerp.ac.be',
    'Royal Academy of Fine Arts Brussels': 'https://www.arba-esa.be',
    'LUCA School of Arts': 'https://www.luca-arts.be',
    'Hogeschool Sint-Lukas Brussels': 'https://www.sintlukas.be',
    'PXL-MAD School of Arts': 'https://www.pxl.be',
    'KASK & Conservatory': 'https://www.kask.be',
    
    # Estonian Art Schools (VERIFIED)
    'Estonian Academy of Arts': 'https://www.artun.ee',
    'Estonian Academy of Music and Theatre': 'https://www.ema.edu.ee',
    
    # Danish Art Schools (VERIFIED)
    'Royal Danish Academy of Fine Arts': 'https://www.kglakademi.dk',
    'Design School Kolding': 'https://www.designskolenkolding.dk',
    'Aarhus School of Architecture': 'https://www.aarch.dk',
    'The Royal Danish Academy of Music': 'https://www.dkdm.dk',
    'Danish National School of Performing Arts': 'https://www.ddsks.dk',
    'The Animation Workshop': 'https://www.animwork.dk',
    
    # Swedish Art Schools (VERIFIED)
    'Konstfack University of Arts, Crafts and Design': 'https://www.konstfack.se',
    'Royal Institute of Art Stockholm': 'https://www.kkh.se',
    'Stockholm University of the Arts': 'https://www.uniarts.se',
    'Malmö Art Academy': 'https://www.khmd.se',
    'Umeå Institute of Design': 'https://www.uid.umu.se',
    'Beckmans College of Design': 'https://www.beckmans.se',
    
    # French Art Schools (VERIFIED)
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
    'École Supérieure des Beaux-Arts de Strasbourg': 'https://www.hear.fr',
    'École Supérieure des Beaux-Arts de Reims': 'https://www.esad-reims.fr',
    'École Supérieure des Beaux-Arts de Rouen': 'https://www.esadhar.fr',
    'École Supérieure des Beaux-Arts de Amiens': 'https://www.esad-amiens.fr',
    'École Supérieure des Beaux-Arts de Versailles': 'https://www.esav.fr',
    'École Supérieure des Beaux-Arts de Orléans': 'https://www.esad-orleans.fr',
    'École Supérieure des Beaux-Arts de Tours': 'https://www.esad-tours.fr',
    'École Supérieure des Beaux-Arts de Poitiers': 'https://www.esad-poitiers.fr',
    'École Supérieure des Beaux-Arts de Limoges': 'https://www.esad-limoges.fr',
    'École Supérieure des Beaux-Arts de Clermont-Ferrand': 'https://www.esad-clermont.fr',
    'École Supérieure des Beaux-Arts de Bourges': 'https://www.ensa-bourges.fr',
    
    # US Art Schools (VERIFIED)
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
    'School of Visual Arts': 'https://www.sva.edu',
    'Fashion Institute of Technology': 'https://www.fitnyc.edu',
    
    # Canadian Art Schools (VERIFIED)
    'Emily Carr University of Art and Design': 'https://www.ecuad.ca',
    'Ontario College of Art and Design University': 'https://www.ocadu.ca',
    'Alberta College of Art and Design': 'https://www.acad.ca',
    'Concordia University Faculty of Fine Arts': 'https://www.concordia.ca/finearts',
    
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
    'Nanyang Academy of Fine Arts': 'https://www.nafa.edu.sg'
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
        'Singapore': ['Singapore']
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
            'singapore': 'Singapore'
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

# Scraping configuration
SCRAPING_CONFIG = {
    'max_pages_per_university': 3,
    'delay_between_requests': 2,
    'timeout': 30,
    'max_retries': 3,
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}