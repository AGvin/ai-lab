# Documentation Requirements

## Requirements

- Identify Envoy AI Gateway as an open-source, Kubernetes-oriented gateway built on Envoy Gateway for routing and managing GenAI/LLM traffic.
- Preserve its selected placement under `gateways/api-management-gateways`; it extends Envoy's gateway/control-plane model with AI-specific routing, provider integration, policy, rate-limiting, failover, and security concerns.
- Preserve the dependency/boundary with Envoy Gateway rather than describing Envoy AI Gateway as a standalone model provider.
- Preserve joint project origin as the open collaboration initiated by Tetrate and Bloomberg, while keeping current multi-organization community maintenance distinct from either origin organization acting alone.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep provider counts, release versions, installation commands, API stability, maintainer affiliations, and other mutable implementation/project-state details source-backed when expanded.
- Include current official Envoy AI Gateway documentation, repository, origin, and maintainer references.

## Validation

- The page describes an AI-focused gateway/control-plane extension, not an LLM provider or hosted model API.
- Envoy Gateway remains part of the architectural boundary.
- Tetrate and Bloomberg are represented as joint originators without implying sole ownership or sole current maintenance by either organization.
- Current maintenance is not collapsed into a fabricated single-company relation.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
