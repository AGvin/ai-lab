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

## Scoped original-source qualification — 2026-11-06

- AWS Agent Registry reached GA on 2026-08-31 as a private, governed registry/discovery catalog for agent, MCP server, skill and custom resource records; it does not execute the agents it indexes. The new `agent-registry` API/ARN/IAM namespace has its own registry and approval workflow. Migration docs say support for the earlier `bedrock-agentcore` preview registry namespace ends 2026-10-30; do not present the old preview namespace as current.
- Provider documentation distinguishes draft/pending/approved record states, hybrid search for approved resources, IAM-controlled registry APIs and optional MCP endpoints. Resource approval metadata or discovery is not proof that a third-party agent is safe, that its tools can be invoked by a caller, or that Amazon Bedrock AgentCore and Agent Registry are a single service.
- Cross-account auto-discovery, AWS KMS keys, regional support, quotas, record permissions, pricing and integrations require exact current account/region policy verification; no independent IAM or security test is implied.
- Verified first-party source 1: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-get-started.html
- Verified first-party source 2: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-search-records.html
- Verified first-party source 3: https://aws.amazon.com/about-aws/whats-new/2026/08/aws-agent-registry-generally-available/
- Scope is source-backed existing governance/registry service identity and publisher-documented operational boundaries only. No new entity/metadata, independent compliance/security/runtime proof, comprehensive freshness audit, whole-repository schema/cache/CI/render, reader-repair, clean pass, final gate or merge credit.
