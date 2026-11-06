# Sentry Skills

**Sentry Skills** is [Sentry](../../../../../producers/sub/s/sub/sentry/)'s official repository of Agent Skills for its engineering and development teams. It covers coding practices, code reviews, security, documentation, PR workflows and related work. This collection is separate from **Sentry for AI**, which supplies developer-facing plugin integrations for Sentry setup and monitoring.

## Collection and distribution

The first-party repository keeps skills under `skills/`, supporting agent instructions under `agents/`, and marketplace metadata in `.claude-plugin/`. The marketplace registers a `sentry-skills` plugin from the root; `.agents/skills` mirrors the source tree for compatible clients. Entries such as `code-review`, `security-review`, `commit` and `skill-scanner` are **collection-owned skills**, not independently counted AI Lab entities.

The published [README](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/README.md) documents Claude Code registration via `claude plugin marketplace add getsentry/skills` and `claude plugin install sentry-skills@sentry-skills`. For compatible skills.sh hosts, it also documents `npx skills add getsentry/skills`. Installation support and permissions depend on the specific client and organization.

## Permissions and licensing

Some workflows inspect source, run tools, work with Git/GitHub or depend on access to engineering infrastructure. Review each pinned `SKILL.md` and its dependencies; operate only in authorized repositories, keep credentials scoped, and obtain approval before changes or production actions. Generated findings and reviews require independent verification.

The repository's root [Apache-2.0 license](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/LICENSE) governs covered source material, not private Sentry projects, telemetry, vendor accounts or third-party vendored sources without their own terms. No skills were installed or executed for this catalog entry.

## Relations

- Produced by: [Sentry](../../../../../producers/sub/s/sub/sentry/)
- Separate collection: [Sentry for AI](../sentry-for-ai/)

## Official resources

- [Sentry Skills source](https://github.com/getsentry/skills)
- [Pinned README and installation](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/README.md)
- [Marketplace manifest](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/.claude-plugin/marketplace.json)
- [License](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/LICENSE)
