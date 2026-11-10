# Documentation Requirements

## Requirements
- Present one trained K2 Horizon MoE model identity.
- Preserve total and active parameters as separate facts and source both to the current IFM model card.
- Keep architecture, routing, context, license, benchmark, and deployment/hardware-fit claims source-conditioned.

## Validation
- The model remains a member of K2 Horizon and active parameters are not inferred from naming alone.

## Source-backed rendering facts (2026-10-30)

- The official [IFM model card](https://huggingface.co/IFM/K2-Horizon-375B-A23B) reports 375B total parameters and 23B activated per token. Render total and activated counts separately, attributed to IFM; these are card-reported figures, not an independent tensor count.
- The card reports native 524,288-token context and Apache-2.0 licensing. Context length does not establish usable throughput or memory fit.
- Active parameter count is not the complete weight-storage footprint. Hardware needs also depend on precision, KV cache, batch size and serving implementation; published recipes are examples, not minimum requirements.
- Keep publisher benchmark results distinct from independently reproduced measurements. Quantized packages do not create another trained-model identity.
