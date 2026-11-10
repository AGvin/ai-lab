# Documentation Requirements

## Requirements

- Identify Amazon Nova 2 Lite as the released fast, cost-efficient Nova 2 reasoning model announced on 2025-12-02.
- Preserve first-party multimodal text/image/video input positioning, up to 1M context, extended thinking with low/medium/high intensity, and customization capabilities only while current official documentation supports them.
- Attribute workload/value positioning to AWS and keep Bedrock pricing, regions, quotas, and hosted service behavior freshness-sensitive.

## Validation

- Nova 2 Lite is not conflated with Nova 2 Pro Preview or Nova 2 Sonic.
- Hosted service state is distinguished from model identity.

## Decision and operational boundaries

- Preserve this canonical boundary: Concrete Nova 2 generation model, identified in Bedrock as amazon.nova-2-lite-v1:0. AWS documents a 1M-token context and low, medium and high thinking levels. Text, image and video input support does not imply speech output or an embeddings API. Bedrock inference profiles and regional routing are access choices rather than separate trained identities.
- AWS introduced Lite on December 2, 2025 with low, medium and high thinking levels and a 1M-token context. These are source-bound model capabilities, not a guarantee of task accuracy. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)
- The Bedrock card identifies `amazon.nova-2-lite-v1:0` and text/image/video inputs with text output. Apply its current API and inference-profile matrix when choosing a route. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html)
- Keep a geographic or global inference profile separate from model identity; profile availability does not imply an in-Region endpoint in every location. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html)
