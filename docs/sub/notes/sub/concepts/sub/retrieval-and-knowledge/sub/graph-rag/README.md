# GraphRAG

Legacy residual retained for application selection, graph-construction verification, provenance maintenance, baseline comparison, and operational-cost guidance that are intentionally outside the canonical GraphRAG concept owner.

> **Migration note:** GraphRAG identity, RAG-subtype ownership, knowledge-graph versus GraphRAG separation, graph-source variability, acquisition/indexing/retrieval/context stages, structural-connectivity versus relevance/causality boundaries, fallible extraction, freshness, staged evaluation, and non-guarantees for grounding or reasoning are already preserved in `docs/sub/concepts/sub/ai-engineering/sub/architectures-and-patterns/sub/rag/sub/graph-rag/`. The remaining material below stays here until its exact learning, graph/retrieval-engineering, evaluation, operations, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application-selection residual

Use graph structure when the target questions materially depend on relationships, hierarchy, aggregation, topology, dependencies, ownership, provenance, or multi-hop context. Typical candidates include cross-document entity questions, dependency/impact investigation, organization/project relationships, code or service dependency analysis, and corpus-level sensemaking.

Compare against simpler lexical, semantic, hybrid, structured-query, or ordinary RAG baselines. A graph adds construction and maintenance cost and should not be introduced merely because the source corpus contains entities and relationships.

## Construction and provenance residual

When nodes or edges are extracted or generated automatically, preserve source evidence and extraction status so plausible but unsupported relationships do not silently become trusted facts. Entity resolution, deduplication, relation typing, temporal qualifiers, and graph updates need explicit validation appropriate to the domain.

Retain provenance through entity consolidation, clustering/community summaries, graph compression, and derived graph artifacts so an answer can be traced back to the source evidence rather than only to a generated graph node or summary.

## Evaluation and operations residual

Evaluate graph/source quality, entity/relation extraction, retrieval/subgraph selection, context organization, and final answer quality separately enough to diagnose failures. Compare GraphRAG with non-graph baselines under comparable context/model/budget conditions so gains are not incorrectly attributed to graph structure.

Track update/freshness behavior when underlying documents or records change. Derived edges, communities, summaries, embeddings, and indexes can become stale independently and need invalidation or rebuild rules.

Do not treat graph adjacency as relevance, a graph path as causality, or graph traversal as a replacement for lexical/semantic retrieval when those signals better match the query.

These application-selection, construction, provenance, evaluation, and operational practices remain migration source material until their exact learning, graph/retrieval-engineering, evaluation, operations, or decision-support owners are verified.
