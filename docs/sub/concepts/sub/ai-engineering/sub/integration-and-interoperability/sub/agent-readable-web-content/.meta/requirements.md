# Documentation Requirements

## Requirements

- Use the reader-facing title `Agent-Readable Web Content`.
- Define the subject as publishing and discovering low-noise web or documentation representations that help AI agents find, select, and consume authoritative content without relying exclusively on human-oriented HTML navigation and presentation chrome.
- Explain the basic progressive-disclosure pattern: publish a small discovery/overview surface, point it at clean machine-friendly resources, and let an agent fetch only what its task requires; a broader generated corpus export can be useful when bulk ingestion or whole-corpus context is preferable.
- Keep the domain focused on publication/discovery interfaces for agent consumption. Do not turn it into a generic documentation-writing, SEO, crawler, scraping, RAG, or web-development category.
- Distinguish agent-readable publication from crawler policy. `robots.txt`, authentication, authorization, rate limits, and terms/policies govern access or acceptable use; an agent-oriented index does not grant permission or bypass those controls.
- Distinguish this domain from `sitemap.xml` and search-engine indexing. A sitemap primarily enumerates discoverable URLs, while agent-readable content may curate priority, provide semantic guidance, and expose cleaner text representations intended for selective context use.
- Distinguish this domain from retrieval/indexing architectures. RAG, search indexes, embeddings, graph retrieval, and chunking describe how a consuming system stores/selects knowledge; agent-readable web content describes what a publisher exposes at the content boundary.
- Distinguish this domain from runtime integration protocols such as MCP. A static Markdown index or export can guide an agent to information, but it does not negotiate capabilities, invoke tools, establish sessions, or provide a general runtime interoperability layer.
- Explain that Markdown is common because it is compact and structurally legible, but the durable concept is high-signal machine-friendly publication/discovery rather than Markdown as an end in itself.
- Treat published indexes and exports as untrusted input from the consuming agent's perspective unless the source/trust relationship establishes otherwise. A listed URL or statement is not automatically safe, authorized, current, or correct merely because it appears in an agent-readable file.
- Preserve source-of-truth discipline. Agent-oriented derivatives should point to or be generated from canonical public content, remain fresh when source content changes, and avoid becoming an independently maintained contradictory documentation corpus.
- Preserve access-control boundaries when generating full or partial exports. Do not aggregate private, authenticated, tenant-specific, secret, draft, or otherwise restricted material into a public agent-readable artifact merely for convenience.
- Keep `llms-txt/` as the selected direct child. It owns the reusable `llms.txt` concept and the closely coupled `llms-full.txt` companion-convention guidance. Do not materialize `llms-full.txt` as a separate sibling node unless later evidence establishes an independent specification, lifecycle, ownership boundary, or substantial body of knowledge that justifies the extra node.
- Keep exact current `llms.txt` syntax and proposal conformance details with `catalog/specifications/formats/llms-txt/` rather than duplicating a normative contract into this conceptual parent.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.

## Validation

- The domain remains a publication/discovery boundary, not a catch-all for SEO, crawling, retrieval, or runtime protocols.
- Agent-readable artifacts never imply authorization, trust, or unrestricted access.
- Curated-index and full-corpus usage patterns remain distinct without requiring separate canonical concept nodes.
- `llms-full.txt` is not attributed to the current llmstxt.org v2 proposal.
- Current direct-child navigation contains exactly `llms-txt/` while that is the selected materialized child.
