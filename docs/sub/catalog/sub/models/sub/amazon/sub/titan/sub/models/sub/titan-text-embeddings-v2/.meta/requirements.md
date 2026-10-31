# Documentation Requirements

## Requirements

- Identify Amazon Titan Text Embeddings V2 at canonical ID `catalog/models/amazon/titan/models/titan-text-embeddings-v2`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Distinct Titan V2 embedding identity with Active Bedrock route amazon.titan-embed-text-v2:0. Input is bounded by 8192 tokens or 50000 characters. Dimensions are 1024 by default, 512 or 256; normalization defaults to true. A binary-only request omits the top-level embedding field and uses embeddingsByType. V2 generates retrieval vectors rather than text; language and cross-language quality need workload validation.
- The current card marks `amazon.titan-embed-text-v2:0` Active and supports text input with embedding output through Invoke. [Titan Text Embeddings V2 model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-text-embeddings-v2.html)
- The guide bounds input at 8192 tokens or 50,000 characters. It recommends logical document chunks, describes optimization for English and cautions that cross-language retrieval can perform poorly. [Titan Text Embeddings V2 guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html)
- Choose 1024 (default), 512 or 256 dimensions. Normalization defaults to true. `embeddingTypes` selects floating-point, binary or both representations; a binary-only response omits the top-level `embedding` and returns `embeddingsByType`. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html)
