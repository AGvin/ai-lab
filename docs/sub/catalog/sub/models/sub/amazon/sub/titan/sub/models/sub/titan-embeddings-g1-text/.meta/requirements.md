# Documentation Requirements

## Requirements

- Identify Amazon Titan Embeddings G1 - Text at canonical ID `catalog/models/amazon/titan/models/titan-embeddings-g1-text`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Distinct Titan G1 text embedding identity, currently marked Active in its Bedrock card. The route amazon.titan-embed-text-v1 uses Invoke and an inputText request to produce a vector and token count; it is not a Converse text-generation model. Do not apply Titan V2 dimensionality, normalization or binary-output options to this G1 request schema.
- The current card marks `amazon.titan-embed-text-v1` Active and lists an 8K-token context with text input and embedding output. [Titan Embeddings G1 Text model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html)
- The G1 request accepts `inputText` and returns an embedding with `inputTextTokenCount`. V2-only options for dimensions, normalization and binary output must not be applied to G1. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html)
- Use the model-specific Invoke request. The card does not support Converse; a vector response is an input to retrieval or similarity logic rather than an assistant answer. [Titan Embeddings G1 Text model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html)
