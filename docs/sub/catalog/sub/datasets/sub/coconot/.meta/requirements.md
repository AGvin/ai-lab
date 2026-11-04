# Documentation Requirements

## Requirements

- Identify CoCoNot as a published instruction-following/noncompliance benchmark dataset, not a refusal-policy standard, model checkpoint, or hosted agent service.
- At the pinned source revision, the Original Set lists 1,001 evaluation examples and 11,477 supervised fine-tuning examples, while the Contrast Set lists 379 evaluation and 927 preference examples. Preserve original, contrast and preference configurations when comparing scores.
- Official README points to Hugging Face dataset allenai/coconot and uses Open-Instruct to run inference/evaluation. Treat that dependency as evaluation software, not an additional CoCoNot dataset identity.
- Test both harmful/invalid requests requiring appropriate noncompliance and benign requests for which over-refusal is a failure. Outcome metrics are model/prompt/judge dependent, and benchmark exposure can contaminate evaluations.
- The root repository LICENSE is MIT for covered code/material; verify exact hosted dataset subset, annotation rights, original seed prompts and model-provider terms independently before redistributing.
- No model invocation, held-out split download, evaluation, legal review of all prompts or whole-catalog clean pass was performed.

## Validation

- One frozen dataset identity, pinned publisher sources, distinct benchmark task/harness/model/service artifacts and canonical index link.
- No live vulnerability code, score, legal clearance, complete CI or whole-catalog clean pass is implied.
