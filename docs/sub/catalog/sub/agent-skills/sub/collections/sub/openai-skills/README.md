# OpenAI Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

The `openai/skills` repository is retained here as the source of the selected OpenAI system skill, but the repository is currently deprecated. Its official notice directs current Codex plugin examples and new plugin development to [OpenAI Plugins](https://github.com/openai/plugins).

## Producer

- [OpenAI](../../../../../producers/sub/o/sub/openai/)

## Selected skill

| Skill | Purpose | Official source |
| --- | --- | --- |
| Skill Creator | Guide for creating or updating effective Agent Skills. | [Source](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |

### Skill Creator

Skill Creator documents how to design and update skills around a required `SKILL.md` plus optional scripts, references, assets, and agent-facing metadata. The selected source is the `.system/skill-creator` directory in the deprecated repository; this page does not treat differently named skills in the successor plugin repository as the same identity without an explicit upstream mapping.

## Local execution, validation and rights

The selected historical [initializer](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/init_skill.py) creates a skill directory and writes `SKILL.md`, `agents/openai.yaml`, and optional example files. The separate metadata generator can write or replace `agents/openai.yaml`. **Review the output path and approve repository changes before executing these scripts.**

The bundled [`quick_validate.py`](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py) checks basic frontmatter structure and metadata, **not** generated code safety, runtime behavior, dependency integrity or authorization. The inspected Python helpers do not themselves declare network operations, but downstream skills or external integrations can access other systems and require separate approval.

The selected Skill Creator directory contains an [Apache-2.0 license](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt). Its imported [PyYAML dependency is MIT licensed](https://github.com/yaml/pyyaml/blob/main/LICENSE). This does not grant rights over project files, other repository skills or optional connected services. Source checks were static only: no script was installed or executed.

## Repository status

As verified on 2026-08-12, `openai/skills` is deprecated and points readers to `openai/plugins` for current Codex plugin examples. The old repository remains relevant here because it is still the official source path for the selected Skill Creator material documented above.

## Source interpretation

OpenAI marks openai/skills deprecated and directs current Codex skill/plugin examples to openai/plugins. Retain this identity only as the historical/system source already selected here; it is not a current-installation recommendation. Licenses are stored per skill directory. Repository deprecation is distinct from GitHub archival status.

[Reviewed original README](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Deprecated OpenAI Skills repository](https://github.com/openai/skills)
- [OpenAI Plugins repository](https://github.com/openai/plugins)
