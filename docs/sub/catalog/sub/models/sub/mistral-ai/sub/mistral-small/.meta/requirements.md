# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Link translated pages only when their destinations are materialized and resolve.

- Identify Mistral Small as a model family based on Mistral AI's current upstream terminology.
- Link the canonical producer and materialized concrete models.
- Do not invent an intermediate series layer when the current source does not require one for the documented branch.
- Keep model-specific properties on concrete model pages.

## Validation

- Mistral Small 4 is not misrepresented as a version/revision of another trained model.
- No task-selection recommendation is stored as a family fact.

## Source-backed profile

- Required reader orientation: Mistral Small is a model family produced by Mistral AI. Mistral AI describes Mistral Small 4 as a major release in this family.
- Preserve this model-scoped fact: Mistral Small 4 combines general instruction following and configurable reasoning. Mistral explicitly identifies Leanstral 1.5 as a specialization within this family. [Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)

## Operational and interpretation boundaries

- Explain this boundary: Leanstral’s retired Labs endpoint does not erase the released checkpoint. Quantized weights, EAGLE decoding heads and reasoning modes are not additional family-level trained-model identities. [Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
