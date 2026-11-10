# MCP Gateway & Registry

MCP Gateway & Registry is an open-source self-hosted registry and gateway for governing MCP and related agent assets, published by the Agentic Community project.

## Role and product boundaries

The software supports discovery and governance of MCP servers, tools, agents, skills and other assets, with configurable identity, access controls, routing and audit visibility. Docker Compose, Helm/Kubernetes and ECS deployment methods are modes of the same product. Unlike Kuadrant's Kubernetes policy gateway, this product combines a broader asset registry and access plane.

## Release and safe operation

The recorded Apache-2.0 release is v1.32.1 (2026-10-06); its package constraints hold the MCP dependency below 2.0. Verify API, transport, supported identity-provider and deployment compatibility for the selected release. Configure TLS, OIDC/OBO, tool permissions, secrets, trusted ingress/egress and audit retention explicitly; deployment examples do not imply secure defaults.

## Relations

- Produced by: [Agentic Community](../../../../../../../producers/sub/a/sub/agentic-community/)

## Official resources

- [Repository](https://github.com/agentic-community/mcp-gateway-registry)
- [Documentation](https://agentic-community.github.io/mcp-gateway-registry/)
- [Releases](https://github.com/agentic-community/mcp-gateway-registry/releases)
