# Granite Switch 4.1 30B

Granite Switch 4.1 30B is IBM's stable composed 30B-class checkpoint for chat, decision, Guardian evaluation and speech input.

## Architecture and operating boundaries

The **4.1.1 revision** (27 October 2026) updates the learned `decision` aLoRA adapter and embeds the multilingual, punctuating Granite Speech 5.0 TurboCTC while preserving the 30B Granite 4.1 base and the model's stable canonical identity. Pin the intended revision rather than assuming a deployment uses the older English-only 4.1 weights. [IBM announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) [Exact 30B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b).

The published 4.1.1 30B card lists speech input in English, French, German, Spanish, Portuguese, Italian and Japanese; the broader announcement says ten languages without matching the exact bundled-card list. Treat additional languages as **unverified** pending IBM clarification, and test recognition and downstream decisions. The ASR encoder is not jointly trained with the language model. [30B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) [IBM announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1).

The checkpoint bundles decision and Guardian adapters and a speech encoder alongside the selected 30B language-model base. Its documented chat template, processor and control-token contract determines mode selection. Runtime support for each mode must be checked independently; modular composition is not permission to replace components with later standalone releases.

The released weights use Apache-2.0; hosted terms differ. Pin checkpoint and runtime, then evaluate memory, latency and task quality. The 30B parameter class is not a hardware-fit guarantee.

## Family and official source

- [Granite Switch 4.1 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-30b)
- [4.1.1 revision announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1)
