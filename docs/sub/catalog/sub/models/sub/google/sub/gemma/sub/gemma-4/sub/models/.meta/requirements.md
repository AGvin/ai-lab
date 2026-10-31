# Documentation Requirements

## Requirements

- Present the concrete Gemma 4 models currently represented in the migrated catalog.
- Keep this page as navigation rather than duplicating generation-wide or concrete-model facts.
- List only implemented child nodes.

## Content Specification

- Use `Gemma 4 Models` as the page title.
- Link the parent Gemma 4 generation.
- List Gemma 4 E2B Instruct, E4B Instruct, 12B Unified Instruct, 26B A4B Instruct, and 31B Instruct with short identity-level descriptions.
- Preserve that `E` denotes effective parameters while avoiding complete parameter tables on the index.
- Do not repeat contextual scale labels, artifact inventories, VRAM planning, runtime guidance, or model-selection conclusions.

## Validation

- Every listed child resolves to a canonical documentation node.
- The page contains no placeholder wording.
- The page does not act as a second Gemma 4 generation profile.

## Verified identity and provenance

Navigation index of released Gemma 4 instruction checkpoints; model size labels, architecture, artifact format, and quantization are separate dimensions.

## Source-scoped operating boundaries

- List all five represented instruction variants with their exact official checkpoint links on the concrete pages. E2B/E4B use effective parameter labels, 26B A4B separates total from active parameters, and 12B Unified removes separate modality encoders. [Gemma 4 model matrix](https://ai.google.dev/gemma/docs/core/model_card_4).
- A size label or download size is not a runtime-memory estimate or a guarantee of supported modalities. Read the concrete profile and selected artifact before deployment.

## Source evidence

- <https://ai.google.dev/gemma/docs/core/model_card_4>
- <https://ai.google.dev/gemma/docs/core>
