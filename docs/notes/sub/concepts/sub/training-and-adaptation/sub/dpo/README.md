# DPO

Direct Preference Optimization, or DPO, trains a model directly from preferred and rejected response pairs without first fitting a separate reward model and running a full reinforcement-learning loop.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

DPO increases the relative likelihood of preferred responses while constraining the adapted model against a reference model. It simplifies preference training and is often easier to implement than RLHF.

## Practical use

- Refine an instruction-tuned model using comparison data.
- Adjust style, refusal behavior, or task preferences.
- Experiment with preference alignment using a simpler pipeline.

## Trade-offs and limitations

DPO still depends on high-quality preference pairs and an appropriate reference model. It can overfit annotation artifacts, reduce response diversity, or optimize subjective style instead of correctness.

## Common mistakes

- Using weak or inconsistent rejected responses.
- Assuming DPO removes the need for evaluation.
- Comparing DPO and RLHF without matching data and objectives.
- Training on preference pairs that contain hidden factual errors.

## Related concepts

- [Training and Adaptation](../../)
- [Preference Optimization](../preference-optimization/)
- [RLHF](../rlhf/)
- [Evaluation Datasets](../../../evaluation-and-operations/sub/evaluation-datasets/)
