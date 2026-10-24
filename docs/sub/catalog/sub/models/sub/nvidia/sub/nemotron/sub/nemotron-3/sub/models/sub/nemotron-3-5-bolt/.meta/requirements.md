# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3.5 Bolt as a distinct NVIDIA checkpoint released on 2026-10-15.
- Preserve the explicit Super VL compression lineage and reciprocal derived-from relationship.
- Keep the advertised 24GB deployment footprint tied to its particular artifact, runtime and workload; it is not a BF16 memory guarantee.
- Treat LiLiCorr as a separately trained dependent speculative-decoding drafter requiring its own classification review, not as an alias or a standalone replacement. Its official Hugging Face metadata targets the quantized `NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB` release and reports 673.5M parameters; NVIDIA model-card review separately reports 1.113B parameters excluding shared target embeddings/head. Do not conflate these source-specific counts or infer a canonical count until accounting is reconciled.

## Validation

- Family membership resolves reciprocally through Nemotron 3; producer provenance remains inherited through the existing family relation chain.
- Exact source and trained identity remain distinct from serving artifacts.
