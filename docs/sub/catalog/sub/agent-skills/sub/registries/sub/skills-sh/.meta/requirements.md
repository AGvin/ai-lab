# Documentation Requirements

## Requirements

- Present skills.sh as the public Agent Skills discovery index and leaderboard, distinct from independently cataloged Skills CLI software from Vercel Labs.
- Link to the independent Skills CLI profile for versioned installation commands, supported agents and telemetry. Do not duplicate that software's operating instructions on the registry page.
- Explain that installation copies skills into selected agent/client locations and that subsequent local edits or update behavior depend on the current CLI/client workflow.
- Document current ranking/popularity and telemetry behavior only from current official sources; include opt-out behavior such as `DISABLE_TELEMETRY=1` only while it remains verified.
- Explain security/scanning signals as registry features, not guarantees of quality, safety, or trustworthiness.
- Describe the optional Skills Packs feature as unlisted, not access-controlled: anyone holding a pack URL may view and install it even when it contains private files or GitHub-sourced material. Warn never to package secrets, credentials, confidential instructions or proprietary third-party material without appropriate rights and disclosure approval.
- Clarify source/redistribution rights: skills.sh's official Terms say the original authors retain ownership and source-repository licenses control individual skills. The separate Vercel Labs Skills CLI's MIT repository license does not confer rights over third-party indexed skill contents or hosted private packs.
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

## Pack privacy and rights source reconciliation — 2026-11-09

- [First-party Packs documentation](https://www.skills.sh/docs/packs) explicitly states that packs can include private files, folders, zip archives and connected GitHub skills, but pack URLs are **unlisted, not access-controlled**. A recipient with the URL can install the pack; do not place secrets in it.
- [First-party skills.sh Terms](https://www.skills.sh/terms) state that original skill authors retain content ownership, applicable source-repository licenses control reuse, and directory listing transfers no rights. The [Vercel Labs Skills CLI MIT license](https://github.com/vercel-labs/skills/blob/main/LICENSE) is scoped to the software repository, not every indexed skill.
- These observations concern the registry and pack privacy boundary; current API, CLI update/install semantics, per-skill ownership, pack security and independent runtime behavior remain unverified. No pack, skill or CLI was installed or executed.
