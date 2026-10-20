# Strands Decider E2B Gemma4 v1-2610

Strands Decider E2B Gemma4 v1-2610 is a released typed-decision checkpoint built on the text decoder of google/gemma-4-E2B-it.

## Scope and boundaries

Released strands-decider-E2B-gemma4-v1-2610 adapter and decision head on google/gemma-4-E2B-it. The three-run combination is a trained model identity, not a runtime package or a mirror. It uses text only and requires the repository code with Gemma support, which the cited card says is not yet in PyPI. Model size labels do not establish memory fit or inherited base modalities. Short-task confidence calibration must be tested on the target questions. E2B needs the documented eager-attention workaround for cached-state scoring; pre-fix Decision Index results may be affected. Runtime state is truncated by default; strict-window mode rejects oversize input.

## Decision and operational boundaries

- The exact card publishes `strands-decider-E2B-gemma4-v1-2610` on `google/gemma-4-E2B-it` with an October 9, 2026 release. It combines three training runs into a rank-48 LoRA adapter and a scoring head; its Amazon mirror is the same identity. [Strands Decider E2B Gemma4 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v1-2610)
- Gemma support is documented in the code repository main branch and is not yet in the PyPI package described by the card. The runtime loads the Gemma text decoder and discards its vision/audio encoders, so the base model modalities do not transfer. [Strands Decider E2B Gemma4 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v1-2610) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- The size label is copied from the base model name. It is not a peak-memory claim. Pin the model release and compatible runtime; default state truncation and confidence thresholds need explicit application choices. [Strands Decider model release naming](https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Use the documented eager-attention handling for E2B: the default CUDA kernel can return incorrect cached-state scores for certain question lengths. The model card warns that its pre-fix Decision Index score may be affected. [Strands Decider E2B Gemma4 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v1-2610) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- The model card publishes the adapter/head under Apache-2.0 and loads the base weights separately. Preserve source-specific data terms and pin the released files and compatible code; a model license does not grant a blanket training-data redistribution right. [Strands Decider E2B Gemma4 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v1-2610)

## Relations

- member-of: [`catalog/models/amazon/strands-decider`](../../../../)

## Official resources

- <https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v1-2610>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md>
- <https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026/>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md>
