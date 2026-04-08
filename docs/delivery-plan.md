# Delivery Plan

> Aktiv leveransplan i revision mode. Fokus ligger på att hålla leveransfiler synkade efter godkända revisioner.

## Aktiva leveranser
- `docs/chapters/*.md`
- `docs/manuscript-full.md`
- `docs/manuscript.pdf`
- `docs/book-edition.pdf`
- `docs/book-cover-art.png`

## Revisionsstyrd arbetsordning
1. Godkänn och klassificera revisionen.
2. Uppdatera stöddokument som krävs för ändringstypen.
3. Revidera berörda kapitel.
4. Kör relevant QA.
5. Bygg om `docs/manuscript-full.md` och PDF-filerna om manusleveransen har påverkats.
6. Logga revisionen som klar först när exporterna motsvarar senaste godkända manusläge.

## När ombyggnad krävs
- alltid efter kapiteländringar som påverkar manusleveransen
- inte nödvändigt efter ren dokumentkonvertering eller stödjande metadataändringar utan manuspåverkan

## Definition av leveranssynk
- kapitelmapp, sammanslaget manus och relevanta PDF-filer speglar samma godkända revisionsnivå
- revisionslogg och revisions-QA pekar på samma status som leveransfilerna
