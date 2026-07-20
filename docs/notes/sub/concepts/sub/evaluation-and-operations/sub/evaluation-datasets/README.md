# Evaluation Datasets

An evaluation dataset is a curated set of inputs, expected properties, reference answers, labels, or scoring criteria used to test a model or system.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

The dataset should represent the distribution and risk of actual use. It may include ordinary cases, difficult edge cases, invalid inputs, adversarial examples, and historical incidents. The expected result can be exact, rubric-based, or open to human judgment depending on the task.

## Practical design

- Separate development, validation, and held-out test sets.
- Record source, license, date, and data transformations.
- Remove duplicates and near-duplicates from training data where possible.
- Include examples for every important failure category.
- Version the dataset and scoring rules together.

## Trade-offs and limitations

A static dataset becomes stale as user behavior and models change. Small sets are easy to review but have high variance; large sets improve coverage but are expensive to label and inspect.

## Common mistakes

- Reusing the test set for prompt tuning.
- Including only previously successful examples.
- Treating synthetic labels as ground truth.
- Changing labels without recording a new version.

## Related concepts

- [Evaluation and Operations](../../)
- [Evals](../evals/)
- [Datasets](../../../training-and-adaptation/sub/datasets/)
- [Reproducibility](../reproducibility/)
