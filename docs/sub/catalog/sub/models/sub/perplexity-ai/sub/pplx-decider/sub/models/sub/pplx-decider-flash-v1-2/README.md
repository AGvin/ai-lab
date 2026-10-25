# PPLX Decider Flash V1.2

PPLX Decider Flash V1.2 is Perplexity AI's **smaller, separately released decision model**, based on **Qwen3.5-4B** and distilled from larger 27B Decider models. It is **not** a quantized copy or hosted alias of [PPLX Decider V1.2](../pplx-decider-v1-2/). The checkpoint is published under **Apache-2.0**.

## Decision interface and limits

Flash V1.2 supports the shared **joint state-and-multiple-question request protocol**, including text/image input and calibrated per-question decisions. Apply its checkpoint-specific prompt, output-marker and decision-calibration contract. Smaller model size, grouping recommendations, accuracy, memory and compile/runtime needs must be assessed for the selected checkpoint.

The separately distributed **GGUF** repository is a packaging/quantization artifact of this model, not another trained identity. The named Qwen3.5-4B base does not create an unresolved canonical derived-from graph edge until its exact base entity is materialized.

## Family and official source

- [PPLX Decider family](../../../../)
- [Official Perplexity checkpoint](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2)
