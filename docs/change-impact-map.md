# Change Impact Map

## Generella regler
- Typ A påverkar normalt bara målfilen och revisionslogg/QA.
- Typ B kan påverka målfilen plus lokala grannkapitel och ska därför jämföras mot närliggande canon.
- Typ C ska alltid kontrollera chapter plan, canon ledger och närliggande revealpunkter.
- Typ D och Typ E ska alltid kontrollera story core, synopsis, structure grid, clue chain, canon ledger, chapter plan och relevanta kapitel.
- Vid upprepade mellanaktsbeteckningar ska fullständigt filnamn användas i stället för etikett som `16a`.

## Aktiva impact-poster

| CR | Primär ändring | Måste inspekteras eller uppdateras | Kapitelrisk | Obligatoriska agenter |
| --- | --- | --- | --- | --- |
| `REV-001` | Styrsystemskonvertering | `AGENTS.md`, `.codex/agents/`, revisionsdokumenten, `docs/blockers.md`, `docs/research-log.md`, `docs/decisions.md` | inga kapiteländringar | `revision-orchestrator`, `qa-release` |
| `REV-002` | Canonbackfill | `docs/canon-ledger.md`, `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/clue-chain.md`, `docs/chapter-plan.md`, `docs/chapter-true-story.md` | hela manuskedjan som läsbas, inga textändringar krävs i startläget | `continuity-canon`, `mystery-clue-integrity`, `revision-orchestrator` |
| `REV-003` | Continuity- och mystery-audit | `docs/canon-ledger.md`, `docs/clue-chain.md`, `docs/revision-qa.md`, `docs/change-requests.md`, `docs/chapter-true-story.md` | öppning, midpoint, senreveal och finalkedja är högst känsliga | `continuity-canon`, `mystery-clue-integrity`, `qa-release` |
| `REV-004` | Kapitelkänslighet och revisionsordning | `docs/chapter-plan.md`, `docs/change-requests.md` | inga textändringar, men skyddade kapitel ska markeras tydligt | `revision-orchestrator`, `continuity-canon` |
| `REV-005` | Titel- och paketeringslinje | `AGENTS.md`, `docs/decisions.md`, `docs/canon-ledger.md`, `docs/delivery-plan.md`, omslag och exportfiler som referens | inga kapiteländringar i startläget, men påverkar paketets yttre identitet | `revision-orchestrator`, `qa-release` |
| `REV-006` | Sammanfogning av `03` och tidigare `03A` | `docs/manuscript-full.md`, `docs/chapter-plan.md`, `docs/structure-grid.md`, `docs/chapter-true-story.md`, `docs/revision-log.md`, `docs/revision-qa.md`, arkivplats för tidigare `03A` | öppningsmotor med hög reveal- och kontinuitetskänslighet; övergången till `04` måste läsas utan omtag och utan för tidig exponering av `Rutan`-, Torkel- eller sjömärkesspår | `revision-orchestrator`, `plot-structure-revision`, `continuity-canon`, `mystery-clue-integrity`, `qa-release` |
| `REV-007` | Ledtrådsbärare i `04` flyttas från vägg- och dammspår till en kvarlämnad Severinnotis på flygfotot över Stenshuvud som angriparen försökt få med sig; själva avläsningen fördröjs till `06`; senare tre-referens i `11` synkas | `docs/manuscript-full.md`, `docs/change-requests.md`, `docs/revision-log.md`, `docs/revision-qa.md`; kontrollera `docs/canon-ledger.md` och närliggande revealpunkter i `05`, `06`, `11`, `14` och `15` utan uppdatering om de fortfarande läser rent | öppningsmotor med lokal mysterykänslighet; Stenshuvud måste fortsatt öppnas tidigt utan att senare payoff eller antagonisternas logik förskjuts | `plot-structure-revision`, `continuity-canon`, `mystery-clue-integrity`, `qa-release` |
| `REV-008` | Pensionatssekvensen renodlas så att `05` äger fynden, `05A` äger bryggan mot hemkomsten och `06` fortsatt är första fulla åtkomsten till Arvid Malms material | `docs/chapters/05-offrets-sista-karta.md`, `docs/chapters/05a-det-som-saknas-i-rummet.md`, `docs/manuscript-full.md`, `docs/change-requests.md`, `docs/revision-log.md`, `docs/revision-qa.md`; kontrollera `docs/chapter-plan.md`, `docs/canon-ledger.md` och revealpunkterna i `05`, `05A` och `06` utan uppdatering om de fortfarande läser rent | öppningsmotor med lokal reveal- och övergångskänslighet; `05A` får inte läsa som alternativ version av pensionsrummet och `Rutan` får inte namnges explicit före `06` | `plot-structure-revision`, `continuity-canon`, `mystery-clue-integrity`, `qa-release` |
