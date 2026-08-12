# Documentation Requirements

## Requirements

- Identify NVIDIA Skills as NVIDIA's official verified Agent Skills catalog and link the canonical NVIDIA producer profile, official repository, and official documentation.
- Explain that the catalog includes NVIDIA-authored and product-repository skills and uses an automated synchronization/catalog pipeline; keep provenance/governance language scoped to what the official repository supports.
- Present the selected collection-owned Skill Card Generator with a compact overview and a concise detail section; do not create a duplicate standalone catalog page.
- Describe Skill Card Generator as a governance workflow for generating or updating a draft skill card for an existing Agent Skill directory, not as a general skill authoring tool.
- Preserve current prerequisites: Python 3, `jinja2`, an existing target skill directory, scoped file access, and the three bundled scripts `discover_assets.py`, `render_card.py`, and `validate_submission.py`.
- Preserve the bundled style guide, card template, catalogs, and human-review boundary; generated cards remain drafts and do not replace legal, safety, or owner review.
- Link the selected skill to `https://github.com/NVIDIA/skills/tree/main/skills/skill-card-generator` and retain the official `skills` CLI installation context without hardcoding mutable catalog counts.

## Validation

- Skill Card Generator is represented exactly once and links to its official source directory.
- Runtime permissions and human-review constraints are not weakened or generalized beyond the upstream skill.
- No local standalone Skill Card Generator catalog node is linked.
- The page contains no temporary RC summary wording.
