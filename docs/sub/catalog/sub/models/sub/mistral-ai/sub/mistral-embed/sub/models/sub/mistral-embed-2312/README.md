# Mistral Embed 2312

Mistral Embed 2312 is Mistral AI’s general text-embedding model, released in December 2023.

## Translations

- English

## Relations

- Family: [Mistral Embed](../../../../)

## Model profile

The model card lists the GA Premier identifier `mistral-embed-2312` and an 8K-token context. [Mistral Embed model card](https://docs.mistral.ai/models/mistral-embed-23-12)

The `mistral-embed` interface produces a 1,024-dimensional vector for each text input. [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings)

## Operational boundaries

Keep document and query embeddings in the same model space and dimension. Similarity is a retrieval signal, not an accuracy or access-control decision. [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings)

Codestral Embed’s code specialization and configurable output dimensions do not transfer to this checkpoint.

## Official resources

- [Mistral Embed model card](https://docs.mistral.ai/models/mistral-embed-23-12)
- [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings)
