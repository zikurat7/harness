# Sources

Where vacancy listings come from. `kb-sync` reads this file to know what to fetch.

## How listings get in

1. **Career pages** (table below): `kb-sync` fetches each public careers page and saves junior-relevant software roles to `context/vacancies/`.
2. **Inbox**: you drop links or pasted text into `context/inbox/` (see its README). `kb-sync` turns each item into a vacancy file. Use this for LinkedIn, Indeed and any other board.

## Blocked / not automated (tested 2026-11-12)
- Indeed.nl: HTTP 403
- Nationale Vacaturebank: fetch refused
- Werkzoeken.nl: loads but ignores location and keyword filters, returns unrelated national results
- LinkedIn: login required, scraping restricted. Use the inbox.
- Search engines (DuckDuckGo): bot check

## Company career pages (tracked)

Found by a research pass on 2026-11-12. "Seen" means what the page showed that day, not a promise.

| Company | Town | Careers URL | Seen on 2026-11-12 | English |
|---|---|---|---|---|
| ilionx | Zwolle | https://werkenbij.ilionx.com/vacatures | Junior Data & AI Consultant (Zwolle); .NET, Java, AI developer roles | partly |
| Fellowmind | Zwolle, Deventer | https://career.fellowmind.nl/jobs | No junior label; "New Fellow Program" filter exists | no |
| Zonneplan | Zwolle | https://careers.zonneplan.nl/vacatures | Only a medior Laravel role | no |
| Univé | Zwolle | https://www.vacaturesbijunive.nl/ | No junior IT; some listings hidden behind loading | no |
| Enexis | Zwolle office | https://werkenbij.enexis.nl/vacatures?workArea=it | Graduate internships | partly |
| Achmea | Apeldoorn | https://www.werkenbijachmea.nl/vacatures?f=22 | IT Management Trainee, internships | no |
| Thinkwise | Apeldoorn | https://werkenbijthinkwise.nl/ | Nothing junior; /students section not yet read | unclear |
| Kadaster | Apeldoorn | https://www.werkenbijhetkadaster.nl/vacatures/ | Medior and senior IT only | no |
| Vitens | Zwolle | https://www.werkenbijvitens.nl/go/Digitalisering/8974701/ | Traineeship Hbo/Wo page; no junior dev | no |
| Baker Tilly | Zwolle | https://www.werkenbijbakertilly.nl/vacatures?f=52 | Junior Consultant IT Advisory (advisory, not coding) | no |

## Not tracked yet (listings load dynamically, unreliable to read)
Topicus (Deventer, English OK), Saxion, Windesheim, Belastingdienst, Sioux, SmartDocuments.

## Leads without a verified company (use the inbox once you find the listing)
- "Junior Software Engineer Robotica", Zwolle
- "Junior Software Engineer Industriële Automatisering", Zwolle
- a similar junior software role in Steenwijk

## Search terms (for manual searching on boards)
- junior software developer, junior software engineer, junior developer, starter software, trainee developer
- Dutch: junior softwareontwikkelaar, medewerker software development, starter ICT

## Area (within 50 km of Zwolle)
Zwolle, Kampen, Meppel, Deventer, Apeldoorn, Hardenberg, Raalte, Heerde, Hasselt, Steenwijk, Dalfsen, Ommen
