# Documentation Requirements

## Requirements

- Identify NVIDIA Skills as NVIDIA's official verified Agent Skills catalog and link the canonical NVIDIA producer profile, official repository, and official documentation.
- Explain that the catalog includes NVIDIA-authored and product-repository skills and uses an automated synchronization/catalog pipeline; keep provenance/governance language scoped to what the official repository supports.
- Preserve the collection-level governance artifacts that extend the base Agent Skills package: `skill-card.md` identity/governance documentation, detached `skill.oms.sig` signatures, evaluation datasets, generated benchmark reports where available, and the published trust anchor used for signature verification.
- Explain the cryptographic-verification boundary: a valid signature can establish that published files match the signed NVIDIA package, but it does not establish suitability for a repository, credential scope, production environment, or organizational policy.
- Preserve the updated first-party installation recommendation: `npx skills add nvidia/skills --skill nvidia-skill-finder --yes` installs the collection-owned discovery router first, while `npx skills add nvidia/skills` remains the broader browse/select option. Both are documented examples, not authorization to install or modify agent capabilities; the finder skill requires user approval before installing further skills.
- Treat the `nvidia-skill-finder` as one collection-owned router, not a peer catalog product. Inventory labels (including ETHOS.md and NeMo Data Designer) change independently of NVIDIA's underlying products, sources or license rights.
- Preserve current NVIDIA DOCA/BlueField Agent Skills as collection/product-repository inventory rather than peer canonical skill nodes; their supported DOCA/BlueField workflows, prerequisites, and product coverage remain freshness-sensitive and do not expand the collection's trust boundary.
- Position the collection as a useful source for NVIDIA CUDA-X / AI-platform skill guidance and for studying signed skill distribution, provenance, skill cards, evaluation artifacts, governance controls, and revision-based organizational allow-listing; make clear that these are practical governance/study use cases rather than proof that a skill is safe or suitable for a specific environment.
- Present the selected collection-owned Skill Card Generator with a compact overview and a concise detail section; do not create a duplicate standalone catalog page.
- Describe Skill Card Generator as a governance workflow for generating or updating a draft skill card for an existing Agent Skill directory, not as a general skill authoring tool.
- Preserve current prerequisites: Python 3, `jinja2`, an existing target skill directory, scoped file access, and the three bundled scripts `discover_assets.py`, `render_card.py`, and `validate_submission.py`.
- Preserve the bundled style guide, card template, catalogs, and human-review boundary; generated cards remain drafts and do not replace legal, safety, or owner review.
- Link the selected skill to `https://github.com/NVIDIA/skills/tree/main/skills/skill-card-generator`.

## Validation

- Skill Card Generator is represented exactly once and links to its official source directory.
- Collection-level signing, provenance, and evaluation artifacts remain distinguishable from the selected Skill Card Generator workflow.
- Signature verification is not presented as proof of runtime safety, permission appropriateness, or production suitability.
- Practical governance/use-case positioning does not weaken the separate suitability and permission review boundary.
- Runtime permissions and human-review constraints are not weakened or generalized beyond the upstream skill.
- No local standalone Skill Card Generator catalog node is linked.
- The page contains no temporary RC summary wording.

## Bounded installation-source reconciliation — 2026-11-09

- Compared earlier [NVIDIA README](https://github.com/NVIDIA/skills/blob/fc38e7248fff9e958ed3c17f5dc79808b3348d4f/README.md) with [newer README](https://github.com/NVIDIA/skills/blob/fce3cca4170be75e82c64920654d56ee2811b005/README.md): the recommended CLI now installs `nvidia-skill-finder` as a first step, with a general catalog CLI route retained. [NVIDIA Skill Finder SKILL.md](https://github.com/NVIDIA/skills/blob/fce3cca4170be75e82c64920654d56ee2811b005/skills/nvidia-skill-finder/SKILL.md) explicitly requires user permission before installing or modifying agent capabilities.
- Root `LICENSE-APACHE` and `LICENSE-CC-BY-4.0` blobs are unchanged between the compared revisions. This is not a full mirrored-source, permissions, hardware, benchmark, signature or dependency verification.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
