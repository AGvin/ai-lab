# Documentation Requirements

## Requirements

- Identify Amazon Titan at canonical ID `catalog/models/amazon/titan`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: AWS-pretrained model family, distinct from the Bedrock hosting service. Its text and multimodal embedding identities have different request schemas, input limits and vector dimensions. This page does not infer that every historically documented Titan model remains currently accessible. Family membership does not transfer image generation, fine-tuning or a single embedding schema across members.
- AWS identifies Titan as its pretrained foundation-model family. The family overview includes different task categories, which must be resolved at the concrete model. [Amazon Titan models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html)
- Text embeddings and multimodal embeddings have separate input contracts: the text API distinguishes G1 and V2 parameters, while Multimodal G1 accepts text and/or an image. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html) [Titan Multimodal Embeddings G1 guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html)
- For current deployment, use the exact model card and regional lifecycle record. Historical presence in the family overview does not settle access for every listed model. [Amazon Bedrock model cards: Amazon](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html) [Bedrock lifecycle for models launched before September 7, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)
