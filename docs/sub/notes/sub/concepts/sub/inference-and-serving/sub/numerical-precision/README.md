# Numerical Precision

Legacy residual retained for hardware/runtime capability verification, precision-path observability, stability testing, fallback diagnosis, and deployment benchmarking guidance that are intentionally outside the canonical Numerical Precision concept owner.

> **Migration note:** Numerical-precision identity, bit-width versus format semantics, storage/compute/activation/accumulation/cache distinctions, mixed-precision boundaries, reduced floating point versus quantization separation, numerical range/error/stability limits, and hardware/runtime dependence are already preserved in `docs/sub/concepts/sub/models/sub/optimization-and-compression/sub/numerical-precision/`. The remaining material below stays here until its exact learning, inference-engineering, runtime, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Capability-verification residual

Verify the exact model, runtime/kernel, accelerator/CPU, driver/firmware, and operation path before selecting a precision configuration. A device may advertise support for a numerical format while the required model operations fall back to conversion, emulation, or another precision path that changes performance or memory behavior.

Check weight/storage, activation, accumulation, cache, input/output, and intermediate precision separately where the runtime exposes them. Do not infer the effective compute path solely from the serialized artifact or a single `dtype` label.

## Stability and quality residual

Test representative inputs for numerical instability, overflow/underflow, NaN/Inf propagation, output-quality regressions, calibration changes, and long-context or high-dynamic-range edge cases when they are relevant to the workload. A lower-bit format can work well for common cases while failing on sensitive operations or model families.

Compare candidate precision configurations under matched runtime, model, context, batching, and workload conditions so quality or speed differences are not attributed to precision while another execution variable changed.

## Fallback diagnosis residual

Use runtime/profiler/log evidence where available to confirm which kernels and data types actually execute. Unexpected latency, memory use, or device utilization can indicate hidden conversions, higher-precision accumulation, unsupported operators, host fallback, or mixed execution rather than the intended low-precision path.

Treat unsupported or partially supported paths as deployment constraints, not merely documentation inconsistencies. Prefer a well-supported higher-precision route over a nominally smaller format when the fallback path negates the expected benefit.

## Deployment-benchmark residual

Measure model load size, resident RAM/VRAM, runtime workspace, cache memory, prompt/prefill latency, decode speed, throughput, concurrency, and accepted-result quality on the actual target environment. Record model/runtime/hardware versions with the result so later precision support changes can be re-evaluated.

These capability, stability, fallback, and deployment-benchmark practices remain migration source material until their exact learning, inference-engineering, runtime, evaluation, or decision-support owners are verified.
