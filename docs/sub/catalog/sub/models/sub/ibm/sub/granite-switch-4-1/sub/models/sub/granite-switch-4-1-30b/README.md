# Granite Switch 4.1 30B

Granite Switch 4.1 30B is IBM's stable composed 30B-class checkpoint for chat, decision, Guardian evaluation and speech input.

## Architecture and operating boundaries

The checkpoint bundles decision and Guardian adapters and a speech encoder alongside the selected 30B language-model base. Its documented chat template, processor and control-token contract determines mode selection. Runtime support for each mode must be checked independently; modular composition is not permission to replace components with later standalone releases.

The released weights use Apache-2.0; hosted terms differ. Pin checkpoint and runtime, then evaluate memory, latency and task quality. The 30B parameter class is not a hardware-fit guarantee.

## Family and official source

- [Granite Switch 4.1 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-30b)
