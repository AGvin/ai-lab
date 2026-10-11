# Documentation Requirements

## Requirements

- Catalog Diffbot as a producer-operated structured web extraction and independently maintained knowledge-graph access service. Preserve separate Extract/Analyze page-to-JSON content recognition, Knowledge Graph DQL search and Enhance entity enrichment surfaces within one service family.
- Distinguish querying preassembled Diffbot Knowledge Graph entities from on-demand web-page rendering/extraction, and distinguish both from generic direct web search or a reusable local NLP library.
- The first-party Extract API includes stable article/product/media/discussion endpoints while List, Event and Job extraction can be designated BETA in current docs; preserve feature-specific maturity rather than treating the entire service as experimental.
- Treat extracted organization/individual facts, provenance, crawl freshness, entity matching/confidence, schema versions, rate/credit usage, and retention as mutable. Correlate to original sources for decision-making; automated enrichment can be incomplete or incorrect.
- Preserve legitimate content access, reuse rights and privacy rules, especially for person profiles and company data; do not present commercial graph access as a license for unrestricted downstream republishing.
- Keep only a canonical Diffbot producer and direct inverse relation, not a separate producer for its query language or data-collection methods.

## Validation

- Published first-party documentation demonstrates a live publicly documented hosted service rather than roadmap-only capability.
- Scope/feature maturity and site/data access limits are source-backed and not overgeneralized.
- Exact `produced-by` relation has an inverse `produces` link in the named vendor producer.
