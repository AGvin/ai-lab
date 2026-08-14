# Anthropic Skills

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

## Official resources

- [Anthropic Skills repository](https://github.com/anthropics/skills)
