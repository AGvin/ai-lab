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

## Scoped original-source qualification — 2026-11-06

- Amazon Bedrock AgentCore is a managed agent infrastructure/service boundary, not Bedrock model inference or an individual LLM. The official developer guide differentiates framework-agnostic Runtime hosting from the managed Harness orchestration loop and lists separate capabilities for Memory, Gateway, Identity, browser/code tools and observability. Optional feature availability does not imply one uniform stable contract.
- AgentCore Runtime and Harness, tool credentials, network permissions, session isolation, log payloads, IAM roles, regional access, quotas and metering must be checked for the selected resource. AWS Agent Registry's separate service lifecycle and the Bedrock Agents Classic maintenance boundary do not create extra AgentCore source identities.
- Verified first-party source 1: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Verified first-party source 2: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html
- Verified first-party source 3: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html
- Scope: originally documented hosted service identity and lifecycle/usage limits only; not a complete freshness/legal/security review, independent runtime execution, full schema/cache/CI/render, clean pass or final delivery gate.
