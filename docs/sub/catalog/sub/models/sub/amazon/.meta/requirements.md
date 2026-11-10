# Documentation Requirements

## Requirements

- Identify this as the Amazon-branded navigation view for Nova, Titan and Strands Decider, with Amazon Web Services as the canonical producer.
- Keep Amazon Bedrock, Nova Forge, API routing, pricing, regional availability, and service limits outside model identity.
- Keep exact Nova family/series/model facts with their canonical owners.

## Validation

- The page remains model-domain navigation/context and does not create a duplicate AWS producer organization.

## Decision and operational boundaries

- Preserve this canonical boundary: Navigation view for Amazon Nova, Amazon Titan and Strands Decider. Amazon Web Services remains the canonical producer; this view is not another organization. Nova and Titan are model families, while Strands Decider checkpoints perform typed decisions. Bedrock access and the Strands runtime are separate from trained model identity. Availability must be established for the particular model and route.
- Nova generation, speech and embedding models have different input and output contracts; a family name does not establish a shared API or context limit. [Amazon Nova version 1 model overview](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html)
- Titan embedding models and Strands Decider checkpoints need different application integrations: vector retrieval for the former, typed option scoring for the latter. [Titan text embeddings parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Use model-specific lifecycle evidence. An older overview or model-card listing can retain a model whose documented Bedrock routes have reached end of life. [Amazon Bedrock model cards: Amazon](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html) [Bedrock lifecycle for models launched before September 7, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)
