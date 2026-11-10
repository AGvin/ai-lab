# Documentation Requirements

## Requirements

- Identify MarkItDown as independent Microsoft-origin MIT-licensed Python **document-to-Markdown conversion library and CLI**, rather than an LLM, complete RAG retrieval engine, separately hosted Azure service, benchmark, or pixel-faithful human document renderer.
- Pin primary-source released identity: public **v0.1.9**, published **2026-10-21** as a non-prerelease; tagged `__about__.py` confirms 0.1.9. Tagged `pyproject.toml` declares **Python >=3.10,<3.15**, `markitdown` CLI, MIT license, and optional package extras.
- Explain supported source families and scope: PDF, PowerPoint, Word, Excel, HTML, text formats, ZIP, EPUB, select image/audio and YouTube sources. Preserve text structure for LLM input; not all formats have equal fidelity, and minimal installation does not enable every optional converter.
- Distinguish default package from extras `[pdf]`, `[docx]`, `[pptx]`, `[xlsx]`, `[all]` and optional plugins including OCR/LLM or external transcription; dependencies, privacy, network use and fees can differ. Preserve `markitdown input.pdf -o output.md` as documented CLI example without claiming execution.
- State **I/O permission risk upfront**: original publisher warns conversion can read paths and fetch network resources with caller-process privileges. Sanitize untrusted inputs, restrict file permissions and egress/SSRF surface, avoid unbounded archive extraction, and use narrow `convert_local()` or `convert_stream()` methods for the trust boundary.
- Treat converted documents/web pages as potentially hostile prompt-injection inputs to downstream LLM/agent consumers. Separate optional Azure, LLM, transcription, OCR/plugin processing from purely local conversion, with explicit authorization and privacy, retention, billing and credential controls.
- Separate source code's MIT terms from copyright and redistribution rights of third-party source files, embedded media, plugins, provider model outputs and dependencies. Microsoft is confirmed publisher; full corporate beneficial ownership and indirect Russian-stake checks remain unperformed, so no unsupported Tier 1/2 judgment.
- Maintain one canonical `produced-by` relation to `catalog/producers/m/microsoft` and reciprocal producer `produces`; do not count Microsoft or Microsoft GraphRAG again.

## Validation

- Official tag, code, package metadata and public release establish published software; canonical entity/requirements/reader, parent navigation and producer reciprocal relations must resolve.
- Reader differentiates preprocessing from faithful rendering and hosted APIs; documents actionable untrusted-input controls. No actual converter execution, third-party document handling, broad dependency audit, global schema/cache/render/CI or complete company ownership verification is claimed.
