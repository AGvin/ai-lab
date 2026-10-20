# Documentation Requirements

## Requirements

- Identify Amazon Nova Multimodal Embeddings at canonical ID `catalog/models/amazon/nova/nova-2/models/nova-multimodal-embeddings`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Nova 2 embedding identity with Bedrock route amazon.nova-2-multimodal-embeddings-v1:0. Output is vectors, not generated text. The guide limits a model input to 8K tokens or 30 seconds of audio/video; longer media uses asynchronous segmentation. Supported dimensions are 256, 384, 1024 and 3072. Corpus/query embedding purpose and synchronous single-input versus asynchronous segmented requests are operational choices, not additional models.
- The model card maps the identity to `amazon.nova-2-multimodal-embeddings-v1:0`, and Nova 2 documentation records it among the initial series releases. [Nova Multimodal Embeddings model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html) [Nova 2 documentation history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html)
- The guide bounds an individual model input at 8K tokens or 30 seconds of audio/video. Longer media uses segmented asynchronous processing and returns per-segment vectors rather than one unbounded input. [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html)
- Choose 256, 384, 1024 or 3072 dimensions consistently across an index. Use `GENERIC_INDEX` for corpus content and an appropriate retrieval purpose for queries. A synchronous `SINGLE_EMBEDDING` request contains exactly one supported input object; `SEGMENTED_EMBEDDING` uses the asynchronous path. [Nova embeddings request and response schema](https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html)
- The feature guide expresses context in tokens, while the request schema separately describes text validation in characters. Keep those units distinct and use the selected schema and truncation mode to handle oversize requests. [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html) [Nova embeddings request and response schema](https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html)
