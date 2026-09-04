# Documentation Requirements

## Requirements

- Teach Synthetic Data as purpose-driven generated examples whose usefulness depends on the target task, generation process, validation, and downstream acceptance criteria.
- Record generator/model/simulator version, source or seed data where applicable, prompts/rules/configuration, sampling settings, post-processing, filtering, label/judge origin, and output version needed to reproduce the dataset.
- Use suitable independent validators when generated outputs require correctness beyond surface plausibility; do not rely on the same generator lineage as the only judge when independent evidence matters.
- Review generated examples for reproduced personal, confidential, copyrighted, secret, or otherwise restricted content; synthetic output is not automatically anonymous or redistribution-safe.
- Keep synthetic training and synthetic evaluation generation sufficiently independent when evaluation is intended to estimate real-world performance; shared generators, prompts, corpora, or judges can create optimistic correlation.
- Use synthetic cases to stress rare conditions, invariants, safety scenarios, known failure modes, or controlled labels while retaining held-out real/independently sourced evidence where ecological validity matters.
- Measure usefulness by target coverage, correctness, diversity, downstream performance, and known-gap exposure rather than generated row count.

## Validation

- Synthetic frequency is not interpreted automatically as real-world prevalence.
- Privacy claims depend on the actual mechanism rather than the word `synthetic`.
- Evaluation independence from the generation pipeline is explicit when required.
