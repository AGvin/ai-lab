# Documentation Requirements

## Requirements

- Use the reader-facing title `llms-full.txt` and identify it as an **ecosystem convention** for publishing a large single-file Markdown representation of a documentation corpus or substantial site content for AI ingestion/context use.
- State the standards boundary prominently: the current llmstxt.org v2 proposal defines `llms.txt` but does not currently define `llms-full.txt`. Do not present `llms-full.txt` as a mandatory llmstxt.org file or formal companion specification unless the upstream proposal changes.
- Explain the core contrast:
  - `llms.txt` is a small curated index that helps an agent decide what to fetch;
  - `llms-full.txt` provides much broader or full content in one fetch so a consumer can ingest, index, search, cache, or supply the corpus as context without traversing many links.
- Explain appropriate uses: small-to-medium documentation corpora that fit the consumer's context/ingestion budget; offline or batch indexing; evaluation/research snapshots; tools that can ingest one remote document; and workflows where broad cross-page context is more useful than selective navigation.
- Explain when not to load it blindly: large documentation sites, narrow questions, expensive context windows, high-change corpora, bandwidth-sensitive clients, or cases where selective retrieval from `llms.txt` is substantially cheaper and more precise.
- Teach the practical consumption workflow:
  1. inspect source, freshness, visibility, and approximate size before loading;
  2. determine whether the task needs whole-corpus context or selective retrieval;
  3. ingest/index or attach the file only when the consumer can handle its size safely;
  4. retain page/source boundaries and citations when downstream tooling supports them;
  5. refresh or invalidate derived indexes when the source corpus changes.
- Teach the publishing workflow as generation rather than duplicate authoring:
  1. select the canonical public corpus;
  2. export pages to clean Markdown or equivalent text;
  3. preserve page titles/source URLs or stable boundaries so provenance survives concatenation;
  4. concatenate deterministically;
  5. exclude private, authenticated, draft, secret, tenant-specific, or otherwise non-public material;
  6. regenerate on publication changes;
  7. validate size, completeness, links/source markers, and access behavior.
- Recommend automatic generation for frequently changing documentation. A hand-maintained `llms-full.txt` should not become a second source of truth that silently diverges from the public docs.
- Explain that "full" is an implementation convention rather than a guarantee of mathematically complete site coverage. Publishers should document exclusions, auth boundaries, unsupported page types, generated content, or other material omissions when they matter.
- Explain scaling trade-offs: a single file reduces multi-page fetch overhead and can simplify bulk ingestion, but increases transfer size, context/token cost, duplication, cache invalidation scope, and the risk that a consumer loads far more information than the task requires.
- Explain privacy/security trade-offs: corpus aggregation can accidentally make sensitive material easier to discover or copy. Generation must respect the same or stricter publication/access boundaries as the underlying pages; the file is not an authorization bypass.
- Preserve prompt-injection/trust boundaries. A full export can amplify malicious or untrusted instructions by concentrating content; consumers must still apply source trust, instruction hierarchy, sanitization, and action authorization controls.
- Explain freshness: include or preserve source/page provenance where possible, regenerate predictably, and avoid treating a cached full export as current when its source corpus has changed.
- Recommend pairing the convention with `llms.txt` rather than treating them as mutually exclusive: the small index supports selective discovery while the full export supports bulk-context/ingestion workflows.
- Include a concise comparison table covering purpose, typical size, consumption model, strengths, and principal risks for `llms.txt` versus `llms-full.txt`.
- Use GitBook and Mintlify only as ecosystem implementation evidence; do not treat one vendor's exact output structure, size policy, hosting path, or generation behavior as a universal `llms-full.txt` specification.
- Treat client/crawler adoption, observed traffic, indexing behavior, and platform implementation details as mutable evidence rather than guaranteed behavior.

## Validation

- The page clearly states that current llmstxt.org v2 does not define `llms-full.txt`.
- `llms-full.txt` is not treated as universally required or as a ratified standard.
- Whole-corpus convenience is balanced against context size, bandwidth, freshness, duplication, privacy, and trust risks.
- Publishing guidance favors deterministic generation from canonical public content rather than manual duplication.
- Vendor implementation details remain examples/evidence rather than universal format rules.
- The comparison with `llms.txt` preserves their distinct use cases: selective discovery versus bulk/full-context export.
