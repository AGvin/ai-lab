# Documentation Requirements

## Requirements

- Represent Granite TTM R3 as a model series because IBM explicitly describes it as a family of pretrained models.
- Preserve the official toolkit boundary: it selects among multiple R3 revision keys according to context length, prediction horizon, decomposed architecture, and Lite/non-Lite mode.
- Do not equate the repository's default safetensors/config artifact with the whole R3 family, and do not materialize every revision key as a catalog node without a separate identity intake.
- Preserve forecasting tasks, model-size ranges, architecture, throughput and benchmark claims only at the exact current source scope.

## Validation

- Membership resolves to Granite Time Series.
- The canonical ID is unchanged and the taxonomy correction adds no Model denominator node.
- Runtime revision selection is documented as an implementation contract, not as a set of aliases.
