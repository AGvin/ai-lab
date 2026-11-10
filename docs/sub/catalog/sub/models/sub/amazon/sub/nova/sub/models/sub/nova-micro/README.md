# Amazon Nova Micro

Amazon Nova Micro is a first-generation Nova model accepting text and producing text.

## Scope and boundaries

Distinct first-generation Nova trained identity with Bedrock route amazon.nova-micro-v1:0. The current card marks it Active and lists 128K context with a 10K output maximum. It accepts text and produces text. Micro does not inherit multimodal or document-file input support from Lite and Pro. Converse and Invoke support and regional availability belong to the hosted access contract.

## Decision and operational boundaries

- The current card marks `amazon.nova-micro-v1:0` Active and gives a `128K` context and `10K` output maximum. Its minimum EOL date is not a retirement announcement. [Nova Micro model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-micro.html) [Bedrock lifecycle for models launched before September 7, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)
- The Nova version 1 guide supports Converse and Invoke for this model. The version 1 guide does not list document-file input for Micro; prepare text rather than assuming the file inputs supported by Lite and Pro. [Amazon Nova version 1 model overview](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)
- AWS capability and efficiency positioning does not establish relative quality for a workload; evaluate the intended language, prompt and task before using it as a selection conclusion. [Nova Micro, Lite and Pro service card](https://docs.aws.amazon.com/ai/responsible-ai/nova-micro-lite-pro/overview.html)

## Relations

- member-of: [`catalog/models/amazon/nova`](../../../../)

## Official resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-micro.html>
- <https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html>
- <https://docs.aws.amazon.com/ai/responsible-ai/nova-micro-lite-pro/overview.html>
- <https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html>
