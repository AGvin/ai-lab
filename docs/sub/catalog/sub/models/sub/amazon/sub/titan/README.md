# Amazon Titan

Amazon Titan is a family of foundation models pretrained by Amazon Web Services, with model-specific text, embedding and image-generation roles.

## Scope and boundaries

AWS-pretrained model family, distinct from the Bedrock hosting service. Its text and multimodal embedding identities have different request schemas, input limits and vector dimensions. This page does not infer that every historically documented Titan model remains currently accessible. Family membership does not transfer image generation, fine-tuning or a single embedding schema across members.

## Decision and operational boundaries

- AWS identifies Titan as its pretrained foundation-model family. The family overview includes different task categories, which must be resolved at the concrete model. [Amazon Titan models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html)
- Text embeddings and multimodal embeddings have separate input contracts: the text API distinguishes G1 and V2 parameters, while Multimodal G1 accepts text and/or an image. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html) [Titan Multimodal Embeddings G1 guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html)
- For current deployment, use the exact model card and regional lifecycle record. Historical presence in the family overview does not settle access for every listed model. [Amazon Bedrock model cards: Amazon](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html) [Bedrock lifecycle for models launched before September 7, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)

## Relations

- has-member: [`catalog/models/amazon/titan/models/titan-embeddings-g1-text`](sub/models/sub/titan-embeddings-g1-text/)
- has-member: [`catalog/models/amazon/titan/models/titan-multimodal-embeddings-g1`](sub/models/sub/titan-multimodal-embeddings-g1/)
- has-member: [`catalog/models/amazon/titan/models/titan-text-embeddings-v2`](sub/models/sub/titan-text-embeddings-v2/)
- Produced by: [`catalog/producers/a/amazon-web-services`](../../../../../producers/sub/a/sub/amazon-web-services/)

## Official resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html>

## Child pages

- [Models](./sub/models/)
