# Kuadrant MCP Gateway

Kuadrant MCP Gateway is a self-hosted Kubernetes-native gateway for aggregating, routing and governing Model Context Protocol (MCP) servers.

## Role and product boundaries

It integrates Kubernetes Gateway API and Envoy/Istio routing with policy attachment for authentication, authorization and rate limiting. Controller, operator, custom resources and installation manifests belong to the same product. This is not a hosted MCP server or the general Envoy AI/model gateway.

## Release and safe operation

The canonical record documents Apache-2.0-licensed v1.0.1 (2026-09-25). Actual access controls require configuration of identity providers, Gateway API resources and downstream policy enforcement. Verify supported MCP transports, controller and Kubernetes versions, OIDC credentials, network ingress/egress and identity propagation for each deployed release.

## Relations

- Produced by: [Kuadrant](../../../../../../../producers/sub/k/sub/kuadrant/)

## Official resources

- [Repository](https://github.com/Kuadrant/mcp-gateway)
- [Releases](https://github.com/Kuadrant/mcp-gateway/releases)
- [Quick start](https://github.com/Kuadrant/mcp-gateway/blob/main/docs/guides/quick-start.md)
