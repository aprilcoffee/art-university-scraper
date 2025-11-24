"""
University configuration for art university job scraper.
Prioritized by media art, design, and digital focus.

Priority Order:
1. Media Art & Design Schools (highest priority)
2. Film & Media Universities
3. Design-focused Fachhochschulen
4. Design-focused Art Schools
5. Traditional Art Schools
6. Music/Theater Schools (lower priority)
"""

UNIVERSITIES = [
    # ===== HIGHEST PRIORITY: Media Art & Design Schools =====

    # Germany - Media Art Leaders
    {
        'name': 'Kunsthochschule für Medien Köln',
        'website': 'https://www.khm.de',
        'country': 'DE',
        'city': 'Köln',
        'job_page_url': None,
    },
    {
        'name': 'Staatliche Hochschule für Gestaltung Karlsruhe',
        'website': 'https://www.hfg-karlsruhe.de',
        'country': 'DE',
        'city': 'Karlsruhe',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Gestaltung Schwäbisch Gmünd',
        'website': 'https://www.hfg-gmuend.de',
        'country': 'DE',
        'city': 'Schwäbisch Gmünd',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Gestaltung Offenbach am Main',
        'website': 'https://www.hfg-offenbach.de',
        'country': 'DE',
        'city': 'Offenbach',
        'job_page_url': None,
    },
    {
        'name': 'Bauhaus-Universität Weimar',
        'website': 'https://www.uni-weimar.de',
        'country': 'DE',
        'city': 'Weimar',
        'job_page_url': None,
    },
    {
        'name': 'Universität der Künste Berlin',
        'website': 'https://www.udk-berlin.de',
        'country': 'DE',
        'city': 'Berlin',
        'job_page_url': 'https://www.udk-berlin.de/universitaet/stellenausschreibungen/',
    },

    # Film & Media Universities
    {
        'name': 'Filmuniversität Babelsberg Konrad Wolf',
        'website': 'https://www.filmuniversitaet.de',
        'country': 'DE',
        'city': 'Potsdam',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Fernsehen und Film München',
        'website': 'https://www.hff-muenchen.de',
        'country': 'DE',
        'city': 'München',
        'job_page_url': None,
    },

    # Austria - Media/Design Focus
    {
        'name': 'Universität für angewandte Kunst Wien',
        'website': 'https://www.dieangewandte.at',
        'country': 'AT',
        'city': 'Wien',
        'job_page_url': None,
    },
    {
        'name': 'Kunstuniversität Linz',
        'website': 'https://www.ufg.at',
        'country': 'AT',
        'city': 'Linz',
        'job_page_url': None,
    },

    # Switzerland - Design/Media Leaders
    {
        'name': 'Zürcher Hochschule der Künste',
        'website': 'https://www.zhdk.ch',
        'country': 'CH',
        'city': 'Zürich',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Gestaltung und Kunst Basel',
        'website': 'https://www.fhnw.ch/de/hochschule-fur-gestaltung-und-kunst',
        'country': 'CH',
        'city': 'Basel',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule der Künste Bern',
        'website': 'https://www.hkb.bfh.ch',
        'country': 'CH',
        'city': 'Bern',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule Luzern - Design & Kunst',
        'website': 'https://www.hslu.ch',
        'country': 'CH',
        'city': 'Luzern',
        'job_page_url': None,
    },
    {
        'name': 'Haute école d\'art et de design Genève',
        'website': 'https://www.hesge.ch/head',
        'country': 'CH',
        'city': 'Genève',
        'job_page_url': None,
    },
    {
        'name': 'Fachhochschule Nordwestschweiz - Hochschule für Gestaltung und Kunst',
        'website': 'https://www.fhnw.ch/hgk',
        'country': 'CH',
        'city': 'Basel',
        'job_page_url': None,
    },

    # ===== HIGH PRIORITY: Design-focused Fachhochschulen =====

    {
        'name': 'Hochschule für Angewandte Wissenschaften Hamburg',
        'website': 'https://www.haw-hamburg.de',
        'country': 'DE',
        'city': 'Hamburg',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Angewandte Wissenschaften München',
        'website': 'https://www.hm.edu',
        'country': 'DE',
        'city': 'München',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Technik und Wirtschaft Berlin',
        'website': 'https://www.htw-berlin.de',
        'country': 'DE',
        'city': 'Berlin',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Technik, Wirtschaft und Kultur Leipzig',
        'website': 'https://www.htwk-leipzig.de',
        'country': 'DE',
        'city': 'Leipzig',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Gestaltung Pforzheim',
        'website': 'https://www.hs-pforzheim.de',
        'country': 'DE',
        'city': 'Pforzheim',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule Mannheim',
        'website': 'https://www.hs-mannheim.de',
        'country': 'DE',
        'city': 'Mannheim',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule Darmstadt',
        'website': 'https://www.h-da.de',
        'country': 'DE',
        'city': 'Darmstadt',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Technik und Wirtschaft Dresden',
        'website': 'https://www.htw-dresden.de',
        'country': 'DE',
        'city': 'Dresden',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule Augsburg',
        'website': 'https://www.hs-augsburg.de',
        'country': 'DE',
        'city': 'Augsburg',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule Düsseldorf',
        'website': 'https://www.hs-duesseldorf.de',
        'country': 'DE',
        'city': 'Düsseldorf',
        'job_page_url': None,
    },

    # ===== MEDIUM PRIORITY: Contemporary/Design-oriented Art Schools =====

    {
        'name': 'Burg Giebichenstein Kunsthochschule Halle',
        'website': 'https://www.burg-halle.de',
        'country': 'DE',
        'city': 'Halle',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für bildende Künste Hamburg',
        'website': 'https://www.hfbk-hamburg.de',
        'country': 'DE',
        'city': 'Hamburg',
        'job_page_url': None,
    },
    {
        'name': 'Kunsthochschule Berlin-Weißensee',
        'website': 'https://www.kh-berlin.de',
        'country': 'DE',
        'city': 'Berlin',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Grafik und Buchkunst Leipzig',
        'website': 'https://www.hgb-leipzig.de',
        'country': 'DE',
        'city': 'Leipzig',
        'job_page_url': None,
    },
    {
        'name': 'Folkwang Universität der Künste',
        'website': 'https://www.folkwang-uni.de',
        'country': 'DE',
        'city': 'Essen',
        'job_page_url': None,
    },
    {
        'name': 'Muthesius Kunsthochschule',
        'website': 'https://www.muthesius.de',
        'country': 'DE',
        'city': 'Kiel',
        'job_page_url': None,
    },

    # ===== STANDARD PRIORITY: Traditional Art Schools =====

    {
        'name': 'Hochschule für Bildende Künste Braunschweig',
        'website': 'https://www.hbk-bs.de',
        'country': 'DE',
        'city': 'Braunschweig',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Künste Bremen',
        'website': 'https://www.hfk-bremen.de',
        'country': 'DE',
        'city': 'Bremen',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Bildende Künste Dresden',
        'website': 'https://www.hfbk-dresden.de',
        'country': 'DE',
        'city': 'Dresden',
        'job_page_url': None,
    },
    {
        'name': 'Kunstakademie Düsseldorf',
        'website': 'https://www.kunstakademie-duesseldorf.de',
        'country': 'DE',
        'city': 'Düsseldorf',
        'job_page_url': None,
    },
    {
        'name': 'Staatliche Hochschule für Bildende Künste – Städelschule',
        'website': 'https://www.staedelschule.de',
        'country': 'DE',
        'city': 'Frankfurt',
        'job_page_url': None,
    },
    {
        'name': 'Kunsthochschule Mainz',
        'website': 'https://www.kunsthochschule-mainz.de',
        'country': 'DE',
        'city': 'Mainz',
        'job_page_url': None,
    },
    {
        'name': 'Akademie der Bildenden Künste München',
        'website': 'https://www.adbk.de',
        'country': 'DE',
        'city': 'München',
        'job_page_url': None,
    },
    {
        'name': 'Kunstakademie Münster',
        'website': 'https://www.kunstakademie-muenster.de',
        'country': 'DE',
        'city': 'Münster',
        'job_page_url': None,
    },
    {
        'name': 'Akademie der Bildenden Künste Nürnberg',
        'website': 'https://www.adbk-nuernberg.de',
        'country': 'DE',
        'city': 'Nürnberg',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule der Bildenden Künste Saar',
        'website': 'https://www.hbksaar.de',
        'country': 'DE',
        'city': 'Saarbrücken',
        'job_page_url': None,
    },
    {
        'name': 'Staatliche Akademie der Bildenden Künste Stuttgart',
        'website': 'https://www.abk-stuttgart.de',
        'country': 'DE',
        'city': 'Stuttgart',
        'job_page_url': None,
    },
    {
        'name': 'Alanus Hochschule für Kunst und Gesellschaft',
        'website': 'https://www.alanus.edu',
        'country': 'DE',
        'city': 'Alfter',
        'job_page_url': None,
    },

    # Austria - Traditional
    {
        'name': 'Kunstuniversität Graz',
        'website': 'https://www.kug.ac.at',
        'country': 'AT',
        'city': 'Graz',
        'job_page_url': None,
    },
    {
        'name': 'Akademie der bildenden Künste Wien',
        'website': 'https://www.akbild.ac.at',
        'country': 'AT',
        'city': 'Wien',
        'job_page_url': None,
    },

    # ===== LOWER PRIORITY: Music/Theater Schools =====

    {
        'name': 'Hochschule für Musik und Theater Hamburg',
        'website': 'https://www.hfmt-hamburg.de',
        'country': 'DE',
        'city': 'Hamburg',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Musik und Theater München',
        'website': 'https://www.musikhochschule-muenchen.de',
        'country': 'DE',
        'city': 'München',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Musik und Theater Leipzig',
        'website': 'https://www.hmt-leipzig.de',
        'country': 'DE',
        'city': 'Leipzig',
        'job_page_url': None,
    },
    {
        'name': 'Universität Mozarteum Salzburg',
        'website': 'https://www.moz.ac.at',
        'country': 'AT',
        'city': 'Salzburg',
        'job_page_url': None,
    },
    {
        'name': 'Hochschule für Musik und Darstellende Kunst Wien',
        'website': 'https://www.mdw.ac.at',
        'country': 'AT',
        'city': 'Wien',
        'job_page_url': None,
    },
]


def get_universities_by_country(country_code):
    """Get all universities from a specific country."""
    return [u for u in UNIVERSITIES if u['country'] == country_code]


def get_university_by_name(name):
    """Get university config by name."""
    for u in UNIVERSITIES:
        if u['name'] == name:
            return u
    return None


def get_all_universities():
    """Get all universities in priority order."""
    return UNIVERSITIES


def get_high_priority_universities():
    """Get only highest priority universities (media art & design focus)."""
    # First 26 universities in the list
    return UNIVERSITIES[:26]


def get_media_art_universities():
    """Get media art focused universities only."""
    return UNIVERSITIES[:8]
