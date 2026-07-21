# Knowledge Graphs

A knowledge graph represents entities and their relationships as structured nodes and edges, often with types, properties, and provenance.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Graphs make relationships directly queryable. Instead of searching only for text that mentions two concepts, a graph can represent that one service depends on another, a person owns a project, or a document supersedes an older version.

## Practical use

- Organizational and asset relationships.
- Dependency and impact analysis.
- Entity resolution across multiple datasets.
- Multi-hop queries and graph-based retrieval.
- Integrating structured and unstructured knowledge.

## Design considerations

Define an ontology or schema that explains entity and relationship types. Assign stable identifiers. Track where every fact came from and when it was valid. Separate asserted facts from inferred relationships.

## Trade-offs and limitations

Knowledge graphs require governance, entity resolution, and continuous updates. Automatically extracted graphs can contain duplicates and incorrect edges. A rigid ontology may also fail to represent evolving domain knowledge.

## Common mistakes

- Creating nodes from every noun without a stable identity strategy.
- Omitting temporal validity and source provenance.
- Treating graph completeness as guaranteed.
- Using a graph where a relational table or document index would be simpler.

## Related concepts

- [Retrieval and Knowledge](../../)
- [GraphRAG](../graph-rag/)
- [Metadata Filtering](../metadata-filtering/)
- [Provenance](../../../safety-privacy-and-reliability/sub/provenance/)