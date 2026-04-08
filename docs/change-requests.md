# Change Requests

## Användning
Varje icke-trivial revision får ett ID i formatet `CR-XXX`.

Minimifält per ärende:
- mål
- revisionsklass Typ A-E
- berörda filer
- risker
- beroenden
- status
- acceptanskriterier

## Statusnyckel
- `förslag`
- `planerad`
- `pågår`
- `klar`
- `arkiverad`

## CR-000 Revision mode-konvertering
- Status: klar
- Typ: E
- Mål: Arkivera first-version-styrningen, etablera aktiv revisionsstyrning och skapa spårbara kontrollfiler för fortsatt arbete.
- Berörda filer: `AGENTS.md`, `AGENTS_FIRST_VERSION.md`, `.codex/agents/*`, `docs/fv-*.md`, `docs/revision-*.md`, `docs/change-requests.md`, `docs/change-impact-map.md`, `docs/canon-ledger.md`, `docs/decisions.md`, `docs/blockers.md`, `docs/research-log.md`
- Risker: Otydlig aktiv styrning, fortsatt first-version-beteende, tyst glidning mellan manus och stöddokument.
- Beroenden: Genomgång av befintlig repo- och dokumentstruktur.
- Acceptanskriterier:
  - first-version-systemet är tydligt arkiverat
  - ny `AGENTS.md` är aktiv och revisionsspecifik
  - relevanta revisionsagenter finns
  - change request, impact map, canon ledger, revision log och revision QA finns
  - skillnaden mellan språkputs och plotrevision är explicit dokumenterad

## CR-001 Lås revisionens prioriteringsordning
- Status: förslag
- Typ: D
- Mål: Få en explicit prioritering för nästa större revisionsvåg: språk, struktur, handling, karaktär, mysterium, slut eller titel/paketering.
- Berörda filer: `docs/change-requests.md`, `docs/change-impact-map.md`, senare relevanta styr- och kapitel­filer
- Risker: Systemet finns men nästa arbetsrunda saknar prioriterad riktning.
- Beroenden: Ingen blockerande beroende, men användarinput kan bli relevant när själva revisionsordningen ska låsas.
- Acceptanskriterier:
  - nästa revisionsspår är valt
  - scope och ambitionsnivå är dokumenterade
  - följdverkningar kan kartläggas innan textändring

## CR-002 Bygg ut canon- och true-story-täckning
- Status: förslag
- Typ: D
- Mål: Få mer komplett kapitelvis canon- och sanningsdokumentation för att säkra senare struktur- och plotändringar.
- Berörda filer: `docs/canon-ledger.md`, `docs/chapter-true-story.md`, vid behov `docs/change-impact-map.md`, `docs/revision-log.md`
- Risker: Dolda motsägelser och sämre spårbarhet vid senare omskrivningar.
- Beroenden: Revision mode måste vara etablerat.
- Acceptanskriterier:
  - centrala kapitelkedjor har sammanhängande true-story-stöd
  - canonluckor som påverkar större revisioner är täckta

## CR-003 Avgör titel- och paketeringslinje
- Status: förslag
- Typ: C
- Mål: Låsa om projektet ska använda `The Serpent of Österlen`, `Ormleden: En Österlenthriller` eller en annan kontrollerad titel i styrning och leveranser.
- Berörda filer: `project-instructions.md`, `docs/manuscript-full.md`, `scripts/build_book_pdf.py`, exportfiler och omslagsmaterial
- Risker: Otydlig intern och extern identitet mellan manus, omslag och styrfiler.
- Beroenden: Ingen blockerare för revision mode, men beslut krävs före slutlig releasepolish.
- Acceptanskriterier:
  - en titel är uttryckligt låst
  - manus, PDF och omslagskedja är synkade
