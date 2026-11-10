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

## Scoped original-source qualification — 2026-11-06

- Anthropic's direct Claude API exposes Messages, Message Batches, token counting, Models, Files and other documented endpoints. The same API platform also exposes Managed Agents and beta surfaces; preserve the independently cataloged Claude Managed Agents platform boundary.
- API version and beta headers, workspace/key authentication, feature availability, rate limits and model inventory are operationally mutable. Anthropic-trained Claude model provenance is not reassigned to Bedrock, Vertex AI or other hosted routes.
- Verified first-party source 1: https://platform.claude.com/docs/en/api/overview
- Verified first-party source 2: https://platform.claude.com/docs/en/api/http
- This accepts only service-scoped source identity and documented capability boundaries; it is not an exhaustive freshness audit, authenticated endpoint test, independent compliance/ownership review, global schema/cache/CI/render verification, clean pass or final-delivery gate.
