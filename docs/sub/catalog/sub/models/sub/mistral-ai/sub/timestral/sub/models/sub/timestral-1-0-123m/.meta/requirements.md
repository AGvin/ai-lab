# Documentation Requirements

## Requirements

- Identify Timestral 1.0 123M as a distinct released trained-model identity from Mistral AI.
- Render the standard entity-relations block from validated canonical metadata.
- Keep model-specific specifications, artifact representations and hosted access context distinct.

## Validation

- The entity ID matches the canonical path and reciprocal relations resolve.
- Claims stay at the documented release scope, and generated output is not treated as a correctness or security guarantee.

## Source-backed profile

- Required reader orientation: Timestral 1.0 123M is Mistral AI’s 123M-parameter time-series forecasting checkpoint in the October 2026 Timestral release.
- Preserve this model-scoped fact: The patch-based transformer has 20 layers and an embedding width of 640; it processes numeric series, not chat tokens. [Timestral 123M released weights](https://huggingface.co/mistralai/Timestral-123M)
- Preserve this model-scoped fact: It accepts up to 32,768 time steps and forecasts 1,024 steps per forward pass, returning 21 quantiles. Longer forecasts feed each block’s median back as context. [Timestral 123M released weights](https://huggingface.co/mistralai/Timestral-123M)
- Preserve this model-scoped fact: The released weights are published by Mistral AI; its model card labels this release public preview. [Timestral 1.0 123M model card](https://docs.mistral.ai/models/timestral-1-0-123m)

## Operational and interpretation boundaries

- Explain this boundary: The Modified MIT weight license restricts use above US$20 million in preceding-month global consolidated company/employer revenue. The inference code’s Apache 2.0 license does not replace the weight license. [Timestral 123M Modified MIT license](https://huggingface.co/mistralai/Timestral-123M/blob/main/LICENSE)
- Explain this boundary: Supply only covariates available at forecast time and preserve missing-value masks. Quantile outputs are model estimates, not guaranteed coverage; evaluate leakage and calibration on held-out time periods.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
