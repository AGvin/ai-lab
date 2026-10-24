# Documentation Requirements

## Requirements

- Present NNCF as the Neural Network Compression Framework for inference optimization through quantization, weight compression, pruning/sparsity, and related model-compression techniques.
- Keep training-time compression methods within the NNCF optimization identity when efficient inference remains the product center.
- Treat supported frameworks/models, OpenVINO compatibility, algorithms, package versions, and hardware/runtime support as freshness-sensitive.
- Describe NNCF's participation in default-enabled OpenVINO telemetry using Google Analytics, which upstream calls anonymous usage data. Give `opt_in_out --opt_out` as the documented control in the Python environment where NNCF is installed; do not imply that local model optimization guarantees no outbound telemetry.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NNCF remains optimization/compression-first rather than general model-development ownership.
- Producer provenance resolves to the OpenVINO Toolkit project identity.
