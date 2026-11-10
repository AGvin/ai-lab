# Documentation Requirements

## Requirements

- Identify Agent Router (formerly Envoy AI Gateway) as an Apache-2.0, Kubernetes-oriented AI/agent traffic control plane built on Envoy and Envoy Gateway; retain the existing canonical `envoy-ai-gateway` slug for stable internal references.
- Preserve its placement under `gateways/api-management-gateways`: general ingress/control-plane governance with AI/MCP traffic routing, model integrations, policy, rate-limiting, failover, security, and shared credential controls; do not recast it as a hosted-only model gateway.
- Preserve the dependency/boundary with Envoy Gateway rather than describing Envoy AI Gateway as a standalone model provider.
- Preserve joint historical project origin from Tetrate and Bloomberg as `produced-by` relations, separate from current Agentic AI Foundation stewardship via `maintained-by`; the rename and AAIF transition took effect on 2026-09-10, without implying that historical origin organizations currently operate the product.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep provider counts, release versions, installation commands, API stability, maintainer affiliations, and other mutable implementation/project-state details source-backed when expanded. The 2026-10-06 Agent Router v1.2.0 release is a dated source check, not a guarantee of future currency.
- Include current official Agent Router documentation, its renamed repository, the September 2026 rename announcement, and historical Envoy AI Gateway origin references. Preserve deployed compatibility names: `aigw`, `AIGatewayRoute`, `AIServiceBackend`, `BackendSecurityPolicy`, `aigateway.envoyproxy.io`, existing Helm/container/module namespaces.

## Validation

- The page uses the name Agent Router, explains the Envoy AI Gateway alias and 2026 AAIF transition, and describes an AI-focused gateway/control-plane extension, not an LLM provider or hosted model API.
- Envoy Gateway remains part of the architectural boundary.
- Tetrate and Bloomberg are represented as joint originators without implying sole ownership or current maintenance, and the separate AAIF `maintained-by` / `maintains` inverse resolves.
- Current maintenance is not collapsed into a fabricated single-company relation.
- Current official resources and release notes match canonical entity metadata; historic names in deployed APIs are not mistakenly renamed.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
