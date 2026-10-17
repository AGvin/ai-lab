# Documentation Requirements

## Requirements

- Identify Windmill as a self-hostable developer platform with an AGPLv3 core for turning code and scripts into jobs, workflows, APIs, internal applications, and related operational automation.
- Preserve its primary placement under `automation/developer-automation`; its workflow engine is part of a broader developer-facing automation platform rather than the sole product identity.
- Distinguish customer-operated Windmill deployments from Windmill Cloud. The self-hosted architecture separates the API/UI server, job-executing workers and PostgreSQL state/queue; documented deployment options include Docker and Kubernetes.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep supported languages, deployment modes, performance claims, enterprise features, and other mutable implementation details source-backed when expanded.
- Include current official Windmill site, repository, deployment and license references.
- Preserve the mixed-license boundary: AGPLv3 source, Apache 2.0 client/specification files and proprietary enterprise code. Prebuilt Community Edition images and release binaries include proprietary components with additional use/distribution terms; they are not interchangeable with a build from only the open-source portions.

## Validation

- The page presents Windmill as developer automation software rather than a generic AI agent or a hosted-only service.
- Hosted and self-managed operating boundaries are not conflated.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
