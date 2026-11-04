# Documentation Requirements

## Requirements

- Identify kagent as the Kubernetes-native open-source agent framework at `kagent-dev/kagent`, not a hosted LLM service, an individual MCP server, or a managed commercial offering.
- Pin source commit `e3b807935db59cfb161f87e898d8e203715a5b79` (2026-11-03) and the first-party README and Apache-2.0 LICENSE. Source code licensing does not automatically extend to providers, models or third-party components.
- Describe the 1.x Harness, AgentTemplate, Agent and Session model, its Kubernetes controller, Agent Substrate, optional UI, PostgreSQL session storage, and configurable model/provider interfaces.
- Distinguish the [1.x installation guide](https://kagent.dev/docs/kagent/1.x/setup/installation/) from older 0.x guidance: the current 1.x documentation requires a Kubernetes 1.37+ cluster and warns that installing 1.x is not an in-place upgrade from 0.10.x because of CRD changes.
- Explicitly describe the access boundary. Kubernetes RBAC protects resource authoring, but the 1.x open-source gRPC API authorizes callers who can reach it; restrict exposure and place suitable authentication controls at the ingress. Grant agents least-privilege tool and service-account rights, control model credentials, data egress and cost, and require approval for sensitive cluster actions.
- Do not claim an installed cluster, executed agent, validated production upgrade, dependency/security audit, full CI, or whole-catalog clean pass.

## Validation

- Official source, 1.x architecture/installation docs, and pinned license support identity and operational boundaries.
- Exactly one canonical reader is linked from Agent Frameworks, with no invented producer or managed-service entity.
