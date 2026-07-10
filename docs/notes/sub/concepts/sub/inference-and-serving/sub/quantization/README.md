# Quantization

Reducing numerical precision to lower model memory and compute requirements.

## Core idea

Reducing numerical precision to lower model memory and compute requirements. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Quantization represents weights or activations with fewer bits than the original floating-point format.
- Methods differ in calibration, grouping, scaling, outlier handling, and whether activations or only weights are quantized.
- The runtime must support the specific quantization format and kernels.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Quantization affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Fit larger models into available RAM or VRAM.
- Reduce memory bandwidth and sometimes improve inference speed.

## Example

A 7B model in a four-bit GGUF variant may fit into much less memory than its FP16 version.

## Trade-offs and limitations

- Aggressive quantization can reduce accuracy, especially on sensitive tasks or small layers.
- A smaller file does not guarantee faster execution on unsupported hardware.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Quantization expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../)
- [Inference](../inference/)
- [Numerical Precision](../numerical-precision/)
