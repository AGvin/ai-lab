# Documentation Requirements

## Requirements

- Identify Flowise as the generative-AI development platform with an Apache-2.0 core and separately licensed commercial components for visually building AI agents and LLM workflows through Assistant, Chatflow, and Agentflow builders, while reflecting its current upstream lifecycle rather than presenting it as an actively developed product.
- Preserve its primary placement under `workflow-engines/visual-ai-workflows`; tracing, evaluation, HITL, APIs/SDKs, teams, and deployment features extend the visual workflow platform rather than creating separate products.
- Preserve FlowiseAI Inc. as the producer/company behind the upstream project while keeping the company, archived software codebase, Flowise Cloud, and future community forks as distinct identity/operation layers.
- State the upstream lifecycle from the first-party sunset notice: July 29, 2026 is the feature-freeze date, August 10 the repository-archival date, and August 31 the EOL milestone for official core-team GitHub/Discord presence. The current repository is marked archived.
- Do not represent the archived upstream as currently maintained; the first-party sunset notice explicitly encourages users to fork the Apache-2.0-licensed code for internal or community-led maintenance.
- Distinguish locally/self-hosted Flowise software from Flowise Cloud and other managed service surfaces when discussing historical/current operating boundaries.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep builder capabilities, integrations, supported Node versions, hosted-service availability, migration/fork status, and other mutable implementation details source-backed when expanded.
- Include current official Flowise documentation, archived repository, legal, and sunset references.

- Scope the fork/licensing boundary to the Apache-2.0 portion: `packages/server/src/enterprise` and explicitly marked files use a commercial license, while third-party components retain their original licenses. The sunset notice does not replace those file-level license conditions.

## Validation

- The page reflects the August 2026 archived/EOL-transition state and does not imply active upstream feature development.
- FlowiseAI Inc., archived OSS code, hosted-service surfaces, and community-maintained forks are not conflated.
- The page reflects the known Assistant/Chatflow/Agentflow scope without reducing Flowise to a simple chain editor.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
