# Vector Databases

Storage and indexing systems optimized for vectors and similarity search.

## Core idea

Storage and indexing systems optimized for vectors and similarity search. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A vector database stores embeddings together with identifiers, payloads, and metadata.
- It provides vector indexes, filtering, insertion and deletion, and often replication or persistence features.
- The original source remains authoritative; the vector store is a derived search index that must be synchronized.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Vector Databases affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Operate semantic search or RAG over large and changing collections.
- Combine vector retrieval with metadata filters and application-level access control.

## Example

A PostgreSQL application can add pgvector for embeddings while keeping document metadata and permissions in the same database.

## Trade-offs and limitations

- A dedicated vector database may be unnecessary for small corpora that fit an existing database or in-memory index.
- Index updates, deletes, backups, and tenant isolation add operational complexity.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Vector Databases expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../)
- [Vector Search](../vector-search/)
- [Keyword Search](../keyword-search/)
