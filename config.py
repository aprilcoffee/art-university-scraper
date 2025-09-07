"""
Configuration file for the Art University Job Scraper
"""

# Separated search terms for PhD programs vs Job offers
SEARCH_TERMS = {
    'german': {
        # PhD PROGRAMS - Academic Research Positions
        'phd_programs': {
            'media_art_phd': [
                'Medienkunst Promotion', 'Digitale Kunst Promotion', 'Neue Medien Promotion',
                'Medienkunst Doktorand', 'Digitale Kunst Doktorand', 'Neue Medien Doktorand',
                'Medienkunst PhD', 'Digitale Kunst PhD', 'Neue Medien PhD',
                'Doktorandenprogramm Medienkunst', 'Promotionsprogramm Digitale Kunst'
            ],
            'ai_art_phd': [
                'KI-Kunst Promotion', 'Künstliche Intelligenz Kunst Promotion', 'AI Art Promotion',
                'KI-Kunst Doktorand', 'AI Art Doktorand', 'Machine Learning Kunst Doktorand',
                'KI-Kunst PhD', 'AI Art PhD', 'Algorithmische Kunst PhD',
                'Doktorandenprogramm KI-Kunst', 'Promotionsprogramm AI Art'
            ],
            'artistic_research_phd': [
                'Artistic Research', 'Künstlerische Forschung', 'Practice-based PhD', 'Praxis-basierte Promotion',
                'Artistic PhD', 'Künstlerische Promotion', 'Forschung in der Kunst', 'Kunst als Forschung',
                'Doktorat in Kunst', 'Promotion Kunst', 'Künstlerische Doktorarbeit', 'Forschungsprojekt Kunst',
                'Doktorandenprogramm Kunst', 'Promotionsprogramm Kunstforschung'
            ],
            'sound_art_phd': [
                'Klangkunst Promotion', 'Sound Art Promotion', 'Audio Art Promotion',
                'Klangkunst Doktorand', 'Sound Art Doktorand', 'Audio Art Doktorand',
                'Klangkunst PhD', 'Sound Art PhD', 'Audio Art PhD',
                'Doktorandenprogramm Klangkunst', 'Promotionsprogramm Sound Art',
                'Musik und Medien PhD', 'Tonkunst PhD', 'Akustische Kunst PhD'
            ],
            'performance_art_phd': [
                'Performance Art Promotion', 'Aufführungskunst Promotion', 'Live Art Promotion',
                'Performance Art Doktorand', 'Aufführungskunst Doktorand', 'Live Art Doktorand',
                'Performance Art PhD', 'Aufführungskunst PhD', 'Live Art PhD',
                'Doktorandenprogramm Performance', 'Promotionsprogramm Live Art'
            ],
            'interactive_art_phd': [
                'Interaktive Kunst Promotion', 'Interactive Art Promotion', 'Partizipative Kunst Promotion',
                'Interaktive Kunst Doktorand', 'Interactive Art Doktorand', 'Partizipative Kunst Doktorand',
                'Interaktive Kunst PhD', 'Interactive Art PhD', 'Partizipative Kunst PhD',
                'Doktorandenprogramm Interaktion', 'Promotionsprogramm Interactive Art'
            ],
            'general_phd': [
                'Promotion', 'Doktorand', 'PhD', 'Doktorarbeit', 'Doktorat', 'Doktorandenstelle',
                'Promotionsstelle', 'Doktorandenprogramm', 'Graduate School', 'Graduiertenschule',
                'Doktorandenkolleg', 'Promotionsprogramm', 'Doktorandenausbildung'
            ]
        },
        
        # JOB OFFERS - Employment Positions
        'job_offers': {
            'media_art_jobs': [
                'Medienkunst Mitarbeiter', 'Digitale Kunst Mitarbeiter', 'Neue Medien Mitarbeiter',
                'Künstlerische Mitarbeiter Medienkunst', 'Wissenschaftliche Mitarbeiter Medienkunst',
                'Medienkunst Stelle', 'Digitale Kunst Stelle', 'Neue Medien Stelle',
                'Stellenausschreibung Medienkunst', 'Stellenangebot Digitale Kunst'
            ],
            'ai_art_jobs': [
                'KI-Kunst Mitarbeiter', 'Künstliche Intelligenz Kunst Mitarbeiter', 'AI Art Mitarbeiter',
                'Künstlerische Mitarbeiter KI', 'Wissenschaftliche Mitarbeiter KI',
                'KI-Kunst Stelle', 'AI Art Stelle', 'Machine Learning Kunst Stelle',
                'Stellenausschreibung KI-Kunst', 'Stellenangebot AI Art'
            ],
            'sound_art_jobs': [
                'Klangkunst Mitarbeiter', 'Sound Art Mitarbeiter', 'Audio Art Mitarbeiter',
                'Künstlerische Mitarbeiter Klangkunst', 'Wissenschaftliche Mitarbeiter Klangkunst',
                'Klangkunst Stelle', 'Sound Art Stelle', 'Audio Art Stelle',
                'Stellenausschreibung Klangkunst', 'Stellenangebot Sound Art',
                'Musik und Medien Mitarbeiter', 'Tonkunst Mitarbeiter', 'Akustische Kunst Mitarbeiter'
            ],
            'performance_art_jobs': [
                'Performance Art Mitarbeiter', 'Aufführungskunst Mitarbeiter', 'Live Art Mitarbeiter',
                'Künstlerische Mitarbeiter Performance', 'Wissenschaftliche Mitarbeiter Performance',
                'Performance Art Stelle', 'Aufführungskunst Stelle', 'Live Art Stelle',
                'Stellenausschreibung Performance', 'Stellenangebot Live Art'
            ],
            'interactive_art_jobs': [
                'Interaktive Kunst Mitarbeiter', 'Interactive Art Mitarbeiter', 'Partizipative Kunst Mitarbeiter',
                'Künstlerische Mitarbeiter Interaktion', 'Wissenschaftliche Mitarbeiter Interaktion',
                'Interaktive Kunst Stelle', 'Interactive Art Stelle', 'Partizipative Kunst Stelle',
                'Stellenausschreibung Interaktion', 'Stellenangebot Interactive Art'
            ],
            'artistic_research_jobs': [
                'Künstlerische Forschung Mitarbeiter', 'Artistic Research Mitarbeiter',
                'Künstlerische Mitarbeiter Forschung', 'Wissenschaftliche Mitarbeiter Kunstforschung',
                'Forschung in der Kunst Mitarbeiter', 'Kunst als Forschung Mitarbeiter',
                'Stellenausschreibung Kunstforschung', 'Stellenangebot Artistic Research'
            ],
            'academic_jobs': [
                'Künstlerische Mitarbeiter', 'Wissenschaftliche Mitarbeiter', 'Künstlerische Mitarbeiterin',
                'Wissenschaftliche Mitarbeiterin', 'Künstlerischer Mitarbeiter', 'Wissenschaftlicher Mitarbeiter',
                'Künstlerische Mitarbeiter/in', 'Wissenschaftliche Mitarbeiter/in', 'Mitarbeiter Kunst',
                'Mitarbeiter Forschung', 'Künstlerische Assistenz', 'Wissenschaftliche Assistenz',
                'Künstlerische Hilfskraft', 'Wissenschaftliche Hilfskraft', 'Kunstwissenschaftliche Mitarbeiter'
            ],
            'general_jobs': [
                'Stellenausschreibung', 'Stelle', 'Job', 'Position', 'Bewerbung', 'Stellenangebot',
                'Ausschreibung', 'Stellenmarkt', 'Karriere', 'Arbeitsplatz', 'Vakanz',
                'Mitarbeiter', 'Mitarbeiterin', 'Assistent', 'Assistentin',
                'Professor', 'Professorin', 'Dozent', 'Dozentin', 'Lehrbeauftragter', 'Lehrbeauftragte',
                'Wissenschaftliche Mitarbeiter', 'Wissenschaftliche Mitarbeiterin',
                'Künstlerische Mitarbeiter', 'Künstlerische Mitarbeiterin',
                'Doktorand', 'Doktorandin', 'Promovend', 'Promovendin',
                'Postdoc', 'Postdoktorand', 'Postdoktorandin',
                'Forschungsassistent', 'Forschungsassistentin',
                'Werkvertrag', 'Freelancer', 'Freiberufler', 'Projektmitarbeiter',
                'Kurator', 'Kuratorin', 'Kustos', 'Kustodin',
                'Werkstattleiter', 'Werkstattleiterin', 'Ateliermitarbeiter',
                'Studienberater', 'Studienberaterin', 'Studienkoordinator', 'Studienkoordinatorin',
                'Forschungskoordinator', 'Forschungskoordinatorin', 'Forschungsmanager',
                'Restaurator', 'Restauratorin', 'Konservator', 'Konservatorin',
                # AI and Machine Learning Positions (Priority)
                'KI-Experte', 'KI-Expertin', 'AI Expert', 'Machine Learning Engineer',
                'Maschinelles Lernen Ingenieur', 'Deep Learning Engineer', 'Neural Network Developer',
                'Algorithmic Artist', 'Algorithmische Künstler', 'Algorithmische Künstlerin',
                'Generative AI Artist', 'Generative Kunst Künstler', 'Generative Kunst Künstlerin',
                'AI Art Specialist', 'KI-Kunst Spezialist', 'KI-Kunst Spezialistin',
                'Computational Creativity Researcher', 'Computational Arts Researcher',
                'Creative AI Developer', 'Kreative KI Entwickler', 'Kreative KI Entwicklerin',
                'AI Tools Developer', 'KI-Tools Entwickler', 'KI-Tools Entwicklerin',
                'ChatGPT Specialist', 'DALL-E Specialist', 'Midjourney Specialist',
                'Stable Diffusion Expert', 'Generative Models Expert',
                # Technical and Programming Positions
                'Programmierer', 'Programmiererin', 'Softwareentwickler', 'Softwareentwicklerin',
                'Entwickler', 'Entwicklerin', 'Developer', 'Coder', 'Programmer',
                'Webentwickler', 'Webentwicklerin', 'Web Developer', 'Frontend Developer',
                'Backend Developer', 'Full Stack Developer', 'Mobile Developer',
                'Game Developer', 'Spieleentwickler', 'Spieleentwicklerin',
                'Unity Developer', 'Unreal Developer', 'VR Developer', 'AR Developer',
                'Creative Technologist', 'Creative Coder', 'Generative Designer',
                'Algorithmic Designer', 'Computational Designer',
                # Sound and Audio Positions
                'Sound Designer', 'Sounddesigner', 'Sounddesignerin',
                'Audio Engineer', 'Audioingenieur', 'Audioingenieurin',
                'Tontechniker', 'Tontechnikerin', 'Tonmeister', 'Tonmeisterin',
                'Musikproduzent', 'Musikproduzentin', 'Producer', 'Composer',
                'Komponist', 'Komponistin', 'Elektronische Musik', 'Electronic Music',
                'Max/MSP Entwickler', 'Pure Data Entwickler', 'SuperCollider Entwickler',
                'Audio Programmer', 'Audio Software Developer', 'DSP Engineer',
                'Spatial Audio Engineer', '3D Audio Designer', 'Ambisonic Engineer',
                'Audio Visual Artist', 'AV Artist', 'Live Coder', 'Live Coding',
                'Algorithmic Composition', 'Generative Music', 'Interactive Sound',
                # Media Art and Technology Positions
                'Medienkünstler', 'Medienkünstlerin', 'Digital Artist', 'Electronic Artist',
                'Interactive Designer', 'Interaktiver Designer', 'Interaktive Designerin',
                'Installation Artist', 'Installationskünstler', 'Installationskünstlerin',
                'Video Artist', 'Videokünstler', 'Videokünstlerin', 'Experimental Filmmaker',
                'Motion Graphics Designer', 'Motion Graphics Artist', 'VFX Artist',
                'Visual Effects Artist', 'Post Production Artist', 'Animation Artist',
                'Data Visualization Designer', 'Information Designer', 'Infographic Designer',
                'Machine Learning Engineer', 'AI Engineer', 'Neural Network Developer',
                'Computer Vision Engineer', 'Image Processing Engineer', 'Signal Processing Engineer',
                'Robotics Engineer', 'Kinetic Artist', 'Mechanical Artist', 'Automated Artist',
                'Bio Artist', 'Bio Media Artist', 'Biotechnology Artist', 'Synthetic Biology Artist',
                'Wearable Technology Designer', 'Smart Textiles Designer', 'E-Textiles Designer',
                'IoT Developer', 'Embedded Systems Developer', 'Microcontroller Programmer',
                'Arduino Developer', 'Raspberry Pi Developer', 'Processing Developer',
                'OpenFrameworks Developer', 'TouchDesigner Developer', 'vvvv Developer',
                'Isadora Developer', 'Resolume Developer', 'MadMapper Developer',
                'Blender Artist', 'Cinema 4D Artist', 'Maya Artist', '3D Artist',
                'After Effects Artist', 'Premiere Pro Editor', 'Final Cut Pro Editor',
                'DaVinci Resolve Colorist', 'Colorist', 'Color Grading Artist'
            ]
        }
    },
    'english': {
        # PhD PROGRAMS - Academic Research Positions
        'phd_programs': {
            'media_art_phd': [
                'Media Art PhD', 'Digital Art PhD', 'New Media PhD',
                'Media Art Doctorate', 'Digital Art Doctorate', 'New Media Doctorate',
                'Media Art Doctoral', 'Digital Art Doctoral', 'New Media Doctoral',
                'Doctoral Program Media Art', 'PhD Program Digital Art'
            ],
            'ai_art_phd': [
                'AI Art PhD', 'Artificial Intelligence Art PhD', 'AI Art Doctorate',
                'AI Art Doctoral', 'Machine Learning Art PhD', 'Neural Art PhD',
                'AI Art Doctoral Program', 'Algorithmic Art PhD',
                'Doctoral Program AI Art', 'PhD Program Machine Learning Art'
            ],
            'artistic_research_phd': [
                'Artistic Research', 'Practice-based PhD', 'Artistic PhD', 'Research in Art', 'Art as Research',
                'Doctorate in Art', 'PhD in Art', 'Artistic Doctorate', 'Research Project Art', 'Creative Research',
                'Practice-led Research', 'Artistic Practice Research', 'Studio-based Research',
                'Doctoral Program Art', 'PhD Program Artistic Research'
            ],
            'sound_art_phd': [
                'Sound Art PhD', 'Audio Art PhD', 'Sonic Art PhD',
                'Sound Art Doctorate', 'Audio Art Doctorate', 'Sonic Art Doctorate',
                'Sound Art Doctoral', 'Audio Art Doctoral', 'Sonic Art Doctoral',
                'Doctoral Program Sound Art', 'PhD Program Audio Art',
                'Music and Media PhD', 'Acoustic Art PhD', 'Sonic Studies PhD'
            ],
            'performance_art_phd': [
                'Performance Art PhD', 'Live Art PhD', 'Performance Studies PhD',
                'Performance Art Doctorate', 'Live Art Doctorate', 'Performance Studies Doctorate',
                'Performance Art Doctoral', 'Live Art Doctoral', 'Performance Studies Doctoral',
                'Doctoral Program Performance', 'PhD Program Live Art'
            ],
            'interactive_art_phd': [
                'Interactive Art PhD', 'Participatory Art PhD', 'Interactive Media PhD',
                'Interactive Art Doctorate', 'Participatory Art Doctorate', 'Interactive Media Doctorate',
                'Interactive Art Doctoral', 'Participatory Art Doctoral', 'Interactive Media Doctoral',
                'Doctoral Program Interaction', 'PhD Program Interactive Art'
            ],
            'general_phd': [
                'PhD', 'Doctorate', 'Doctoral', 'Graduate Studies', 'PhD Position', 'Doctoral Position',
                'PhD Program', 'Doctoral Program', 'Graduate Program', 'PhD Student', 'Doctoral Student',
                'PhD Candidate', 'Doctoral Candidate', 'Graduate Student', 'Research Student'
            ]
        },
        
        # JOB OFFERS - Employment Positions
        'job_offers': {
            'media_art_jobs': [
                'Media Art Assistant', 'Digital Art Assistant', 'New Media Assistant',
                'Artistic Assistant Media Art', 'Research Assistant Media Art',
                'Media Art Position', 'Digital Art Position', 'New Media Position',
                'Media Art Job', 'Digital Art Job', 'New Media Job'
            ],
            'ai_art_jobs': [
                'AI Art Assistant', 'Artificial Intelligence Art Assistant', 'AI Art Staff',
                'Artistic Assistant AI', 'Research Assistant AI',
                'AI Art Position', 'AI Art Job', 'Machine Learning Art Position',
                'AI Art Employment', 'Machine Learning Art Job'
            ],
            'artistic_research_jobs': [
                'Artistic Research Assistant', 'Research Assistant Art', 'Artistic Research Staff',
                'Artistic Assistant Research', 'Research Collaborator Art',
                'Artistic Research Position', 'Research in Art Position',
                'Artistic Research Job', 'Research in Art Job'
            ],
            'academic_jobs': [
                'Artistic Assistant', 'Research Assistant', 'Academic Assistant', 'Artistic Staff',
                'Research Staff', 'Academic Staff', 'Artistic Collaborator', 'Research Collaborator',
                'Artistic Associate', 'Research Associate', 'Artistic Fellow', 'Research Fellow',
                'Artistic Coordinator', 'Research Coordinator', 'Artistic Technician', 'Research Technician'
            ],
            'sound_art_jobs': [
                'Sound Art Assistant', 'Audio Art Assistant', 'Sonic Art Assistant',
                'Artistic Assistant Sound', 'Research Assistant Sound',
                'Sound Art Position', 'Audio Art Position', 'Sonic Art Position',
                'Sound Art Job', 'Audio Art Job', 'Sonic Art Job',
                'Music and Media Position', 'Acoustic Art Position'
            ],
            'performance_art_jobs': [
                'Performance Art Assistant', 'Live Art Assistant', 'Performance Studies Assistant',
                'Artistic Assistant Performance', 'Research Assistant Performance',
                'Performance Art Position', 'Live Art Position', 'Performance Studies Position',
                'Performance Art Job', 'Live Art Job', 'Performance Studies Job'
            ],
            'interactive_art_jobs': [
                'Interactive Art Assistant', 'Participatory Art Assistant', 'Interactive Media Assistant',
                'Artistic Assistant Interaction', 'Research Assistant Interaction',
                'Interactive Art Position', 'Participatory Art Position', 'Interactive Media Position',
                'Interactive Art Job', 'Participatory Art Job', 'Interactive Media Job'
            ],
            'general_jobs': [
                'Job Opening', 'Position', 'Vacancy', 'Employment', 'Career', 'Job Opportunity',
                'Academic Position', 'Research Position', 'Faculty Position',
                'Staff Position', 'Academic Job', 'Research Job',
                'Assistant', 'Associate', 'Coordinator', 'Manager', 'Director',
                'Professor', 'Lecturer', 'Senior Lecturer', 'Reader',
                'Research Assistant', 'Research Associate', 'Research Fellow',
                'PhD Student', 'Graduate Student', 'Doctoral Student',
                'Postdoc', 'Postdoctoral Researcher', 'Postdoctoral Fellow',
                'Research Coordinator', 'Research Manager', 'Research Administrator',
                'Academic Advisor', 'Student Affairs', 'Program Coordinator',
                'Curator', 'Curatorial', 'Conservator', 'Conservation',
                'Contract', 'Temporary', 'Seasonal', 'Part-time', 'Full-time',
                'Freelance', 'Consultant', 'Independent Contractor', 'Contractor',
                # AI and Machine Learning Positions (Priority)
                'AI Expert', 'Machine Learning Engineer', 'Deep Learning Engineer',
                'Neural Network Developer', 'Algorithmic Artist', 'Generative AI Artist',
                'AI Art Specialist', 'Computational Creativity Researcher',
                'Computational Arts Researcher', 'Creative AI Developer',
                'AI Tools Developer', 'ChatGPT Specialist', 'DALL-E Specialist',
                'Midjourney Specialist', 'Stable Diffusion Expert', 'Generative Models Expert',
                # Technical and Programming Positions
                'Programmer', 'Developer', 'Coder', 'Software Developer', 'Software Engineer',
                'Web Developer', 'Frontend Developer', 'Backend Developer', 'Full Stack Developer',
                'Mobile Developer', 'Game Developer', 'Unity Developer', 'Unreal Developer',
                'VR Developer', 'AR Developer', 'Creative Technologist', 'Creative Coder',
                'Generative Designer', 'Algorithmic Designer', 'Computational Designer',
                # Sound and Audio Positions
                'Sound Designer', 'Audio Engineer', 'Audio Producer', 'Music Producer',
                'Composer', 'Electronic Music Producer', 'Max/MSP Developer', 'Pure Data Developer',
                'SuperCollider Developer', 'Audio Programmer', 'Audio Software Developer',
                'DSP Engineer', 'Spatial Audio Engineer', '3D Audio Designer', 'Ambisonic Engineer',
                'Audio Visual Artist', 'AV Artist', 'Live Coder', 'Live Coding Artist',
                'Algorithmic Composer', 'Generative Music Artist', 'Interactive Sound Artist',
                # Media Art and Technology Positions
                'Media Artist', 'Digital Artist', 'Electronic Artist', 'Interactive Designer',
                'Installation Artist', 'Video Artist', 'Experimental Filmmaker', 'Motion Graphics Designer',
                'Motion Graphics Artist', 'VFX Artist', 'Visual Effects Artist', 'Post Production Artist',
                'Animation Artist', 'Data Visualization Designer', 'Information Designer',
                'Infographic Designer', 'Machine Learning Engineer', 'AI Engineer',
                'Neural Network Developer', 'Computer Vision Engineer', 'Image Processing Engineer',
                'Signal Processing Engineer', 'Robotics Engineer', 'Kinetic Artist',
                'Mechanical Artist', 'Automated Artist', 'Bio Artist', 'Bio Media Artist',
                'Biotechnology Artist', 'Synthetic Biology Artist', 'Wearable Technology Designer',
                'Smart Textiles Designer', 'E-Textiles Designer', 'IoT Developer',
                'Embedded Systems Developer', 'Microcontroller Programmer', 'Arduino Developer',
                'Raspberry Pi Developer', 'Processing Developer', 'OpenFrameworks Developer',
                'TouchDesigner Developer', 'vvvv Developer', 'Isadora Developer',
                'Resolume Developer', 'MadMapper Developer', 'Blender Artist', 'Cinema 4D Artist',
                'Maya Artist', '3D Artist', 'After Effects Artist', 'Premiere Pro Editor',
                'Final Cut Pro Editor', 'DaVinci Resolve Colorist', 'Colorist', 'Color Grading Artist'
            ]
        }
    },
    'dutch': {
        # PhD PROGRAMS - Academic Research Positions
        'phd_programs': {
            'media_art_phd': [
                'Media Kunst PhD', 'Digitale Kunst PhD', 'Nieuwe Media PhD',
                'Media Kunst Doctoraat', 'Digitale Kunst Doctoraat', 'Nieuwe Media Doctoraat',
                'Media Kunst Promotie', 'Digitale Kunst Promotie', 'Nieuwe Media Promotie',
                'Doctoraal Programma Media Kunst', 'PhD Programma Digitale Kunst'
            ],
            'ai_art_phd': [
                'AI Kunst PhD', 'Kunstmatige Intelligentie Kunst PhD', 'AI Art PhD',
                'AI Kunst Doctoraat', 'Machine Learning Kunst PhD', 'Neurale Netwerken Kunst PhD',
                'AI Kunst Promotie', 'Algorithmische Kunst PhD', 'Generatieve AI PhD',
                'Doctoraal Programma AI Kunst', 'PhD Programma Machine Learning Kunst'
            ],
            'sound_art_phd': [
                'Geluidskunst PhD', 'Sound Art PhD', 'Audio Art PhD',
                'Geluidskunst Doctoraat', 'Sound Art Doctoraat', 'Audio Art Doctoraat',
                'Geluidskunst Promotie', 'Sound Art Promotie', 'Audio Art Promotie',
                'Doctoraal Programma Geluidskunst', 'PhD Programma Sound Art',
                'Muziek en Media PhD', 'Akoestische Kunst PhD', 'Elektronische Muziek PhD'
            ],
            'artistic_research_phd': [
                'Artistiek Onderzoek', 'Practice-based PhD', 'Artistieke PhD', 'Onderzoek in Kunst',
                'Kunst als Onderzoek', 'Doctoraat in Kunst', 'PhD in Kunst', 'Artistiek Doctoraat',
                'Onderzoeksproject Kunst', 'Creatief Onderzoek', 'Praktijkgericht Onderzoek',
                'Studio-gebaseerd Onderzoek', 'Doctoraal Programma Kunst', 'PhD Programma Artistiek Onderzoek'
            ],
            'general_phd': [
                'PhD', 'Doctoraat', 'Promotie', 'Graduate Studies', 'PhD Positie', 'Doctoraal Positie',
                'PhD Programma', 'Doctoraal Programma', 'Graduate Programma', 'PhD Student', 'Doctoraal Student',
                'PhD Kandidaat', 'Doctoraal Kandidaat', 'Graduate Student', 'Onderzoeksstudent'
            ]
        },
        # JOB OFFERS - Employment Positions
        'job_offers': {
            'media_art_jobs': [
                'Media Kunst Medewerker', 'Digitale Kunst Medewerker', 'Nieuwe Media Medewerker',
                'Artistieke Medewerker Media Kunst', 'Onderzoeksmedewerker Media Kunst',
                'Media Kunst Positie', 'Digitale Kunst Positie', 'Nieuwe Media Positie',
                'Vacature Media Kunst', 'Vacature Digitale Kunst'
            ],
            'ai_art_jobs': [
                'AI Kunst Medewerker', 'Kunstmatige Intelligentie Kunst Medewerker', 'AI Art Medewerker',
                'Artistieke Medewerker AI', 'Onderzoeksmedewerker AI',
                'AI Kunst Positie', 'AI Art Positie', 'Machine Learning Kunst Positie',
                'Vacature AI Kunst', 'Vacature AI Art'
            ],
            'sound_art_jobs': [
                'Geluidskunst Medewerker', 'Sound Art Medewerker', 'Audio Art Medewerker',
                'Artistieke Medewerker Geluid', 'Onderzoeksmedewerker Geluid',
                'Geluidskunst Positie', 'Sound Art Positie', 'Audio Art Positie',
                'Vacature Geluidskunst', 'Vacature Sound Art',
                'Muziek en Media Medewerker', 'Elektronische Muziek Medewerker'
            ],
            'artistic_research_jobs': [
                'Artistiek Onderzoek Medewerker', 'Onderzoeksmedewerker Kunst', 'Artistiek Onderzoek Personeel',
                'Artistieke Medewerker Onderzoek', 'Onderzoeksmedewerker Kunstonderzoek',
                'Artistiek Onderzoek Positie', 'Onderzoek in Kunst Positie',
                'Artistiek Onderzoek Vacature', 'Onderzoek in Kunst Vacature'
            ],
            'academic_jobs': [
                'Artistieke Medewerker', 'Onderzoeksmedewerker', 'Academische Medewerker', 'Artistiek Personeel',
                'Onderzoekspersoneel', 'Academisch Personeel', 'Artistieke Medewerker', 'Onderzoeksmedewerker',
                'Artistieke Associate', 'Onderzoeksassociate', 'Artistieke Fellow', 'Onderzoeksfellow',
                'Artistieke Coördinator', 'Onderzoekscoördinator', 'Artistieke Technicus', 'Onderzoekstechnicus'
            ],
            'general_jobs': [
                'Vacature', 'Positie', 'Baan', 'Werk', 'Carrière', 'Job Mogelijkheid',
                'Academische Positie', 'Onderzoekspositie', 'Kunst Positie', 'Faculteit Positie',
                'Personeel Positie', 'Academische Baan', 'Onderzoeksbaan', 'Kunst Baan'
            ]
        }
    },
    'estonian': {
        # PhD PROGRAMS - Academic Research Positions
        'phd_programs': {
            'media_art_phd': [
                'Meediakunst PhD', 'Digitaalne Kunst PhD', 'Uued Meediad PhD',
                'Meediakunst Doktorikraad', 'Digitaalne Kunst Doktorikraad', 'Uued Meediad Doktorikraad',
                'Meediakunst Doktoritöö', 'Digitaalne Kunst Doktoritöö', 'Uued Meediad Doktoritöö',
                'Doktoriprogramm Meediakunst', 'PhD Programma Digitaalne Kunst'
            ],
            'ai_art_phd': [
                'AI Kunst PhD', 'Tehisintellekt Kunst PhD', 'AI Art PhD',
                'AI Kunst Doktorikraad', 'Masinõpe Kunst PhD', 'Neuraalvõrgu Kunst PhD',
                'AI Kunst Doktoritöö', 'Algoritmiline Kunst PhD', 'Generatiivne AI PhD',
                'Doktoriprogramm AI Kunst', 'PhD Programma Masinõpe Kunst'
            ],
            'sound_art_phd': [
                'Helikunst PhD', 'Sound Art PhD', 'Audio Art PhD',
                'Helikunst Doktorikraad', 'Sound Art Doktorikraad', 'Audio Art Doktorikraad',
                'Helikunst Doktoritöö', 'Sound Art Doktoritöö', 'Audio Art Doktoritöö',
                'Doktoriprogramm Helikunst', 'PhD Programma Sound Art',
                'Muusika ja Meedia PhD', 'Akustiline Kunst PhD', 'Elektrooniline Muusika PhD'
            ],
            'artistic_research_phd': [
                'Kunstiline Uuring', 'Practice-based PhD', 'Kunstiline PhD', 'Uuring Kunstis',
                'Kunst kui Uuring', 'Doktorikraad Kunstis', 'PhD Kunstis', 'Kunstiline Doktorikraad',
                'Uuringuprojekt Kunst', 'Loov Uuring', 'Praktikapõhine Uuring',
                'Stuudio-põhine Uuring', 'Doktoriprogramm Kunst', 'PhD Programma Kunstiline Uuring'
            ],
            'general_phd': [
                'PhD', 'Doktorikraad', 'Doktoritöö', 'Graduate Studies', 'PhD Positsioon', 'Doktori Positsioon',
                'PhD Programma', 'Doktoriprogramma', 'Graduate Programma', 'PhD Üliõpilane', 'Doktori Üliõpilane',
                'PhD Kandidaat', 'Doktori Kandidaat', 'Graduate Üliõpilane', 'Uuringu Üliõpilane'
            ]
        },
        # JOB OFFERS - Employment Positions
        'job_offers': {
            'media_art_jobs': [
                'Meediakunst Töötaja', 'Digitaalne Kunst Töötaja', 'Uued Meediad Töötaja',
                'Kunstiline Töötaja Meediakunst', 'Uuringutöötaja Meediakunst',
                'Meediakunst Positsioon', 'Digitaalne Kunst Positsioon', 'Uued Meediad Positsioon',
                'Tööpakkumine Meediakunst', 'Tööpakkumine Digitaalne Kunst'
            ],
            'ai_art_jobs': [
                'AI Kunst Töötaja', 'Tehisintellekt Kunst Töötaja', 'AI Art Töötaja',
                'Kunstiline Töötaja AI', 'Uuringutöötaja AI',
                'AI Kunst Positsioon', 'AI Art Positsioon', 'Masinõpe Kunst Positsioon',
                'Tööpakkumine AI Kunst', 'Tööpakkumine AI Art'
            ],
            'sound_art_jobs': [
                'Helikunst Töötaja', 'Sound Art Töötaja', 'Audio Art Töötaja',
                'Kunstiline Töötaja Heli', 'Uuringutöötaja Heli',
                'Helikunst Positsioon', 'Sound Art Positsioon', 'Audio Art Positsioon',
                'Tööpakkumine Helikunst', 'Tööpakkumine Sound Art',
                'Muusika ja Meedia Töötaja', 'Elektrooniline Muusika Töötaja'
            ],
            'artistic_research_jobs': [
                'Kunstiline Uuring Töötaja', 'Uuringutöötaja Kunst', 'Kunstiline Uuring Personal',
                'Kunstiline Töötaja Uuring', 'Uuringutöötaja Kunstiuuring',
                'Kunstiline Uuring Positsioon', 'Uuring Kunstis Positsioon',
                'Kunstiline Uuring Tööpakkumine', 'Uuring Kunstis Tööpakkumine'
            ],
            'academic_jobs': [
                'Kunstiline Töötaja', 'Uuringutöötaja', 'Akadeemiline Töötaja', 'Kunstiline Personal',
                'Uuringupersonal', 'Akadeemiline Personal', 'Kunstiline Töötaja', 'Uuringutöötaja',
                'Kunstiline Associate', 'Uuringuassociate', 'Kunstiline Fellow', 'Uuringufellow',
                'Kunstiline Koordinaator', 'Uuringukoordinaator', 'Kunstiline Tehnik', 'Uuringutehnik'
            ],
            'general_jobs': [
                'Tööpakkumine', 'Positsioon', 'Töökoht', 'Töö', 'Karjäär', 'Töövõimalus',
                'Akadeemiline Positsioon', 'Uuringupositsioon', 'Kunst Positsioon', 'Fakulteet Positsioon',
                'Personal Positsioon', 'Akadeemiline Töö', 'Uuringutöö', 'Kunst Töö'
            ]
        }
    }
}

# University data organized by countries/regions (prioritized by German-speaking countries)
UNIVERSITIES_BY_COUNTRY = {
    'germany': [
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
            'phd_url': 'https://www.udk-berlin.de/en/research/graduate-school/',
            'coordinates': [52.5200, 13.4050]
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
            'alternative': 'Dr.phil',
            'coordinates': [48.1351, 11.5820]
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
        }
    ],
    
    'german_speaking': [
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
        },
        {
            'name': 'Universität Mozarteum Salzburg',
            'city': 'Salzburg',
            'country': 'Austria',
            'website': 'https://www.moz.ac.at',
            'has_phd': True,
            'phd_url': 'https://www.moz.ac.at/studium/studienangebot/doctoral-studies'
        },
        {
            'name': 'Hochschule für Musik und Darstellende Kunst Wien',
            'city': 'Wien',
            'country': 'Austria',
            'website': 'https://www.mdw.ac.at',
            'has_phd': True,
            'phd_url': 'https://www.mdw.ac.at/studium/studienangebot/doctoral-studies'
        },
        {
            'name': 'Hochschule für Gestaltung und Kunst Basel',
            'city': 'Basel',
            'country': 'Switzerland',
            'website': 'https://www.fhnw.ch/hgk',
            'has_phd': True,
            'phd_url': 'https://www.fhnw.ch/hgk/forschung'
        },
        {
            'name': 'Zürcher Hochschule der Künste',
            'city': 'Zürich',
            'country': 'Switzerland',
            'website': 'https://www.zhdk.ch',
            'has_phd': True,
            'phd_url': 'https://www.zhdk.ch/forschung'
        },
        {
            'name': 'Hochschule für Gestaltung und Kunst Luzern',
            'city': 'Luzern',
            'country': 'Switzerland',
            'website': 'https://www.hslu.ch/hgk',
            'has_phd': False,
            'alternative': 'Design Studies'
        },
        {
            'name': 'Hochschule für Gestaltung und Kunst Bern',
            'city': 'Bern',
            'country': 'Switzerland',
            'website': 'https://www.hkb.bfh.ch',
            'has_phd': False,
            'alternative': 'Design Studies'
        }
    ],
    
    'eu_other': [
        # Belgium (French/Dutch speaking)
        {
            'name': 'Royal Academy of Fine Arts Antwerp',
            'city': 'Antwerp',
            'country': 'Belgium',
            'website': 'https://www.antwerp.ac.be',
            'has_phd': True,
            'phd_url': 'https://www.antwerp.ac.be/en/research'
        },
        {
            'name': 'LUCA School of Arts',
            'city': 'Brussels',
            'country': 'Belgium',
            'website': 'https://www.luca-arts.be',
            'has_phd': True,
            'phd_url': 'https://www.luca-arts.be/en/research'
        },
        {
            'name': 'École nationale supérieure des arts visuels de La Cambre',
            'city': 'Brussels',
            'country': 'Belgium',
            'website': 'https://www.lacambre.be',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Royal Conservatory of Brussels',
            'city': 'Brussels',
            'country': 'Belgium',
            'website': 'https://www.kcb.be',
            'has_phd': True,
            'phd_url': 'https://www.kcb.be/en/research'
        },
        # Netherlands (Dutch speaking)
        {
            'name': 'Gerrit Rietveld Academie',
            'city': 'Amsterdam',
            'country': 'Netherlands',
            'website': 'https://www.rietveldacademie.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Design Academy Eindhoven',
            'city': 'Eindhoven',
            'country': 'Netherlands',
            'website': 'https://www.designacademy.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'ArtEZ University of the Arts',
            'city': 'Arnhem',
            'country': 'Netherlands',
            'website': 'https://www.artez.nl',
            'has_phd': True,
            'phd_url': 'https://www.artez.nl/en/research'
        },
        {
            'name': 'Royal Academy of Art The Hague',
            'city': 'The Hague',
            'country': 'Netherlands',
            'website': 'https://www.kabk.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'HKU University of the Arts Utrecht',
            'city': 'Utrecht',
            'country': 'Netherlands',
            'website': 'https://www.hku.nl',
            'has_phd': True,
            'phd_url': 'https://www.hku.nl/en/research'
        },
        {
            'name': 'Willem de Kooning Academy',
            'city': 'Rotterdam',
            'country': 'Netherlands',
            'website': 'https://www.wdka.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        # Estonia
        {
            'name': 'Estonian Academy of Arts',
            'city': 'Tallinn',
            'country': 'Estonia',
            'website': 'https://www.artun.ee',
            'has_phd': True,
            'phd_url': 'https://www.artun.ee/en/research'
        },
        {
            'name': 'Estonian Academy of Music and Theatre',
            'city': 'Tallinn',
            'country': 'Estonia',
            'website': 'https://www.ema.edu.ee',
            'has_phd': True,
            'phd_url': 'https://www.ema.edu.ee/en/research'
        },
        {
            'name': 'University of Tartu Viljandi Culture Academy',
            'city': 'Viljandi',
            'country': 'Estonia',
            'website': 'https://www.ut.ee/en/viljandi-culture-academy',
            'has_phd': False,
            'alternative': 'Bachelor and Master Programs'
        },
        # UK (English speaking)
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
            'name': 'Goldsmiths University of London',
            'city': 'London',
            'country': 'UK',
            'website': 'https://www.gold.ac.uk',
            'has_phd': True,
            'phd_url': 'https://www.gold.ac.uk/art/'
        },
        {
            'name': 'University of the Arts London',
            'city': 'London',
            'country': 'UK',
            'website': 'https://www.arts.ac.uk',
            'has_phd': True,
            'phd_url': 'https://www.arts.ac.uk/research'
        },
        {
            'name': 'Slade School of Fine Art',
            'city': 'London',
            'country': 'UK',
            'website': 'https://www.ucl.ac.uk/slade',
            'has_phd': True,
            'phd_url': 'https://www.ucl.ac.uk/slade/research'
        },
        {
            'name': 'Glasgow School of Art',
            'city': 'Glasgow',
            'country': 'UK',
            'website': 'https://www.gsa.ac.uk',
            'has_phd': True,
            'phd_url': 'https://www.gsa.ac.uk/research'
        },
        {
            'name': 'Edinburgh College of Art',
            'city': 'Edinburgh',
            'country': 'UK',
            'website': 'https://www.eca.ed.ac.uk',
            'has_phd': True,
            'phd_url': 'https://www.eca.ed.ac.uk/research'
        },
        {
            'name': 'Gerrit Rietveld Academie',
            'city': 'Amsterdam',
            'country': 'Netherlands',
            'website': 'https://www.rietveldacademie.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Design Academy Eindhoven',
            'city': 'Eindhoven',
            'country': 'Netherlands',
            'website': 'https://www.designacademy.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Royal Academy of Art The Hague',
            'city': 'The Hague',
            'country': 'Netherlands',
            'website': 'https://www.kabk.nl',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Konstfack University of Arts, Crafts and Design',
            'city': 'Stockholm',
            'country': 'Sweden',
            'website': 'https://www.konstfack.se',
            'has_phd': True,
            'phd_url': 'https://www.konstfack.se/en/research'
        },
        {
            'name': 'Royal Danish Academy of Fine Arts',
            'city': 'Copenhagen',
            'country': 'Denmark',
            'website': 'https://www.kadk.dk',
            'has_phd': True,
            'phd_url': 'https://www.kadk.dk/en/research'
        },
        {
            'name': 'Oslo National Academy of the Arts',
            'city': 'Oslo',
            'country': 'Norway',
            'website': 'https://www.khio.no',
            'has_phd': True,
            'phd_url': 'https://www.khio.no/en/research'
        },
        {
            'name': 'École Nationale Supérieure des Beaux-Arts',
            'city': 'Paris',
            'country': 'France',
            'website': 'https://www.beauxartsparis.fr',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'École Nationale Supérieure des Arts Décoratifs',
            'city': 'Paris',
            'country': 'France',
            'website': 'https://www.ensad.fr',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Accademia di Belle Arti di Brera',
            'city': 'Milan',
            'country': 'Italy',
            'website': 'https://www.accademiadibrera.milano.it',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
        {
            'name': 'Accademia di Belle Arti di Firenze',
            'city': 'Florence',
            'country': 'Italy',
            'website': 'https://www.accademia.firenze.it',
            'has_phd': False,
            'alternative': 'Master Programs'
        },
    ],
    
    'others': [
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
        },
        {
            'name': 'School of the Art Institute of Chicago',
            'city': 'Chicago',
            'country': 'USA',
            'website': 'https://www.saic.edu',
            'has_phd': True,
            'phd_url': 'https://www.saic.edu/academics/graduate-studies'
        },
        {
            'name': 'Yale School of Art',
            'city': 'New Haven',
            'country': 'USA',
            'website': 'https://www.art.yale.edu',
            'has_phd': True,
            'phd_url': 'https://www.art.yale.edu/graduate-program'
        },
        {
            'name': 'Massachusetts College of Art and Design',
            'city': 'Boston',
            'country': 'USA',
            'website': 'https://www.massart.edu',
            'has_phd': False,
            'alternative': 'MFA Programs'
        },
        {
            'name': 'Art Center College of Design',
            'city': 'Pasadena',
            'country': 'USA',
            'website': 'https://www.artcenter.edu',
            'has_phd': False,
            'alternative': 'Graduate Programs'
        },
        {
            'name': 'Emily Carr University of Art and Design',
            'city': 'Vancouver',
            'country': 'Canada',
            'website': 'https://www.ecuad.ca',
            'has_phd': False,
            'alternative': 'Graduate Programs'
        },
        {
            'name': 'Ontario College of Art and Design University',
            'city': 'Toronto',
            'country': 'Canada',
            'website': 'https://www.ocadu.ca',
            'has_phd': False,
            'alternative': 'Graduate Programs'
        },
        {
            'name': 'Nova Scotia College of Art and Design',
            'city': 'Halifax',
            'country': 'Canada',
            'website': 'https://www.nscad.ca',
            'has_phd': False,
            'alternative': 'Graduate Programs'
        }
    ]
}

# Legacy compatibility - combine all universities
UNIVERSITIES = []
for country_group in UNIVERSITIES_BY_COUNTRY.values():
    UNIVERSITIES.extend(country_group)

# Department and Faculty Detection
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
        # AI and Machine Learning Related (Priority)
        'Künstliche Intelligenz', 'KI', 'Artificial Intelligence', 'AI', 'Machine Learning',
        'Maschinelles Lernen', 'Deep Learning', 'Neuronale Netze', 'Neural Networks',
        'Algorithmic Art', 'Algorithmische Kunst', 'Generative AI', 'Generative Kunst',
        'AI Art', 'KI-Kunst', 'Computational Creativity', 'Computational Arts',
        'Creative AI', 'Kreative KI', 'AI Tools', 'KI-Tools', 'ChatGPT', 'DALL-E',
        'Midjourney', 'Stable Diffusion', 'Generative Models', 'Generative Models',
        # Code and Programming Related
        'Informatik', 'Computer Science', 'Software Engineering', 'Programmierung',
        'Digitale Technologien', 'Medieninformatik', 'Computational Arts',
        'Creative Coding', 'Generative Design', 'Algorithmic Design',
        'Human-Computer Interaction', 'Interactive Systems', 'User Experience',
        'Web Development', 'Mobile Development', 'Game Design', 'Game Development',
        'Virtual Reality', 'Augmented Reality', 'Mixed Reality', 'VR', 'AR', 'MR',
        # Sound and Audio Related
        'Musik', 'Musikwissenschaft', 'Komposition', 'Sound Design', 'Klangkunst',
        'Audio Engineering', 'Tontechnik', 'Audioproduktion', 'Musikproduktion',
        'Elektronische Musik', 'Elektroakustik', 'Akustik', 'Sound Art',
        'Audio Visual', 'Medienkunst', 'Interaktive Klanginstallation',
        'Spatial Audio', '3D Audio', 'Binaural Audio', 'Ambisonic',
        'Max/MSP', 'Pure Data', 'SuperCollider', 'Csound', 'ChucK',
        'Digital Audio Workstation', 'DAW', 'Pro Tools', 'Ableton Live',
        'Logic Pro', 'Cubase', 'Reaper', 'Ardour',
        # Media Art and Technology
        'Medienkunst', 'Digital Art', 'Electronic Art', 'Cyber Art',
        'Net Art', 'Internet Art', 'Web Art', 'Software Art',
        'Generative Art', 'Algorithmic Art', 'Computational Art',
        'Interactive Art', 'Participatory Art', 'Installation Art',
        'Video Art', 'Digital Video', 'Experimental Film', 'Animation',
        'Motion Graphics', 'Visual Effects', 'VFX', 'Post Production',
        'Multimedia', 'Cross Media', 'Transmedia', 'Hybrid Media',
        'Performance Art', 'Live Art', 'Body Art', 'Conceptual Art',
        'Data Visualization', 'Information Design', 'Infographic',
        'Machine Learning', 'Artificial Intelligence', 'Neural Networks',
        'Computer Vision', 'Image Processing', 'Signal Processing',
        'Robotics', 'Kinetic Art', 'Mechanical Art', 'Automated Art',
        'Bio Art', 'Bio Media', 'Biotechnology', 'Synthetic Biology',
        'Wearable Technology', 'Smart Textiles', 'E-Textiles',
        'Internet of Things', 'IoT', 'Embedded Systems', 'Microcontrollers',
        'Arduino', 'Raspberry Pi', 'Processing', 'OpenFrameworks',
        'TouchDesigner', 'vvvv', 'Isadora', 'Resolume', 'MadMapper',
        'Unity', 'Unreal Engine', 'Blender', 'Cinema 4D', 'Maya',
        'After Effects', 'Premiere Pro', 'Final Cut Pro', 'DaVinci Resolve'
    ],
    'english': [
        'Art School', 'Art Academy', 'College of Art', 'School of Art',
        'Faculty of Art', 'Faculty of Design', 'Faculty of Media',
        'Department of Art', 'Department of Design', 'Department of Media',
        'Institute of Art', 'Institute of Design', 'Institute of Media',
        'Art Program', 'Design Program', 'Media Program',
        'Art Studies', 'Media Studies', 'Design Studies',
        'Digital Art', 'New Media', 'Interactive Media',
        'Photography', 'Painting', 'Sculpture', 'Graphic Design', 'Illustration',
        'Communication Design', 'Product Design', 'Fashion', 'Textile',
        'Architecture', 'Interior Design', 'Landscape Architecture',
        'Art History', 'Art Education', 'Art Therapy',
        'Research Institute', 'Research Center', 'Graduate School',
        # AI and Machine Learning Related (Priority)
        'Artificial Intelligence', 'AI', 'Machine Learning', 'Deep Learning', 'Neural Networks',
        'Algorithmic Art', 'Generative AI', 'AI Art', 'Computational Creativity',
        'Computational Arts', 'Creative AI', 'AI Tools', 'ChatGPT', 'DALL-E',
        'Midjourney', 'Stable Diffusion', 'Generative Models', 'Generative Art',
        # Code and Programming Related
        'Computer Science', 'Software Engineering', 'Programming', 'Coding',
        'Digital Technologies', 'Media Informatics', 'Computational Arts',
        'Creative Coding', 'Generative Design', 'Algorithmic Design',
        'Human-Computer Interaction', 'Interactive Systems', 'User Experience',
        'Web Development', 'Mobile Development', 'Game Design', 'Game Development',
        'Virtual Reality', 'Augmented Reality', 'Mixed Reality', 'VR', 'AR', 'MR',
        # Sound and Audio Related
        'Music', 'Musicology', 'Composition', 'Sound Design', 'Sound Art',
        'Audio Engineering', 'Audio Technology', 'Audio Production', 'Music Production',
        'Electronic Music', 'Electroacoustics', 'Acoustics', 'Audio Visual',
        'Interactive Sound Installation', 'Spatial Audio', '3D Audio', 'Binaural Audio',
        'Ambisonic', 'Max/MSP', 'Pure Data', 'SuperCollider', 'Csound', 'ChucK',
        'Digital Audio Workstation', 'DAW', 'Pro Tools', 'Ableton Live',
        'Logic Pro', 'Cubase', 'Reaper', 'Ardour',
        # Media Art and Technology
        'Media Art', 'Digital Art', 'Electronic Art', 'Cyber Art',
        'Net Art', 'Internet Art', 'Web Art', 'Software Art',
        'Generative Art', 'Algorithmic Art', 'Computational Art',
        'Interactive Art', 'Participatory Art', 'Installation Art',
        'Video Art', 'Digital Video', 'Experimental Film', 'Animation',
        'Motion Graphics', 'Visual Effects', 'VFX', 'Post Production',
        'Multimedia', 'Cross Media', 'Transmedia', 'Hybrid Media',
        'Performance Art', 'Live Art', 'Body Art', 'Conceptual Art',
        'Data Visualization', 'Information Design', 'Infographic',
        'Machine Learning', 'Artificial Intelligence', 'Neural Networks',
        'Computer Vision', 'Image Processing', 'Signal Processing',
        'Robotics', 'Kinetic Art', 'Mechanical Art', 'Automated Art',
        'Bio Art', 'Bio Media', 'Biotechnology', 'Synthetic Biology',
        'Wearable Technology', 'Smart Textiles', 'E-Textiles',
        'Internet of Things', 'IoT', 'Embedded Systems', 'Microcontrollers',
        'Arduino', 'Raspberry Pi', 'Processing', 'OpenFrameworks',
        'TouchDesigner', 'vvvv', 'Isadora', 'Resolume', 'MadMapper',
        'Unity', 'Unreal Engine', 'Blender', 'Cinema 4D', 'Maya',
        'After Effects', 'Premiere Pro', 'Final Cut Pro', 'DaVinci Resolve'
    ]
}

# Academic Position Hierarchy
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

# Employment Details Detection
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
        'salary': ['Salary', 'Pay Grade', 'Compensation', 'Remuneration', 'Stipend'],
        'requirements': ['Requirements', 'Qualifications', 'Education', 'Experience', 'Skills']
    }
}

# Additional German Fachhochschulen and Art Institutions
FACHHOCHSCHULEN_AND_ART_SCHOOLS = [
    # Fachhochschulen with Media/Design Programs
    {
        'name': 'Fachhochschule Potsdam',
        'city': 'Potsdam',
        'country': 'Germany',
        'website': 'https://www.fh-potsdam.de',
        'has_phd': False,
        'alternative': 'Design Studies'
    },
    {
        'name': 'Hochschule für Gestaltung Schwäbisch Gmünd',
        'city': 'Schwäbisch Gmünd',
        'country': 'Germany',
        'website': 'https://www.hfg-gmuend.de',
        'has_phd': False,
        'alternative': 'Design Studies'
    },
    {
        'name': 'Hochschule für Technik und Wirtschaft Berlin',
        'city': 'Berlin',
        'country': 'Germany',
        'website': 'https://www.htw-berlin.de',
        'has_phd': False,
        'alternative': 'Media Studies'
    },
    {
        'name': 'Hochschule für Medien Stuttgart',
        'city': 'Stuttgart',
        'country': 'Germany',
        'website': 'https://www.hdm-stuttgart.de',
        'has_phd': False,
        'alternative': 'Media Studies'
    },
    {
        'name': 'Hochschule für Technik und Wirtschaft Dresden',
        'city': 'Dresden',
        'country': 'Germany',
        'website': 'https://www.htw-dresden.de',
        'has_phd': False,
        'alternative': 'Design Studies'
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
        'name': 'Hochschule für Bildende Künste Hamburg',
        'city': 'Hamburg',
        'country': 'Germany',
        'website': 'https://www.hfbk-hamburg.de',
        'has_phd': True,
        'phd_url': 'https://www.hfbk-hamburg.de/en/studium/promotion-der-hfbk-hamburg/'
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
        'name': 'Hochschule für Bildende Künste Braunschweig',
        'city': 'Braunschweig',
        'country': 'Germany',
        'website': 'https://www.hbk-bs.de',
        'has_phd': True,
        'phd_url': 'https://www.hbk-bs.de/hochschule/forschung-entwicklung/'
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
        'name': 'Bauhaus-Universität Weimar',
        'city': 'Weimar',
        'country': 'Germany',
        'website': 'https://www.uni-weimar.de',
        'has_phd': True,
        'phd_url': 'https://www.uni-weimar.de/en/art-and-design/studies/doctorate-at-the-faculty-of-art-and-design/degree-programmes/degree-programme-phd/'
    },
    # Additional Art Schools and Design Universities
    {
        'name': 'Hochschule für Gestaltung und Kunst Basel',
        'city': 'Basel',
        'country': 'Switzerland',
        'website': 'https://www.fhnw.ch/hgk',
        'has_phd': True,
        'phd_url': 'https://www.fhnw.ch/hgk/forschung'
    },
    {
        'name': 'Zürcher Hochschule der Künste',
        'city': 'Zürich',
        'country': 'Switzerland',
        'website': 'https://www.zhdk.ch',
        'has_phd': True,
        'phd_url': 'https://www.zhdk.ch/forschung'
    },
    {
        'name': 'Hochschule für Gestaltung und Kunst Luzern',
        'city': 'Luzern',
        'country': 'Switzerland',
        'website': 'https://www.hslu.ch/hgk',
        'has_phd': False,
        'alternative': 'Design Studies'
    },
    {
        'name': 'Hochschule für Gestaltung und Kunst Bern',
        'city': 'Bern',
        'country': 'Switzerland',
        'website': 'https://www.hkb.bfh.ch',
        'has_phd': False,
        'alternative': 'Design Studies'
    },
    # Austrian Universities
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
    },
    {
        'name': 'Universität Mozarteum Salzburg',
        'city': 'Salzburg',
        'country': 'Austria',
        'website': 'https://www.moz.ac.at',
        'has_phd': True,
        'phd_url': 'https://www.moz.ac.at/studium/studienangebot/doctoral-studies'
    },
    {
        'name': 'Hochschule für Musik und Darstellende Kunst Wien',
        'city': 'Wien',
        'country': 'Austria',
        'website': 'https://www.mdw.ac.at',
        'has_phd': True,
        'phd_url': 'https://www.mdw.ac.at/studium/studienangebot/doctoral-studies'
    }
]

# Additional major international art universities
INTERNATIONAL_UNIVERSITIES = [
    # UK Universities
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
        'name': 'Goldsmiths University of London',
        'city': 'London',
        'country': 'UK',
        'website': 'https://www.gold.ac.uk',
        'has_phd': True,
        'phd_url': 'https://www.gold.ac.uk/art/'
    },
    {
        'name': 'University of the Arts London',
        'city': 'London',
        'country': 'UK',
        'website': 'https://www.arts.ac.uk',
        'has_phd': True,
        'phd_url': 'https://www.arts.ac.uk/research'
    },
    {
        'name': 'Slade School of Fine Art',
        'city': 'London',
        'country': 'UK',
        'website': 'https://www.ucl.ac.uk/slade',
        'has_phd': True,
        'phd_url': 'https://www.ucl.ac.uk/slade/research'
    },
    {
        'name': 'Glasgow School of Art',
        'city': 'Glasgow',
        'country': 'UK',
        'website': 'https://www.gsa.ac.uk',
        'has_phd': True,
        'phd_url': 'https://www.gsa.ac.uk/research'
    },
    {
        'name': 'Edinburgh College of Art',
        'city': 'Edinburgh',
        'country': 'UK',
        'website': 'https://www.eca.ed.ac.uk',
        'has_phd': True,
        'phd_url': 'https://www.eca.ed.ac.uk/research'
    },
    # USA Universities
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
    },
    {
        'name': 'School of the Art Institute of Chicago',
        'city': 'Chicago',
        'country': 'USA',
        'website': 'https://www.saic.edu',
        'has_phd': True,
        'phd_url': 'https://www.saic.edu/academics/graduate-studies'
    },
    {
        'name': 'Yale School of Art',
        'city': 'New Haven',
        'country': 'USA',
        'website': 'https://www.art.yale.edu',
        'has_phd': True,
        'phd_url': 'https://www.art.yale.edu/graduate-program'
    },
    {
        'name': 'Massachusetts College of Art and Design',
        'city': 'Boston',
        'country': 'USA',
        'website': 'https://www.massart.edu',
        'has_phd': False,
        'alternative': 'MFA Programs'
    },
    {
        'name': 'Art Center College of Design',
        'city': 'Pasadena',
        'country': 'USA',
        'website': 'https://www.artcenter.edu',
        'has_phd': False,
        'alternative': 'Graduate Programs'
    },
    # Canadian Universities
    {
        'name': 'Emily Carr University of Art and Design',
        'city': 'Vancouver',
        'country': 'Canada',
        'website': 'https://www.ecuad.ca',
        'has_phd': False,
        'alternative': 'Graduate Programs'
    },
    {
        'name': 'Ontario College of Art and Design University',
        'city': 'Toronto',
        'country': 'Canada',
        'website': 'https://www.ocadu.ca',
        'has_phd': False,
        'alternative': 'Graduate Programs'
    },
    {
        'name': 'Nova Scotia College of Art and Design',
        'city': 'Halifax',
        'country': 'Canada',
        'website': 'https://www.nscad.ca',
        'has_phd': False,
        'alternative': 'Graduate Programs'
    },
    # Dutch Universities
    {
        'name': 'Gerrit Rietveld Academie',
        'city': 'Amsterdam',
        'country': 'Netherlands',
        'website': 'https://www.rietveldacademie.nl',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    {
        'name': 'Design Academy Eindhoven',
        'city': 'Eindhoven',
        'country': 'Netherlands',
        'website': 'https://www.designacademy.nl',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    {
        'name': 'Royal Academy of Art The Hague',
        'city': 'The Hague',
        'country': 'Netherlands',
        'website': 'https://www.kabk.nl',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    # Scandinavian Universities
    {
        'name': 'Konstfack University of Arts, Crafts and Design',
        'city': 'Stockholm',
        'country': 'Sweden',
        'website': 'https://www.konstfack.se',
        'has_phd': True,
        'phd_url': 'https://www.konstfack.se/en/research'
    },
    {
        'name': 'Royal Danish Academy of Fine Arts',
        'city': 'Copenhagen',
        'country': 'Denmark',
        'website': 'https://www.kadk.dk',
        'has_phd': True,
        'phd_url': 'https://www.kadk.dk/en/research'
    },
    {
        'name': 'Oslo National Academy of the Arts',
        'city': 'Oslo',
        'country': 'Norway',
        'website': 'https://www.khio.no',
        'has_phd': True,
        'phd_url': 'https://www.khio.no/en/research'
    },
    # French Universities
    {
        'name': 'École Nationale Supérieure des Beaux-Arts',
        'city': 'Paris',
        'country': 'France',
        'website': 'https://www.beauxartsparis.fr',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    {
        'name': 'École Nationale Supérieure des Arts Décoratifs',
        'city': 'Paris',
        'country': 'France',
        'website': 'https://www.ensad.fr',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    # Italian Universities
    {
        'name': 'Accademia di Belle Arti di Brera',
        'city': 'Milan',
        'country': 'Italy',
        'website': 'https://www.accademiadibrera.milano.it',
        'has_phd': False,
        'alternative': 'Master Programs'
    },
    {
        'name': 'Accademia di Belle Arti di Firenze',
        'city': 'Florence',
        'country': 'Italy',
        'website': 'https://www.accademia.firenze.it',
        'has_phd': False,
        'alternative': 'Master Programs'
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