# AGENTS.md

## Projektets uppdrag
Detta projekt ska leverera en originalskriven, researchförankrad och fullt fungerande thrillerroman med arbetstiteln **The Serpent of Österlen**. Slutmålet är inte synopsis, utkast eller fragment utan ett komplett manus med tillhörande stöddokument och exportformat enligt projektets leveransdefinition.

## Hårda projektregler
- Arbeta på svenska.
- Använd tät tredje person som huvudform.
- Romanen ska vara en högdriven konspirationsthriller / historisk thriller / mysteriethriller.
- Österlen ska fungera som narrativ maskin, inte som kuliss.
- Fornnordiskt material ska behandlas realistiskt och researchförankrat.
- Nutida Forn Sed eller annan modern religiös praktik får inte sensationaliseras eller användas slarvigt som skräckkuliss.
- `project-instructions.md`, `thriller-style.md` och `style-guide.pdf` är bindande styrdokument.
- Kortkapitelsdriv, cliffhangers, omtolkningar, tydlig gåtkedja och stigande insatser är obligatoriskt.
- Ingen fas får markeras som klar om leveransgrinden för fasen inte är verifierad i dokumentation.

## Faser och grindar

### Fas 1: Styrsystem
Krav för klarstatus:
- `AGENTS.md` finns och är projektspecifik.
- agentfiler under `.codex/agents/` finns och har tydliga ansvarsområden
- arbetsfiler för discovery, struktur, synopsis, kapitelplan, research, QA, leverans och blockerare finns

### Fas 2: Discovery
Krav för klarstatus:
- bindande krav från samtliga styrdokument är extraherade
- öppna frågor är sorterade i tre klasser: fråga användaren, standardantagande, senare iteration
- romanens stora hemlighet, story goal, consequence, protagonistens inre brist, influence character, antagonistens logik, tickande klocka, huvudplatser och slutets etiska val är låsta
- nödvändiga externa beroenden är verifierade

### Fas 3: Struktur och manusberedskap
Krav för klarstatus:
- story core, synopsis, strukturgrid, ledtrådskedja och kapitelplan är sammanhängande
- mysteriet fungerar baklänges och framlänges
- reveal-ordning, villospår och omtolkningar är kontrollerade
- agentsystemet är uppdaterat utifrån faktisk discovery

### Fas 4: Iterativ manusproduktion
Krav för klarstatus per iteration:
- en sammanhängande delkedja är färdigskriven, inte bara skissad
- delkedjan har QA-kontrollerats mot tempo, scenfunktion, mysterium, research, kontinuitet och stil
- beslut, risker och kvarstående luckor är dokumenterade

### Fas 5: Slutrevision och leverans
Krav för klarstatus:
- alla kapitel finns som separata `.md`-filer
- ett sammanslaget manus i `.md` finns
- en PDF finns
- QA-checklistan är genomgången
- blockerarlistan innehåller inga interna blockerare

## Orkestreringsregler
- Orkestratorn äger helheten och får inte acceptera intern “nästan klar”.
- När osäkerhet kan lösas genom research ska research göras före fråga till användaren.
- Frågor till användaren får endast ställas när ett felaktigt standardantagande riskerar att styra romanen tydligt fel.
- Alla större antaganden ska loggas i `docs/decisions.md`.
- Alla blockerare ska loggas i `docs/blockers.md`.
- Alla iterationer ska loggas i `docs/iteration-log.md`.

## Dramaturgisk miniminivå
- Story goal och consequence måste vara tydliga.
- Requirements, forewarnings, costs, dividends, prerequisites och preconditions ska finnas på romannivå.
- Minst tre större omtolkningar ska finnas.
- Klimax ska lösa både yttre handling och huvudpersonens inre val.
- Varje större del måste fördjupa mysteriet, höja hotet, omtolka tidigare fakta eller skärpa relation/idékonflikt.

## Researchhierarki
1. Officiella och primära källor
2. Museer, myndigheter, nationalpark, kulturarvsinstitutioner
3. Relevanta forsknings- eller kunskapskällor
4. Lokala aktörer som komplement

Om fakta är osäkra:
- märk osäkerheten i `docs/research-log.md`
- använd inte osäkra påståenden som bärande scenfakta utan märkning eller senare verifiering

## Leveransformat
- Kapitel: `docs/chapters/NN-kapitelrubrik.md`
- Sammanställt manus: `docs/manuscript-full.md`
- PDF-export: `docs/manuscript.pdf`

## Definition av klart
Projektet är klart först när den fulla romanen, dess stöddokument och exportformat finns på plats och den samlade QA:n visar att mysterium, struktur, geografi, ton, kontinuitet och leveransformat fungerar tillsammans.
