# Few-Shot Prompting

Legacy residual retained for example-design, evaluation, and privacy guidance that are intentionally outside the canonical Few-Shot Prompting concept owner.

> **Migration note:** Few-shot identity, inference-time/in-context behavior, separation from weight updates and retrieval, context-relative example counts, demonstration capabilities and sensitivity, and copying/anchoring/bias/leakage limitations are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/prompting/sub/few-shot-prompting/`. The remaining material below stays here until its exact learning, evaluation, retrieval, privacy, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Example-design residual

Useful design practices include:

- choose demonstrations that are representative of the actual task rather than only easy or ideal cases;
- include relevant edge, invalid, or failure cases when they materially affect the required behavior;
- use positive and negative examples when the distinction helps communicate a boundary;
- keep example formatting and labels internally consistent;
- inspect demonstrations for accidental instruction-like content or contradictions with the current task;
- treat label balance, example similarity, diversity, ordering, and count as task-specific variables to evaluate rather than universal rules.

## Evaluation residual

Evaluate few-shot prompts on representative held-out cases instead of assuming that adding demonstrations improves performance. Compare against simpler zero-shot or one-shot baselines when useful, and re-run relevant checks after material model, provider, prompt, or example-set changes.

Examples consume context and can anchor behavior to superficial patterns, so evaluate both accepted-result quality and the context/cost trade-off for the concrete workload.

## Privacy residual

Do not place sensitive or confidential example data into demonstrations unless the application has an appropriate data-handling basis and the concrete model/provider path is permitted for that data. Prefer synthetic or appropriately sanitized examples when they satisfy the learning objective.

These example-design, evaluation, and privacy practices remain migration source material until their exact learning, evaluation, privacy, retrieval, or decision-support owners are verified.
