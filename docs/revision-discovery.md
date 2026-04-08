# Revision Discovery

## Status
Revision mode är etablerat på systemnivå. Detta dokument beskriver vad som i repot tillhör first-version-historik, vad som nu är aktiv baseline och vilka risker eller nästa frågor som följer.

## Repoanalys
- Git-status vid start: ren arbetsyta på `main` med `origin`
- Aktivt manus: `docs/chapters/` med 66 kapitel- och mellanaktsfiler
- Sammanställt manus: `docs/manuscript-full.md`
- Verifierat omfång i nuvarande manusbas: cirka 144 530 ord
- Exportkedja finns via `scripts/build_manuscript.py` och `scripts/build_book_pdf.py`

## First-version-system som nu är arkiverat
- `AGENTS_FIRST_VERSION.md`
- `.codex/agents/fv-orchestrator.md`
- `.codex/agents/fv-structure.md`
- `.codex/agents/fv-mystery.md`
- `.codex/agents/fv-research.md`
- `.codex/agents/fv-scene-language.md`
- `.codex/agents/fv-dialogue-naturalism.md`
- `.codex/agents/fv-qa-editor.md`
- `docs/fv-discovery.md`
- `docs/fv-brief-lock.md`
- `docs/fv-qa-checklist.md`
- `docs/fv-delivery-plan.md`
- `docs/fv-iteration-log.md`
- `docs/fv-chapter-feedback.md`

## Filbeslut för centrala styr- och planfiler

| Fil eller grupp | Beslut | Skäl i revision mode |
| --- | --- | --- |
| `AGENTS_FIRST_VERSION.md` | arkiverad | historiskt first-version-system, ej aktiv styrning |
| `.codex/agents/fv-*.md` | arkiverade | bevarar gamla roller men får inte styra vidare revision |
| `project-instructions.md`, `thriller-style.md`, `style-guide.pdf` | behåll aktiv | fortsatt bindande övergripande kvalitets- och genredirektiv |
| `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/chapter-plan.md`, `docs/clue-chain.md` | behåll aktiv | utgör nuvarande baseline för plot, struktur och mysterium |
| `docs/research-log.md` | skriv om delvis, behåll aktiv | fortsatt aktiv faktabas men tidigare repo-status var felaktig |
| `docs/decisions.md` | skriv om delvis, behåll aktiv | tidigare beslut gäller men behöver kompletteras med revisionsbeslut |
| `docs/blockers.md` | skriv om delvis, behåll aktiv | ska spegla aktiva blockerare och risker i revision mode |
| `docs/chapter-true-story.md` | behåll aktiv | direkt användbar i revision mode men ofullständig och därför markerad som partiell |
| `docs/fv-discovery.md`, `docs/fv-brief-lock.md`, `docs/fv-qa-checklist.md`, `docs/fv-delivery-plan.md`, `docs/fv-iteration-log.md`, `docs/fv-chapter-feedback.md` | arkiverade | beskriver first-version-resan eller redan avklarad leverans, inte aktiv revision |
| `docs/change-requests.md`, `docs/change-impact-map.md`, `docs/canon-ledger.md`, `docs/revision-log.md`, `docs/revision-qa.md`, `docs/revision-workflow.md` | nya aktiva revisionsdokument | behövs för spårbar ändringsstyrning, konsekvenskontroll och canonbevakning |

## Stabil baseline
- Romanens nuvarande A/B-motor, Ormledens faktiska natur, Helena Wredes plan och den övergripande kapitelkedjan är väl dokumenterade i story core, struktur, chapter plan och clue chain.
- Leveransartefakter finns redan: kapitelmapp, sammanslaget manus, PDF och bokutgåva.
- Researchgrunden för huvudplatserna är etablerad nog för vidare revisioner.

## Provisoriska eller svaga delar
- Titeln är inte låst mellan styrdokument och nuvarande manus- och exportkedja.
- `docs/chapter-true-story.md` täcker bara en liten del av kapitelkedjan och bör byggas ut inför större struktur- eller plotrevisioner.
- First-version-dokumenten bar flera "allt klart"-markeringar som inte kan fungera som aktiv revisionsstyrning.
- Kapitelfloran med många mellanaktsfiler och återanvända suffix är hanterbar som baseline men bör kartläggas noga vid större strukturändringar.

## Absolut nödvändiga frågor till användaren just nu
Inga blockerande frågor krävs för att etablera revision mode.

## Frågor som sannolikt blir viktiga i nästa steg
- Vilken revisionsklass ska prioriteras först: språkputs, struktur, handling, karaktärer, mysterium, slut eller titel/paketering?
- Vilka delar av nuvarande bok betraktas som mest låsta av användaren?
- Hur djup ska nästa revisionsvåg vara: lätt puts, kraftig omarbetning eller djup omstrukturering?

## Nästa rimliga steg
- Använd CR-001 för att låsa nästa revisionsspår.
- Använd CR-002 för att bygga ut canon- och true-story-underlaget inför större ändringar.
- Använd CR-003 för att avgöra titel- och paketeringslinje innan senare releasepolish.
