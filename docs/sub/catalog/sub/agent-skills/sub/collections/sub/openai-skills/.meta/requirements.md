# Documentation Requirements

## Requirements

- Identify OpenAI Skills as the `openai/skills` collection retained for cataloging the selected historical/system skill source, while clearly stating that the repository is deprecated and directs current Codex plugin examples to `openai/plugins`.
- Link the canonical OpenAI producer profile, the deprecated source repository, and the current OpenAI Plugins successor repository.
- Time-scope the deprecation statement to current source verification rather than implying that repository status can never change.
- Preserve the deprecated repository's historical `.system`, `.curated`, and `.experimental` category distinction only as time-scoped source history; do not present those categories or their former `$skill-installer` flows as the current Codex distribution contract.
- Preserve the collection-level licensing boundary that individual skills can carry their own license files; do not infer one license or trust level for every skill in the repository.
- Present Skill Creator as the selected collection-owned skill source from `skills/.system/skill-creator` in the deprecated repository; do not create a duplicate standalone catalog page.
- Describe Skill Creator as guidance for creating or updating effective skills, including the role of `SKILL.md`, optional scripts, references, assets, and OpenAI agent-facing metadata where supported by its source.
- Specify the historical Skill Creator's real execution/permission scope: `init_skill.py` creates a skill directory, `SKILL.md`, and `agents/openai.yaml` with optional examples, while `generate_openai_yaml.py` updates YAML metadata. Require explicit authorization for the intended project/output path.
- `quick_validate.py` checks only basic SKILL.md YAML/frontmatter/name/description: this is not a code security audit, execution sandbox, malware scan, dependency integrity review, or behavioral test.
- Distinguish the selected directory's Apache-2.0 license from external PyYAML's MIT license, non-selected historical skills, third-party services and user content. A reference example showing an external MCP endpoint is documentation, not an automatically enabled integration.
- Do not claim that the deprecated OpenAI Skills repository is the current primary Codex skill distribution surface.
- Do not substitute the differently named `plugin-creator` or other successor-repository skills for Skill Creator unless a future source explicitly establishes that identity relationship.

## Selected Skill Source

- Skill Creator: `https://github.com/openai/skills/tree/main/skills/.system/skill-creator`

## Validation

- The collection page visibly distinguishes deprecated source status from the current OpenAI Plugins repository.
- Historical `.system`, `.curated`, and `.experimental` structure is labeled as deprecated-source history rather than current installation guidance.
- Skill-level license variability is preserved without turning source presence into a quality or safety endorsement.
- Skill Creator is represented exactly once as collection-owned historical/system source material.
- No local standalone Skill Creator catalog node is linked.
- Claims about current OpenAI distribution are not inferred beyond the official repository deprecation notice.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.

## Selected Skill Creator source, rights and local-effects review — 2026-11-09

- Read the complete selected upstream `skills/.system/skill-creator` tree at revision `49f948faa9258a0c61caceaf225e179651397431`; directory entries and repository README match the inspected current/default branch. This is source parity, not current runtime certification.
- [Original instructions](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md), [initializer](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/init_skill.py), [metadata generator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/generate_openai_yaml.py) and [quick validator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py) establish the bounded local write/validation scope; no scripts were executed.
- [Selected skill LICENSE.txt](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt) states Apache-2.0. The runtime import PyYAML is separately [MIT licensed](https://github.com/yaml/pyyaml/blob/main/LICENSE). Neither license covers non-selected skills, private project data or connected MCP services.
- The three selected bundled Python scripts have no apparent direct network or subprocess calls in the read source. This is static source evidence, not an assertion about Python environment behavior or generated scripts. Approve path writes and review generated code before execution.
