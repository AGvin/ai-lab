# Documentation Requirements

## Requirements

- Identify **Trail of Bits Skills** as a first-party coordinated Agent Skills and Claude plugin marketplace repository produced by Trail of Bits, not a standalone AI model, a multi-publisher skill discovery service, or separate canonically accepted identities for each nested skill and plugin.
- Distinguish the repository-wide `.claude-plugin/marketplace.json` catalog from selected `plugins/*` plugin packaging and nested `SKILL.md` workflow directories. Package/version metadata belong to individual plugins; marketplace metadata `1.0.0` is not the version of every plugin or guaranteed installed version.
- Use the pinned official repository state `711af095215ad4ecde5b90cd1d0124b3f1c4ca9e` (2026-11-02): first-party README, root LICENSE, marketplace manifest, and selected plugin/skill examples. Keep mutable supported hosts, plugin set, CLI syntax, dependency and permission requirements source-scoped.
- Show grounded examples (e.g., `differential-review` and `supply-chain-risk-auditor`) only as **collection-owned** entries, not independent canonical software or skill profiles; no second collection node for the ChatGPT import flow.
- Describe documented distribution accurately: Claude Code marketplace registration, Codex plugin marketplace registration, and ChatGPT workspace marketplace imports from the manifest. Import support is not a claim that every host, user account, or enterprise policy currently permits installation of every included plugin.
- The root repository LICENSE is CC BY-SA 4.0. Explain attribution/share-alike requirements for covered material; scripts, dependencies, references and target artifacts can have separate rights. Do not infer that the root license grants permission to analyze unrelated repositories or systems.
- Warn that skill/plugin instructions can call local tools, scripts, analyzers, network services and filesystem or Git operations. Review origin, code and permissions at a pinned revision; use least privilege, isolated test environments, trusted inputs and explicit security-assessment authorization. Installation does not make output correct, a plugin safe or a vulnerability finding validated.
- Avoid instructions to target systems without authorization, execute examples against production, or assert executed tests/installed integrations. Pin source links; do not hardcode plugin counts or claim a complete independent supply-chain audit.
- Preserve one reciprocal `produced-by` / `produces` relation with `catalog/producers/t/trail-of-bits`; index the collection exactly once in Agent Skill Collections.

## Validation

- [Pinned README](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/README.md), [marketplace manifest](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/.claude-plugin/marketplace.json), [root license](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/LICENSE), [differential-review plugin](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/plugins/differential-review/.claude-plugin/plugin.json), and [skill instructions](https://github.com/trailofbits/skills/blob/711af095215ad4ecde5b90cd1d0124b3f1c4ca9e/plugins/differential-review/skills/differential-review/SKILL.md) support these claims.
- Producer inverse, direct-child collection index and relative links resolve; no collection-owned skill is promoted to an independently accepted entity.
- No plugin installation, production security scan, credentialed action, full license/dependency audit, runtime safety certification, complete repository CI or whole-catalog clean pass is claimed.
