# Revision Log

## 2026-04-09 - `REV-008` - Renodling av kapitelkedjan `05` / `05A` / `06`
Status: klar

Genomfört:
- registrerat ärendet som Typ C för den tidiga Kivik-kedjan
- flyttat Stenportens förhandsnarrativ, Cecilia/H-spåret och det sista pensionsrummets konkreta fynd till kapitel 5 så att hela bevisgången i rummet ägs av samma kapitel
- skrivit om kapitel 5A till ett rent bryggkapitel som börjar i receptionen och därefter bär vittnesuppgiften, vägen genom Kivik, hamnen och Majas psykologiska uppladdning inför hemkomsten
- tagit bort den tidigare rumsöverlappningen mellan `05` och `05A` i både kapiteltexten och `docs/manuscript-full.md`
- tagit bort den explicita förhandsnämningen av `Rutan` i `05A` så att `06` fortsatt är första platsen där namnet blir uttalat och operativt

Verifierat:
- kapitelkedjan läser nu rent som `05 = fynd och riktningsskifte`, `05A = förflyttning och emotionell/investigativ brygga`, `06 = arkiv, familjekonflikt och nästa operativa spår`
- inga bevis upptäcks längre två gånger i pensionsrummet
- revealordningen är bevarad: Severins mönster, Stenportens narrativkontroll, `MALM`-kopplingen, återvändandet till hemmet, Arvids material och därefter `Rutan`
- chapter plan och canon ledger behövde inte ändras efter kontroll

## 2026-04-09 - `git-gate` / `revision-orchestrator` - Gitgrind skärpt
Status: klar

Genomfört:
- förtydligat i `AGENTS.md` att `git-gate` ska signalera commit- eller pushmognad självmant eller på uppdrag av `revision-orchestrator`
- skärpt `git-gate` så att explicit status måste avges både vid tydlig mognad i worktreet och vid orchestratorstyrd klar- eller handoffpunkt
- skärpt `revision-orchestrator` så att revisioner inte får markeras redo för commit eller push utan aktuell `git-gate`-bedömning
- lagt in samma grind i `docs/revision-workflow.md` som ett obligatoriskt slutsteg före gitbeslut

Verifierat:
- gitbeslut är nu uttryckligen bundna till en formell `git-gate`-status, inte bara till ad hoc-frågor
- styrningen tillåter både proaktiv signalering och orchestratorstyrd inhämtning utan att ge `git-gate` mandat att köra git automatiskt

## 2026-04-09 - `REV-007` - Renodling av Glimmingehusledtrådarna kring Stenshuvud
Status: klar

Genomfört:
- registrerat lokal clue-justering som Typ C för öppningsmotorn
- flyttat Stenshuvud-spåret i kapitel 4 från vägg- och dammledtrådar till en Severinnotis på baksidan av flygfotot som inkräktaren verkar ha försökt få med sig men tappat
- flyttat själva avläsningen av flygfotot från kapitel 4 till kapitel 6 så att informationen kommer fram först när läsaren hunnit släppa detaljen och den kan klicka ihop med faderns sjövägsspår
- ändrat den kvarvarande läsbara kärnan till `fri sikt` så att spåret pekar mot Stenshuvud som observations- och läsposition utan att lösa mysteriet för tidigt
- tagit bort `tre kritstreck`-passagen i magasinet och den senare väggristan `Stenshuvud`
- renodlat objektkedjan så att flygfotot över Stenshuvud bara förekommer som det tappade fyndet vid magasinströskeln, inte som dubblerat material i den tidigare bildbunten
- synkat den senare tre-kedjan i kapitel 11 och `docs/manuscript-full.md` så att den inte längre bygger på magasindammet

Verifierat:
- Stenshuvud öppnas fortfarande tidigt som riktning men fungerar ännu inte som full läsnyckel
- kapitel 5, kapitel 6, kapitel 14 och kapitel 15 kan fortfarande bära `fel riktning?`, Stenshuvud som observationspunkt, havsläsningen och payoffen kring `inte uppåt`
- intrångsscenen läser nu tydligare som sabotage och rensning, där angriparen försöker få med sig relevant material snarare än lämna hjälpsamma ledtrådar

## 2026-04-09 - `language-polish.md` - Typ A språkstyrning
Status: klar

Genomfört:
- lagt in en uttrycklig språkregel mot den AI-präglade negeringsformeln `inte x, inte y, utan z` och närliggande varianter som standardgrepp i berättarprosa
- lagt till en positiv motregel om att föredra rakare, positiva påståenden när samma sak kan sägas klarare utan negeringskedja

Verifierat:
- ändringen skärper språkstyrningen utan att ändra storyfakta, scenfunktion eller revealordning i aktiv text
- regeln är avsedd att styra framtida Typ A-pass och fånga ett återkommande AI-markörmönster i manuset

## 2026-04-09 - Kapitel `04-glimmingehus-efter-stangning.md` - Typ A språkputs
Status: klar

Genomfört:
- gjort ett `language-polish`-pass på hela kapitel 4 med fokus på mjukare rytm, mindre kompakta meningar och mer idiomatisk svenska
- justerat berättarprosa och repliker mot naturligare läsbarhet utan att ändra fakta, POV, scenfunktion eller revealordning
- ersatt abstrakt `läsning` med mer precisa formuleringar där det gick att göra inom Typ A
- rättat en överdriven skadeformulering i arbetsrumsbeskrivningen från `det sönderslagna` till `röran` så att texten bättre stämmer med vad scenen faktiskt visar
- bytt ut den oidiomatiska formuleringen `Latinsk kursiv hand` mot en rakare beskrivning av skriftbilden
- rättat en felaktig platsreferens i Linneas replik från `Ales stenar` till `Hällevik` så att kapitlet stämmer med aktiv canon för fyndplatsen
- bytt ut uttrycket `Ingen rund hand` mot en idiomatisk svensk beskrivning av skriftens form
- justerat Linneas skeptiska replik så att den svarar naturligare på Majas tolkning utan att föra in ett omotiverat skattespår
- stramat upp replikväxlingen efter Linneas invändning genom att ta bort den oklara jämförelsen `Värre`
- förtydligat referensen `sidan` till `utskriften` så att repliken tydligt pekar på materialet i pärmen och inte telefonbilden
- gjort relationen mellan telefonbilden och pärmutskriften explicit, och bytt `byggde den själv` till en tydligare formulering om att Severin själv satte ihop jämförelsen
- skrivit om den krystade raden `Inte ett skepp. Inte en ritual. Ett led.` till en tydligare formulering om att Maja uppfattar en riktning genom landskapet
- skrivit om `inte uppåt`-replikskiftet så att ledtråden förblir delvis gåtfull men ger en konkret mikroinsikt om läsriktning genom pilen och bildmaterialet
- rättat ordföljden i `Han drog den upp` till idiomatisk svensk meningsbyggnad
- bytt ut den visuellt orimliga detaljen `ett vältränat ben` mot en mörker- och rörelsemässigt rimligare observation
- bytt ut den slitna formuleringen `hårt ansikte` och förtydligat Noahs order från `Ut!` till `Ut härifrån!` så att faran och avsikten läses klarare
- omformulerat Noahs order till en kort, tydlig säkerhetsreplik som uttryckligen förklarar varför de måste lämna magasinet
- putsat slutet på kapitel 4 så att Linneas skrik får tydlig utlösare och övergången till kapitel 5 binds tätare till brandlarmets efterspel
- förtydligat slutrörelsen så att det uttryckligen framgår att larmet driver ut dem ur byggnaden innan kapitel 5 tar vid
- bytt ut den oklara formuleringen `Rop, steg, riktningar åt upp varandra` mot en rakare beskrivning av larmkaoset
- ersatt `Det skulle ta timmar innan de fick tillbaka rummet` med en mer precis formulering om att de inte får tillträde igen på länge
- synkat samma språkjustering i `docs/manuscript-full.md`

Verifierat:
- inga storyfakta, motiv eller reveals har ändrats
- Majas POV, clue-kedjan och kapitlets upptrappning från arbetsrummet till intrånget och `Stenshuvud`-markeringen är bevarade
- revisionen håller sig inom Typ A och kräver ingen uppgradering

## 2026-04-09 - Kapitel `03-noah-rask.md` - Typ A språkputs av infogad `03A`-bro
Status: klar

Genomfört:
- gjort ett separat `language-polish`-pass på den inflyttade övergången mellan mordplatsen och Glimmingehus i kapitel 3
- justerat repliker, meningsrytm och ordval mot mer idiomatisk svenska och jämnare ton mot resten av kapitlet
- synkat samma språkjustering i `docs/manuscript-full.md`

Verifierat:
- ingen storyinformation, scenfunktion eller revealordning har ändrats
- bron bär fortfarande exakt samma funktion: gemensam avfärd, kort fördjupning av Majas hållning till fadern och ankomst till Glimmingehus

## 2026-04-08 - `REV-006` - Sammanfogning av kapitel `03` och tidigare `03A`
Status: klar

Genomfört:
- klassat ärendet som Typ D och registrerat det i change request- och impact-dokumenten
- gjort `03` till ensam aktiv öppningsnod för mordplatsen och övergången mot Glimmingehus
- räddat in ett kort, stramat brostycke från tidigare `03A` till slutet av `03`: gemensam bilfärd, kort fördjupning av Majas bevisdisciplin och ankomst till Glimmingehus
- flyttat kapitelgränsen så att `04` börjar vid Linneas praktiska genomgång i stället för med dubblerad ankomst
- tagit bort `03A` ur den aktiva manussekvensen i `docs/manuscript-full.md` och arkiverat den äldre texten utanför aktiv baseline
- synkat `docs/chapter-plan.md`, `docs/structure-grid.md` och `docs/chapter-true-story.md` mot den nya aktiva sekvensen

Verifierat:
- aktiv läsordning är nu `03 -> 04` utan dubblerad mordplatskonfrontation eller omtag av Glimmingehusankomsten
- `03` har fortsatt företräde i all överlappande geografi, scenordning och dialogfunktion
- tidiga `Rutan`-, Torkel- och sjömärkesrevealpunkter har inte förts fram i öppningskedjan
- ingen ny storyinformation har skapats; ändringen består av omplacering, stramning och utfasning av osynkad text

## 2026-04-08 - `language-polish.md` och kapitel `03-noah-rask.md` - Typ A språkputs, sjätte passet
Status: klar

Genomfört:
- lagt in ett uttryckligt förbud i `language-polish.md` mot abstrakt styrsystems-, myndighets- och konsultspråk i berättarprosa
- lagt till exempelregel mot pseudoexakta sammansättningar som `beroendeyta`
- bytt ut formuleringen `lokal beroendeyta` i kapitel 3 och `manuscript-full.md` mot en konkret och idiomatisk formulering

Verifierat:
- ingen storyinformation, scenfunktion eller revealordning har ändrats
- justeringen skärper språkstyrningen och rättar ett konkret uttryck i aktiv text

## 2026-04-08 - Kapitel `03-noah-rask.md` - Typ A språkputs, femte passet
Status: klar

Genomfört:
- gjort ett nytt helhetspass med fokus på naturlig svensk romanprosa, begriplighet vid första läsningen och mindre översatt eller konstruerat språk
- skrivit om ett större antal meningar helt i stället för att bara putsa ytan där formuleringarna fortfarande kändes stela eller oidiomatiska
- synkat samma reviderade version i `docs/manuscript-full.md`

Verifierat:
- inga storyfakta, motiv eller reveals har flyttats
- POV, scenfunktion, konfliktriktning och rörelsen mot Glimmingehus är bevarade
- kapitlet är språkligt omarbetat men innehållsligt oförändrat på Typ A-nivå

## 2026-04-08 - Kapitel `03-noah-rask.md` - Typ A språkputs, fjärde passet
Status: klar

Genomfört:
- bytt ut ett missvisande känsloord i slutpartiet mot en mer idiomatisk och betydelseklar formulering

Verifierat:
- ingen scenfunktion, revealordning eller sakinformation har ändrats
- justeringen gäller endast ordprecision i Noahs reaktion

## 2026-04-08 - Kapitel `03-noah-rask.md` - Typ A språkputs, tredje passet
Status: klar

Genomfört:
- rättat en geografiskt felriktad platsbild i slutpartiet så att miljön stämmer med Hällevik/Stenshuvud och inte Ales/Kåseberga
- bevarat scenfunktion, rörelse mot parkeringen och den avslutande upptrappningen

Verifierat:
- ingen scenfunktion, revealordning eller lokal rörelse har ändrats
- platsbilden är nu förenlig med kapitel 1 och synopsis

## 2026-04-08 - Kapitel `03-noah-rask.md` - Typ A språkputs, andra passet
Status: klar

Genomfört:
- gjort ett nytt Typ A-pass med fokus på idiomatisk svenska, semantisk precision och korrekt syftning
- skrivit om formuleringar som tidigare lät litterära utan att bära exakt innebörd
- behållit scenfunktion, POV, informationsordning och revealordning oförändrade

Verifierat:
- inga storyfakta, motiv eller reveals har flyttats
- kapitlets konflikt, maktspel och Glimmingehus-rörelse är intakta
- eventrepliken är fortfarande ett språk- och logikförtydligande inom Typ A, inte en scenändring

## 2026-04-08 - Kapitel `03-noah-rask.md` - Typ A språkputs
Status: klar

Genomfört:
- mjukat upp meningsrytm, minskat kompakthet och förbättrat läsbarheten i hela kapitel 3
- justerat dialog och berättarprosa mot tydligare, mer naturligt läsbar språkföring utan ändrad scenfunktion
- gjort ett lokalt logikförtydligande i Cecilias eventreplik utan att ändra informationsinnehåll eller revealordning

Verifierat:
- inga storyfakta, motiv eller reveals har flyttats
- Noahs POV och kapitlets scenfunktion är bevarade
- Glimmingehus-spåret, Stenportens positionering och slutbilden med kalken är oförändrade i funktion

## 2026-04-08 - `REV-001` - Konvertering till revision mode
Status: klar

Genomfört:
- arkiverat first-version-styrningen som `AGENTS_FIRST_VERSION.md`, `.codex/agents/fv-*.md` och `docs/fv-*.md`
- skapat ny aktiv `AGENTS.md` för revision mode
- skapat nytt revisionsanpassat agentteam
- skapat change request-system, impact map, canon ledger, revision workflow, revisionsdiscovery och revisions-QA
- ersatt first-version-kapitelplan och first-version-leveransplan med aktiva revisionsversioner
- korrigerat aktiva stöddokument som tidigare signalerade fel git-status eller osynkade öppningsfakta

Kvar som nästa rimliga steg:
- `REV-002` canonbackfill
- `REV-003` continuity- och mystery-audit
- `REV-004` förfinad kapitelkänslighetskarta
