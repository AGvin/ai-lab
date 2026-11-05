# NVIDIA Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA Skills is NVIDIA's official verified Agent Skills catalog for NVIDIA software and platform workflows. The catalog includes NVIDIA-authored and product-repository skills and uses a synchronization pipeline to keep catalog entries aligned with their sources.

## Producer

- [NVIDIA](../../../../../producers/sub/n/sub/nvidia/)

## Selected skills

| Skill | Purpose | Official source |
| --- | --- | --- |
| Skill Card Generator | Generate or update a draft NVIDIA governance card for an existing Agent Skill directory. | [Source](https://github.com/NVIDIA/skills/tree/main/skills/skill-card-generator) |

### Skill Card Generator

Skill Card Generator gathers source signals from an existing skill, helps build grounded card context, renders the governance card, and validates that review markers have been resolved before submission. It is not a general skill-authoring tool and does not replace required human legal, safety, or owner review.

Current prerequisites include Python 3, `jinja2`, an existing target skill directory, and the declared file/shell permissions. The bundled workflow uses `discover_assets.py`, `render_card.py`, and `validate_submission.py` together with the style guide, card template, and supporting governance catalogs.

## Installation

The NVIDIA catalog supports selective installation through the `skills` CLI. Catalog contents evolve over time, so use the official catalog rather than a hardcoded skill count when selecting additional skills.

## Source interpretation

NVIDIA's synchronized catalog mirrors product-repository skills. Documentation and skills use CC-BY-4.0, while source code uses Apache-2.0; linked external materials retain separate terms. Signatures or NVIDIA verification labels establish bounded distribution/provenance properties, not workload suitability or permission to execute commands.

[Reviewed original README](https://github.com/NVIDIA/skills/blob/fc38e7248fff9e958ed3c17f5dc79808b3348d4f/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [NVIDIA Skills repository](https://github.com/NVIDIA/skills)
- [NVIDIA Skills documentation](https://docs.nvidia.com/skills/)
