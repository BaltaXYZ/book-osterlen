# Revision Mode Transition

## Baslinestatus vid konvertering
- Repo: git-repo med `origin` och aktiv arbetsbranch `codex/revision-mode-transition`.
- Manusbaseline: `docs/chapters/*.md` plus `docs/manuscript-full.md`.
- Verifierat omfång vid genomgång: cirka 144 530 ord i sammanslaget manus och kapitelmapp.
- Exportbaseline finns redan: `docs/manuscript.pdf` och `docs/book-edition.pdf`.
- Aktiv styrning före konvertering var fortfarande first-version-orienterad trots att manusbaseline redan existerade.

## Det som uttryckligen tillhörde first-version-systemet
- `AGENTS.md` och agenterna i `.codex/agents/` styrde fortfarande mot discovery, strukturbygge, manusproduktion och slutleverans.
- `docs/discovery.md`, `docs/brief-lock.md`, tidigare `docs/chapter-plan.md`, `docs/iteration-log.md`, `docs/qa-checklist.md`, `docs/delivery-plan.md` och `docs/chapter-feedback.md` fungerade som first-version-planering eller first-version-historik.
- flera dokument signalerade felaktigt att projektet inte var ett git-repo eller att arbetet redan var slutverifierat

## Filbeslut

| Fil eller grupp | Beslut | Revision mode-status | Kommentar |
| --- | --- | --- | --- |
| `AGENTS.md` | arkiverad som `AGENTS_FIRST_VERSION.md` och ersatt | historik + ny aktiv fil | first-version-styrningen får inte längre vara aktiv |
| `.codex/agents/orchestrator.md` m.fl. | arkiverade som `.codex/agents/fv-*.md` | historik | gamla agentroller bevaras men är uttryckligen inaktiva |
| `project-instructions.md` | behåll aktiv | bindande | fortsatt överordnat projektdokument |
| `thriller-style.md` | behåll aktiv | bindande | fortsatt överordnat genredokument |
| `style-guide.pdf` | behåll aktiv | bindande | fortsatt överordnat strukturstöd |
| `docs/fv-discovery.md` | arkiverad | historik | discovery för first-version, inte aktiv revisionsdiscovery |
| `docs/fv-brief-lock.md` | arkiverad | historik | ersatt i praktiken av baseline- och canonstyrning |
| `docs/story-core.md` | behåll aktiv och märkt som baseline | aktiv | styr storykärnan men får bara ändras via change request vid större påverkan |
| `docs/synopsis.md` | behåll aktiv och märkt som baseline | aktiv | sammanfattar nuvarande baseline, inte fri designyta |
| `docs/structure-grid.md` | behåll aktiv och märkt som baseline | aktiv | används i impact- och strukturkontroll |
| `docs/clue-chain.md` | behåll aktiv och märkt som baseline | aktiv | används i mystery- och revealkontroll |
| `docs/fv-chapter-plan.md` | arkiverad | historik | ersatt av ny revisionskarta i `docs/chapter-plan.md` |
| `docs/chapter-true-story.md` | behåll aktiv men markera som partiell | aktiv | fungerar som växande sanningsstöd där ifylld, men ersätts inte som helhet ännu |
| `docs/research-log.md` | omskriven för revision mode | aktiv | felaktig git-status korrigerad, fortsatt faktastöd |
| `docs/decisions.md` | behåll aktiv och utökad | aktiv | tidigare beslut bevaras, nya revisionsbeslut läggs till |
| `docs/blockers.md` | omskriven för revision mode | aktiv | används för riktiga blockerare och risker under revision |
| `docs/fv-iteration-log.md` | arkiverad | historik | ersatt av `docs/revision-log.md` |
| `docs/fv-qa-checklist.md` | arkiverad | historik | ersatt av `docs/revision-qa.md` |
| `docs/fv-delivery-plan.md` | arkiverad | historik | ersatt av aktiv revisionsleveransplan |
| `docs/fv-chapter-feedback.md` | arkiverad | historik | tidigare feedback bevaras men styr inte aktivt revisionsflöde |
| `docs/manuscript-full.md` och `docs/chapters/*.md` | behåll aktiv | baseline | behandlas som revisionsunderlag, inte råmaterial för nygenerering |

## Nya aktiva revisionsfiler
- `docs/revision-discovery.md`
- `docs/revision-workflow.md`
- `docs/change-requests.md`
- `docs/change-impact-map.md`
- `docs/canon-ledger.md`
- `docs/revision-log.md`
- `docs/revision-qa.md`
- ny `docs/chapter-plan.md`
- ny `docs/delivery-plan.md`

## Verifiering
- [x] first-version-systemet är tydligt arkiverat
- [x] ny aktiv `AGENTS.md` är revisionsspecifik
- [x] nya revisionsagenter finns under `.codex/agents/`
- [x] change request-system finns
- [x] impact mapping finns
- [x] canon ledger finns
- [x] revisionslogg finns
- [x] revisions-QA finns
- [x] skillnaden mellan språkputs och plotrevision är dokumenterad
- [x] projektets styrning leder nu mot säker revision snarare än nygenerering

## Beslut
**Revision mode etablerat.**
