# MarkItDown

**MarkItDown** is Microsoft's MIT-licensed Python document-to-Markdown utility and CLI for preparing text and structural context for LLM ingestion. It is separate from [Microsoft GraphRAG](../microsoft-graphrag/), which implements retrieval workflows, and is not a cloud document service or a pixel-faithful PDF/Office renderer.

## Scope and version

- Original public **v0.1.9 (2026-10-21)**; Python **3.10–3.14** according to tagged package metadata (`>=3.10,<3.15`).
- Converts PDF, DOCX, PPTX, XLS/XLSX, HTML, CSV/JSON/XML, ZIP and other selected document/media sources to Markdown that preserves useful headings, lists and table structure. Output is intended for analysis, not exact visual layout reproduction.
- Official CLI: `markitdown report.pdf -o report.md`. Optional extras enable additional converters; media transcription, image description, third-party plugins and some URL conversion paths may depend on external packages or paid/model services.

## Safety and data handling

**Original source warns that conversion uses its process's file and network privileges.** For untrusted local paths, archives and remote URLs, restrict filesystem access and network destinations (including SSRF-sensitive local endpoints); sanitize the source and use a narrow `convert_local()` or `convert_stream()` route when practical. Limit resources and do not expose production credentials.

Converted source content can carry prompt-injection instructions; downstream agents must treat it as **data**. External OCR/LLM, Azure or speech services may receive document content and create separate cost, consent, privacy and retention obligations. MIT licensing of the converter does not license third-party source documents or plugin assets.

## Relations

- Produced by: [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/).
- Different purpose: [Microsoft GraphRAG](../microsoft-graphrag/) provides graph-based retrieval.

## Original sources

- [Original repository](https://github.com/microsoft/markitdown)
- [v0.1.9 release](https://github.com/microsoft/markitdown/releases/tag/v0.1.9)
- [Python package](https://pypi.org/project/markitdown/)
- [Tagged package metadata](https://github.com/microsoft/markitdown/blob/v0.1.9/packages/markitdown/pyproject.toml)
- [Tagged conversion and security guidance](https://github.com/microsoft/markitdown/blob/v0.1.9/README.md)
