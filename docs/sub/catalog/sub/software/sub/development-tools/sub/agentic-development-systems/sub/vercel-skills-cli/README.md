# Vercel Skills CLI

**Vercel Skills CLI** is the independent MIT-licensed npm `skills` tool for discovering and managing Agent Skills across coding agents. It is not the public [skills.sh registry](../../../../../../../agent-skills/sub/registries/sub/skills-sh/) or the [Vercel Agent Skills collection](../../../../../../../agent-skills/sub/collections/sub/vercel-agent-skills/).

## Released software

- Original public stable **v1.7.4 (2026-10-19)** requires **Node.js >=22.20.0**, and exposes `skills` / `add-skill` binaries; the publisher documents invocation as `npx skills`.
- Find, install, list, use, check, update, remove and initialize skills using the `add`, `find`, `list`, `use`, `check`, `update`, `remove` and `init` commands. `experimental_sync` and `experimental_install` are previews.
- Repository and local sources, project or global installs, target-agent paths and update behavior depend on the pinned version and client. Pin original source revisions when reproducible installation matters.

## Operational risks

Installed skills may contain untrusted scripts, agent instructions and file operations. Inspect the entire original skill, dependencies, requested permissions, repository revision and local changes before running with coding-agent privileges. Registry ranking or scanning is not a security guarantee.

Original documentation describes anonymous telemetry and security-audit requests. It documents `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` to disable these in the inspected version. This is not independent privacy verification for other agents, Git hosting or third-party skills. The CLI code is MIT; installed skills have separate licenses and provenance. Ultimate beneficial ownership and indirect stakes remain unaudited.

## Relations

- Produced by: [Vercel Inc.](../../../../../../../producers/sub/v/sub/vercel-inc/).
- Related discovery registry: [skills.sh](../../../../../../../agent-skills/sub/registries/sub/skills-sh/).
- Separate original skill collection: [Vercel Agent Skills](../../../../../../../agent-skills/sub/collections/sub/vercel-agent-skills/).

## Original sources

- [Source](https://github.com/vercel-labs/skills)
- [v1.7.4 release](https://github.com/vercel-labs/skills/releases/tag/v1.7.4)
- [npm package](https://www.npmjs.com/package/skills)
- [Original command reference](https://github.com/vercel-labs/skills/blob/v1.7.4/docs/commands.md)
- [Telemetry and configuration](https://github.com/vercel-labs/skills/blob/v1.7.4/docs/troubleshooting.md)
