# Documentation Requirements

## Requirements
- Present one trained K2 Horizon model identity and keep parameter/context/license/benchmark facts source-backed to the current IFM model card.
- Do not promote quantized artifacts to peer trained-model identities.

## Validation
- The model remains a member of K2 Horizon.

## Source-backed rendering facts (2026-10-30)

- The official [IFM model card](https://huggingface.co/IFM/K2-Horizon-32B) describes a 32B dense decoder-only model with native 524,288-token context from midtraining onward. The card declares Apache-2.0 licensing.
- Preserve the publisher's parameter terminology; in particular, core parameters are not an independently counted total including every component.
- These are publisher-reported specifications, not independent parameter measurements or hardware-fit guarantees. Context capacity does not establish throughput or memory requirements. Benchmark results depend on the publisher's evaluation setup and have not been reproduced here. Quantized packages remain distributions rather than separate trained-model identities.
