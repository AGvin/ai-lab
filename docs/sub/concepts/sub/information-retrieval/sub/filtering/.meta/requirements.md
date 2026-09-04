# Documentation Requirements

## Requirements

- Use the reader-facing title `Retrieval Filtering` and introduce `metadata filtering` as the common case represented by the merged legacy source.
- Define retrieval filtering as restricting the eligible retrieval candidate set through explicit predicates or attributes such as source, type, date, version, language, collection, tenant, status, tags, or other structured fields, independently from or alongside relevance ranking.
- Distinguish filtering from relevance scoring. A filter determines eligibility according to a predicate; a lexical, semantic, vector, or reranking score orders or evaluates eligible candidates. One query can use both.
- Explain that filtering may be applied before candidate search, during index traversal/search, after an initial candidate stage, or at several stages; placement affects efficiency and potentially recall but is an implementation contract rather than part of the generic definition.
- Explain that metadata quality, normalization, completeness, update/version semantics, and field cardinality can materially affect filtering behavior. Missing or stale metadata can wrongly exclude or include items.
- Distinguish ordinary search/convenience filters from authorization. Security-sensitive access decisions must be enforced by an authoritative access-control layer/policy and must not rely solely on model-generated filter values, client-side hiding, or untrusted metadata.
- When access-control attributes are also used as retrieval filters, make clear that the filter is an execution mechanism for an already-authorized policy decision rather than the policy authority by itself.
- Explain that filters can interact with approximate vector search, candidate counts, distributed indexes, and post-filtering behavior; do not assume all backends preserve identical recall/performance semantics for the same expression.
- Keep concrete filter languages, database/vector-engine syntax, tenant schemas, ACL/ABAC implementation, index tuning, performance measurements, and product-specific limitations with their applicable engineering, security, catalog, or evidence owners.
- Use the canonical entity references as research inputs for retrieval and authorization boundaries when reader-facing rendering is activated.

## Validation

- The page does not create a separate canonical `metadata-filtering` child.
- Filtering is distinguished from lexical/semantic similarity, ranking, and reranking.
- Search filters are not presented as a substitute for authoritative authorization/access control.
- Pre-filter/post-filter behavior and performance effects are not generalized across all backends.
- Metadata completeness is not assumed, and missing/stale attributes are recognized as a retrieval risk.
- Legacy security guidance is preserved as an ownership/enforcement boundary rather than as a product-specific implementation recipe.
