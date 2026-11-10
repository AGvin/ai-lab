# Google Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Google Agent Skills is Google's official repository-backed collection of Agent Skills for Google products and technologies, including Google Cloud.

## Producer

- [Google](../../../../../producers/sub/g/sub/google/)

## Collection boundary

Individual skills remain part of the collection unless a later task establishes a durable standalone identity. The collection is distinct from Google ADK, Gemini CLI, Gemini models, and Google Cloud services even when skills operate those surfaces.

Exact skill inventory, plugin packaging, installation commands, supported coding agents, and repository structure are freshness-sensitive.

## Recently added skill sources and boundaries

The [newer first-party skills index](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/README.md) adds two entries relative to the previous inspected revision:

- [`pathways-workload`](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/skills/cloud/pathways-workload/SKILL.md) — investigates failed, restarting or stalled Pathways-on-Cloud GKE workloads from Cloud Logging, node and workload evidence. Its diagnostic context is not authorization to create clusters or deploy workloads.
- [`api-gateway-troubleshooting`](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/skills/cloud/api-gateway-troubleshooting/SKILL.md) — diagnoses *Google Cloud API Gateway* failures, not Apigee, Cloud Endpoints or GKE Gateway API. Read-only investigation is the default; IAM, gateway and API-config modifications require explicit authorization. Do not grant broad access, expose backends publicly, or include secrets in logs.

The first-party install/update commands are `npx skills add google/skills` and `npx skills update`. Skills are instruction content, not OAuth grants, Google Cloud roles, operational approval or a guarantee that linked repositories/preview capabilities work in a selected client.

## Source interpretation

Google's Apache-2.0 collection covers Google product and Cloud workflows. Its index includes entries explicitly labeled preview and links additional independently maintained skill repositories; collection publication does not make every contained API generally available or every linked repository part of this distribution. Cloud IAM, billing and client prerequisites remain external.

[Reviewed original README](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Google Agent Skills repository](https://github.com/google/skills)
