# Documentation Requirements

## Identity and provenance

- Identify Granite Embedding 97M Multilingual R2 as the smaller concrete R2 embedding checkpoint.
- Preserve the exact derived-from relation to Granite Embedding 311M Multilingual R2; the authored card documents layer pruning and vocabulary selection rather than an inferred family relationship.

## Operational decision boundaries

- Preserve the documented 32,768-token maximum sequence length and 384-dimensional embeddings.
- Do not inherit the 311M model's Matryoshka output dimensions: the 97M card presents a fixed 384-dimensional output contract.
- Weights state Apache 2.0. Multilingual and code retrieval quality must be validated on the intended corpus and query/document roles.

## Validation

- Membership resolves to Granite Embedding Multilingual R2.
- derived-from resolves reciprocally to the 311M node's has-derivative relation.
- This assessment grants no runtime or benchmark-reproduction credit.
