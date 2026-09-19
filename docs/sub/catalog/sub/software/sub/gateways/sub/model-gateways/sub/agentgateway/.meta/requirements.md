# Documentation Requirements

## Requirements

- Identify `agentgateway` as the stable open-source, AI-native gateway project for unified HTTP, gRPC, LLM inference, MCP, and A2A traffic.
- Preserve its primary self-managed software identity under model/AI gateways even though the data plane also handles conventional API traffic and the project supports both standalone and Kubernetes deployment modes.
- Preserve provenance and stewardship separately: Solo.io created the project; it is now an Agentic AI Foundation (AAIF) hosted project under Linux Foundation governance.
- Keep Solo Enterprise for agentgateway as commercial packaging, support, management, and enterprise distribution around the open-source project rather than creating a duplicate canonical gateway identity solely from the enterprise edition name.
- Keep kgateway, Istio integration, cloud-marketplace distributions, individual MCP servers, models, and downstream enterprise products as separate identities/integrations.
- Treat release versions, protocol support, APIs/CRDs, Helm charts, commercial-edition features, deployment modes, security policies, model/provider support, and project governance as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains the open-source gateway project rather than the Solo Enterprise product edition.
- `produced-by` preserves historical Solo.io origin and `maintained-by` preserves current AAIF stewardship.
- Current stable documentation/release state is used instead of alpha/RC artifacts.
