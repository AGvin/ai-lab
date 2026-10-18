# Documentation Requirements

## Requirements

- Identify `text-embedding-3-large` as OpenAI's current highest-capability text embedding model.
- Preserve the current default 3072-dimensional output, 8192-token maximum input, text-only input-to-vector role, multilingual positioning, and dimension-shortening support only while current first-party documentation supports those facts.
- Treat MTEB values and comparative quality claims as provider/evaluation evidence rather than universal retrieval quality.
- Keep API pricing, rate limits, batch behavior, encoding format, regional processing, and vector-store integration freshness-sensitive.

## Validation

- The model remains distinct from the smaller `text-embedding-3-small` member.
- Vector dimensionality does not by itself establish downstream retrieval quality.

## Source-scoped operating boundaries

- Vector length is an adjustable representation choice, not proof of downstream retrieval quality. Choose and evaluate the dimensions used by the index and queries together [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).
- Vectors from different model/configuration spaces should not be compared as if interchangeable. The retrieval application still controls which source documents a user may access.

## Source evidence

- [text-embedding-3-large model reference](https://developers.openai.com/api/docs/models/text-embedding-3-large).
- [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).
