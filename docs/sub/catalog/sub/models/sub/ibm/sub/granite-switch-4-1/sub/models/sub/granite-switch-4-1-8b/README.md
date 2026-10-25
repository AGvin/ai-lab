# Granite Switch 4.1 8B

Granite Switch 4.1 8B is IBM's stable composed 8B-class checkpoint combining chat, decision and Guardian adapters with a bundled speech encoder.

## Architecture and operating boundaries

The chat template, supported processor and control tokens determine which component handles each mode. The presence of bundled modules does not guarantee that an arbitrary inference backend can activate all modes. Use the supported runtime and checkpoint-specific configuration; do not substitute newer standalone speech-encoder or adapter weights without verifying compatibility.

The released weights use Apache-2.0; hosted service terms may differ. Pin the checkpoint and evaluate task quality, memory and latency on target inputs. The 8B label alone does not establish hardware fit.

## Family and official source

- [Granite Switch 4.1 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-8b)
