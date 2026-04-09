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
