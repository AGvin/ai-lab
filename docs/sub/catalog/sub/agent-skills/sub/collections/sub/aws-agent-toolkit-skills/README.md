# Agent Toolkit for AWS Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Agent Toolkit for AWS Skills is the official AWS-supported collection of Agent Skills packaged within the broader Agent Toolkit for AWS repository.

## Producer

- [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/)

## Collection boundary

The skill collection remains distinct from the toolkit's MCP server, plugins, rules files, CLI and setup flows, and managed AWS services even when those surfaces are designed to work together. AWS identifies Agent Toolkit as the successor to earlier AWS Labs MCP, skills, and plugin tooling; that lineage does not erase the historical predecessor identities.

Exact skill inventory, categories, installation paths, plugin bundling, supported agents, and toolkit setup commands are freshness-sensitive.

## Distribution paths and example skill

The pinned [AWS Toolkit skills index](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/skills/README.md) describes standalone core and specialized instructions under `skills/`, distinct from client plugins that bundle skills and MCP configuration. `npx skills add aws/agent-toolkit-for-aws/skills` installs from the standalone tree; runtime MCP discovery does not install those files locally.

The plugin-bundled [`aws-ai-ml` skill](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/plugins/aws-core/skills/aws-ai-ml/SKILL.md) resides under `plugins/aws-core/skills/`, not the standalone `skills/` tree. Its SageMaker guidance covers model selection, datasets, training and fine-tuning, evaluation, deployment, inference optimization and endpoint diagnostics, including Python SDK v3. Bedrock-native Agents, Knowledge Bases and Guardrails are explicitly outside its validated workflows.

Public skill discovery does not grant credentials. Cloud actions, training, endpoint changes and deployments require approved AWS permissions, regional/data-boundary review and cost controls. No AWS operations or client installation were performed in this audit.

## Source interpretation

The AWS toolkit's skill collection is distinct from its MCP server, client plugins, rules files and cloud services. The repository license is Apache-2.0. Public documentation search and discovery do not require an AWS account; API operations and scripts require configured AWS credentials and separate scoped authorization.

[Reviewed original README](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws)
- [Pinned standalone skills index](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/skills/README.md)
- [Pinned bundled `aws-ai-ml` skill](https://github.com/aws/agent-toolkit-for-aws/blob/24865b67ffc305fc4e05c4097bc573d7a83037ca/plugins/aws-core/skills/aws-ai-ml/SKILL.md)
