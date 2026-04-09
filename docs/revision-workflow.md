# Revision Workflow

## Grundregel
Revision mode utgår från att manus och stöddokument redan finns. Arbetet börjar därför med klassificering, påverkan och dokumentstyrning, inte med fri omskrivning i kapiteltext.

## Standardflöde
1. Klassificera ändringen som Typ A-E.
2. Registrera eller uppdatera change request i `docs/change-requests.md`.
3. Kartlägg påverkan i `docs/change-impact-map.md`.
4. Uppdatera relevanta baseline-dokument.
5. Revidera berörda kapitel eller scener.
6. Kör continuity-, mystery-, research- och QA-kontroll på rätt nivå.
7. Uppdatera `docs/revision-log.md`, `docs/revision-qa.md` och vid behov leveransfilerna.
8. Låt `revision-orchestrator` inhämta explicit status från `git-gate` innan revisionen markeras klar för commit- eller pushhandoff.

## Typ A: språkputs / line edit
Före ändring:
- bekräfta att ändringen verkligen inte påverkar storyfakta eller scenfunktion

Måste uppdateras:
- normalt ingen stöddokumentation utöver revisionslogg och QA

Agenter:
- `language-polish`
- `qa-release`

Klar när:
- språket är starkare
- inga storyfakta, motiv eller reveals har flyttats

## Typ B: scenrevision utan ändrad storyfunktion
Före ändring:
- definiera vilken scenfunktion som ska bevaras

Måste uppdateras:
- revisionslogg och QA
- impact map om flera filer påverkas

Agenter:
- `scene-line-edit`
- `continuity-canon`
- `qa-release`

Klar när:
- scenen är bättre
- dess funktion och informationsinnehåll är intakta

## Typ C: kapitelrevision med lokal storypåverkan
Före ändring:
- skapa change request
- lista lokala beroenden och vilka andra kapitel som måste jämföras

Måste uppdateras:
- berörda delar av chapter plan
- canon ledger vid faktapåverkan
- relevanta storydokument om ändringen spiller över

Agenter:
- `plot-structure-revision`
- `scene-line-edit`
- `continuity-canon`
- `mystery-clue-integrity` vid mysterypåverkan
- `qa-release`

Klar när:
- lokala följdeffekter är lösta
- stöddokument och kapitel pekar åt samma håll

## Typ D: strukturändring med flera beroenden
Före ändring:
- formellt change request är obligatoriskt
- impact map ska visa påverkade kapitel, stöddokument och risker

Måste uppdateras före kapiteltext:
- `docs/story-core.md` vid kärnpåverkan
- `docs/synopsis.md`
- `docs/structure-grid.md`
- `docs/chapter-plan.md`
- `docs/clue-chain.md` om mysterykedjan påverkas
- `docs/canon-ledger.md` vid canonpåverkan

Agenter:
- `revision-orchestrator`
- `plot-structure-revision`
- `continuity-canon`
- `mystery-clue-integrity`
- `research-fact-check` vid verklighetsanknuten påverkan
- `qa-release`

Klar när:
- ändringen fungerar både framåt och bakåt
- följdkapitel är reviderade eller uttryckligen loggade som öppna

## Typ E: större plotändring
Före ändring:
- samma krav som Typ D, men med fullständig konsekvenskedja
- ändringen får inte starta i kapiteltext

Måste uppdateras före kapiteltext:
- samtliga berörda baselinedokument
- canon ledger
- change impact map

Agenter:
- hela revisionsteamet vid behov

Klar när:
- antagonistlogik, reveal-ordning, tidslinje och clue chain är omtestade
- QA bedömer revisionen som större plotändring klar, inte bara textmässigt bättre

## Särskilda regler
- Skyddade kapitel `01` och `02` får inte ändras utan användartillstånd.
- Om en tänkt Typ A eller Typ B visar sig ändra storyfakta ska den uppgraderas innan mer text revideras.
- Om fakta är osäkra ska osäkerheten dokumenteras i `docs/research-log.md` innan ändringen betraktas som klar.
- `git-gate` ska inte bara svara på fråga utan också självmant signalera när ett revisionspaket tydligt nått `redo att committa` eller `redo att pusha`.
- `revision-orchestrator` får inte lämna en revision vidare till gitbeslut utan en aktuell `git-gate`-status i standardformatet.
