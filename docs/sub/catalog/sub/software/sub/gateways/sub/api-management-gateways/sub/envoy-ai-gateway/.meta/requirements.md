# Documentation Requirements

## Requirements

- Identify Envoy AI Gateway as an open-source, Kubernetes-oriented gateway built on Envoy Gateway for routing and managing GenAI/LLM traffic.
- Preserve its selected placement under `gateways/api-management-gateways`; it extends Envoy's gateway/control-plane model with AI-specific routing, provider integration, policy, rate-limiting, failover, and security concerns.
- Preserve the dependency/boundary with Envoy Gateway rather than describing Envoy AI Gateway as a standalone model provider.
- Keep provider counts, release versions, installation commands, API stability, and other mutable implementation details source-backed when expanded.
- Include current official Envoy AI Gateway documentation and repository references.

## Validation

- The page describes an AI-focused gateway/control-plane extension, not an LLM provider or hosted model API.
- Envoy Gateway remains part of the architectural boundary.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
