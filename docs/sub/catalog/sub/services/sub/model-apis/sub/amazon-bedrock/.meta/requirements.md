# Documentation Requirements

## Requirements

- Present Amazon Bedrock as AWS's fully managed generative-AI/model-access service for using Amazon and third-party foundation models through managed APIs and associated model-development/application capabilities.
- Preserve the model-access service boundary: Bedrock exposes model catalog/inference, model customization/evaluation, marketplace access, guardrails, knowledge/RAG, and agent-related capabilities, while separately canonical Amazon Bedrock AgentCore owns the newer managed agent-runtime/platform boundary.
- Keep concrete Amazon Nova and third-party trained-model identities with their model owners; Bedrock availability does not transfer model producer provenance to AWS.
- Keep Amazon Bedrock Marketplace as a Bedrock catalog/deployment capability unless current lifecycle establishes a stronger separately useful service boundary.
- Treat model inventory, regions, invocation APIs, pricing, quotas, marketplace subscriptions, customization options, inference profiles, provisioned capacity, and capability lifecycle as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Amazon Bedrock remains a hosted model-access/generative-AI service rather than a trained-model family.
- AgentCore is not collapsed into the general Bedrock model-access identity.
- Third-party model provenance remains with the upstream model producer.
- Producer provenance resolves bidirectionally to Amazon Web Services.

## Scoped original-source qualification — 2026-11-06

- Amazon Bedrock is an AWS-managed inference and application platform offering AWS and third-party foundation models. Its documented runtime compatibility includes InvokeModel, Converse, and OpenAI-compatible Chat Completions/Responses patterns; support is model- and region-dependent.
- AWS hosting, inference profiles, marketplace subscriptions, security/guardrail features and regional availability do not make AWS the original producer of third-party trained models. API compatibility does not guarantee parameter parity or portable data-processing behavior.
- Verified first-party source 1: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- Verified first-party source 2: https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html
- This accepts only service-scoped source identity and documented capability boundaries; it is not an exhaustive freshness audit, authenticated endpoint test, independent compliance/ownership review, global schema/cache/CI/render verification, clean pass or final-delivery gate.
