# Documentation Requirements

## Requirements

- Identify Amazon Nova 2 as the generation containing distinct Nova 2 Lite, Nova 2 Pro, and Nova 2 Sonic model identities.
- Preserve released/GA versus Preview lifecycle boundaries at concrete-model scope.
- Keep shared generation-level reasoning or multimodal claims narrowly source-backed; Nova 2 Sonic has a materially different speech-to-speech role from Lite/Pro.
- Keep Bedrock/Forge pricing, regional availability, quotas, and service-tier behavior outside stable series identity.

## Validation

- Lite, Pro, and Sonic are not treated as aliases or parameter variants of one model.
- Preview lifecycle is not generalized from Nova 2 Pro to released Nova 2 models.

## Decision and operational boundaries

- Preserve this canonical boundary: Nova generation within the AWS-produced Nova family. Its initial documentation names Lite, Sonic and Multimodal Embeddings; the launch announcement separately identifies Nova 2 Pro as Preview. Text generation, speech-to-speech and vector embeddings have different contracts. The series has no single inherited modality, output type, context limit or access entitlement.
- The initial Nova 2 documentation names Lite, Sonic and Multimodal Embeddings. Nova 2 Pro was announced as Preview with early access through Nova Forge customers and AWS account teams. [Nova 2 documentation history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html) [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)
- Lite uses generation requests, Sonic uses speech streaming, and Multimodal Embeddings produces vectors for retrieval. Select an individual member before applying limits or integration requirements. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html) [Nova conversational speech and session behavior](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html) [Nova multimodal embeddings guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html)
- A model announcement does not establish access for every account or Region. Pro has no confirmed later general-availability evidence in the linked sources. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) [Amazon Nova models](https://aws.amazon.com/nova/models/)
