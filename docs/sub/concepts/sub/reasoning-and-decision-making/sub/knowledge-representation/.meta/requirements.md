# Documentation Requirements

## Requirements

- Use the reader-facing title `Knowledge Representation`.
- Define knowledge representation as the design and use of machine-processable structures and semantics that stand for relevant aspects of a domain so systems can store, query, communicate about, infer over, constrain, plan with, or otherwise operate on represented knowledge.
- Make clear that a representation is a model or commitment about a domain, not the domain itself and not a guarantee that represented claims are true, complete, current, or unbiased.
- Distinguish knowledge representation from raw data storage or serialization. Tables, JSON documents, graphs, vectors, files, or databases become knowledge representations only through the identities, semantics, constraints, relations, interpretation rules, and intended operations attached to them; a file format or storage engine alone is not the concept.
- Cover common representational ingredients as families rather than mandatory features: entities/objects, classes/types, properties, relations, events, states, rules, constraints, temporal/contextual qualifiers, uncertainty, provenance, and identity links can all be represented depending on the formalism and task.
- Distinguish syntax from semantics. Two systems can serialize similar structures while assigning different meanings, identity rules, inference assumptions, or validity conditions; interoperable representation requires the relevant semantic contract, not only matching field names or graph shapes.
- Explain ontological commitment as choosing which kinds of things and relations a representation distinguishes and how they may be combined. An ontology or explicit schema can formalize this commitment, but not every knowledge representation requires the same ontology language or level of formalization.
- Explain inference as one possible role rather than a universal requirement. A representation may support deduction, rule application, constraint checking, probabilistic reasoning, search, graph traversal, planning, or simple explicit query without requiring a general-purpose automated reasoner.
- Distinguish asserted, observed, imported, extracted, derived, and inferred knowledge where the distinction matters. Derived conclusions should not be silently treated as equivalent to source assertions when provenance or auditability is required.
- Treat provenance, temporal validity, source scope, confidence/uncertainty, and authority as representational context when claims can change or conflict. A bare proposition without its applicability conditions can be misleading even when its syntax is valid.
- Distinguish open-world and closed-world assumptions, unique-name assumptions, default reasoning, monotonic/non-monotonic behavior, and other logical conventions as design choices of particular formalisms or systems rather than universal knowledge-representation rules.
- Distinguish explicit knowledge representation from learned representation under `machine-learning/representation-learning/`. Embeddings and latent features can support reasoning/retrieval and can encode useful structure, but their learned geometry is not automatically an explicit symbolic/semantic knowledge model.
- Explain that hybrid systems can combine explicit structured knowledge with learned representations, retrieval, probabilistic models, rules, search, or neural models; primary ownership follows the represented knowledge semantics rather than the implementation mix.
- Keep `knowledge-graphs/` as the currently selected direct child and do not infer additional descendants such as ontologies, semantic networks, frames, logic programming, RDF, graph databases, or rule systems unless architecture selects them explicitly.
- Keep concrete ontologies, schemas, taxonomies, knowledge bases, graph datasets, query languages, reasoning engines, software products, domain vocabularies, and project-specific representation models with their applicable catalog/project/specification owners.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Use the canonical entity reference as a research input for the broad roles and trade-offs of knowledge representation when reader-facing rendering is activated.

## Validation

- Knowledge representation is not equated with a database, file format, graph, ontology, RDF, or rule engine alone.
- The represented model is not presented as complete or objectively true merely because it is explicit or machine-readable.
- Syntax/storage and semantic commitments are distinguished.
- Automated inference is treated as optional/formalism-dependent rather than mandatory for every representation.
- Learned embeddings/latent representations are kept distinct from explicit knowledge representation while allowing hybrid use.
- Concrete ontologies, schemas, knowledge bases, software, and domain-specific models remain outside the reusable parent owner.
- Direct-child navigation contains only currently materialized selected descendants.
