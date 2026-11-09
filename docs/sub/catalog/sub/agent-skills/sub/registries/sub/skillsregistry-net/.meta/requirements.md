# Documentation Requirements

## Requirements

- Present SkillsRegistry.net as an independent Agent Skills registry/governance service with emphasis on organizational discovery and trust/security controls.
- Document trust scoring, scanning, governance, private-registry, organization/team, installation, and supported-client behavior only when verified from current first-party sources.
- Separate registry-provided security signals from independent proof that a skill is safe or suitable for a consequential workflow.
- Keep generic enterprise skill-governance methodology outside this concrete registry profile.

## Freshness

- Re-verify security/trust features, private-registry behavior, plans/access boundaries, client support, and installation workflow before substantive edits.

## References

- Official site: https://skillsregistry.net/

## Scoped original-source qualification — 2026-11-06

- SkillsRegistry.net exposes hosted REST/MCP discovery, provenance/trust-score signals and a separately documented self-host option. Its first-party source explicitly distinguishes indexed records from audited/signed subsets, so it does not promise all indexed skills have undergone deep review.
- Unsigned or unscanned entries must not be described as verified; any security score or hosted/self-hosted feature is an operator claim, not independent validation of a skill.
- Verified first-party source 1: https://skillsregistry.net/
- Verified first-party source 2: https://skillsregistry.net/agents
- This review accepts only the current registry identity and source boundaries. It does not assert a full freshness audit, vendor-independent security, tested skill execution, complete CI/cache/schema/render, copyright clearance or verified current listing totals.

## Hosted/local parity and freshness reconciliation — 2026-11-09

- First-party [SkillsRegistry site](https://skillsregistry.net/) advertises one-command local deployment with hosted-equivalent semantic search, publishing, scoring and MCP. The separate [publisher source README](https://github.com/cogniumhq/skillsregistry) explicitly says the Apache-2.0 repository includes SDKs and a single-tenant local node, while the actual hosted service runs separately on **proprietary code**. This is a material provider-source discrepancy; do not certify local/hosted feature parity from marketing.
- The source README states local `apps/local` requires Postgres/pgvector and an embedding provider; air-gap search and local publishing are supported, but the local node **does not run Cognium's hosted trust-scoring engine**, and local `resolve_composition` is not implemented yet. Hosted scoring/leaderboards require separate provider keys, with connected-mode signup described as preview.
- Distinguish advertised dashboard counts, scores and scanned or verified subsets from complete independent safety coverage. Dynamic index totals on publisher landing pages are not an identity denominator. Require the exact deployed revision, deployment image provenance, current docs, provider terms and actual environment integration tests before recommending parity or claims of 100% verified skills.
- Source: inspected publisher README `cogniumhq/skillsregistry` blob `6dd253530ac60127a64d73e96886f271d379a33a` and Apache-2.0 root LICENSE blob `ccd24c8eaf707ccada1d864b62ef578f84c19580` on 2026-11-09; compared first-party hosted page. Full independent CI, endpoint access/security scoring, license of proprietary hosted code, and local image execution remain outside this bounded review.
