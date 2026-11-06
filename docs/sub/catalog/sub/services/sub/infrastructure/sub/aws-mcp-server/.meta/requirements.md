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

## Scoped original-source qualification — 2026-11-06

- AWS's original Agent Toolkit documentation presents AWS MCP Server as a managed remotely hosted MCP endpoint. Documentation lookup and service information can be read without AWS IAM authentication, but AWS API execution, sandboxed scripts and curated skill actions require authenticated IAM credentials and retain AWS policy/CloudTrail boundaries.
- Keep the hosted server distinct from Agent Toolkit distribution, the independently cataloged AWS Skills collection, locally installed predecessor MCP servers, Amazon Bedrock AgentCore and Agent Registry. One shared endpoint does not make every surfaced AWS API or MCP tool a separate managed service or transfer the underlying product owner.
- Authentication methods, IAM condition keys, regional supported endpoints, pricing, quotas, serverless diagnostics, logged payload/metadata and supported tool list are mutable and must be checked against the active AWS account and version. A managed tool broker is not independent certification of arbitrary agent command safety.
- Verified first-party source 1: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html
- Verified first-party source 2: https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/
- Accept only the present managed infrastructure service identity and source-scoped lifecycle/authorization boundaries. No new entity/metadata, reader repair, independent security/legal/runtime audit, full freshness, whole-repository schema/cache/CI/render, clean pass, final delivery or merge.
