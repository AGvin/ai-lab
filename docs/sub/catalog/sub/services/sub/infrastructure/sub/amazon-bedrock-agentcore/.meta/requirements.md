# Documentation Requirements

## Requirements

- Identify Amazon Bedrock AgentCore as AWS's generally available managed agentic platform for building, deploying, operating, and observing AI agents using multiple frameworks, models, and protocols.
- Preserve major platform capabilities such as Runtime, Memory, Gateway, Identity, Observability, Policy, Evaluations, managed harness, payments, browser/code execution, and knowledge/retrieval only with their applicable lifecycle and release boundaries.
- Preserve the current Registry boundary: AWS Agent Registry began as an AgentCore preview capability but, as of its 2026-08-31 GA launch, has a dedicated `agent-registry` namespace, console/API/IAM surface, and canonical service identity under `services/ai-management-platforms/`; AgentCore integrates with Registry but no longer owns Registry identity.
- Keep AgentCore as one hosted runtime/platform identity rather than materializing every remaining capability as a peer service solely because it has an independent GA announcement.
- Preserve preview/GA distinctions for individual capabilities; current preview-only features must not be generalized into the stable platform contract.
- Keep open-source SDKs/frameworks such as Strands Agents separate from the managed AgentCore service.

## Validation

- AgentCore is not conflated with Amazon Bedrock model hosting generally, Strands Agents software, or AWS Agent Registry.
- Feature-level GA does not imply that every AgentCore capability is GA.
- Region availability, quotas, pricing, integrations, and capability inventory remain mutable source-scoped facts.
