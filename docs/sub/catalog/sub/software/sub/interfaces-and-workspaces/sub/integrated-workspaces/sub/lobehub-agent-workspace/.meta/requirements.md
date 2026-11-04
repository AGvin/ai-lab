# Documentation Requirements

## Requirements

- Identify LobeHub (historically LobeChat) as a source-available, self-hostable integrated agent workspace, rather than a model, model-serving API, unrestricted open-source SDK, or hosted inference service.
- Pin the first-party source snapshot at `b2b1601f6fe51148b09289aecfd71eba6af22da1` with [README](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/README.md), [self-hosting architecture](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/docs/self-hosting/start.mdx), and [LICENSE](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/LICENSE).
- Describe agent creation, scheduling, model-provider integrations and collaborative workflows at the application level. Keep provider capabilities and hosted/paid product offerings separate.
- Distinguish self-hosted deployment methods, including Docker Compose, from operation of LobeHub's hosted service. The documented self-hosting stack uses a Next.js application, PostgreSQL, optional Redis and S3-compatible file storage; optional observability or search services are not mandatory in every installation.
- Explicitly state **LobeHub Community License** (custom source-available terms): the first-party license permits commercial operation of unmodified software and calls for a commercial license when developing and distributing commercial derivative works. It is **not** an unmodified Apache-2.0 license, and no permission beyond the text of the actual license is implied.
- Disclose backup, secrets, S3/object storage access, database migration, reverse-proxy, authentication, logging, agent permissions, workflow scheduling and model/API costs as operator responsibilities. Self-hosting does not prevent data egress to external model or connector services.
- Avoid inventing support/pricing guarantees, source-code redistribution rights, executed deployments, whole-repository QA, license counsel review or a whole-catalog clean pass.

## Validation

- Pinned official identity, deployment and license sources are independently recoverable.
- Exactly one canonical workspace identity is linked under Integrated Workspaces; older LobeChat name remains an alias rather than an extra entity.
