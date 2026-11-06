# Amazon models

Amazon models groups Amazon-branded model families and released trained identities under the Amazon Web Services producer record.

## Scope and boundaries

Navigation view for Amazon Nova, Amazon Titan and Strands Decider. Amazon Web Services remains the canonical producer; this view is not another organization. Nova and Titan are model families, while Strands Decider checkpoints perform typed decisions. Bedrock access and the Strands runtime are separate from trained model identity. Availability must be established for the particular model and route.

## Child pages

- [Amazon Nova](./sub/nova/)
- [Amazon Titan](./sub/titan/)
- [Strands Decider](./sub/strands-decider/)

## Official resources

- <https://aws.amazon.com/nova/models/>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html>
- <https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026/>
- <https://github.com/strands-labs/strands-decider>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html>

## Decision and operational boundaries

- Nova generation, speech and embedding models have different input and output contracts; a family name does not establish a shared API or context limit. [Amazon Nova version 1 model overview](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html)
- Titan embedding models and Strands Decider checkpoints need different application integrations: vector retrieval for the former, typed option scoring for the latter. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Use model-specific lifecycle evidence. An older overview or model-card listing can retain a model whose documented Bedrock routes have reached end of life. [Amazon Bedrock model cards: Amazon](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html) [Bedrock lifecycle for models launched before September 7, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)
