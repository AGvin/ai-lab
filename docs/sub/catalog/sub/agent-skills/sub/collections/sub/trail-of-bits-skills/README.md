# Trail of Bits Skills

**Trail of Bits Skills** is [Trail of Bits](../../../../../producers/sub/t/sub/trail-of-bits/)' first-party repository of Agent Skills and Claude plugins for AI-assisted security research, auditing and development. It publishes a coordinated plugin marketplace from one maintained source repository, not an independent multi-publisher skill registry or one separately counted catalog product per included plugin.

## Collection and example workflows

The pinned source includes a [marketplace manifest](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/.claude-plugin/marketplace.json), plugin packages under `plugins/`, and skill instructions with optional bundled scripts/resources inside individual plugins. Selected collection-owned examples:

| Included plugin | Purpose | First-party source |
| --- | --- | --- |
| Differential Review | Security-focused review of code changes using git history, call-site impact and validation evidence. | [Source](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/plugins/differential-review/skills/differential-review/SKILL.md) |
| Supply Chain Risk Auditor | Assess npm, PyPI and Go dependencies for published advisories, maintainer concentration and installation risks. | [Source](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/plugins/supply-chain-risk-auditor/.claude-plugin/plugin.json) |

These are examples **inside this collection**, not standalone AI Lab catalog entities. Available plugins and version numbers may change; the root marketplace version does not represent the installed version of every plugin.

## Distribution and installation

The [official README](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/README.md) documents Claude Code registration via `/plugin marketplace add trailofbits/skills` and Codex registration via `codex plugin marketplace add trailofbits/skills`, followed by selection of individual plugins. It also describes importing the repository's `.claude-plugin/marketplace.json` into supported ChatGPT workspaces. Host capabilities, enterprise policy, bundled dependencies and required permissions vary. This record does not claim that the collection is installed in any environment.

## Security, licensing and provenance

**Use only in authorized contexts.** Skills can request filesystem access, shell tools, analyzers, network services and repository changes. Before use, inspect a pinned `SKILL.md`, executable dependencies, plugin manifest and permissions; use least privilege, trusted inputs and an isolated test environment. Do not run security scans on systems without permission, treat generated findings as verified without corroboration or give plugins production secrets by default.

The repository's root license is [Creative Commons Attribution-ShareAlike 4.0](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/LICENSE). Attribution and share-alike terms apply to covered material, but do not automatically clear rights for third-party code, dependencies, datasets, artifacts or systems under assessment. No local installation, vulnerability scan, comprehensive dependency audit or runtime verification was performed for this catalog profile.

## Relations

- Produced by: [Trail of Bits](../../../../../producers/sub/t/sub/trail-of-bits/)

## Official resources

- [Trail of Bits Skills source](https://github.com/trailofbits/skills)
- [Pinned setup and plugin list](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/README.md)
- [Marketplace manifest](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/.claude-plugin/marketplace.json)
- [Root license](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/LICENSE)
