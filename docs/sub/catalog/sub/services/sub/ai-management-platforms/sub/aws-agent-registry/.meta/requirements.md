# Documentation Requirements

## Requirements

- Identify AWS Agent Registry as AWS's generally available private, governed organizational catalog and discovery service for agents, tools, skills, MCP servers, and custom resources.
- Preserve its primary AI-management/governance identity: Registry provides organization-wide discovery, approval, lifecycle metadata, access control, cross-account sharing, auto-detection, and resource reuse rather than agent execution itself.
- Preserve the current product boundary introduced at GA: AWS Agent Registry has its own console, `agent-registry` API/IAM namespace, managed IAM policy, resource ARN namespace, and lifecycle independent of the earlier AgentCore preview namespace.
- Keep Amazon Bedrock AgentCore as a separate managed agent runtime/platform identity. Agent Registry can discover and integrate with AgentCore resources but is not merely an AgentCore capability after the GA namespace split.
- Keep Amazon Quick, Kiro, external agents/tools, registered records, MCP servers, and Agent Skills as separate products/resources rather than parts of the Registry producer identity.
- Treat regions, registry/record schemas, approval workflows, auto-detection, authorization, integrations, quotas, pricing, APIs, and migration timelines as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains a governed registry/control-plane service rather than an agent runtime, model host, or static asset collection.
- GA status is not projected backward onto the April 2026 public-preview AgentCore namespace.
- Producer provenance resolves to Amazon Web Services.
