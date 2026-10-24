# Documentation Requirements

## Requirements

- Identify Kuadrant MCP Gateway as a separately released, self-hosted Kubernetes-native MCP server aggregation/routing and policy gateway, not a hosted service or an alias of the generic Envoy AI/model inference gateway.
- Preserve the first-party non-prerelease **v1.0.1 (2026-09-25)** release boundary, Apache-2.0 repository license, and project maintainership by Kuadrant. Broker/router/controller, operator/CRDs and installation manifests are components of one software product.
- Describe the Gateway API and Envoy/Istio integration, aggregation/routing of MCP servers and policy attachment for authentication, authorization and rate limiting. A deployment depends on actual Kubernetes Gateway API, policy providers and identity configuration; do not imply turnkey default access control.
- Distinguish it from general API gateways (Kong, Higress, APISIX), agent/model inference gateways and tool-security scanners. Do not create duplicate canonical products for transport configurations or the companion test MCP servers.
- **Compatibility and security:** confirm the particular release's MCP protocol revision, transport/session behavior and controller compatibility before recommendations; require bounded ingress, correctly scoped OIDC/service credentials, least-privilege policy, network restrictions and verified downstream identity propagation.
- Record exact `produced-by` / `produces` reciprocity with `catalog/producers/k/kuadrant`.

## Validation

- Official repository, non-prerelease v1.0.1 release notes, quick start and LICENSE substantiate the released identity and cluster integration.
- Canonical software/producer paths resolve with exact reciprocal relation targets.
