# Quantization

Quantization represents model weights, activations, or cache values with lower-precision numbers to reduce memory use and computation cost.

## Core idea

A model trained in floating-point precision can often be converted to formats using fewer bits per value. Weight-only quantization is common for local language-model inference, while server runtimes may also quantize activations or the KV cache.

## Common forms

- FP16 or BF16 for reduced-precision floating-point inference.
- INT8 or FP8 in supported accelerator runtimes.
- 4-bit, 5-bit, 6-bit, or 8-bit weight formats used by local runtimes.
- Mixed quantization where sensitive layers use higher precision.

## Practical use

Quantization can make a model fit into available RAM or VRAM and may improve speed when the hardware has efficient low-precision kernels. Compare several quantization levels on representative tasks, because quality loss varies by architecture, task, and quantizer.

## Trade-offs and limitations

Lower bit depth saves memory but can reduce instruction following, reasoning, factual recall, or output stability. Smaller files are not always faster if the hardware must dequantize inefficiently. Different quantization methods with the same nominal bit count may have different quality.

## Common mistakes

- Selecting a quantization only by file size.
- Assuming every 4-bit format has equivalent quality.
- Benchmarking short prompts when the real workload uses long context.
- Ignoring KV-cache memory after fitting the weights.

## Related concepts

- [Inference and Serving](../../)
- [Numerical Precision](../numerical-precision/)
- [Model Formats](../model-formats/)
- [GPU Offloading](../gpu-offloading/)
