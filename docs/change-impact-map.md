# Change Impact Map

## Syfte
Kartlägga vilka artefakter som måste ses över när en viss typ av revision öppnas.

## Standardmatris per revisionstyp

| Revisionstyp | Minsta påverkade artefakter | Måste kontrolleras extra |
| --- | --- | --- |
| Typ A | kapiteltext, `docs/change-requests.md`, `docs/revision-log.md`, `docs/revision-qa.md` | att ingen canon-, clue- eller revealglidning smugit in |
| Typ B | kapiteltext, `docs/change-requests.md`, `docs/revision-log.md`, `docs/revision-qa.md`, vid behov `docs/chapter-true-story.md` | scenfunktion, POV, lokal kontinuitet |
| Typ C | kapiteltext, `docs/chapter-true-story.md`, vid behov `docs/canon-ledger.md`, `docs/clue-chain.md`, logg och QA | lokal storypåverkan, relationer, clue-timing |
| Typ D | `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/chapter-plan.md`, vid behov `docs/clue-chain.md`, `docs/canon-ledger.md`, `docs/research-log.md`, därefter kapitel | revealordning, beroendekedjor, kapitelomläggning |
| Typ E | alla relevanta styrdokument, canon, clue chain, research, decisions, blockers, kapitel och exportkedja vid behov | storysanning, mysteriemotor, tidslinje, stakes, publikationseffekter |

## Högpåverkande beroenden i just detta projekt
- Ändringar i Dokument A/B påverkar minst `docs/story-core.md`, `docs/structure-grid.md`, `docs/chapter-plan.md`, `docs/clue-chain.md`, `docs/canon-ledger.md` och flera senkapitel.
- Ändringar i Helena Wredes plan påverkar stakes, revealdisciplin, `Olofslinjen`, canon och finalkapitel.
- Ändringar i Maja/Noah-dynamiken påverkar både kapiteltext, true-story, struktur och klimaxval.
- Ändringar i Forn Sed-spåret kräver både mystery- och researchkontroll för att inte bryta realism eller etik.
- Ändringar i titel eller paketering påverkar både styrdokument, manus, byggscript och exportfiler.

## CR-000 Revision mode-konvertering
- Typ: E
- Påverkade filer:
  - `AGENTS_FIRST_VERSION.md`
  - `.codex/agents/fv-*.md`
  - `docs/fv-*.md`
  - ny aktiv `AGENTS.md`
  - nya revisionsagenter under `.codex/agents/`
  - `docs/revision-workflow.md`
  - `docs/change-requests.md`
  - `docs/change-impact-map.md`
  - `docs/canon-ledger.md`
  - `docs/revision-log.md`
  - `docs/revision-qa.md`
  - `docs/revision-discovery.md`
  - `docs/decisions.md`
  - `docs/blockers.md`
  - `docs/research-log.md`
- Särskild kontroll:
  - att first-version-material är begripligt men inaktivt
  - att aktiv styrning inte längre pekar mot discovery-först eller första fullversion som arbetsläge
  - att skillnaden mellan språkputs och plotrevision är explicit

## Nästa sannolika impact-ärenden
- CR-001: påverkar prioritetsordning och därmed vilket revisionsspår som öppnas först
- CR-002: påverkar canonunderlag men inte nödvändigtvis kapiteltext direkt
- CR-003: påverkar styrning, manusrubriker, byggscript och export
