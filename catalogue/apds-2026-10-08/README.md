# APDS archival bibliography — 8 October 2026

82 bibliographic records have been imported into Zotero group 6701789 and assigned to its existing thematic collections. Reports also belong to `16 - Technical reports`, and theses to `15 - Theses & dissertations`.

The group is the live data source of the existing GitHub Pages application. This directory documents the completed import; the application does not need a new data loader. Zotero changes are visible independently of a merge of this Git branch.

## Files

- `notices.json`: bibliographic metadata prepared from title pages and introductory evidence; no scans, OCR corpus, private paths or personal research data.
- `imported-items.json`: permanent Zotero keys, links and collection assignments for the 82 imported notices.
- `verification.json`: final public-API verification of the import.

The batch contains 65 reports, 10 theses, 5 book chapters and 2 books. Seven notices have an externally checked stable source and `STATUS:Verified`; 75 retain `STATUS:Metadata-Incomplete` because an external stable source was not established. This distinction must remain visible when extending the catalogue.

No new DOI was assigned from filenames, cited references or an unconfirmed match. Two published articles found in the archive already existed in Zotero and were not duplicated. A related workshop packet was also left under its existing record pending a packet-versus-synthesis distinction.

## Preferred online version — 12 October 2026

When an archival scan is confirmed to represent the same publication as an online publisher or institutional copy, prefer that online version in the existing Zotero record. Verify title, authors, edition or language, publication date and pagination before matching. Use a verified DOI as the stable URL when available; otherwise retain a verified publisher or institutional link. A DOI found only in the bibliography, a later article derived from a report, or a translated edition does not establish an identical work.

Keep the APDS archive provenance and inventory identifiers, and explicitly describe missing pages or uncertain metadata. Do not create a second record for a scan or an alternative DOI of the same publication. Relevant works without a confirmed online equivalent retain their honest archival notice with missing information identified.

An online match does not clear sensitive content or authorize redistribution of the scan. Preserve any controlled-consultation warning where justified; full-text review and link verification are recorded separately in the private audit.

## Reuse

This is a record of an **already completed import**, not a queue to import again. Before any future import, compare Zotero keys, DOI identity and title/author/date combinations against the current group. Multiple scans of one work are not separate publications.

During the first metadata-only pass, no archival PDF or attachment was published. Six separately reviewed redacted plans were subsequently published; see the update below. A public bibliographic notice does not authorize publication of the corresponding scan. Copyright, private information, community knowledge and precise locations require a separate review before full-text release. The detailed archive inventory and sensitivity findings remain in the local private audit report, outside this repository.

## Completed second pass — 10 October 2026

All 36 previously held relevant works now have honest bibliographic notices in Zotero: 20 reports, 8 manuscripts/research proposals, 4 books and 4 composite documents. Unknown authors, dates and identifiers remain explicit; no DOI was inferred. The reports also belong to collection 16. Drafts and proposals are not presented as completed research results.

The archive contributes 118 new notices in total. All 118 identify a copy retained at the Bibliothèque des APDS and its APDS inventory identifier. Twenty-five second-pass originals contain sensitive material and are represented only by minimal bibliographic metadata and a controlled-consultation warning. No original PDF or private OCR corpus was uploaded.

Six historical village plans are available as [redacted public PDFs](plans-publics/README.md). Their immutable links are in Zotero. Source page numbering is retained after a new explanatory cover. Detailed maps, signatures, unnecessary names and identified personal passages were removed. The public copies have no source OCR, annotations or embedded attachments. They document historical plans and assessments, not present-day conditions.

- `catalogue-final.json`: current public metadata for all 118 archive notices.
- `second-pass-imported-items.json`: permanent Zotero keys for the 36 additional notices; do not reimport.
- `second-pass-verification.json`: API verification and integrity checks on 10 October.

The application changes on this branch display archive provenance, missing-information notices and controlled-consultation warnings in both cards and the comparison table. Zotero imports are live immediately; the branch's interface changes require a separate merge/deployment. This work does not modify or merge `main`. Independent bibliography updates since the initial import have been preserved.
