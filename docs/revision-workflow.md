# Revision Workflow

## Syfte
Detta dokument definierar hur framtida revisioner ska drivas utan att baseline-manuset eller stöddokumenten glider isär.

## Baselineprincip
- Existerande manus och aktiva stöddokument gäller tills en uttrycklig revision säger annat.
- Varje icke-trivial ändring ska spåras med change request-ID.
- Typ D och Typ E får aldrig börja som direkt omskrivning i kapiteltext.

## Revisionsklasser

| Typ | Namn | Före ändring | Måste uppdateras | Obligatoriska roller | Klar när |
| --- | --- | --- | --- | --- | --- |
| A | Språkputs / line polish | Avgränsa textscope och bekräfta att inga storyfakta ska ändras | `docs/change-requests.md`, `docs/revision-log.md`, `docs/revision-qa.md` | `language-polish`, `qa-release` | Texten är starkare utan faktaskifte eller revealförskjutning |
| B | Scenrevision utan ändrad storyfunktion | Bekräfta att scenens funktion, POV och information ska bevaras | relevanta kapitel, vid behov `docs/chapter-true-story.md`, logg och QA | `scene-line-edit`, `continuity-canon`, `qa-release` | Scenen fungerar bättre men berättar samma sak |
| C | Kapitelrevision med lokal storypåverkan | Identifiera lokal följdeffekt på canon, clue eller relation | kapitel, `docs/chapter-true-story.md`, vid behov `docs/canon-ledger.md`, `docs/clue-chain.md`, logg och QA | `scene-line-edit`, `continuity-canon`, vid behov `mystery-clue-integrity` eller `research-fact-check`, `qa-release` | Kapitel och närliggande stöddokument är synkade |
| D | Strukturändring med flera beroenden | Formellt change request och impact mapping krävs | `docs/story-core.md`, `docs/synopsis.md`, `docs/structure-grid.md`, `docs/chapter-plan.md`, vid behov `docs/clue-chain.md`, `docs/canon-ledger.md`, `docs/research-log.md`, därefter kapitel | `revision-orchestrator`, `plot-structure-revision`, `continuity-canon`, `mystery-clue-integrity`, vid behov `research-fact-check`, `qa-release` | Stöddokument uppdaterade före text, beroenden kontrollerade, QA godkänd |
| E | Större plotändring med canon-/mysteriepåverkan | Formellt change request, impact mapping och explicit riskbedömning krävs | alla relevanta struktur- och canondokument före kapitel, plus logg, beslut och QA | hela revisionslaget | Plotförändringen är spårbar, testad mot canon/mysterium/research och verifierad som helhet |

## Standardflöde
1. Registrera ärendet i `docs/change-requests.md`.
2. Klassificera typen A-E.
3. Kartlägg påverkan i `docs/change-impact-map.md`.
4. Uppdatera stöddokument före kapiteltext när ändringen är Typ C-E. För Typ D-E är detta absolut krav.
5. Revidera manusfiler.
6. Kör rätt kontroller:
   - canon/continuity
   - mystery/clue
   - research/fakta
   - QA/release
7. Logga resultat, restarbete och beslut.

## Språkputs-läge
Typ A får:
- skärpa rytm, konkretion, precision och muntlighet
- strama upp klumpiga eller abstrakta formuleringar
- minska onödig förklaring

Typ A får inte:
- lägga till ny information
- ändra motiv, relationer eller handlingsutfall
- flytta reveals eller ändra vad läsaren vet när
- byta POV eller scenfunktion

## Plotregel
Ändringar i handling, motiv, tidslinje, antagonistlogik, reveal-ordning, ledtrådskedja eller karaktärsbåge måste först finnas som change request med konsekvensanalys och uppdaterade stöddokument.

## Releaseprincip
Ingen revision räknas som klar förrän rätt nivå i `docs/revision-qa.md` är explicit markerad som klar.
