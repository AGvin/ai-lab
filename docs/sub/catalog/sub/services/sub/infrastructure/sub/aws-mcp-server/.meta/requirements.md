# Documentation Requirements

## Requirements

- Present AWS MCP Server as Amazon Web Services' managed remote Model Context Protocol server for giving AI coding agents secure access to AWS documentation, service information, authenticated AWS API operations, sandboxed script execution, and curated AWS skills through a single hosted endpoint.
- Preserve its independent managed-service identity while keeping Agent Toolkit for AWS as the broader distribution/setup bundle that can configure the server together with skills, plugins, and rules files.
- Keep the official AWS Agent Skills collection, Agent Toolkit plugins/rules, AWS CLI setup commands, individual downstream AWS services, and predecessor local AWS MCP servers outside this service identity.
- Treat supported Regions/endpoints, OAuth/SigV4 authentication, tool inventory, IAM context keys/policies, CloudWatch metrics, CloudTrail behavior, quotas, pricing, and service capabilities such as serverless diagnostics as freshness-sensitive.
- Do not materialize each MCP tool or downstream AWS API as a peer service solely because AWS MCP Server exposes it.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- AWS MCP Server remains a producer-hosted managed infrastructure/service surface rather than self-managed MCP software.
- Its identity remains distinct from Amazon Bedrock AgentCore and AWS Agent Registry.
- Producer provenance resolves bidirectionally to Amazon Web Services.
