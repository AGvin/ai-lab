# Documentation Requirements

## Requirements

- Identify Amazon Titan Multimodal Embeddings G1 at canonical ID `catalog/models/amazon/titan/models/titan-multimodal-embeddings-g1`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Distinct Titan multimodal embedding identity with Active Bedrock route amazon.titan-embed-image-v1. It accepts text and/or an image and returns a vector, not generated images. The guide specifies English text, a 256-token text input limit, images up to 25MB at 2048 by 2048, and output dimensions of 1024 by default, 384 or 256. Its multimodal schema and limits differ from Titan text embeddings and Nova Multimodal Embeddings.
- The current card marks `amazon.titan-embed-image-v1` Active and supports text/image input with embedding output through Invoke, without Converse. [Titan Multimodal Embeddings G1 model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-multimodal-embeddings-g1.html)
- The guide accepts text and/or an image, limits English text to 256 tokens and images to 25MB at 2048 by 2048, and supports 1024 (default), 384 or 256 output dimensions. [Titan Multimodal Embeddings G1 guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html)
- Keep inference limits separate from fine-tuning dataset requirements. Image-text customization has its own caption and validation-data rules; it does not change this model into an image generator. [Titan Multimodal Embeddings G1 guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html)
