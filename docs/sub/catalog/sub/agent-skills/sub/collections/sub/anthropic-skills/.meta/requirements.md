# Documentation Requirements

## Requirements

- Identify Anthropic Skills through Anthropic's official `anthropics/skills` repository and link the canonical Anthropic producer profile.
- Explain that the repository contains Anthropic's implementation of skills for Claude and includes the source-available document skills used to demonstrate production-scale document capabilities.
- Present the selected collection-owned skills with one compact overview followed by concise per-skill detail sections; do not create duplicate standalone catalog pages for them.
- Selected skills are DOCX, PDF, PPTX, and XLSX.
- For DOCX, describe Word-document creation, reading, editing, tracked-change/comment workflows, and visual verification; retain the current upstream dependencies on the `docx` package, Pandoc, LibreOffice, and Poppler where relevant, plus the bundled office/XML/comment/validation helpers.
- For PDF, describe reading/extraction, creation, merge/split/rotation, forms, protection, and OCR workflows; retain the operation-dependent `pypdf`, `pdfplumber`, `reportlab`, OCR/PDF tooling, and bundled advanced/form references without implying every operation needs every dependency.
- For PPTX, describe PowerPoint creation, reading, editing, rendering, and visual/structural verification; retain the current `pptxgenjs`, Python, LibreOffice, Poppler, and `markitdown` requirements where applicable and the bundled thumbnail, slide-manipulation, cleanup, and validation helpers.
- For XLSX, describe spreadsheet creation, reading, editing, formatting, recalculation, and validation; retain the current `openpyxl`, `pandas`, `markitdown`, and LibreOffice requirements where applicable and the bundled recalculation/validation helpers.
- Link each selected skill to its official source directory under `https://github.com/anthropics/skills/tree/main/skills/`.
- Explain collection-level installation only at the level supported by the official repository: the `document-skills` plugin can install the document-skill set, while runtime dependencies remain skill- and operation-specific.

## Selected Skill Sources

- DOCX: `https://github.com/anthropics/skills/tree/main/skills/docx`
- PDF: `https://github.com/anthropics/skills/tree/main/skills/pdf`
- PPTX: `https://github.com/anthropics/skills/tree/main/skills/pptx`
- XLSX: `https://github.com/anthropics/skills/tree/main/skills/xlsx`

## Validation

- All four selected skills are represented exactly once in the collection page.
- Dependency wording remains operation-scoped where upstream does not require every tool for every task.
- No selected document skill is linked as a local standalone catalog node.
- Reader-facing claims are consistent with the current official repository and selected `SKILL.md` files.
