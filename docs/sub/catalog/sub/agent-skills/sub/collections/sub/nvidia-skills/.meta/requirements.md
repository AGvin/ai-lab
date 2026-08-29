# Documentation Requirements

## Requirements

- Identify NVIDIA Skills as NVIDIA's official verified Agent Skills catalog and link the canonical NVIDIA producer profile, official repository, and official documentation.
- Explain that the catalog includes NVIDIA-authored and product-repository skills and uses an automated synchronization/catalog pipeline; keep provenance/governance language scoped to what the official repository supports.
- Preserve the collection-level governance artifacts that extend the base Agent Skills package: `skill-card.md` identity/governance documentation, detached `skill.oms.sig` signatures, evaluation datasets, generated benchmark reports where available, and the published trust anchor used for signature verification.
- Explain the cryptographic-verification boundary: a valid signature can establish that published files match the signed NVIDIA package, but it does not establish suitability for a repository, credential scope, production environment, or organizational policy.
- Retain the official Skills CLI installation context at collection level (`npx skills add nvidia/skills`) without hardcoding mutable catalog counts or implying that installation is a trust endorsement.
- Present the selected collection-owned Skill Card Generator with a compact overview and a concise detail section; do not create a duplicate standalone catalog page.
- Describe Skill Card Generator as a governance workflow for generating or updating a draft skill card for an existing Agent Skill directory, not as a general skill authoring tool.
- Preserve current prerequisites: Python 3, `jinja2`, an existing target skill directory, scoped file access, and the three bundled scripts `discover_assets.py`, `render_card.py`, and `validate_submission.py`.
- Preserve the bundled style guide, card template, catalogs, and human-review boundary; generated cards remain drafts and do not replace legal, safety, or owner review.
- Link the selected skill to `https://github.com/NVIDIA/skills/tree/main/skills/skill-card-generator`.

## Validation

- Skill Card Generator is represented exactly once and links to its official source directory.
- Collection-level signing, provenance, and evaluation artifacts remain distinguishable from the selected Skill Card Generator workflow.
- Signature verification is not presented as proof of runtime safety, permission appropriateness, or production suitability.
- Runtime permissions and human-review constraints are not weakened or generalized beyond the upstream skill.
- No local standalone Skill Card Generator catalog node is linked.
- The page contains no temporary RC summary wording.
