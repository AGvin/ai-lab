# Anthropic Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Anthropic Skills is Anthropic's public repository of skills for Claude. AI Lab currently focuses on the source-available document skills published there.

## Producer

- [Anthropic](../../../../../producers/sub/a/sub/anthropic/)

## Selected skills

| Skill | Purpose | Official source |
| --- | --- | --- |
| DOCX | Create, read, edit, redline, comment on, and verify Word documents. | [Source](https://github.com/anthropics/skills/tree/main/skills/docx) |
| PDF | Read, extract, create, combine, transform, fill, protect, and OCR PDF files. | [Source](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| PPTX | Create, read, edit, render, and verify PowerPoint presentations. | [Source](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| XLSX | Create, read, edit, format, recalculate, and validate spreadsheets. | [Source](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

### DOCX

The DOCX skill covers both high-level document creation and lower-level editing of existing Office XML packages. Depending on the operation, its current upstream workflow uses the `docx` package, Pandoc, LibreOffice, Poppler, Python helpers, and bundled scripts for conversion, XML run handling, comments, tracked changes, and validation.

### PDF

The PDF skill covers extraction and table reading, PDF creation, merge/split/rotation, forms, protection, image extraction, and OCR. Its toolchain is operation-dependent and includes libraries such as `pypdf`, `pdfplumber`, and `reportlab`, with additional PDF/OCR utilities and bundled advanced and form-processing references where needed.

### PPTX

The PPTX skill covers presentation creation, reading, editing, rendering, and visual or structural verification. Its current upstream workflows use `pptxgenjs`, Python, LibreOffice, Poppler, and `markitdown` where applicable, with bundled helpers for thumbnails, slide manipulation, cleanup, Office conversion, and package validation.

### XLSX

The XLSX skill covers spreadsheet creation and editing, data handling, formatting, formula recalculation, and validation. Its current workflow uses `openpyxl`, `pandas`, `markitdown`, and LibreOffice where applicable, together with bundled recalculation and validation helpers.

## Installation

Anthropic's repository exposes the document skills through its `document-skills` plugin flow. Runtime dependencies still vary by skill and by operation, so installing the collection does not make every listed dependency mandatory for every task.

## Source interpretation

Anthropic's public collection contains illustrative skills and service-governed document implementations. The four document LICENSE.txt files use Anthropic agreement terms with additional restrictions on extraction, copying, derivative works and redistribution; they are not Apache-2.0 examples. Check the selected path and applicable agreement. Examples and hosted Claude behavior can differ.

[Reviewed original README](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Anthropic Skills repository](https://github.com/anthropics/skills)
