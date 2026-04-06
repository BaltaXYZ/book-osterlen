# Delivery Plan

## Slutleveranser
- `docs/chapters/*.md`
- `docs/manuscript-full.md`
- `docs/manuscript.pdf`
- `docs/book-edition.pdf`
- `docs/book-cover-art.png`

## Arbetsordning
1. Skriv kapitel som separata markdownfiler.
2. Bygg sammanslaget manus automatiskt från kapitelmappen.
3. Exportera PDF från det sammanslagna manuset.
4. Bygg separat formgiven bokutgåva i A5-format med omslag och baksida.

## Filkonvention
- kapitel prefixas med tvåsiffrigt nummer
- filnamn hålls korta och ASCII-baserade
- första rad i varje kapitel är kapitelrubrik

## Byggregler
- sammanslaget manus ska ha titel, eventuell delindelning och kapitel i rätt ordning
- PDF ska kunna genereras lokalt utan externa konton eller molntjänster
- bokutgåvan ska kunna genereras lokalt med egen omslagsbild och modern boklayout
- om PDF-bygg kedjan faller ska blockeraren loggas med exakt orsak

## Definition av leveransklar
- manus är komplett
- sammanslaget manus är uppdaterat från senaste kapitelversioner
- PDF är exporterad efter senaste manusändring
- bokutgåvan är exporterad efter senaste manusändring
