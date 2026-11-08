# Amazon Bedrock

Amazon Bedrock is AWS's managed generative-AI/model-access service for invoking Amazon and third-party foundation models through managed APIs. It also offers model-selection, customization, evaluation, guardrail, knowledge-base and associated application-development capabilities. [AWS overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).

## Service boundary

Bedrock is a hosted model-access platform, not a single Amazon-trained model. Nova and partner-model identities, release histories and authorship stay with their original model producers. AWS hosting and a common invocation route do not transfer that provenance or guarantee equivalent model versions and parameters across providers.

[Amazon Bedrock AgentCore](../../infrastructure/sub/amazon-bedrock-agentcore/) is a separately cataloged managed agent-runtime/platform service; agents, knowledge bases, Bedrock Marketplace and inference profiles should not be promoted into new model/API identities solely because they are accessible through Bedrock.

## Operational boundaries

Converse, InvokeModel and compatible request interfaces depend on the chosen model and deployment route. Verify current model availability, regions, IAM permissions, pricing, quotas, inference profiles, customization, marketplace subscriptions, retention and applicable guardrails before deployment. API compatibility is not a guarantee of identical behavior or data-processing terms. [Bedrock runtime and API compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html).

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Bedrock overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Supported model API compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html)
