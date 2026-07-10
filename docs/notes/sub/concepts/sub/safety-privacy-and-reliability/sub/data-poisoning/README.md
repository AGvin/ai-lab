# Data Poisoning

<!--
ai_content:
  managed: true
  l10n: true
-->

Data poisoning corrupts training or adaptation data to degrade model quality, create targeted behavior, or introduce hidden backdoors.

## Core idea

An attacker may insert mislabeled examples, repeated propaganda, trigger phrases, malicious code, or subtly modified records. Poisoning can affect foundation-model pretraining, fine-tuning datasets, preference data, or evaluation sets.

## Risk reduction

- Control who can contribute data.
- Preserve source provenance and signatures.
- Detect duplicates, outliers, and unexpected label patterns.
- Review high-impact or newly added sources.
- Separate training, validation, and test data.
- Rebuild and compare models after suspected compromise.

## Trade-offs and limitations

Large datasets make complete manual review impossible. Automated filters can miss subtle poisoning or remove legitimate rare cases. Some attacks become visible only after deployment.

## Common mistakes

- Trusting open contributions without provenance.
- Using model-generated labels as unquestioned truth.
- Evaluating with data from the same compromised source.
- Treating retrieval poisoning and training poisoning as the same remediation problem.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Datasets](../../../training-and-adaptation/sub/datasets/)
- [Retrieval Poisoning](../retrieval-poisoning/)
- [Provenance](../provenance/)
