# Human Evaluation

Human evaluation uses people to assess model outputs against explicit criteria or compare alternative responses.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Humans are needed when quality depends on nuanced meaning, domain expertise, usability, tone, or real-world consequences that automated metrics do not capture. Reliable human evaluation requires a clear rubric and consistent annotation process.

## Practical design

- Define criteria with positive and negative examples.
- Train evaluators and measure agreement.
- Randomize and blind model identity.
- Separate factual correctness from style preferences.
- Record uncertainty and reasons for difficult judgments.
- Escalate specialist topics to domain experts.

## Trade-offs and limitations

Human evaluation is expensive, slow, and influenced by fatigue, culture, preference, and presentation order. Agreement can be low when the rubric is vague or the task is genuinely subjective.

## Common mistakes

- Asking which answer is “better” without criteria.
- Using one evaluator for high-impact conclusions.
- Showing model names or expected rankings.
- Treating majority preference as factual correctness.

## Related concepts

- [Evaluation and Operations](../../)
- [LLM as a Judge](../llm-as-a-judge/)
- [Preference Optimization](../../../training-and-adaptation/sub/preference-optimization/)
- [Evaluation Datasets](../evaluation-datasets/)
