# Documentation Requirements

## Requirements

- Identify K-EXAONE 2.0 as the 750B-parameter model released by LG AI Research on 2026-07-31.
- Preserve the Apache-2.0 commercial-use release boundary and first-party benchmark claims only at exact checkpoint scope.
- Treat quantizations, runtime support, deployment guidance, and third-party hosting as freshness-sensitive.

## Validation

- Membership resolves to K-EXAONE.

## Verified model-card facts (2026-10-30)

- The [official model card](https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B) identifies a MoE model with 750B total parameters, 37B active parameters and a 262,144-token context. Render total and active counts separately and attribute them to LG.
- Active parameters are not the stored-weight footprint; context capacity does not establish hardware fit. The card describes upcycling from the earlier K-EXAONE model; do not invent a canonical predecessor node or infer expert counts beyond explicit evidence.
