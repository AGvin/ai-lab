# Perplexity Embeddings API

Perplexity Embeddings API provides hosted access to standard text embeddings and document-context embeddings. The service owns authentication, quotas and request/response behavior; the trained models retain their own catalog identities.

## Use and deployment boundaries

Keep independent inputs separate from grouped document chunks. Match vector dimensions, encoding and similarity function: current guidance uses cosine similarity for unnormalized int8 output and Hamming distance for binary output. Data retention depends on the configured account and applicable API terms.

## Producer

- [Perplexity AI](../../../../../producers/sub/p/sub/perplexity-ai/README.md).

## Official resources

- [API documentation](https://docs.perplexity.ai/docs/embeddings/quickstart).
- [API privacy and retention](https://docs.perplexity.ai/docs/resources/privacy-security).
