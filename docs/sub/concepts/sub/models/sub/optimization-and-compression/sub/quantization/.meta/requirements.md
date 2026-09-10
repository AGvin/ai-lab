# Documentation Requirements

## Requirements

- Use the reader-facing title `Quantization`.
- Define quantization as mapping model values or computations from a source numerical representation into a more restricted representable set, commonly using lower-bit integer or low-bit floating formats together with scaling or related encoding rules, so storage and/or arithmetic can use reduced precision.
- Distinguish quantization from numerical precision in general. Numerical precision describes the representations/arithmetic used by model components; quantization is a transformation/scheme that maps values into a restricted representation. FP16 or BF16 execution alone is therefore not automatically a quantization scheme, while FP8/FP4 can participate in explicit quantize/dequantize schemes depending on the implementation.
- Explain quantize/dequantize semantics conceptually: a quantizer approximates source values with representable quantized values and associated scale/metadata as required; some execution paths later dequantize for higher-precision operations while others execute quantized arithmetic directly.
- Distinguish weight-only, activation, weight-and-activation, and cache/KV quantization. A model described as `4-bit` or `8-bit` is incomplete unless the affected values, representation, grouping/scaling scheme, and relevant compute behavior are identified.
- Present per-tensor, per-channel/per-axis, group/block, symmetric/asymmetric, static/calibrated, and dynamic scaling as common quantization design dimensions rather than one universal taxonomy or required combination.
- Distinguish post-training quantization from quantization-aware training or other training-time adaptation. Quantization can be applied after training, simulated/accounted for during training, or integrated into specialized training/conversion pipelines; one workflow is not part of the universal definition.
- Explain that nominal bit count alone does not determine approximation quality. Quantizer design, scale granularity, clipping/range estimation, outliers, calibration data, tensor sensitivity, architecture, task, and model-specific behavior can materially change error at the same bit width.
- Make clear that smaller quantized weights or caches do not guarantee faster end-to-end inference. Runtime kernels, hardware support, memory bandwidth, dequantization/conversion overhead, batching, context length, offloading, and mixed-precision execution can dominate realized performance.
- Distinguish quantization from pruning/sparsity, distillation, model scale classification, and artifact/container format. A quantized artifact can use a particular file format, but the format is not the quantization concept itself and a quantized LLM does not become an SLM solely because its representation is smaller.
- Explain that quality effects must be evaluated on representative tasks and operating conditions. Quantization can preserve behavior closely in some settings and degrade capability, calibration, stability, or particular task families in others; do not claim monotonic loss based only on bit width.
- Keep concrete quantization algorithms, GGUF/GPTQ/AWQ or other artifact/method identities, runtime-specific kernels, exact calibration recipes, model-specific quality/performance benchmarks, hardware compatibility, and deployment recommendations with their applicable catalog, specification, inference, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for quantize/dequantize mappings, training/post-training boundaries, and modern scaling/granularity schemes when reader-facing rendering is activated.

## Validation

- The page does not list FP16/BF16 reduced-precision execution as automatically synonymous with quantization.
- A nominal `4-bit` or `8-bit` label is not treated as a complete quantization specification.
- Weight precision, activation precision, cache precision, and actual compute precision are not assumed identical.
- Quantization is not conflated with pruning, sparsity, distillation, artifact format, or SLM/LLM scale.
- Lower bit width is not presented as an automatic latency improvement or as a complete predictor of quality loss.
- Post-training and training-aware quantization are distinguished without making either workflow universally required.
- Legacy model/hardware selection guidance is preserved only as evaluation and implementation-dependent boundaries rather than canonical presets.
