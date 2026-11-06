# Gemma 3 27B IT

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Ownership/control-chain review is incomplete; no Russian-control finding or adoption clearance is established. See the [provenance policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Model and access

Google DeepMind's 27B instruction-tuned Gemma 3 checkpoint accepts text and images and produces text. The card reports 128K input context and 8,192-token output, distinct from the 1B text-only context and later Gemma 4. It uses Gemma Terms rather than inheriting another generation's Apache-2.0 label. Hub access requires agreement to publisher conditions; none were accepted here.

## Integration and evidence

Pin the checkpoint, processor and chat template. Treat images and prompts as untrusted inputs; validate application outputs and keep secrets out of prompts. Quantization, runtime memory and benchmark claims need configuration-specific verification.

Publisher capability and benchmark claims are not independently reproduced. Source review: 2026-11-05; no weights, remote model code, inference or tools were executed.

## Relations

- Member of: [Model family](../..//)

## Official resources

- [First-party model card](https://huggingface.co/google/gemma-3-27b-it)
- [License or terms](https://ai.google.dev/gemma/terms)
