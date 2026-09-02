# Quantization

Legacy residual retained for conversion/calibration workflow, representative quality evaluation, runtime-kernel verification, deployment benchmarking, and artifact/version-management guidance that are intentionally outside the canonical Quantization concept owner.

> **Migration note:** Quantization identity, quantize/dequantize semantics, affected-tensor distinctions, scale/granularity design dimensions, post-training versus training-aware boundaries, nominal-bit versus quality limits, realized-performance dependence, and separation from pruning/distillation/format/model-scale are already preserved in `docs/sub/concepts/sub/models/sub/optimization-and-compression/sub/quantization/`. The remaining material below stays here until its exact learning, optimization-engineering, inference-runtime, evaluation, artifact-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Conversion and calibration residual

Pin the exact source model/checkpoint, tokenizer or processor, quantization tool/version, target tensors, representation/bit width, grouping/scaling scheme, calibration dataset where applicable, clipping/range settings, and resulting artifact identity. Two artifacts described only as `4-bit` or `8-bit` are not reproducibly equivalent.

Use calibration data representative of the target activation distribution when the method depends on calibration. Keep calibration examples separate enough from final evaluation that tuning scale/range decisions does not silently optimize to the acceptance set.

## Quality-evaluation residual

Compare quantized artifacts with the source model on representative target tasks and important retained capabilities. Include long-context, reasoning, structured-output, tool-use, multilingual, multimodal, calibration, or stability cases when they matter to the intended deployment rather than testing only a few short prompts.

Evaluate several quantization configurations when the quality/resource frontier is uncertain. Do not infer monotonic quality solely from nominal bit width; method, tensor sensitivity, group size, outlier handling, calibration, and runtime implementation can reverse simple expectations.

## Runtime and kernel residual

Verify the exact runtime/hardware executes efficient kernels for the chosen representation and affected tensors. Measure whether weights, activations, or cache remain quantized in the hot path or are repeatedly converted/dequantized into another format.

Unexpected latency, memory use, or device utilization can indicate unsupported kernels, fallback, mixed execution, or conversion overhead. Prefer a well-supported higher-bit artifact when it provides better end-to-end fit than a nominally smaller configuration with poor kernel support.

## Deployment and artifact residual

Measure serialized size, resident RAM/VRAM, runtime workspace, KV/cache memory where relevant, load time, prompt/prefill latency, decode speed, throughput, concurrency, power/energy where useful, and accepted-result quality on the actual target environment.

Version the source checkpoint, quantization configuration/toolchain, artifact/container, runtime compatibility, and evaluation evidence together. Revalidate after runtime, driver, firmware, kernel, model, or conversion-tool changes and keep a known-good source/higher-precision artifact available for rollback.

These conversion, evaluation, runtime, deployment, and artifact-management practices remain migration source material until their exact learning, optimization-engineering, inference-runtime, evaluation, artifact-management, or decision-support owners are verified.
