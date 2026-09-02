# Semantic Search

Legacy residual retained for retrieval-composition, candidate-evaluation, access-control, and application-guidance material that are intentionally outside the canonical Semantic Retrieval concept owner.

> **Migration note:** Semantic-retrieval identity, learned-representation matching, dense-retrieval implementation boundaries, semantic-versus-vector and semantic-versus-lexical distinctions, similarity non-guarantees, and representation/domain/segmentation dependence are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/semantic-retrieval/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, security, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application-pattern residual

Semantic retrieval is commonly useful for natural-language questions, paraphrase-heavy or cross-lingual search, conceptually related code/tickets/notes, and intent-oriented matching. Treat these as application patterns to evaluate rather than guarantees that semantic retrieval will outperform lexical or structured methods for every corpus.

When exact identifiers, rare names, version strings, error codes, legal citations, negation, or other surface-form evidence matters, combine semantic signals with lexical, structured, or hybrid retrieval as appropriate instead of forcing one retrieval mode to solve every query type.

## Retrieval-composition residual

Useful application practices include:

- apply metadata or structured filters when the task has explicit scope, tenant, type, date, permission, or other constraints;
- use reranking when the initial semantic candidate set is broad and a stronger second-stage relevance model materially improves ordering;
- preserve lexical or exact-match routes for identifiers and other evidence that representation similarity can blur;
- enforce access-control filtering as part of the retrieval path rather than treating semantic relevance as authorization.

## Evaluation residual

Evaluate representative domain queries at several candidate counts instead of judging only the top result. Measure whether the candidate set contains answer-bearing evidence, not merely topically related passages, and inspect misses caused by representation choice, segmentation, filters, domain shift, or exact-term requirements.

Do not treat nearest neighbors or high similarity values as verified answers. The downstream system still needs whatever evidence, validation, grounding, or application checks the task requires.

These composition, evaluation, security, and application practices remain migration source material until their exact learning, retrieval-engineering, evaluation, security, or decision-support owners are verified.
