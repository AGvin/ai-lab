# Documentation Requirements

## Requirements

- Identify Agent Toolkit for AWS Skills as the official AWS-supported collection of agent skills packaged within the broader Agent Toolkit for AWS repository.
- Keep the skill collection distinct from the toolkit's MCP server, plugins, rules files, CLI/setup flows, and managed AWS services even when those surfaces are designed to work together.
- Preserve AWS's current statement that Agent Toolkit succeeds earlier AWS Labs MCP/skills/plugin tooling without erasing historical predecessor identities.
- Treat the exact skill inventory, categories, installation paths, plugin bundling, supported agents, and toolkit setup commands as freshness-sensitive.
- Preserve the current SageMaker optimized generative-AI inference `aws-ai-ml` skill as collection inventory rather than a separate canonical skill: it generates SageMaker Python SDK v3 workflows for benchmarking/recommending/comparing inference deployments and remains subject to the collection's mutable inventory and AWS service/runtime boundaries.
- Preserve source licensing and do not turn official-source status into a blanket quality or safety endorsement.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains a skill collection rather than a duplicate identity for the entire Agent Toolkit or AWS MCP Server.
- Producer provenance resolves to Amazon Web Services.
