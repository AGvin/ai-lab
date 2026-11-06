# Documentation Requirements

## Requirements

- Identify MCP Gateway & Registry as the separately deployed, open-source agent/MCP asset registry and access-control gateway maintained at `agentic-community/mcp-gateway-registry`, not as the MCP protocol specification, official MCP Registry, a general cloud service or a single MCP server.
- Preserve the first-party non-prerelease **1.32.1 (2026-10-06)** boundary and Apache-2.0 source license. Its released Docker Compose, Kubernetes/Helm and ECS/Terraform deployment paths are modes of one canonical product, not independent software peers.
- Describe governed registry/discovery of MCP servers, tools, agents, skills and extensible assets, tool-level controls, identity integration, activity/audit visibility, and supported MCP/A2A/HTTP resource routing. Differentiate the broad asset control plane from Kuadrant MCP Gateway's Kubernetes/Envoy policy routing and general API/model gateways.
- **Compatibility:** the 1.32.1 release pins the `mcp` dependency below 2.0 and documents upgrade/deployment requirements. Verify precise MCP protocol, transport/session semantics and supported identity providers for the selected build; do not infer all future protocol revisions are supported from the registry's feature list.
- **Operations and security:** separately configure trusted ingress/egress, TLS, OIDC/OBO token exchange, least-privilege tool/asset scope, secure service credentials, logs and identity provider; Docker, Helm, ECS and hosted cloud deployment environments have different operational controls. Do not imply ready-to-use secure defaults.
- Reconcile exact `produced-by` / `produces` inverse with `catalog/producers/a/agentic-community`, without duplicating maintainers, deployment packages or bundled plugins.

## Validation

- Official GitHub repository, v1.32.1 release, documentation and LICENSE support current identity, version, code license and deployment scope.
- Software and community-producer reciprocal paths resolve exactly.
