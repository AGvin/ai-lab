# Documentation Requirements

## Requirements

- Present Claude API as Anthropic's direct hosted API service for programmatic access to Claude models.
- Preserve the direct-model-access boundary around Messages, Message Batches, token counting, files and currently released API tools/capabilities while keeping Claude Managed Agents as separately canonical managed agent infrastructure.
- Keep concrete Claude trained-model identities with Model Reference; availability through Amazon Bedrock, Google Cloud, Microsoft Foundry, or Claude Platform on AWS does not transfer model producer provenance to those hosts.
- Keep Claude Console/playground, client SDKs, the `ant` CLI, Claude Apps, Claude Code, and Agent SDK as adjacent product/tool surfaces rather than duplicate API-service identities.
- Treat endpoint inventory, API versions/headers, authentication methods, SDK support, model inventory, tool versions, pricing, rate limits, request limits, cloud-platform availability, beta flags, and deprecations as freshness-sensitive.
- Preserve lifecycle distinctions between stable API capabilities and beta-header/public-beta features.

## Validation

- Claude API remains the direct hosted model-access service rather than the Claude model family or Claude Apps.
- Claude Managed Agents remains separate despite sharing the direct API.
- Third-party/cloud hosting does not change Anthropic model provenance.
- Producer provenance resolves bidirectionally to Anthropic.
