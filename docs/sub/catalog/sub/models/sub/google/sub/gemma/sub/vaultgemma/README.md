# VaultGemma

Pretrained text model released as google/vaultgemma-1b with differentially private training; its training-data guarantee is distinct from prompt, serving, or fine-tuning privacy.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- The pretrained model uses a 1,024-token input context and may be instruction-tuned. Its published training guarantee is sequence-level differential privacy with epsilon at most 2.0 and delta at most 1.1e-10. Preserve the guarantee's unit and training scope. [Model card](https://huggingface.co/google/vaultgemma-1b).
- That guarantee does not automatically extend to new fine-tuning data, user prompts, inference logs, downstream outputs, or a hosting provider. Further private training needs its own privacy accounting and deployment controls. [Training privacy boundary](https://deepmind.google/models/gemma/vaultgemma/).

## Official resources

- <https://deepmind.google/models/gemma/vaultgemma/>
- <https://ai.google.dev/gemma/docs/releases>
- <https://huggingface.co/google/vaultgemma-1b>
