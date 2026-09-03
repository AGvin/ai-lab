# Documentation Requirements

## Requirements

- Teach tokenization as converting raw model input into tokenizer-specific units and IDs; tokens are not universal words, characters, bytes, or semantic concepts.
- Explain that vocabulary, normalization, pre-tokenization, special tokens, and segmentation rules vary across tokenizers/model families, so the same string can have different token counts and boundaries.
- Use the applicable tokenizer or encoding contract when estimating whether input plus expected output fits a concrete context/request budget; generic character-to-token heuristics are only rough estimates.
- Distinguish model tokenization from provider billing/accounting categories. Providers may separately count cached input, generated output, reasoning/internal compute, images, audio, or other service-specific units; those categories are mutable provider facts and must be checked against the concrete service.
- For cost diagnosis, inspect token-dense material such as logs, source code, structured data, and large documents and use the provider's current billable-unit rules rather than assuming all tokens have one universal price/accounting treatment.
- For token-budget-sensitive retrieval/chunking, use the tokenizer/encoding relevant to the embedding or generation pipeline and link corpus-specific segmentation design to Indexing and Chunking.
- Keep concrete tokenizer vocabularies, provider prices/limits/accounting categories, and current service behavior source-backed with catalog/evidence owners.

## Validation

- Token count is not inferred from words or characters as an exact universal conversion.
- Provider billing units are not redefined as intrinsic token semantics.
- Retrieval chunk sizing uses the relevant downstream encoding when a token budget is material.
