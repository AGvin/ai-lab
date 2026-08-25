# Documentation Requirements

## Requirements

- Use the reader-facing title `Semantic Retrieval` and introduce `semantic search` as a common practical label rather than a separate canonical leaf.
- Define semantic retrieval as retrieval that uses learned or otherwise meaning-oriented representations/matching so items can be considered relevant even when query and candidate do not share the same surface terms.
- Present dense dual-encoder retrieval as an important modern implementation pattern, while avoiding the claim that all semantic retrieval must use one embedding model, one dense-vector representation, or one nearest-neighbor index.
- Distinguish semantic retrieval from `vector-search/`: semantic retrieval describes the retrieval objective/matching semantics, while vector search is a mathematical/indexing mechanism over vector representations and can operate on vectors whose meaning is not semantic language similarity.
- Distinguish semantic retrieval from lexical retrieval. Semantic methods can bridge paraphrases or related wording but can also miss exact identifiers, rare strings, negation, or other distinctions that lexical evidence preserves.
- Explain that learned similarity or representation distance is a retrieval signal, not a calibrated probability that the candidate contains the answer, is factually correct, or satisfies the final task.
- Make clear that representation model, training objective, query/document encoding, corpus/domain shift, segmentation, and evaluation set can materially change retrieval behavior.
- Keep the unresolved generic `embeddings/` concept as an architecture gap; refer to learned vector representations descriptively without creating or implying an unselected embedding leaf.
- Keep concrete embedding models, vector dimensions, similarity thresholds, indexes, product settings, benchmark results, access-control policy, and application-specific retrieval recommendations with their applicable catalog, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for learned dense retrieval and semantic-matching boundaries when reader-facing rendering is activated.

## Validation

- The page does not create a separate canonical `semantic-search` child.
- Semantic retrieval is not equated with vector search, embeddings, or one nearest-neighbor implementation.
- Learned similarity is not presented as factuality or answer-correctness evidence.
- The page preserves the lexical-versus-semantic distinction without claiming either class universally dominates the other.
- The blocked `embeddings/` concept is not implicitly materialized.
- Legacy operational recommendations are not copied as universal guidance.
