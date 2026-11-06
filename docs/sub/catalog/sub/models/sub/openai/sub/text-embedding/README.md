# OpenAI Text Embedding

OpenAI’s text-embedding family maps text to vectors for tasks such as semantic search, clustering, and classification. The represented third-generation models are text-embedding-3-small and text-embedding-3-large.

## Profile

The v3 models support a dimensions parameter for shortening vectors. The older text-embedding-ada-002 remains outside this family’s materialized members [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).

## Operating boundaries

The Embeddings API produces vector representations; it is separate from the vector store and retrieval application. Model choice and output dimensionality affect the index configuration [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).

A similarity score is not verification that a claim is true or that a document is authorized for a user. Retrieval access controls belong to the application.

## Child pages

- [Models](sub/models/README.md).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).
- Member: [text-embedding-3-large](sub/models/sub/text-embedding-3-large/README.md).
- Member: [text-embedding-3-small](sub/models/sub/text-embedding-3-small/README.md).

## Official resources

- [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).
- [text-embedding-3-small model reference](https://developers.openai.com/api/docs/models/text-embedding-3-small).
- [text-embedding-3-large model reference](https://developers.openai.com/api/docs/models/text-embedding-3-large).
