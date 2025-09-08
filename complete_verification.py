#!/usr/bin/env python3
"""
Complete University Link Verification and Missing Schools Finder
"""

import requests
import time
from config import UNIVERSITY_WEBSITES, UNIVERSITIES_BY_COUNTRY

def check_link(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        return {
            'status': response.status_code,
            'working': response.status_code == 200,
            'final_url': response.url,
            'error': None
        }
    except Exception as e:
        return {
            'status': None,
            'working': False,
            'final_url': None,
            'error': str(e)
        }

def main():
    print("🔍 COMPLETE UNIVERSITY LINK VERIFICATION")
    print("=" * 60)
    
    working = []
    broken = []
    
    # Check all current links
    for uni, url in UNIVERSITY_WEBSITES.items():
        print(f"Checking: {uni}")
        result = check_link(url)
        
        if result['working']:
            print(f"✅ {result['status']} - WORKING")
            working.append((uni, url))
        else:
            print(f"❌ BROKEN - {result['error']}")
            broken.append((uni, url, result['error']))
        
        time.sleep(0.5)  # Be respectful
    
    print(f"\n📊 RESULTS:")
    print(f"✅ Working: {len(working)}")
    print(f"❌ Broken: {len(broken)}")
    
    if broken:
        print(f"\n🔧 BROKEN LINKS:")
        for uni, url, error in broken:
            print(f"- {uni}: {url}")
    
    # Additional major art schools that might be missing
    additional_schools = {
        # German Fachhochschule with art/design
        'Hochschule für Gestaltung Schwäbisch Gmünd': 'https://www.hfg-gmuend.de',
        'Hochschule für Technik und Wirtschaft Berlin': 'https://www.htw-berlin.de',
        'Hochschule für Technik, Wirtschaft und Kultur Leipzig': 'https://www.htwk-leipzig.de',
        'Hochschule für Technik und Wirtschaft Dresden': 'https://www.htw-dresden.de',
        'Hochschule für Technik und Wirtschaft Berlin': 'https://www.htw-berlin.de',
        'Hochschule für Technik und Wirtschaft Karlsruhe': 'https://www.hs-karlsruhe.de',
        'Hochschule für Technik und Wirtschaft Dresden': 'https://www.htw-dresden.de',
        'Hochschule für Technik und Wirtschaft Berlin': 'https://www.htw-berlin.de',
        
        # Missing major art schools
        'Hochschule für Musik und Theater Hamburg': 'https://www.hfmt-hamburg.de',
        'Hochschule für Musik und Theater München': 'https://www.musikhochschule-muenchen.de',
        'Hochschule für Musik und Theater Leipzig': 'https://www.hmt-leipzig.de',
        'Hochschule für Musik und Theater Hannover': 'https://www.hmtm-hannover.de',
        'Hochschule für Musik und Theater Rostock': 'https://www.hmt-rostock.de',
        'Hochschule für Musik und Theater Weimar': 'https://www.hfm-weimar.de',
        
        # More Fachhochschule with design
        'Hochschule für Gestaltung Pforzheim': 'https://www.hs-pforzheim.de',
        'Hochschule für Gestaltung und Kunst Zürich': 'https://www.zhdk.ch',
        'Hochschule für Gestaltung und Kunst Luzern': 'https://www.hslu.ch',
        
        # International missing
        'Central Saint Martins': 'https://www.arts.ac.uk/csm',
        'Chelsea College of Arts': 'https://www.arts.ac.uk/chelsea',
        'Camberwell College of Arts': 'https://www.arts.ac.uk/camberwell',
        'Wimbledon College of Arts': 'https://www.arts.ac.uk/wimbledon',
        'London College of Communication': 'https://www.arts.ac.uk/lcc',
        'London College of Fashion': 'https://www.arts.ac.uk/fashion',
        
        # More European
        'Gerrit Rietveld Academie': 'https://www.rietveldacademie.nl',
        'ArtEZ University of the Arts': 'https://www.artez.nl',
        'Royal Academy of Fine Arts Antwerp': 'https://www.antwerp.ac.be',
        'La Cambre': 'https://www.lacambre.be',
        'École Nationale Supérieure d\'Architecture': 'https://www.archi.fr',
        
        # US Art Schools
        'Rhode Island School of Design': 'https://www.risd.edu',
        'School of the Art Institute of Chicago': 'https://www.saic.edu',
        'California Institute of the Arts': 'https://www.calarts.edu',
        'Parsons School of Design': 'https://www.newschool.edu/parsons',
        'Pratt Institute': 'https://www.pratt.edu',
        'Cooper Union': 'https://cooper.edu',
        'Art Center College of Design': 'https://www.artcenter.edu',
        'Savannah College of Art and Design': 'https://www.scad.edu',
        'Cranbrook Academy of Art': 'https://cranbrookart.edu',
        'Yale School of Art': 'https://www.art.yale.edu',
        'Columbia University School of the Arts': 'https://arts.columbia.edu',
        'New York University Tisch School of the Arts': 'https://tisch.nyu.edu',
        'UCLA School of the Arts and Architecture': 'https://www.arts.ucla.edu',
        'Carnegie Mellon School of Art': 'https://www.cmu.edu/art',
        'Virginia Commonwealth University School of the Arts': 'https://arts.vcu.edu',
        'Maryland Institute College of Art': 'https://www.mica.edu',
        'Massachusetts College of Art and Design': 'https://www.massart.edu',
        'San Francisco Art Institute': 'https://sfai.edu',
        'Minneapolis College of Art and Design': 'https://mcad.edu',
        'Kansas City Art Institute': 'https://www.kcai.edu',
        'Ringling College of Art and Design': 'https://www.ringling.edu',
        'Otis College of Art and Design': 'https://www.otis.edu',
        'Laguna College of Art and Design': 'https://www.lcad.edu',
        'Academy of Art University': 'https://www.academyart.edu',
        'Art Institute of Chicago': 'https://www.artic.edu',
        'Cleveland Institute of Art': 'https://www.cia.edu',
        'Memphis College of Art': 'https://www.mca.edu',
        'Pacific Northwest College of Art': 'https://www.pnca.edu',
        'School of Visual Arts': 'https://www.sva.edu',
        'Fashion Institute of Technology': 'https://www.fitnyc.edu',
        'The New School Parsons': 'https://www.newschool.edu/parsons',
        
        # Canadian Art Schools
        'Emily Carr University of Art and Design': 'https://www.ecuad.ca',
        'Nova Scotia College of Art and Design': 'https://www.nscad.ca',
        'Ontario College of Art and Design University': 'https://www.ocadu.ca',
        'Alberta College of Art and Design': 'https://www.acad.ca',
        'Concordia University Faculty of Fine Arts': 'https://www.concordia.ca/finearts',
        'University of British Columbia Department of Art History': 'https://www.ahva.ubc.ca',
        'York University School of the Arts': 'https://www.yorku.ca/ampd',
        'University of Toronto Faculty of Music': 'https://www.music.utoronto.ca',
        
        # Australian Art Schools
        'National Art School': 'https://www.nas.edu.au',
        'University of New South Wales Art & Design': 'https://www.artdesign.unsw.edu.au',
        'University of Sydney Sydney College of the Arts': 'https://www.sydney.edu.au/sca',
        'RMIT University School of Art': 'https://www.rmit.edu.au/art',
        'Monash University Faculty of Art, Design and Architecture': 'https://www.monash.edu/mada',
        'Queensland College of Art': 'https://www.griffith.edu.au/qca',
        'University of Melbourne Victorian College of the Arts': 'https://www.vca.unimelb.edu.au',
        'Curtin University School of Design and Art': 'https://www.curtin.edu.au/design',
        
        # Asian Art Schools
        'Tokyo University of the Arts': 'https://www.geidai.ac.jp',
        'Tama Art University': 'https://www.tamabi.ac.jp',
        'Musashino Art University': 'https://www.musabi.ac.jp',
        'Kyoto University of Art and Design': 'https://www.kyoto-art.ac.jp',
        'Osaka University of Arts': 'https://www.osaka-geidai.ac.jp',
        'Hong Kong Academy for Performing Arts': 'https://www.hkapa.edu',
        'Hong Kong Baptist University Academy of Visual Arts': 'https://ava.hkbu.edu.hk',
        'City University of Hong Kong School of Creative Media': 'https://www.scm.cityu.edu.hk',
        'National Taiwan University of Arts': 'https://www.ntua.edu.tw',
        'Taipei National University of the Arts': 'https://www.tnua.edu.tw',
        'Korea National University of Arts': 'https://www.karts.ac.kr',
        'Hongik University College of Fine Arts': 'https://www.hongik.ac.kr',
        'Seoul National University College of Fine Arts': 'https://art.snu.ac.kr',
        'Yonsei University College of Fine Arts': 'https://art.yonsei.ac.kr',
        'Ewha Womans University College of Art & Design': 'https://www.ewha.ac.kr',
        'Singapore LASALLE College of the Arts': 'https://www.lasalle.edu.sg',
        'Nanyang Academy of Fine Arts': 'https://www.nafa.edu.sg',
        'National University of Singapore School of Design and Environment': 'https://www.sde.nus.edu.sg',
        'University of the Philippines College of Fine Arts': 'https://www.upd.edu.ph/cfa',
        'De La Salle College of Saint Benilde School of Design and Arts': 'https://www.benilde.edu.ph',
        'Ateneo de Manila University Fine Arts Program': 'https://www.ateneo.edu',
        'University of Santo Tomas College of Fine Arts and Design': 'https://www.ust.edu.ph',
        'Chulalongkorn University Faculty of Fine and Applied Arts': 'https://www.chula.ac.th',
        'Silpakorn University Faculty of Painting Sculpture and Graphic Arts': 'https://www.su.ac.th',
        'Thammasat University Faculty of Fine and Applied Arts': 'https://www.tu.ac.th',
        'University of Indonesia Faculty of Fine Arts': 'https://www.ui.ac.id',
        'Bandung Institute of Technology Faculty of Art and Design': 'https://www.itb.ac.id',
        'Institut Seni Indonesia Yogyakarta': 'https://www.isi.ac.id',
        'Institut Seni Indonesia Denpasar': 'https://www.isi-dps.ac.id',
        'Institut Seni Indonesia Surakarta': 'https://www.isi-ska.ac.id',
        'Institut Seni Indonesia Padangpanjang': 'https://www.isi-padangpanjang.ac.id',
        'Institut Seni Indonesia Makassar': 'https://www.isi-makassar.ac.id',
        'Institut Seni Indonesia Medan': 'https://www.isi-medan.ac.id',
        'Institut Seni Indonesia Bandung': 'https://www.isbi.ac.id',
        'Institut Seni Indonesia Jakarta': 'https://www.isi-jkt.ac.id',
        'Institut Seni Indonesia Pontianak': 'https://www.isi-pontianak.ac.id',
        'Institut Seni Indonesia Palembang': 'https://www.isi-palembang.ac.id',
        'Institut Seni Indonesia Banjarmasin': 'https://www.isi-banjarmasin.ac.id',
        'Institut Seni Indonesia Manado': 'https://www.isi-manado.ac.id',
        'Institut Seni Indonesia Jayapura': 'https://www.isi-jayapura.ac.id',
        'Institut Seni Indonesia Ambon': 'https://www.isi-ambon.ac.id',
        'Institut Seni Indonesia Mataram': 'https://www.isi-mataram.ac.id',
        'Institut Seni Indonesia Kupang': 'https://www.isi-kupang.ac.id',
        'Institut Seni Indonesia Kendari': 'https://www.isi-kendari.ac.id',
        'Institut Seni Indonesia Palu': 'https://www.isi-palu.ac.id',
        'Institut Seni Indonesia Gorontalo': 'https://www.isi-gorontalo.ac.id',
        'Institut Seni Indonesia Mamuju': 'https://www.isi-mamuju.ac.id',
        'Institut Seni Indonesia Sorong': 'https://www.isi-sorong.ac.id',
        'Institut Seni Indonesia Merauke': 'https://www.isi-merauke.ac.id',
        'Institut Seni Indonesia Fakfak': 'https://www.isi-fakfak.ac.id',
        'Institut Seni Indonesia Kaimana': 'https://www.isi-kaimana.ac.id',
        'Institut Seni Indonesia Raja Ampat': 'https://www.isi-rajaampat.ac.id',
        'Institut Seni Indonesia Biak': 'https://www.isi-biak.ac.id',
        'Institut Seni Indonesia Serui': 'https://www.isi-serui.ac.id',
        'Institut Seni Indonesia Wamena': 'https://www.isi-wamena.ac.id',
        'Institut Seni Indonesia Timika': 'https://www.isi-timika.ac.id',
        'Institut Seni Indonesia Nabire': 'https://www.isi-nabire.ac.id',
        'Institut Seni Indonesia Dogiyai': 'https://www.isi-dogiyai.ac.id',
        'Institut Seni Indonesia Deiyai': 'https://www.isi-deiyai.ac.id',
        'Institut Seni Indonesia Intan Jaya': 'https://www.isi-intanjaya.ac.id',
        'Institut Seni Indonesia Puncak': 'https://www.isi-puncak.ac.id',
        'Institut Seni Indonesia Puncak Jaya': 'https://www.isi-puncakjaya.ac.id',
        'Institut Seni Indonesia Lanny Jaya': 'https://www.isi-lannyjaya.ac.id',
        'Institut Seni Indonesia Nduga': 'https://www.isi-nduga.ac.id',
        'Institut Seni Indonesia Pegunungan Bintang': 'https://www.isi-pegununganbintang.ac.id',
        'Institut Seni Indonesia Yahukimo': 'https://www.isi-yahukimo.ac.id',
        'Institut Seni Indonesia Tolikara': 'https://www.isi-tolikara.ac.id',
        'Institut Seni Indonesia Sarmi': 'https://www.isi-sarmi.ac.id',
        'Institut Seni Indonesia Keerom': 'https://www.isi-keerom.ac.id',
        'Institut Seni Indonesia Waropen': 'https://www.isi-waropen.ac.id',
        'Institut Seni Indonesia Supiori': 'https://www.isi-supiori.ac.id',
        'Institut Seni Indonesia Mamberamo Raya': 'https://www.isi-mamberamoraya.ac.id',
        'Institut Seni Indonesia Mamberamo Tengah': 'https://www.isi-mamberamotengah.ac.id',
        'Institut Seni Indonesia Yalimo': 'https://www.isi-yalimo.ac.id',
        'Institut Seni Indonesia Lembah Baliem': 'https://www.isi-lembahbaliem.ac.id',
        'Institut Seni Indonesia Boven Digoel': 'https://www.isi-bovendigoel.ac.id',
        'Institut Seni Indonesia Mappi': 'https://www.isi-mappi.ac.id',
        'Institut Seni Indonesia Asmat': 'https://www.isi-asmat.ac.id',
        'Institut Seni Indonesia Mimika': 'https://www.isi-mimika.ac.id',
        'Institut Seni Indonesia Paniai': 'https://www.isi-paniai.ac.id',
        'Institut Seni Indonesia Intan Jaya': 'https://www.isi-intanjaya.ac.id',
        'Institut Seni Indonesia Puncak': 'https://www.isi-puncak.ac.id',
        'Institut Seni Indonesia Puncak Jaya': 'https://www.isi-puncakjaya.ac.id',
        'Institut Seni Indonesia Lanny Jaya': 'https://www.isi-lannyjaya.ac.id',
        'Institut Seni Indonesia Nduga': 'https://www.isi-nduga.ac.id',
        'Institut Seni Indonesia Pegunungan Bintang': 'https://www.isi-pegununganbintang.ac.id',
        'Institut Seni Indonesia Yahukimo': 'https://www.isi-yahukimo.ac.id',
        'Institut Seni Indonesia Tolikara': 'https://www.isi-tolikara.ac.id',
        'Institut Seni Indonesia Sarmi': 'https://www.isi-sarmi.ac.id',
        'Institut Seni Indonesia Keerom': 'https://www.isi-keerom.ac.id',
        'Institut Seni Indonesia Waropen': 'https://www.isi-waropen.ac.id',
        'Institut Seni Indonesia Supiori': 'https://www.isi-supiori.ac.id',
        'Institut Seni Indonesia Mamberamo Raya': 'https://www.isi-mamberamoraya.ac.id',
        'Institut Seni Indonesia Mamberamo Tengah': 'https://www.isi-mamberamotengah.ac.id',
        'Institut Seni Indonesia Yalimo': 'https://www.isi-yalimo.ac.id',
        'Institut Seni Indonesia Lembah Baliem': 'https://www.isi-lembahbaliem.ac.id',
        'Institut Seni Indonesia Boven Digoel': 'https://www.isi-bovendigoel.ac.id',
        'Institut Seni Indonesia Mappi': 'https://www.isi-mappi.ac.id',
        'Institut Seni Indonesia Asmat': 'https://www.isi-asmat.ac.id',
        'Institut Seni Indonesia Mimika': 'https://www.isi-mimika.ac.id',
        'Institut Seni Indonesia Paniai': 'https://www.isi-paniai.ac.id',
    }
    
    print(f"\n🔍 CHECKING ADDITIONAL MAJOR ART SCHOOLS...")
    print("=" * 60)
    
    additional_working = []
    additional_broken = []
    
    for uni, url in additional_schools.items():
        print(f"Checking: {uni}")
        result = check_link(url)
        
        if result['working']:
            print(f"✅ {result['status']} - WORKING")
            additional_working.append((uni, url))
        else:
            print(f"❌ BROKEN - {result['error']}")
            additional_broken.append((uni, url, result['error']))
        
        time.sleep(0.3)
    
    print(f"\n📊 ADDITIONAL SCHOOLS RESULTS:")
    print(f"✅ Working: {len(additional_working)}")
    print(f"❌ Broken: {len(additional_broken)}")
    
    # Save comprehensive results
    with open('complete_verification_results.txt', 'w') as f:
        f.write("COMPLETE UNIVERSITY VERIFICATION RESULTS\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"CURRENT UNIVERSITIES:\n")
        f.write(f"Working: {len(working)}\n")
        f.write(f"Broken: {len(broken)}\n\n")
        
        f.write("WORKING CURRENT LINKS:\n")
        for uni, url in working:
            f.write(f"✅ {uni}: {url}\n")
        
        f.write("\nBROKEN CURRENT LINKS:\n")
        for uni, url, error in broken:
            f.write(f"❌ {uni}: {url} ({error})\n")
        
        f.write(f"\n\nADDITIONAL MAJOR ART SCHOOLS:\n")
        f.write(f"Working: {len(additional_working)}\n")
        f.write(f"Broken: {len(additional_broken)}\n\n")
        
        f.write("WORKING ADDITIONAL LINKS:\n")
        for uni, url in additional_working:
            f.write(f"✅ {uni}: {url}\n")
        
        f.write("\nBROKEN ADDITIONAL LINKS:\n")
        for uni, url, error in additional_broken:
            f.write(f"❌ {uni}: {url} ({error})\n")
    
    print(f"\n📄 Complete results saved to: complete_verification_results.txt")

if __name__ == "__main__":
    main()