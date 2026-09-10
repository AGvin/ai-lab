# Documentation Requirements

## Requirements

- Identify Nemotron as NVIDIA's open model family and preserve provenance to the canonical NVIDIA producer.
- Represent Nemotron 3 as a model series because NVIDIA explicitly identifies current Nano, Super, Ultra, and 3.5 Lightning releases as members of the Nemotron 3 model family.
- Keep NIM packaging, quantized checkpoints, deployment backends, GPU fit, throughput, and model-routing recommendations outside stable family identity.

## Validation

- Nemotron 3 remains a series within Nemotron rather than an additional top-level model family.
- Quantized or speculative-decoding artifacts are not represented as additional trained models in this refresh.
