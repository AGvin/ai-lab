# SkillsRegistry.net

SkillsRegistry.net is an independent Agent Skills registry and governance service emphasizing organizational discovery and trust or security controls.

Trust scoring, scanning, governance, private-registry features, organization or team behavior, supported clients, plans or access boundaries, and installation workflows are mutable service facts. Registry-provided signals are not independent proof that a skill is safe or suitable for a consequential workflow.

## Hosted versus self-hosted

The operator's [public site](https://skillsregistry.net/) advertises hosted trust scoring and local deployment together. The [publisher source](https://github.com/cogniumhq/skillsregistry) clarifies that the hosted catalog runs **separately on proprietary code**; its Apache-2.0 repository contains SDK packages and a self-hosted local node, not a complete hosted-service replica.

The local node supports search, MCP discovery and local publishing using Postgres/pgvector and an embedding provider. **It does not run the hosted trust-scoring engine**; composition resolution is incomplete locally, and connected scoring/leaderboards require separate hosted access. A provider trust score or an unscanned record is not independent proof of safe execution. Verify current plan terms, deployment version, underlying source licenses and actual features before treating the local installation as hosted-equivalent.

**Rights boundary:** the [repository Apache-2.0 license](https://github.com/cogniumhq/skillsregistry/blob/main/LICENSE) applies to its open-source code, **not** the hosted proprietary service or third-party listed skills. Never treat an indexed skill as licensed for redistribution merely because it appears in the public catalog. These are source/documentation checks; no server, container, MCP client or skill was installed or executed.
## Official resource

- [SkillsRegistry.net](https://skillsregistry.net/)
