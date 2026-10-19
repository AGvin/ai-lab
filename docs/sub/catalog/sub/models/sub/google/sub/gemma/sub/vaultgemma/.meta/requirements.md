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

## Verified identity and provenance

Pretrained text model released as google/vaultgemma-1b with differentially private training; its training-data guarantee is distinct from prompt, serving, or fine-tuning privacy.

## Source-scoped operating boundaries

- The pretrained model uses a 1,024-token input context and may be instruction-tuned. Its published training guarantee is sequence-level differential privacy with epsilon at most 2.0 and delta at most 1.1e-10. Preserve the guarantee's unit and training scope. [Model card](https://huggingface.co/google/vaultgemma-1b).
- That guarantee does not automatically extend to new fine-tuning data, user prompts, inference logs, downstream outputs, or a hosting provider. Further private training needs its own privacy accounting and deployment controls. [Training privacy boundary](https://deepmind.google/models/gemma/vaultgemma/).

## Source evidence

- <https://huggingface.co/google/vaultgemma-1b>
- <https://deepmind.google/models/gemma/vaultgemma/>
