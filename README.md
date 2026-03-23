# Art Position Finder

Automated weekly search for **PhD**, **Künstlerische Mitarbeit**, and **Wissenschaftliche Mitarbeit** positions in artistic research, art theory, aesthetics, media art, AI in art, media philosophy, and related fields.

**Primary focus:** Germany · Austria · Switzerland · Netherlands · Belgium

---

## How it works

This is a **Claude-native system** — no web scraping scripts, no fragile HTML parsers.

Every **Monday at 08:06 AM**, a scheduled task runs Claude directly. Claude executes 20 targeted search queries across:

- arthist.net, academics.de (via ZEIT), kultweet.de, hochschul-job.de, kimeta.de
- Direct university Stellenausschreibungen pages (UdK, HFBK, HGB, Bauhaus Weimar, Kunstakademie Düsseldorf, AdBK München, HfBK Dresden, Weißensee, etc.)
- Normal university departments (Medienwissenschaft, Kunstgeschichte, Medienphilosophie)
- NWO / FWO / SNSF / DFG-funded PhD project calls
- National job portals: academictransfer.com (NL/BE), academicpositions.com

Results are deduplicated, classified, and compiled into a **standalone HTML report** with filterable cards.

---

## Position types tracked

| Type | Description |
|---|---|
| **PhD / Promotion** | Doctoral positions, Promotionsstellen, prae-doc, funded PhD projects, practice-based doctoral programmes |
| **Künstlerische Mitarbeit** | Practice-based artistic staff positions at Kunsthochschulen (EG 13 TV-L/H) |
| **Wissenschaftliche Mitarbeit** | Research/academic staff positions in art theory, aesthetics, media studies, art history |

---

## Subject priorities

- Media art · Medienkunst
- AI in art · computational art · code-based art
- Media philosophy · Medienphilosophie · philosophy of technology
- Media art history · digital art history
- Interface cultures · time-based media
- Artistic research · art theory · visual studies · Bildwissenschaft

---

## Reports

All reports are saved in `reports/`:

| File | Description |
|---|---|
| `index.html` | Archive of all weekly reports |
| `report_YYYY-MM-DD.html` | Weekly report — open in any browser |
| `report_template.html` | Template used to generate each report (do not delete) |

Open any `.html` file in a browser. Reports are fully self-contained — no server needed.

**Filter options in each report:** All · PhD/Promotion · Künstlerische Mitarbeit · Wissenschaftliche Mitarbeit · Berlin · Hamburg · Other Cities

---

## Email delivery

Each Monday run sends a digest email to **8765498@gmail.com** via Gmail (Chrome automation).
Subject format: `🎨 Art Positions — [date] — [N] positions`

If Chrome/Gmail is unavailable at run time, the email is saved as `reports/email_draft_YYYY-MM-DD.txt`.

---

## Institutions monitored

### Germany
UdK Berlin · HFBK Hamburg · HfK Bremen · HGB Leipzig · Bauhaus-Universität Weimar · Kunstakademie Düsseldorf · AdBK München · HfBK Dresden · HBK Braunschweig · Kunsthochschule Kassel · Weißensee Kunsthochschule Berlin · Burg Giebichenstein Halle · Folkwang Universität der Künste · Muthesius Kunsthochschule · KHM Köln · Merz Akademie Stuttgart · HfG Offenbach · Städelschule Frankfurt · ZKM Karlsruhe · External institutions (museums, Kunsthallen, foundations)

### Austria
Akademie der Bildenden Künste Wien · Universität für angewandte Kunst Wien · Kunstuniversität Linz (Interface Cultures)

### Switzerland
ZHdK / IFCAR Zürich · HGK/FHNW Basel · HEAD Geneva · ECAL Lausanne

### Netherlands
Gerrit Rietveld Academie / Sandberg Instituut (Creator Doctus) · ArtEZ · HKU Utrecht · University of Amsterdam · NWO-funded art research projects

### Belgium
KASK & Conservatorium Ghent · LUCA School of Arts · ARIA (University of Antwerp) · ERG Brussels · FWO-funded positions

---

## Scheduled task

Managed via Claude Cowork → Scheduled section.
Task ID: `art-positions-weekly`
Schedule: Every Monday 08:06 AM (local time)

To run manually: open the Scheduled section in the sidebar and click **Run now**.
