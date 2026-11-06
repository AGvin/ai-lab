# Amazon Nova 2 Sonic

Amazon Nova 2 Sonic is a conversational speech model for bidirectional speech and text interaction in the Nova 2 series.

## Scope and boundaries

Speech-to-speech model identified as amazon.nova-2-sonic-v1:0. The current Bedrock card marks it Active and lists a 1M-token context and 64K maximum output. It uses InvokeModelWithBidirectionalStream, not ordinary Converse or Invoke requests. Connections have an eight-minute session limit independent of context size. The May 2026 automatic refresh is an in-place update, not an additional model identity.

## Relations

- member-of: [`catalog/models/amazon/nova/nova-2`](../../../../)

## Official resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html>
- <https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html>

## Decision and operational boundaries

- The Bedrock card identifies `amazon.nova-2-sonic-v1:0`, marks it Active and lists a 1M-token context with a 64K output maximum. These card values apply to this model, not Nova 2.5 Sonic. [Nova 2 Sonic model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html)
- Use `InvokeModelWithBidirectionalStream` for speech/text sessions. The conversational speech guide imposes an eight-minute connection limit, so applications need session renewal or continuation independently of token capacity. [Nova 2 Sonic model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html) [Nova conversational speech and session behavior](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html)
- AWS rolled out the May 2026 refresh automatically without API or configuration changes. Treat that refresh as service evolution of the existing model route. [Nova Sonic release notes](https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html)
