# Amazon Titan Embeddings G1 - Text

Amazon Titan Embeddings G1 - Text is the Titan text-to-vector model identified by the Bedrock route amazon.titan-embed-text-v1.

## Scope and boundaries

Distinct Titan G1 text embedding identity, currently marked Active in its Bedrock card. The route amazon.titan-embed-text-v1 uses Invoke and an inputText request to produce a vector and token count; it is not a Converse text-generation model. Do not apply Titan V2 dimensionality, normalization or binary-output options to this G1 request schema.

## Decision and operational boundaries

- The current card marks `amazon.titan-embed-text-v1` Active and lists an 8K-token context with text input and embedding output. [Titan Embeddings G1 Text model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html)
- The G1 request accepts `inputText` and returns an embedding with `inputTextTokenCount`. V2-only options for dimensions, normalization and binary output must not be applied to G1. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html)
- Use the model-specific Invoke request. The card does not support Converse; a vector response is an input to retrieval or similarity logic rather than an assistant answer. [Titan Embeddings G1 Text model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html)

## Relations

- member-of: [`catalog/models/amazon/titan`](../../../../)

## Official resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html>
