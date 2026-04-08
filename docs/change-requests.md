# Change Requests

## Aktiv kö

| ID | Titel | Typ | Status | Berörda filer | Risk | Beroenden | Acceptanskriterier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `REV-001` | Konvertera projektet från first-version-styrning till revision mode | D | klar | `AGENTS.md`, `.codex/agents/*`, revisionsdokumenten under `docs/` | medel | inga | first-version-systemet är arkiverat, ny styrning aktiv, QA verifierad |
| `REV-002` | Backfill av canon och aktiv sanningsbok från befintlig baseline | D | öppen | `docs/canon-ledger.md`, `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/clue-chain.md`, kapitel som referens | medel | `REV-001` | canonledgern täcker makro- och kapitelkritiska sanningar utan att luta på first-version-arkiv |
| `REV-003` | Full continuity- och mystery-audit av baseline-manuset | D | öppen | `docs/canon-ledger.md`, `docs/clue-chain.md`, `docs/revision-qa.md`, `docs/chapters/*.md`, `docs/manuscript-full.md` | hog | `REV-001` | motsägelser, revealglapp och kontinuitetsrisker är loggade eller lösta |
| `REV-004` | Känslighetsmärkning och revisionsordning för kapitelkedjan | C | öppen | `docs/chapter-plan.md`, `docs/change-impact-map.md` | låg | `REV-001` | kapitelgrupperna har tydlig revisionskänslighet och rekommenderad arbetsordning |
| `REV-005` | Titel- och paketeringslinje för fortsatt revision | C | öppen | `AGENTS.md`, `docs/decisions.md`, `docs/canon-ledger.md`, `docs/delivery-plan.md`, exportfiler som referens | medel | `REV-001` | aktiv titelstrategi är beslutad utan att tysta motsägelsen mellan working title och nuvarande manuspaket |

## Mall för nya ärenden

### `REV-XXX` Kort titel
- Mål:
- Typ:
- Status:
- Berörda filer:
- Påverkade kapitel:
- Risker:
- Beroenden:
- Involverade agenter:
- Acceptanskriterier:
- Noteringar:
