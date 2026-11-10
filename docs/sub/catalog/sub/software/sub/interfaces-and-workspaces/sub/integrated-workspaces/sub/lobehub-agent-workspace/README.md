# LobeHub Agent Workspace

**LobeHub**, formerly presented as LobeChat, is a source-available workspace for configuring, scheduling and collaborating with AI agents. The [first-party repository](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/README.md) describes an agent-centered application and integrations with separately operated model providers.

## Self-hosting and operations

The [pinned self-hosting guide](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/docs/self-hosting/start.mdx) covers several deployment approaches, including Docker Compose. Its architecture includes a Next.js frontend/backend, PostgreSQL for conversations and agent state, optional Redis for caching/sessions, and S3-compatible object storage for files. Backup and restore of database and stored files, configuration/secrets, authentication, network exposure, updates and observability are the self-hosting operator's responsibilities.

Agents and integrations may forward prompts, documents or tool outputs to external services. Review credentials, scopes, data retention, schedules, model charges and approval for sensitive actions. A local application deployment is not equivalent to locally hosted inference.

## Rights boundary

LobeHub uses the **[LobeHub Community License](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/LICENSE)**, not plain Apache-2.0. The license permits unmodified commercial use but separately requires a commercial license for developing and distributing commercial derivative works. This is a **custom source-available license**, not an unconditional open-source grant. Confirm intended modifications, distribution and hosted-service terms against the published license before deployment; third-party model, extension and data terms remain separate.

This is a source-backed catalog reader, not a claim of installation, runtime testing, full legal review or a whole-catalog clean pass.

## Official sources

- [Pinned LobeHub README](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/README.md)
- [Pinned self-hosting architecture](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/docs/self-hosting/start.mdx)
- [Pinned LobeHub Community License](https://github.com/lobehub/lobehub/blob/b2b1601f6fe51148b09289aecfd71eba6af22da1/LICENSE)
