# Documentation Requirements

## Requirements

- Identify Google Agent Skills as Google's official repository-backed collection of Agent Skills for Google products and technologies, including Google Cloud.
- Preserve the collection boundary rather than creating one catalog entity per individual skill unless a later task explicitly selects independently durable skill identities.
- Treat the exact skill inventory, plugin packaging, installation commands, supported coding agents, and repository structure as freshness-sensitive.
- Preserve two newly indexed, collection-owned skills at the inspected revision: `pathways-workload` (diagnosing Pathways on Cloud GKE workloads) and `api-gateway-troubleshooting` (Google Cloud API Gateway error and deployment diagnosis). Do not turn directories into separate catalog collections or infer their scope from names alone.
- The Pathways troubleshooting skill collects Cloud Logging, node and workload evidence but is not authorization to provision a new cluster or deployment. The API Gateway skill scopes itself to Google Cloud API Gateway (not Apigee, Cloud Endpoints or GKE Gateway API), defaults to read-only diagnosis, requires explicit approval for IAM/API config/gateway changes, and forbids broad IAM grants or making a backend public as an auth workaround; redact tokens and bounded logs.
- Distinguish the source's `npx skills add google/skills` and `npx skills update` from credentials, Cloud IAM, live service access, production operations and independently maintained linked repositories.
- Preserve source licensing and per-skill/reference boundaries without interpreting official source status as a blanket quality or safety endorsement.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The collection is not conflated with Google ADK, Gemini CLI, Gemini models, or Google Cloud services.
- Producer provenance resolves to Google.

## Bounded upstream source reconciliation — 2026-11-09

- Compared [earlier first-party index](https://github.com/google/skills/blob/cd6fde0b299b34bbad05f64ad1ed5bd2ed05e634/README.md) with the [newer index](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/README.md). The exact README diff adds just two skill links: `pathways-workload` and `api-gateway-troubleshooting`.
- Verified the corresponding [Pathways SKILL.md](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/skills/cloud/pathways-workload/SKILL.md), [Gateway SKILL.md](https://github.com/google/skills/blob/2194d3b8b1f31975fef2f1a0ae6b9ab55bd7ceee/skills/cloud/api-gateway-troubleshooting/SKILL.md) and unchanged root Apache-2.0 LICENSE blob between the compared revisions.
- This is a bounded source/permission correction; no full collection freshness marker, runtime test, model evaluation, OAuth validation, cloud service call or independently audited license/dependency clearance is claimed.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
