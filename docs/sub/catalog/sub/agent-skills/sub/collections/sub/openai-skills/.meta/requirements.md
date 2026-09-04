# Documentation Requirements

## Requirements

- Identify OpenAI Skills as the `openai/skills` collection retained for cataloging the selected historical/system skill source, while clearly stating that the repository is deprecated and directs current Codex plugin examples to `openai/plugins`.
- Link the canonical OpenAI producer profile, the deprecated source repository, and the current OpenAI Plugins successor repository.
- Time-scope the deprecation statement to current source verification rather than implying that repository status can never change.
- Preserve the deprecated repository's historical `.system`, `.curated`, and `.experimental` category distinction only as time-scoped source history; do not present those categories or their former `$skill-installer` flows as the current Codex distribution contract.
- Preserve the collection-level licensing boundary that individual skills can carry their own license files; do not infer one license or trust level for every skill in the repository.
- Present Skill Creator as the selected collection-owned skill source from `skills/.system/skill-creator` in the deprecated repository; do not create a duplicate standalone catalog page.
- Describe Skill Creator as guidance for creating or updating effective skills, including the role of `SKILL.md`, optional scripts, references, assets, and OpenAI agent-facing metadata where supported by its source.
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
