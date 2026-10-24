# Documentation Requirements

## Requirements

- Represent Granite TTM R3 as a model series because IBM explicitly describes it as a family of pretrained models.
- Preserve the official toolkit boundary: it selects among multiple R3 revision keys according to context length, prediction horizon, decomposed architecture, and Lite/non-Lite mode.
- Do not equate the repository's default safetensors/config artifact with the whole R3 family, and do not materialize every revision key as a catalog node without a separate identity intake.
- Preserve current supported scenarios from the first-party card, including zero-shot forecasting, few-shot adaptation, full fine-tuning, multivariate forecasting, exogenous/control-variable integration, and high-throughput batch inference.
- Preserve the published model-size boundary exactly: non-Lite R3 models span 1–35M parameters and Lite models span 1–18M parameters.
- Treat card benchmark scores, throughput figures, and speedup claims as provider-reported evidence, not reproduced measurements; keep them scoped to the exact published evaluation context.

## Validation

- Membership resolves to Granite Time Series.
- The canonical ID is unchanged and the taxonomy correction adds no Model denominator node.
- Runtime revision selection is documented as an implementation contract, not as a set of aliases.
- Reader wording separates supported-task/model-family facts from unreplicated benchmark and throughput claims.