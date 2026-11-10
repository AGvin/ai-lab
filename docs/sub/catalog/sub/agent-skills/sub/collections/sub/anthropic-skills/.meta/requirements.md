# Documentation Requirements

## Requirements

- Identify Anthropic Skills through Anthropic's official `anthropics/skills` repository and link the canonical Anthropic producer profile.
- Explain that the repository contains Anthropic's implementation of skills for Claude and includes the source-available document skills used to demonstrate production-scale document capabilities.
- Preserve the broader collection context that the repository also includes specification/template material and examples spanning creative/design, development/technical, enterprise, and communication workflows; treat this as collection-level breadth rather than a requirement to materialize every example as a local catalog node.
- Preserve the revision- and path-specific licensing boundary: at upstream revision `2c5958ecac7cee2b583967a2c4981d0f4a75c579`, all four selected document skill `LICENSE.txt` files use Apache-2.0, superseding their historical Anthropic agreement terms at `ca45fc496a3436251f191354091d557da31c15b5`. Do not infer licenses for other skills, third-party dependencies/assets or hosted Claude services; verify source revision and path before reuse.
- Position the collection as a useful source for studying simple versus production-scale skill structures, use of scripts/references/assets, template-driven authoring, and the boundary between standalone skills and Claude Code plugin packaging; present these as practical study/use cases rather than a blanket endorsement of every upstream skill.
- Present the selected collection-owned skills with one compact overview followed by concise per-skill detail sections; do not create duplicate standalone catalog pages for them.
- Selected skills are DOCX, PDF, PPTX, and XLSX.
- For DOCX, describe Word-document creation, reading, editing, tracked-change/comment workflows, and visual verification; retain the current upstream dependencies on the `docx` package, Pandoc, LibreOffice, and Poppler where relevant, plus the bundled office/XML/comment/validation helpers.
- For PDF, describe reading/extraction, creation, merge/split/rotation, forms, protection, and OCR workflows; retain the operation-dependent `pypdf`, `pdfplumber`, `reportlab`, OCR/PDF tooling, and bundled advanced/form references without implying every operation needs every dependency.
- For PPTX, describe PowerPoint creation, reading, editing, rendering, and visual/structural verification; retain the current `pptxgenjs`, Python, LibreOffice, Poppler, and `markitdown` requirements where applicable and the bundled thumbnail, slide-manipulation, cleanup, and validation helpers.
- For XLSX, describe spreadsheet creation, reading, editing, formatting, recalculation, and validation; retain the current `openpyxl`, `pandas`, `markitdown`, and LibreOffice requirements where applicable and the bundled recalculation/validation helpers.
- Link each selected skill to its official source directory under `https://github.com/anthropics/skills/tree/main/skills/`.
- Explain collection-level installation only at the level supported by the official repository: the repository can be registered as a Claude Code plugin marketplace, the example-skill bundle and `document-skills` bundle are distinct installable surfaces where currently supported, and runtime dependencies remain skill- and operation-specific.

## Selected Skill Sources

- DOCX: `https://github.com/anthropics/skills/tree/main/skills/docx`
- PDF: `https://github.com/anthropics/skills/tree/main/skills/pdf`
- PPTX: `https://github.com/anthropics/skills/tree/main/skills/pptx`
- XLSX: `https://github.com/anthropics/skills/tree/main/skills/xlsx`

## Validation

- All four selected skills are represented exactly once in the collection page.
- Collection breadth is described without implying that every upstream example is a locally selected catalog entity.
- License wording distinguishes the four current Apache-2.0 document-skill license files from historical Anthropic agreement terms and from any unverified dependent assets/services.
- Practical-use positioning does not imply that every upstream skill is reviewed or recommended for every environment.
- Dependency wording remains operation-scoped where upstream does not require every tool for every task.
- No selected document skill is linked as a local standalone catalog node.
- Reader-facing claims are consistent with the current official repository and selected `SKILL.md` files.

## License/source reconciliation — 2026-11-08

- The [current original README](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/README.md) describes the four selected document skills as Apache-2.0. Each of [DOCX](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/docx/LICENSE.txt), [PDF](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pdf/LICENSE.txt), [PPTX](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pptx/LICENSE.txt) and [XLSX](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/xlsx/LICENSE.txt) has the identical Apache License 2.0 text at this revision.
- The previously reviewed [historical DOCX license](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/docx/LICENSE.txt) carried Anthropic agreement restrictions. Preserve that as revision-specific history, not the current licensing status.
- This is a license/source correction for four selected paths only, not an exhaustive collection, dependency, copyright/third-party rights, provenance, runtime or currentness audit.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
