# Documentation Requirements

## Requirements

- Identify Timestral as a distinct released model family from Mistral AI.
- Render the standard entity-relations block from validated canonical metadata.
- Keep model-specific specifications, artifact representations and hosted access context distinct.

## Validation

- The entity ID matches the canonical path and reciprocal relations resolve.
- Claims stay at the documented release scope, and generated output is not treated as a correctness or security guarantee.

## Source-backed profile

- Required reader orientation: Timestral is Mistral AI’s family of numeric time-series foundation models, released on October 15, 2026.
- Preserve this model-scoped fact: Four independently released sizes—5M, 28M, 123M and 209M—produce probabilistic forecasts from univariate or multivariate histories and covariates. [Timestral release](https://mistral.ai/news/timestral/)

## Operational and interpretation boundaries

- Explain this boundary: Time steps and forecast horizons are numeric-series units, not LLM token context. The inference code uses Apache 2.0; released model weights use their own Modified MIT licenses. [Timestral inference code and input contract](https://github.com/mistralai/timestral)
- Explain this boundary: Forecasts are estimates. Evaluation must respect time ordering and use only information available when each forecast would have been made.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
