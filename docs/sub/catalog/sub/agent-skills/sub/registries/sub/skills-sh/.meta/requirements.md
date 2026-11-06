# Documentation Requirements

## Requirements

- Present skills.sh as the public Agent Skills discovery index and leaderboard, distinct from independently cataloged Skills CLI software from Vercel Labs.
- Link to the independent Skills CLI profile for versioned installation commands, supported agents and telemetry. Do not duplicate that software's operating instructions on the registry page.
- Explain that installation copies skills into selected agent/client locations and that subsequent local edits or update behavior depend on the current CLI/client workflow.
- Document current ranking/popularity and telemetry behavior only from current official sources; include opt-out behavior such as `DISABLE_TELEMETRY=1` only while it remains verified.
- Explain security/scanning signals as registry features, not guarantees of quality, safety, or trustworthiness.
- Keep generic advice about reviewing third-party skills, pinning trusted revisions, and cross-client portability in the appropriate concept/learning guidance rather than making it intrinsic skills.sh identity.

## Freshness

- Re-verify CLI commands, supported agents, telemetry, ranking inputs, scanning behavior, and installation/update semantics before substantive edits because these are mutable service/tool facts.

## References

- Official site: https://skills.sh/
- CLI documentation: https://www.skills.sh/docs/cli
- Official repository: https://github.com/vercel-labs/skills

## Scoped original-source qualification — 2026-11-06

- skills.sh is the public Agent Skills leaderboard. The site states that rankings use aggregated anonymized usage telemetry collected by the separate open-source Vercel Labs Skills CLI. The CLI supports installation/update and publishes an opt-out via DISABLE_TELEMETRY=1 or DO_NOT_TRACK=1.
- The registry is not the CLI software entity; scanner/telemetry indicators are not code-safety guarantees. Pinned CLI versions, exact clients and local paths need their own runtime validation.
- Verified first-party source 1: https://www.skills.sh/docs
- Verified first-party source 2: https://github.com/vercel-labs/skills/blob/main/README.md
- This review accepts only the current registry identity and source boundaries. It does not assert a full freshness audit, vendor-independent security, tested skill execution, complete CI/cache/schema/render, copyright clearance or verified current listing totals.
