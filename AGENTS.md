# AGENTS.md

## Projektläge
Projektet är nu i **revision mode**. Uppdraget är att säkert, spårbart och konsekvenskontrollerat vidareutveckla ett redan existerande manusprojekt, inte att generera romanen från noll.

Baseline tills vidare:
- `docs/chapters/*.md`
- `docs/manuscript-full.md`
- `docs/story-core.md`
- `docs/synopsis.md`
- `docs/structure-grid.md`
- `docs/chapter-plan.md`
- `docs/clue-chain.md`
- `docs/chapter-true-story.md`
- `docs/research-log.md`
- `docs/canon-ledger.md`

First-version-systemet är arkiverat i `AGENTS_FIRST_VERSION.md`, `.codex/agents/fv-*.md` och `docs/fv-*.md`.
Titelfrågan är inte tyst löst i detta läge. Motsägelsen mellan **The Serpent of Österlen** och **Ormleden: En Österlenthriller** är ett spårat revisionsärende, inte fri lokal justering.

## Hårda revisionsregler
- Arbeta på svenska.
- Använd tät tredje person som huvudform om inte ett uttryckligt change request säger annat.
- Romanen ska fortsatt vara en högdriven konspirationsthriller / historisk thriller / mysteriethriller.
- Österlen ska fortsatt fungera som narrativ maskin, inte som kuliss.
- Fornnordiskt material ska fortsatt behandlas realistiskt och researchförankrat.
- Nutida Forn Sed eller annan modern religiös praktik får inte sensationaliseras eller användas slarvigt som skräckkuliss.
- `project-instructions.md`, `thriller-style.md` och `style-guide.pdf` är fortsatt bindande styrdokument.
- Ingen revision får kallas klar om följdeffekter, canon, reveal-logik, researchbehov och aktuell QA-nivå inte är verifierade i dokumentation.

## Baselineprincip
- Befintligt manus och existerande stöddokument är baseline tills de uttryckligen revideras.
- Baseline får inte behandlas som fri designyta. Varje större avvikelse måste bära ett formellt ändringsärende.
- Plotändringar ska först uppdatera relevanta stöddokument och därefter kapiteltext.
- Språkputs får inte i smyg ändra fakta, motiv, reveal-ordning, POV-funktion eller scenfunktion.
- Continuity, canon och mystery-integritet ska kontrolleras efter varje revision som rör mer än ren språkputs.

## Revisionsklassificering
- Typ A: språkputs / language polish. Ingen ny storyinformation, ingen ändrad revealordning, inga ändrade motiv.
- Typ B: scenrevision utan ändrad storyfunktion. Förbättrar rytm, scenklarhet, dialog eller tryck men bevarar scenens faktiska funktion.
- Typ C: kapitelrevision med lokal storypåverkan. Kräver lokal impact-analys och uppdatering av berörda stöddokument.
- Typ D: strukturändring med flera beroenden. Kräver change request, impact map, uppdaterade storydokument före kapiteltext och efterföljande canon- och mystery-kontroll.
- Typ E: större plotändring med påverkan på mysterium, reveal-ordning, antagonistlogik, tidslinje eller canon. Kräver full revisionskedja och får inte börja i kapiteltext.

## Obligatorisk konsekvensprincip
Ingen större ändring av handling, motiv, tidslinje, antagonistlogik, reveal-ordning, ledtrådskedja eller karaktärsbåge får genomföras direkt i kapiteltext som första steg.

För Typ D och Typ E gäller alltid:
1. registrera change request i `docs/change-requests.md`
2. kartlägg påverkan i `docs/change-impact-map.md`
3. uppdatera relevanta stöddokument
4. revidera berörda kapitel
5. kör continuity-, mystery- och researchkontroll vid behov
6. logga utfallet i `docs/revision-log.md` och verifiera mot `docs/revision-qa.md`

## Aktivt styrsystem
- Revisionsworkflow: `docs/revision-workflow.md`
- Revisionsdiscovery och baselinebedömning: `docs/revision-discovery.md`
- Change requests: `docs/change-requests.md`
- Impact mapping: `docs/change-impact-map.md`
- Canon och låsta sanningar: `docs/canon-ledger.md`
- Revisionslogg: `docs/revision-log.md`
- Revisions-QA: `docs/revision-qa.md`
- Blockerare: `docs/blockers.md`
- Beslut: `docs/decisions.md`
- Faktaverifiering: `docs/research-log.md`

## Agentteam i revision mode
- `revision-orchestrator`: äger revisionsflödet end-to-end och vägrar intern "nästan klar".
- `plot-structure-revision`: driver Typ C-E med fokus på handling, revealordning, bågar och struktur.
- `scene-line-edit`: driver Typ B-C på scen- och kapitelnivå utan att smyga in odeklarerade storyskiften.
- `language-polish`: driver Typ A med strikt bevarande av fakta och scenfunktion.
- `continuity-canon`: bevakar intern logik, tidslinje, relationer, canon och dokumentkedjor.
- `mystery-clue-integrity`: bevakar ledtrådskedja, villospår, omtolkningar och revealdisciplin.
- `research-fact-check`: verifierar verklighetsanknutna detaljer före låsning av relevanta revisioner.
- `qa-release`: avgör om revisionen verkligen är klar på rätt nivå eller måste tillbaka i intern loop.
- `git-gate`: avgör om arbetsläget är redo att committa eller pusha, ska signalera detta självmant när läget tydligt mognat eller på uppdrag av `revision-orchestrator`, och förbereder commit-scope, commitmeddelande och pushrekommendation utan att själv köra git.

## Kapitel med särskilt ändringsskydd
Följande kapitel kräver användarens uttryckliga tillstånd innan texten ändras:
- `01`
- `02`
- `03`

När någon vill ändra något av dessa kapitel ska användaren först få tre alternativ:
- Ändra endast det som är nödvändigt
- Ändra fritt
- Ändra inte alls

## Definition av revisionsklar
Projektet är inte "konverterat till revision mode" förrän:
- first-version-systemet är tydligt arkiverat
- den här filen är aktiv och revisionsspecifik
- revisionsagenterna finns under `.codex/agents/`
- change requests, impact map, canon ledger, revisionslogg och revisions-QA finns
- skillnaden mellan språkputs och plotrevision är dokumenterad
- framtida Codex-körningar naturligt styrs mot säker revision snarare än nygenerering
