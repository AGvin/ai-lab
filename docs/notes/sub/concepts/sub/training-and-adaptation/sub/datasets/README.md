# Datasets

A dataset is an organized collection of examples and metadata used for training, adaptation, evaluation, or analysis.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Dataset quality includes more than correctness. Relevant properties include coverage, balance, provenance, licensing, consent, deduplication, freshness, labeling consistency, and separation between training and evaluation data.

## Practical lifecycle

1. Define the target task and population.
2. Collect or generate representative examples.
3. Clean, normalize, deduplicate, and label data.
4. Split data to prevent leakage.
5. Record versions and provenance.
6. Evaluate coverage and known gaps.
7. Monitor whether deployment data changes.

## Trade-offs and limitations

Large datasets can still be poor if they contain duplicated, biased, outdated, or irrelevant material. Aggressive cleaning may remove rare but important cases. Public availability does not automatically permit unrestricted reuse.

## Common mistakes

- Mixing training and test examples.
- Losing source and license metadata.
- Measuring only dataset size.
- Keeping personal or secret data without necessity and consent.

## Related concepts

- [Training and Adaptation](../../)
- [Evaluation Datasets](../../../evaluation-and-operations/sub/evaluation-datasets/)
- [Synthetic Data](../synthetic-data/)
- [Data Poisoning](../../../safety-privacy-and-reliability/sub/data-poisoning/)
