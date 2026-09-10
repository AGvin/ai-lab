# Documentation Requirements

## Requirements

- Present `llms.txt` as the current llmstxt.org v2 **proposal / emerging convention**, not as a ratified IETF, W3C, or universally required web standard.
- Keep this node as the formal proposal/format owner. Reusable explanation, usage guidance, trade-offs, and reader mental models belong to the `concepts/ai-engineering/integration-and-interoperability/agent-readable-web-content/llms-txt/` concept.
- Preserve the current path-scoping contract: an `llms.txt` file may be published at `/llms.txt` or under another path such as `/docs/llms.txt`; it describes pages under its path, and when several files apply the most specific applicable one should be used.
- Preserve the current ordered Markdown structure without inventing mandatory fields: optional BOM; one H1 project/site name as the only required section; optional blockquote summary; optional non-heading detail; then zero or more H2-delimited file-list sections.
- Preserve current file-list syntax at a normative level: each list item contains a required Markdown link and may contain a colon followed by notes about that resource.
- Record `## Optional` as a convention for secondary resources that an agent may skip when context must be constrained; do not reinterpret it as a universal Markdown keyword outside this proposal.
- Preserve the proposal's progressive-disclosure intent: keep the index concise, point to detailed LLM-friendly resources, and let agents follow only the links needed for the current task.
- Preserve the current recommendation that useful pages may expose Markdown alternatives through appended/replaced `.md` URLs and advertise them with `rel="alternate" type="text/markdown"`; preserve `rel="describedby"` as the proposed way to identify the applicable `llms.txt` file. Keep exact HTTP/HTML linkage details source-backed to the current upstream proposal.
- Keep `llms.txt` distinct from `robots.txt`, `sitemap.xml`, crawler permissions, authentication/authorization, search indexing, RAG infrastructure, and runtime interoperability protocols.
- Treat proposal revision, exact syntax details, adoption examples, implementation tooling, and current ecosystem behavior as freshness-sensitive. Re-check `llmstxt.org` and the upstream repository before changing normative claims.
- Explicitly state that the current upstream v2 proposal does not define `llms-full.txt`. Do not import ecosystem-specific `llms-full.txt` conventions into this formal artifact unless the upstream proposal changes.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the official llmstxt.org proposal and current upstream repository.

## Validation

- The page never upgrades a proposal/emerging convention into a ratified web standard.
- H1 remains the only required content section under the current v2 proposal; optional elements are not mislabeled as mandatory.
- Path-scoping and most-specific-file semantics match the current upstream proposal.
- `llms-full.txt` is not represented as a current v2 requirement or artifact.
- `llms.txt` is not presented as access-control, crawler-policy, sitemap, retrieval, or protocol functionality.
- The `produced-by` relation resolves to Jeremy Howard and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection.
