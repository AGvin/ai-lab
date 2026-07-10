# Preference Optimization

<!--
ai_content:
  managed: true
  l10n: true
-->

Preference optimization adjusts model behavior using comparisons or scores that indicate which responses are preferred.

## Core idea

Supervised fine-tuning teaches the model to imitate target answers. Preference optimization instead uses relative judgments, such as one response being more helpful, safe, concise, or accurate than another. Methods include RLHF, DPO, and related objectives.

## Practical use

- Improve instruction following and conversational usefulness.
- Shape refusal and safety behavior.
- Reduce undesirable styles or verbosity.
- Align output with task-specific quality criteria.

## Trade-offs and limitations

Preference labels are subjective and can encode annotator or policy bias. Optimizing a proxy preference score may reduce diversity, cause over-refusal, or reward persuasive wording over factual correctness.

## Common mistakes

- Treating preferences as objective truth.
- Collecting comparisons without clear criteria.
- Using one judge model as the only source of labels.
- Evaluating only preference win rate and ignoring factual or task metrics.

## Related concepts

- [Training and Adaptation](../../)
- [RLHF](../rlhf/)
- [DPO](../dpo/)
- [Human Evaluation](../../../evaluation-and-operations/sub/human-evaluation/)
