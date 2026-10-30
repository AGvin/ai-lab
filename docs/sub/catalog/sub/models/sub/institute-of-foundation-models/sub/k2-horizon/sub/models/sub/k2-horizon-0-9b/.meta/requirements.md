# Documentation Requirements

## Requirements
- Present one trained K2 Horizon model identity, not quantized/package variants.
- Keep parameter count, context, architecture, license, intended deployment, benchmark, and artifact claims traceable to the current IFM model card.

## Validation
- The model remains a member of K2 Horizon and package/quantization artifacts are not promoted to peer trained models.

## Source-backed rendering facts (2026-10-30)

- The official [IFM model card](https://huggingface.co/IFM/K2-Horizon-0.9B) describes a 0.9B-class dense decoder-only model with up to 131,072 tokens using YaRN RoPE scaling. The card declares Apache-2.0 licensing.
- Preserve the publisher's parameter terminology; in particular, core parameters are not an independently counted total including every component.
- These are publisher-reported specifications, not independent parameter measurements or hardware-fit guarantees. Context capacity does not establish throughput or memory requirements. Benchmark results depend on the publisher's evaluation setup and have not been reproduced here. Quantized packages remain distributions rather than separate trained-model identities.
