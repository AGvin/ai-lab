# Documentation Requirements

## Requirements
- Present one trained K2 Horizon model identity and keep parameter/context/license/benchmark facts source-backed to the current IFM model card.
- Keep later `Uno` and quantized artifacts separate from this base trained-model identity unless upstream establishes a separately trained model.

## Validation
- The model remains a member of K2 Horizon.

## Source-backed rendering facts (2026-10-30)

- The official [IFM model card](https://huggingface.co/IFM/K2-Horizon-7B) describes a dense decoder-only model described as 7B-core with a 512K context window. The card declares Apache-2.0 licensing.
- Preserve the publisher's parameter terminology; in particular, core parameters are not an independently counted total including every component.
- These are publisher-reported specifications, not independent parameter measurements or hardware-fit guarantees. Context capacity does not establish throughput or memory requirements. Benchmark results depend on the publisher's evaluation setup and have not been reproduced here. Quantized packages remain distributions rather than separate trained-model identities.
