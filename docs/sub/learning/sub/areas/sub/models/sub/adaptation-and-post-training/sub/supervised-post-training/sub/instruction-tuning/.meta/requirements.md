# Documentation Requirements

## Requirements

- Teach Instruction Tuning as supervised post-training over instruction/task examples intended to improve instruction following across varied phrasings, domains, formats, and task combinations.
- Design the instruction mixture around expected task diversity and failure modes rather than raw example count; include ambiguous, underspecified, difficult, and refusal/uncertainty cases where they are part of the acceptance contract.
- Review synthetic or transformed instruction-response pairs for correctness, leakage, duplicate templates, unsafe targets, hidden prompt artifacts, and superficial stylistic shortcuts.
- Keep roles, chat templates, system/user/assistant formatting, tool-call examples, special tokens, and preprocessing aligned with the intended inference interface; verify behavior when provider/runtime templates change.
- Evaluate unseen instruction wording, unseen task combinations, edge cases, and important retained capabilities; compliant tone/format is not a substitute for task correctness or factual reliability.
- Preserve the exact instruction-tuned artifact and evaluation baseline before later preference/alignment stages so behavior changes remain attributable.

## Validation

- Instruction tuning is not treated as equivalent to prompting or preference optimization.
- Interface formatting is not treated as an authorization boundary.
- Generalization evidence includes unseen instructions/tasks rather than only training-distribution imitation.
