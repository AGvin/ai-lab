# FLUX.1-schnell

`black-forest-labs/FLUX.1-schnell` is a downloadable text-to-image model used as the temporary local image-generation candidate in the current portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Model repository: `black-forest-labs/FLUX.1-schnell`
- Provider: Black Forest Labs
- Model type: text-to-image rectified-flow Transformer
- Parameters: 12B
- License: Apache-2.0
- Intended inference: generation in 1–4 steps according to the model card
- Access: downloadable weights and compatible local runtimes; hosted deployments are separate services

The repository's main model file is large enough that file size, precision, runtime components, text encoders, VAE, buffers, and target resolution must all be considered in deployment planning.

## Selection guidance

Consider FLUX.1-schnell for:

- local or temporary text-to-image generation where its license and output workflow are acceptable;
- rapid concept generation with a bounded candidate budget;
- an on-demand GPU worker that starts only after task, rights, quality, storage, and budget checks;
- comparison with hosted image endpoints on accepted-result quality, latency, privacy, and total cost.

Do not assume that a 24 GB GPU is a comfortable deployment from parameter count or one file size. Select the exact runtime, precision, offload, resolution, batch size, text encoders, and VAE, then measure peak VRAM and host RAM.

## Evaluation requirements

Record:

- repository revision and runtime version;
- model files, precision, quantization or conversion;
- scheduler, steps, guidance, seed, dimensions, and batch;
- load, warm-up, and terminal-image latency;
- peak VRAM and RAM;
- prompt adherence, visual defects, typography, and subgroup results;
- candidate count, accepted-result rate, and correction cost;
- input rights, consent, provenance, disclosure, and output-use workflow.

The generator must not approve its own output for consequential use. Apply deterministic file checks plus an independently calibrated perception model or human reviewer.

## On-demand lifecycle

For temporary GPU infrastructure:

1. verify task need, rights, budget, and exact deployment;
2. start the service with an idempotency key;
3. confirm provider state, endpoint readiness, model identity, and required files;
4. generate a bounded candidate set;
5. persist prompts, parameters, seeds, outputs, and provenance outside ephemeral storage;
6. verify artifacts independently;
7. request shutdown and confirm provider and billing state.

A worker reporting completion is not proof that the billable service stopped.

## Evidence boundary

Model identity, architecture class, parameter count, license, and low-step guidance are provider-documented. Hardware fit, quality, safety, accepted-result cost, and runtime behavior require assignment-level measurement.

## Related pages

- [FLUX](../..)
- [Black Forest Labs models](../../../..)
- [Generative Media](../../../../../../../notes/sub/comparisons/sub/model-selection/sub/generative-media/)
- [Resource Lifecycle Orchestration](../../../../../../../notes/sub/comparisons/sub/model-selection/sub/orchestration/sub/resource-lifecycle/)

## Sources

- [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
- [FLUX paper](https://arxiv.org/abs/2412.15170)
