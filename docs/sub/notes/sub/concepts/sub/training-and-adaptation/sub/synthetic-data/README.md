# Synthetic Data

Legacy residual retained for generation-pipeline controls, independent validation, privacy review, real-versus-synthetic evaluation design, and dataset-acceptance guidance that are intentionally outside the canonical Synthetic Data concept owner.

> **Migration note:** Synthetic-data identity, generation-family boundaries, augmentation/imputation distinctions, purpose-specific fidelity/utility, diversity and generator-bias limits, provenance, train/evaluation independence, privacy non-guarantees, DP separation, rare-event/domain-gap semantics, and recursive-generation risks are already preserved in `docs/sub/concepts/sub/machine-learning/sub/data-centric-ml/sub/synthetic-data/`. The remaining material below stays here until its exact learning, dataset-engineering, privacy, evaluation, or project-governance owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Generation-pipeline residual

Define the purpose and acceptance criteria before generating examples. Record the generator/model/simulator version, source or seed data when applicable, prompts/rules/configuration, sampling settings, post-processing, filtering, label/judge origin, and output version needed to reproduce the dataset.

Use deterministic rules, simulators, human review, independent models, domain constraints, or other suitable validators when generated outputs require correctness beyond surface plausibility. Avoid using the same generator lineage as the only judge of its own outputs when independent evidence matters.

## Privacy and sensitive-data residual

Review generated examples for reproduced personal, confidential, copyrighted, secret, or otherwise restricted content even when the generation process is intended to create artificial data. Synthetic output is not automatically anonymous or safe to redistribute.

When the source data are sensitive, assess disclosure/membership risks and the actual privacy mechanism separately from visual or statistical similarity. Use formal privacy mechanisms only when their guarantees and parameters are part of the concrete pipeline rather than labeling ordinary generation as privacy-preserving.

## Evaluation-mixture residual

Keep synthetic training and synthetic evaluation generation sufficiently independent when the evaluation is meant to estimate real-world performance. Shared prompts, source corpora, generator families, judges, or model lineages can create correlated artifacts and optimistic results.

Use synthetic cases to stress rare conditions, invariants, safety scenarios, known failure modes, or controlled labels while retaining held-out real-world/independently sourced evidence where ecological validity or unknown failure discovery matters.

## Acceptance residual

Measure usefulness by target coverage, correctness, diversity, downstream performance, and known gap exposure rather than generated row count. Track where synthetic frequency differs intentionally from real prevalence so oversampled edge cases are not misread as base-rate estimates.

These pipeline, privacy, evaluation, and acceptance practices remain migration source material until their exact learning, dataset-engineering, privacy, evaluation, or project-governance owners are verified.
