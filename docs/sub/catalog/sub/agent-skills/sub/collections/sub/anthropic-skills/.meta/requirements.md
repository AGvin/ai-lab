# Documentation Requirements

## Requirements

- Identify Anthropic Skills through Anthropic's official `anthropics/skills` repository and link the canonical Anthropic producer profile.
- Explain that the repository contains Anthropic's implementation of skills for Claude and includes the source-available document skills used to demonstrate production-scale document capabilities.
- Preserve the broader collection context that the repository also includes specification/template material and examples spanning creative/design, development/technical, enterprise, and communication workflows; treat this as collection-level breadth rather than a requirement to materialize every example as a local catalog node.
- Preserve the per-path licensing boundary: repository presence does not imply one license for every example or production document implementation, so readers must verify the license at the selected source path.
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
- License wording remains path-specific where upstream terms differ.
- Practical-use positioning does not imply that every upstream skill is reviewed or recommended for every environment.
- Dependency wording remains operation-scoped where upstream does not require every tool for every task.
- No selected document skill is linked as a local standalone catalog node.
- Reader-facing claims are consistent with the current official repository and selected `SKILL.md` files.
