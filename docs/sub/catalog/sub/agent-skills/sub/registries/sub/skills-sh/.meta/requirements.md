# Documentation Requirements

## Requirements

- Present skills.sh as a public Agent Skills discovery index/leaderboard paired with the Vercel Labs `skills` CLI for discovering and installing skills from public repositories.
- Document the current CLI installation workflow from official documentation, including repository-source installation and selection of discovered skills/target agents, without treating a copied command as timeless API.
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
