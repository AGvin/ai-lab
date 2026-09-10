# Documentation Requirements

## Requirements

- Teach GraphRAG as a RAG specialization for workloads where explicit relationships, hierarchy, aggregation, topology, dependencies, ownership, provenance, or multi-hop context materially improve retrieval/context construction.
- Compare GraphRAG against simpler lexical, semantic, hybrid, structured-query, or ordinary RAG baselines under comparable model/context/budget conditions; graph construction and maintenance cost must earn measurable value.
- When nodes/edges are extracted automatically, preserve source evidence and extraction status; validate entity resolution, deduplication, relation typing, temporal qualifiers, and updates according to the domain.
- Retain provenance through entity consolidation, clustering/community summaries, graph compression, and other derived graph artifacts so answers remain traceable to original evidence.
- Evaluate source/graph quality, entity/relation extraction, subgraph retrieval, context organization, and final answer quality separately enough to localize failures.
- Define update/invalidation rules for derived edges, communities, summaries, embeddings, and indexes when underlying evidence changes.
- Do not treat graph adjacency as relevance, graph paths as causality, or graph traversal as a replacement for lexical/semantic retrieval when those signals better fit the query.

## Validation

- Graph structure is introduced only when it materially serves the workload.
- Automatically derived relations are not silently promoted to trusted source facts.
- Provenance survives graph-derived transformations.
- GraphRAG gains are compared against non-graph baselines under comparable conditions.
