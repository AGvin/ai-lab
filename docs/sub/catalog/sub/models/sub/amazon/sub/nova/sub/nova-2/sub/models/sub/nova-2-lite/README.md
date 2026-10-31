# Amazon Nova 2 Lite

Amazon Nova 2 Lite is the released reasoning model in the Nova 2 series for text, image and video inputs with text output.

## Scope and boundaries

Concrete Nova 2 generation model, identified in Bedrock as amazon.nova-2-lite-v1:0. AWS documents a 1M-token context and low, medium and high thinking levels. Text, image and video input support does not imply speech output or an embeddings API. Bedrock inference profiles and regional routing are access choices rather than separate trained identities.

## Relations

- member-of: [`catalog/models/amazon/nova/nova-2`](../../../../)

## Official resources

- <https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html>

## Decision and operational boundaries

- AWS introduced Lite on December 2, 2025 with low, medium and high thinking levels and a 1M-token context. These are source-bound model capabilities, not a guarantee of task accuracy. [Nova 2 launch and Nova 2 Pro preview](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)
- The Bedrock card identifies `amazon.nova-2-lite-v1:0` and text/image/video inputs with text output. Apply its current API and inference-profile matrix when choosing a route. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html)
- Keep a geographic or global inference profile separate from model identity; profile availability does not imply an in-Region endpoint in every location. [Nova 2 Lite model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html)
