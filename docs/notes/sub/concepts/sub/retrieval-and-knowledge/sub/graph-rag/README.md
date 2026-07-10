# GraphRAG

<!--
ai_content:
  managed: true
  l10n: true
-->

GraphRAG is a Retrieval-Augmented Generation approach that uses entities, relationships, communities, or graph traversal to assemble context.

## Core idea

Conventional RAG usually retrieves independent text chunks. GraphRAG adds structure that can connect information distributed across documents, such as people linked to projects, services linked to incidents, or concepts linked through citations. The graph may be created from an existing knowledge graph or extracted from text.

## Practical use

- Questions requiring multi-hop relationships.
- Summaries across many connected entities or documents.
- Investigation of dependencies, ownership, or causal chains.
- Navigation through organizational or technical knowledge.

## Trade-offs and limitations

Graph construction is expensive and error-prone. Entity extraction, deduplication, and relationship typing can introduce false links. Graph traversal may also retrieve structurally connected but semantically irrelevant information.

## Good practice

Preserve source evidence for every node and edge. Evaluate graph extraction separately from answer generation. Use graph retrieval only where relationships add value; simple factual lookups may work better with ordinary hybrid search.

## Common mistakes

- Treating automatically extracted relationships as verified facts.
- Building a graph without a question class that needs it.
- Losing document provenance after entity consolidation.
- Assuming graph traversal replaces lexical and semantic retrieval.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Knowledge Graphs](../knowledge-graphs/)
- [RAG](../rag/)
- [Provenance](../../../safety-privacy-and-reliability/sub/provenance/)
