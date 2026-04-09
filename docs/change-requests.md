# Change Requests

## Aktiv kö

| ID | Titel | Typ | Status | Berörda filer | Risk | Beroenden | Acceptanskriterier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `REV-001` | Konvertera projektet från first-version-styrning till revision mode | D | klar | `AGENTS.md`, `.codex/agents/*`, revisionsdokumenten under `docs/` | medel | inga | first-version-systemet är arkiverat, ny styrning aktiv, QA verifierad |
| `REV-002` | Backfill av canon och aktiv sanningsbok från befintlig baseline | D | öppen | `docs/canon-ledger.md`, `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/clue-chain.md`, kapitel som referens | medel | `REV-001` | canonledgern täcker makro- och kapitelkritiska sanningar utan att luta på first-version-arkiv |
| `REV-003` | Full continuity- och mystery-audit av baseline-manuset | D | öppen | `docs/canon-ledger.md`, `docs/clue-chain.md`, `docs/revision-qa.md`, `docs/chapters/*.md`, `docs/manuscript-full.md` | hog | `REV-001` | motsägelser, revealglapp och kontinuitetsrisker är loggade eller lösta |
| `REV-004` | Känslighetsmärkning och revisionsordning för kapitelkedjan | C | öppen | `docs/chapter-plan.md`, `docs/change-impact-map.md` | låg | `REV-001` | kapitelgrupperna har tydlig revisionskänslighet och rekommenderad arbetsordning |
| `REV-005` | Titel- och paketeringslinje för fortsatt revision | C | öppen | `AGENTS.md`, `docs/decisions.md`, `docs/canon-ledger.md`, `docs/delivery-plan.md`, exportfiler som referens | medel | `REV-001` | aktiv titelstrategi är beslutad utan att tysta motsägelsen mellan working title och nuvarande manuspaket |
| `REV-006` | Slå ihop `03` och `03A` till en enda aktiv öppningssekvens | D | klar | `docs/chapters/03-noah-rask.md`, `docs/chapters/04-glimmingehus-efter-stangning.md`, `docs/chapters/_archive/03a-nedfor-asen.pre-merge.md`, `docs/manuscript-full.md`, `docs/chapter-plan.md`, `docs/structure-grid.md`, `docs/chapter-true-story.md`, `docs/change-impact-map.md`, `docs/revision-log.md`, `docs/revision-qa.md` | hög | `REV-001` | aktiv sekvens läses rent som `03 -> 04`, `03A` är inte längre aktivt kapitel, och inga tidiga clue chain-reveals har flyttats fram |
| `REV-007` | Renodla Glimmingehusledtrådarna kring Stenshuvud | C | klar | `docs/chapters/04-glimmingehus-efter-stangning.md`, `docs/chapters/06-det-som-fadern-ritade.md`, `docs/chapters/11-magasin.md`, `docs/manuscript-full.md`, `docs/change-impact-map.md`, `docs/revision-log.md`, `docs/revision-qa.md` | medel | `REV-006` | Stenshuvud-spåret läses som en kvarvarande Severinnotis på flygfotot som angriparen försökt få med sig men tappat; fotot plockas upp i `04` men läses först i `06`, dammstrecken är borttagna och senare tre-kedja är synkad |
| `REV-008` | Renodla `05`, `05A` och `06` till en tydlig scenkedja | C | klar | `docs/chapters/05-offrets-sista-karta.md`, `docs/chapters/05a-det-som-saknas-i-rummet.md`, `docs/manuscript-full.md`, `docs/change-impact-map.md`, `docs/revision-log.md`, `docs/revision-qa.md` | medel | `REV-007` | `05` bär hela pensionatets bevisarbete, `05A` fungerar som brygga efter pensionatet utan rumsöverlapp, och `06` förblir första fulla åtkomsten till Arvid Malms material samt första explicita `Rutan`-noden |

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
