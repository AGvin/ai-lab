# Amazon Nova

Amazon Nova is a family of models produced by Amazon Web Services, covering text and multimodal generation, conversational speech and embeddings.

## Scope and boundaries

AWS model family with generation-specific and task-specific members. Micro accepts text, Lite and Pro also accept images and video, Sonic performs conversational speech, and Multimodal Embeddings produces vectors. These roles do not imply common modalities, context limits or APIs. Nova 2 Pro retains its source-backed preview boundary; Bedrock and Forge are services rather than family members.

## Child pages

- [Amazon Nova 2](./sub/nova-2/)
- [Individual Nova models](./sub/models/)

## Relations

- has-member: [`catalog/models/amazon/nova/nova-2`](sub/nova-2/)
- has-member: [`catalog/models/amazon/nova/models/nova-2-5-sonic`](sub/models/sub/nova-2-5-sonic/)
- has-member: [`catalog/models/amazon/nova/models/nova-lite`](sub/models/sub/nova-lite/)
- has-member: [`catalog/models/amazon/nova/models/nova-micro`](sub/models/sub/nova-micro/)
- has-member: [`catalog/models/amazon/nova/models/nova-pro`](sub/models/sub/nova-pro/)
- Produced by: [`catalog/producers/a/amazon-web-services`](../../../../../producers/sub/a/sub/amazon-web-services/)

## Official resources

- <https://aws.amazon.com/nova/models/>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html>
- <https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html>
- <https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html>
- <https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/>
- <https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/>

## Decision and operational boundaries

- Micro, Lite and Pro are distinct first-generation trained models; Nova 2 is a series with separately documented members. Generation labels do not make their capabilities interchangeable. [Amazon Nova version 1 model overview](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) [Nova 2 documentation history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html)
- Conversational speech uses a bidirectional stream, while embeddings use vector-producing requests. Neither role should inherit text-generation API assumptions. [Nova conversational speech and session behavior](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html) [Nova embeddings request and response schema](https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html)
- AWS announced Nova 2 Pro as Preview. Nova 2.5 Sonic has its own general-availability announcement; neither state transfers to every Nova member. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) [Nova 2.5 Sonic general availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/)
