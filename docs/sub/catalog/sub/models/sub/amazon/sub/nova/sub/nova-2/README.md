# Amazon Nova 2

Amazon Nova 2 groups the Nova 2 generation, including Lite, the announced Pro preview, Sonic and Nova Multimodal Embeddings.

## Scope and boundaries

Nova generation within the AWS-produced Nova family. Its initial documentation names Lite, Sonic and Multimodal Embeddings; the launch announcement separately identifies Nova 2 Pro as Preview. Text generation, speech-to-speech and vector embeddings have different contracts. The series has no single inherited modality, output type, context limit or access entitlement.

## Relations

- member-of: [`catalog/models/amazon/nova`](../../)
- has-member: [`catalog/models/amazon/nova/nova-2/models/nova-2-lite`](sub/models/sub/nova-2-lite/)
- has-member: [`catalog/models/amazon/nova/nova-2/models/nova-2-pro`](sub/models/sub/nova-2-pro/)
- has-member: [`catalog/models/amazon/nova/nova-2/models/nova-2-sonic`](sub/models/sub/nova-2-sonic/)
- has-member: [`catalog/models/amazon/nova/nova-2/models/nova-multimodal-embeddings`](sub/models/sub/nova-multimodal-embeddings/)

## Official resources

- <https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html>

## Decision and operational boundaries

- The initial Nova 2 documentation names Lite, Sonic and Multimodal Embeddings. Nova 2 Pro was announced as Preview with early access through Nova Forge customers and AWS account teams. [Nova 2 documentation history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html) [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)
- Lite uses generation requests, Sonic uses speech streaming, and Multimodal Embeddings produces vectors for retrieval. Select an individual member before applying limits or integration requirements. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html) [Nova conversational speech and session behavior](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html) [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html)
- A model announcement does not establish access for every account or Region. Pro has no confirmed later general-availability evidence in the linked sources. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) [Amazon Nova models](https://aws.amazon.com/nova/models/)

## Child pages

- [Models](./sub/models/)
