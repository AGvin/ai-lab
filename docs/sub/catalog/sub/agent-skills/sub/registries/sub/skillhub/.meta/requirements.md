# Documentation Requirements

## Requirements

- Present SkillHub / skill-marketplace.com as an independent open-source Agent Skills marketplace/aggregation platform.
- Keep claims about source aggregation, search/discovery, installation, supported clients, quality/security signals, hosting/deployment, and marketplace behavior tied to current first-party evidence.
- Distinguish the marketplace/aggregator from the original repositories and publishers whose skills it exposes.
- Do not treat aggregation, ranking, or scanning as proof of safety or quality.

## Freshness

- Re-verify aggregation sources, installation workflow, supported clients, deployment/project status, and trust features before substantive edits.

## References

- Official site: https://www.skill-marketplace.com/

## Scoped original-source qualification — 2026-11-06

- SkillHub presents an open-source aggregation and authoring marketplace drawing from GitHub repositories; its homepage describes full-text discovery, Markdown/YAML authoring, ranking and source aggregation. Counts, features and availability are mutable.
- Aggregation, stars, format checks and quality badges do not establish upstream license provenance, trust or security of installed instructions.
- Verified first-party source 1: https://www.skill-marketplace.com/
- This review accepts only the current registry identity and source boundaries. It does not assert a full freshness audit, vendor-independent security, tested skill execution, complete CI/cache/schema/render, copyright clearance or verified current listing totals.

## Publisher source identity, synchronization and licensing review — 2026-11-09

- The [publisher `dukelyuu/skills-marketplace` README](https://github.com/dukelyuu/skills-marketplace) explicitly links the catalog to `https://www.skill-marketplace.com/` and describes the React 19.2/TypeScript and FastAPI/SQLite deployment, GitHub source management, scheduler, Markdown editor and optional GitHub token. Do not conflate this named marketplace with unrelated Tencent, openJiuwen, or other products called SkillHub.
- The official [source-management page](https://www.skill-marketplace.com/sources) has separately reported `Active`, `Syncing`, and `Pending` sources, including entries with zero indexed skills or `Never` synced. Do not present source count, index count, star sum, source freshness or badge as complete successful source coverage. Current counts are dynamic and contradictory across independently indexed snapshots; no fixed tally is accepted.
- **Publisher license conflict:** the source README displays an `MIT` badge, but the same README's bottom `License` section states `Apache-2.0`, and the actual root [`LICENSE`](https://github.com/dukelyuu/skills-marketplace/blob/main/LICENSE) is Apache-2.0. Prefer the exact license file for identified repository code, record the inconsistent badge as unresolved publisher metadata, and do not infer a blanket license to included third-party skills, GitHub source content or hosted uploads. This corrects the unsupported platform-wide MIT assumption recorded in earlier bounded source notes.
- The product advertises hosted aggregation and an editor; running its published Docker/FastAPI backend and configuring `GITHUB_TOKEN` is a separate trust, deployment and secret-access decision. No server, sync, repo import, generated skill or credential was executed or tested.
- Read-only first-party GitHub README blob `421de55da96708d72b77e67be5cb495d8dca447d` and root LICENSE blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` (2026-11-09); site snapshot has limited machine-readable access, so no complete live inventory/security badge freshness or full hosted feature parity is certified.
