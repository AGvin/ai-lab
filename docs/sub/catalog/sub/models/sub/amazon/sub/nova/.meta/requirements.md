# Documentation Requirements

## Requirements

- Identify Amazon Nova as the model family produced by Amazon Web Services and keep it distinct from Amazon Bedrock as a hosted model service.
- Represent Nova 2 as a series because multiple independently identified Nova 2 models are currently documented.
- Keep Bedrock availability, pricing, regional service state, quotas, Forge access, and selection conclusions outside stable family identity.

## Validation

- Nova 2 remains a series within Amazon Nova rather than a second top-level family.
- Amazon Bedrock is not treated as a model family alias.

## Decision and operational boundaries

- Preserve this canonical boundary: AWS model family with generation-specific and task-specific members. Micro accepts text, Lite and Pro also accept images and video, Sonic performs conversational speech, and Multimodal Embeddings produces vectors. These roles do not imply common modalities, context limits or APIs. Nova 2 Pro retains its source-backed preview boundary; Bedrock and Forge are services rather than family members.
- Micro, Lite and Pro are distinct first-generation trained models; Nova 2 is a series with separately documented members. Generation labels do not make their capabilities interchangeable. [Amazon Nova version 1 model overview](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) [Nova 2 documentation history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html)
- Conversational speech uses a bidirectional stream, while embeddings use vector-producing requests. Neither role should inherit text-generation API assumptions. [Nova conversational speech and session behavior](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html) [Nova embeddings request and response schema](https://docs.aws.amazon.com/nova/latest/userguide/embeddings-schema.html)
- AWS announced Nova 2 Pro as Preview. Nova 2.5 Sonic has its own general-availability announcement; neither state transfers to every Nova member. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) [Nova 2.5 Sonic general availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/)
