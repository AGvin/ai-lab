# Documentation Requirements

## Requirements

- Use the reader-facing title `Knowledge Graphs`.
- Define a knowledge graph as a graph-organized knowledge representation in which identifiable entities, concepts, values, claims, or other represented items are connected through semantically meaningful relationships and may also carry types, properties, qualifiers, provenance, or contextual metadata.
- Distinguish a knowledge graph from an arbitrary graph data structure. The graph's nodes/edges must participate in a knowledge model with explicit or otherwise defined identity/meaning/relationship semantics; a network topology or generic graph algorithm input is not automatically a knowledge graph.
- Distinguish a knowledge graph from a graph database. A graph database is a storage/query implementation family; it can host a knowledge graph, a non-knowledge property graph, or other graph-shaped data. Conversely, a knowledge graph can be represented without a dedicated graph database.
- Do not require RDF. RDF/RDF datasets are one standardized graph-based data model using subject-predicate-object triples; property graphs, labeled graphs, hypergraph-like structures, domain-specific graph models, and other representations can also support knowledge-graph semantics.
- Do not require every knowledge graph to use triples, OWL, SPARQL, a formal ontology, or a general-purpose automated reasoner. These are important representation/query/reasoning options, not universal defining features.
- Explain schema/ontology use as a spectrum. Some knowledge graphs use explicit classes, properties, constraints, ontologies, or shapes; others use lighter schemas, conventions, inferred types, or partially structured vocabularies. The chosen semantics and validation assumptions must be explicit enough for the intended use.
- Treat stable identity and entity resolution as core design concerns. Multiple names, aliases, records, URLs, database keys, or extracted mentions can refer to the same real-world or abstract entity, while superficially similar mentions can refer to different entities.
- Distinguish entities/concepts from literals/attributes and relationships where the representation makes that distinction. Do not create a separate node for every surface string or noun without an identity/semantic reason.
- Distinguish asserted/imported facts from extracted, inferred, predicted, or generated edges/claims. Systems should preserve the status and provenance of derived knowledge when users must know whether a relation came from a source assertion, rule inference, model extraction, or another process.
- Treat provenance and source authority as first-class context when claims can conflict, change, or require verification. A graph edge is not automatically true merely because it exists in the graph.
- Represent temporal validity and context where relevant. Facts such as employment, ownership, dependency, price, membership, software compatibility, or organizational structure can be valid only during a time interval, in one jurisdiction, tenant, environment, version, or source context.
- Do not assume completeness. Missing nodes/edges can mean unknown, not represented, filtered, inaccessible, out of scope, or false depending on the graph's explicit semantics; closed-world assumptions must be documented rather than inferred from absence.
- Explain constraints/validation and reasoning separately. Schema validation can check structural/semantic conditions without deriving new facts; inference can derive additional claims from rules/ontologies/statistical models; either can exist without the other.
- Explain graph traversal and multi-hop querying as capabilities enabled by explicit relationships, not as proof that long paths are semantically valid or causally meaningful. Path interpretation depends on relation types, direction, qualifiers, and domain semantics.
- Distinguish knowledge graphs from knowledge-graph embeddings. Embedding entities/relations into learned vector spaces is a downstream representation-learning technique for prediction, similarity, completion, or retrieval; the embedding is not the graph's complete explicit semantic representation.
- Explain knowledge-graph construction as a separate process family. Graphs can be authored, imported from structured sources, integrated across systems, extracted from text/media, generated from models, or combined; extraction/generation introduces entity-resolution, duplication, provenance, confidence, and error-management obligations.
- Treat inferred or automatically extracted relations as fallible unless validated. Language-model or information-extraction output can create plausible but unsupported nodes/edges and must not silently become trusted canonical facts.
- Explain that knowledge graphs can support integration, semantic query, dependency/impact analysis, entity-centric search, reasoning, recommendations, retrieval, and graph-based AI workflows, while remaining distinct from those downstream application architectures.
- Keep `GraphRAG` outside this node. A GraphRAG system may use a knowledge graph or graph-derived structure as a retrieval/reasoning substrate, but `graph-rag/` remains a separate architecture-gap descendant under the selected RAG owner until explicitly resolved.
- Keep concrete graph databases, knowledge-graph products/services, domain ontologies, schemas, vocabularies, query languages, named knowledge bases/datasets, graph instances, extraction pipelines, benchmark results, and project-specific graph designs with their applicable catalog/specification/project/evidence owners.
- Use the canonical entity references as research inputs for broad knowledge-graph data-model, semantic, query, validation, ontology, and reasoning boundaries when reader-facing rendering is activated.

## Validation

- A knowledge graph is not equated with any graph-shaped dataset or graph database.
- RDF/triples, OWL, SPARQL, explicit ontologies, and automated reasoning are not presented as universal requirements.
- Node/edge existence is not treated as proof of truth, completeness, currency, or provenance.
- Entity identity, source/provenance, temporal/contextual validity, and asserted-versus-derived status remain explicit design concerns.
- Missing graph facts are not automatically interpreted as false without a documented closed-world assumption.
- Knowledge-graph embeddings and GraphRAG are kept distinct from the canonical knowledge-graph concept.
- Concrete products, ontologies, datasets, graphs, extraction pipelines, benchmarks, and project-specific schemas remain outside the reusable concept owner.
