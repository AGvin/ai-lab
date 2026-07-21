# LLM as a Judge

LLM as a judge uses a language model to score, rank, critique, or compare outputs from another model or system.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A judge model can evaluate qualities that are difficult to encode as exact rules, such as relevance, completeness, style, or adherence to a rubric. Pairwise comparison is often more stable than assigning an absolute numerical score.

## Good practice

- Provide a precise rubric and evidence required for scoring.
- Randomize answer order to detect position bias.
- Hide model identity where possible.
- Calibrate against human-reviewed examples.
- Use several judges or repeated runs for high-impact evaluation.
- Keep deterministic checks for facts and schemas.

## Trade-offs and limitations

Judge models have their own biases, preferences, and blind spots. They may favor verbose answers, familiar styles, or outputs from related model families. A judge can also be influenced by prompt injection inside the answer being evaluated.

## Common mistakes

- Using the same model to generate and judge without calibration.
- Treating judge scores as objective ground truth.
- Asking for factual validation without providing sources.
- Ignoring inconsistent results across repeated judgments.

## Related concepts

- [Evaluation and Operations](../../)
- [Human Evaluation](../human-evaluation/)
- [Evals](../evals/)
- [Prompt Injection](../../../safety-privacy-and-reliability/sub/prompt-injection/)
