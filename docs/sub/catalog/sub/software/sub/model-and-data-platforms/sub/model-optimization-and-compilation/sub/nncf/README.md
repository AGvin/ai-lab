# NNCF

NNCF, the Neural Network Compression Framework, is software for inference optimization through quantization, weight compression, pruning and sparsity, and related model-compression techniques.

## Software boundary

NNCF is optimization and compression-first. Training-time compression methods remain part of the same identity when efficient inference is the product center rather than general model development.

Supported frameworks and models, OpenVINO compatibility, algorithms, package versions, and hardware and runtime support are freshness-sensitive.

## Telemetry

NNCF participates in OpenVINO telemetry, which the official guide says is collected by default using Google Analytics. Upstream describes it as anonymous usage data. To disable it, run `opt_in_out --opt_out` in the Python environment where NNCF is installed. Local model optimization should not be assumed to mean no outbound telemetry.

## Relations

- Produced by [OpenVINO Toolkit](../../../../../../../producers/sub/o/sub/openvino-toolkit/).

## Official resources

- [NNCF documentation](https://openvinotoolkit.github.io/nncf/)
- [NNCF repository](https://github.com/openvinotoolkit/nncf)
- [OpenVINO telemetry and opt-out](https://docs.openvino.ai/2026/about-openvino/additional-resources/telemetry.html)
