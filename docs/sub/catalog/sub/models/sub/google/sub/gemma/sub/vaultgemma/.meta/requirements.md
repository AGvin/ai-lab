# Documentation Requirements

## Requirements

- Identify VaultGemma as Google's released 1B open Gemma model trained with sequence-level differential privacy.
- Preserve the documented differential-privacy guarantee, private-training research boundary, and customization positioning only while supported by the exact current first-party model/report revision.
- Keep VaultGemma distinct from generic Gemma, privacy frameworks, confidential-computing products, privacy-preserving serving systems, and downstream private fine-tunes.
- Treat privacy parameters, training setup, artifacts, licenses, runtime/fine-tuning support, utility benchmarks, compute requirements, and downstream privacy accounting as freshness-sensitive.
- Do not claim that the model's training-time differential-privacy guarantee automatically makes downstream fine-tuning, prompts, outputs, logs, or deployments private or compliant.
- Attribute privacy/utility comparisons to Google DeepMind or the cited evaluator.

## Validation

- The node remains a concrete privacy-trained model rather than a generic privacy guarantee.
- Privacy parameters remain tied to the exact upstream training definition and model revision.
