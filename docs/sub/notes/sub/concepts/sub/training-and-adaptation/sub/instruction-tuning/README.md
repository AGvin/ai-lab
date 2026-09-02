# Instruction Tuning

Legacy residual retained for instruction-dataset design, generalization evaluation, template/interface consistency, ambiguity handling, and post-training handoff guidance that are intentionally outside the canonical Instruction Tuning concept owner.

> **Migration note:** Instruction-tuning identity, SFT relationship and terminology overlap, data-source diversity, task-diversity versus dataset-size boundary, prompting and preference-optimization distinctions, interface-authority separation, and factuality/safety non-guarantees are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/fine-tuning/sub/instruction-tuning/`. The remaining material below stays here until its exact learning, dataset-engineering, training-engineering, evaluation, or post-training-workflow owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Instruction-dataset residual

Design the instruction mixture around the range of tasks, phrasings, domains, formats, and failure modes the adapted model is expected to handle. Include difficult, ambiguous, underspecified, and refusal/uncertainty cases when those behaviors are part of the acceptance criteria instead of training only clean success examples.

Review synthetic or transformed instruction-response pairs for correctness, hidden prompt artifacts, duplicate templates, leakage, unsafe targets, and superficial stylistic shortcuts before adding them to the mixture.

## Template and interface residual

Keep roles, chat templates, system/user/assistant formatting, tool-call examples, special tokens, and preprocessing aligned with the intended inference interface. Do not assume a model trained under one conversation schema will preserve behavior under another provider/runtime template without verification.

Treat learned instruction following separately from actual application permissions and instruction hierarchy; interface formatting can teach patterns but does not become a security control.

## Generalization and handoff residual

Evaluate unseen instruction wording, unseen task combinations, edge cases, and important retained base capabilities rather than measuring only imitation of the training distribution. Helpful tone and compliant formatting are not substitutes for task correctness or factual reliability.

If instruction tuning is followed by preference optimization or another alignment stage, preserve the exact instruction-tuned artifact and its evaluation baseline so later behavior changes can be attributed to the correct stage.

These dataset, interface, generalization, and handoff practices remain migration source material until their exact learning, dataset-engineering, training-engineering, evaluation, or post-training-workflow owners are verified.
