# Documentation Requirements

## Requirements

- Identify Agent Toolkit for AWS Skills as the official AWS-supported collection of agent skills packaged within the broader Agent Toolkit for AWS repository.
- Keep the skill collection distinct from the toolkit's MCP server, plugins, rules files, CLI/setup flows, and managed AWS services even when those surfaces are designed to work together.
- Preserve AWS's current statement that Agent Toolkit succeeds earlier AWS Labs MCP/skills/plugin tooling without erasing historical predecessor identities.
- Treat the exact skill inventory, categories, installation paths, plugin bundling, supported agents, and toolkit setup commands as freshness-sensitive.
- Preserve `aws-ai-ml` as collection-owned **plugin-bundled** content located under `plugins/aws-core/skills/aws-ai-ml/`, not a standalone catalog identity or an entry automatically installed from the separate `skills/` tree. Its pinned `SKILL.md` describes SageMaker model selection, data preparation, training/fine-tuning, evaluation, deployment, inference optimization, endpoint diagnosis and Python SDK v3 workflows. Bedrock-native Agents, Knowledge Bases, Guardrails and AgentCore flows are explicitly outside its validated coverage.
- Distinguish plugin installations (which may bundle skills with an AWS MCP configuration), standalone `npx skills add aws/agent-toolkit-for-aws/skills` installation, and on-demand MCP discovery; they have different filesystem and runtime boundaries.
- Installation of instructions does not authorize AWS API calls, IAM changes, model training, deployments, spending or data transfer. Require separate scoped credentials, least privilege, cost and data boundary review.
- Preserve source licensing and do not turn official-source status into a blanket quality or safety endorsement.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains a skill collection rather than a duplicate identity for the entire Agent Toolkit or AWS MCP Server.
- Producer provenance resolves to Amazon Web Services.

## Pinned source reconciliation — 2026-11-08

- The pinned [skills index](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/skills/README.md) separates the standalone `skills/` tree from plugin-bundled skills. The original [aws-ai-ml SKILL.md](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/plugins/aws-core/skills/aws-ai-ml/SKILL.md) is located in `plugins/aws-core/skills/`, supports a broader SageMaker lifecycle and explicitly excludes validated Bedrock-native workflows.
- The change is scoped to documented skill source and boundaries; no standalone package installation, AWS account operation or production-safe execution was tested.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
