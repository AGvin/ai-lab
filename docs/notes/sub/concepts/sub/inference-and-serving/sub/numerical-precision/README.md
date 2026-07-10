# Numerical Precision

The number format used for model weights, activations, and computation.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

The number format used for model weights, activations, and computation. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Numerical precision defines formats such as FP32, FP16, BF16, FP8, INT8, or INT4 used for weights and computation.
- Lower precision reduces storage and bandwidth but provides less numeric range or resolution.
- Mixed-precision systems keep sensitive operations at higher precision while using lower precision elsewhere.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Numerical Precision affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Interpret model requirements and hardware compatibility.
- Choose trade-offs between accuracy, speed, and memory.

## Example

BF16 retains a wide exponent range while using fewer mantissa bits than FP32, making it useful for many training and inference workloads.

## Trade-offs and limitations

- Different formats with the same bit width can have different range and accuracy.
- Hardware support determines whether a format is efficient or emulated.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Numerical Precision expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../)
- [Quantization](../quantization/)
- [Model Formats](../model-formats/)
