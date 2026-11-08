# Sentry Skills

**Sentry Skills** is [Sentry](../../../../../producers/sub/s/sub/sentry/)'s official repository of Agent Skills for its engineering and development teams. It covers coding practices, code reviews, security, documentation, PR workflows and related work. This collection is separate from **Sentry for AI**, which supplies developer-facing plugin integrations for Sentry setup and monitoring.

## Collection and distribution

The first-party repository keeps skills under `skills/`, supporting agent instructions under `agents/`, and marketplace metadata in `.claude-plugin/`. The marketplace registers a `sentry-skills` plugin from the root; `.agents/skills` mirrors the source tree for compatible clients. Entries such as `code-review`, `security-review`, `commit` and `skill-scanner` are **collection-owned skills**, not independently counted AI Lab entities.

The published [README](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/README.md) documents Claude Code registration via `claude plugin marketplace add getsentry/skills` and `claude plugin install sentry-skills@sentry-skills`. For compatible skills.sh hosts, it also documents `npx skills add getsentry/skills`. Installation support and permissions depend on the specific client and organization.

## Newly indexed browser skill and authorization

The [`browse-local-sentry` source](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/browse-local-sentry/SKILL.md) enables development QA and screenshots of Sentry. **Its two modes have different security boundaries:** a `dev-ui` hostname connects to **production Sentry data** through the user's own signed-in Chrome, potentially including elevated staff/superuser privileges, while the full devserver uses a local database.

For `dev-ui`, stay in the explicitly selected organization and read-only until the user approves a specific change. Do not enter the user's credentials, bypass TLS warnings, modify existing user tabs, or change their MCP/browser configuration without consent. No browser or Sentry service was connected or exercised in this research.

## Permissions and licensing

Some workflows inspect source, run tools, work with Git/GitHub or depend on access to engineering infrastructure. Review each pinned `SKILL.md` and its dependencies; operate only in authorized repositories, keep credentials scoped, and obtain approval before changes or production actions. Generated findings and reviews require independent verification.

The repository's root [Apache-2.0 license](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/LICENSE) governs covered source material, not private Sentry projects, telemetry, vendor accounts or third-party vendored sources without their own terms. No skills were installed or executed for this catalog entry.

## Relations

- Produced by: [Sentry](../../../../../producers/sub/s/sub/sentry/)
- Separate collection: [Sentry for AI](../sentry-for-ai/)

## Official resources

- [Sentry Skills source](https://github.com/getsentry/skills)
- [Pinned README and installation](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/README.md)
- [Marketplace manifest](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/.claude-plugin/marketplace.json)
- [License](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/LICENSE)
