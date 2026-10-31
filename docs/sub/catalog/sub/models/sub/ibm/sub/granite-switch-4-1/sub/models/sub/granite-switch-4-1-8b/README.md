# Granite Switch 4.1 8B

Granite Switch 4.1 8B is IBM's stable composed 8B-class checkpoint combining chat, decision and Guardian adapters with a bundled speech encoder.

## Architecture and operating boundaries

The **4.1.1 revision** (27 October 2026) updates the learned `decision` aLoRA adapter and embeds the multilingual, punctuating Granite Speech 5.0 TurboCTC while preserving the 8B Granite 4.1 base and the model's stable canonical identity. Pin the intended revision rather than assuming a deployment uses the older English-only 4.1 weights. [IBM announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) [Exact 8B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b).

The published 4.1.1 8B card lists speech input in English, French, German, Spanish, Portuguese, Italian and Japanese; the broader announcement says ten languages without matching the exact bundled-card list. Treat additional languages as **unverified** pending IBM clarification, and test recognition and downstream decisions. The ASR encoder is not jointly trained with the language model. [8B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) [IBM announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1).

The chat template, supported processor and control tokens determine which component handles each mode. The presence of bundled modules does not guarantee that an arbitrary inference backend can activate all modes. Use the supported runtime and checkpoint-specific configuration; do not substitute newer standalone speech-encoder or adapter weights without verifying compatibility.

The released weights use Apache-2.0; hosted service terms may differ. Pin the checkpoint and evaluate task quality, memory and latency on target inputs. The 8B label alone does not establish hardware fit.

## Family and official source

- [Granite Switch 4.1 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-8b)
- [4.1.1 revision announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1)
