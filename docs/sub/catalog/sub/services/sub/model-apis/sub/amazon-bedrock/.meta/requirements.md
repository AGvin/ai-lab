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
