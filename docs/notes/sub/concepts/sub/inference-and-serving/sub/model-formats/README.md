# Model Formats

File and serialization formats used to store and load model artifacts.

## Core idea

File and serialization formats used to store and load model artifacts. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Model formats define how weights, metadata, tensors, tokenizer data, and sometimes computation graphs are serialized.
- GGUF is common in llama.cpp ecosystems, Safetensors in transformer frameworks, and ONNX for portable computation graphs.
- Conversion may change precision, layout, or supported features.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Model Formats affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Match a downloaded model to a runtime such as llama.cpp, Transformers, ONNX Runtime, or a vendor engine.
- Distribute models safely and reproducibly.

## Example

LM Studio may load a GGUF quantization directly, while a PyTorch workflow usually expects Safetensors plus configuration files.

## Trade-offs and limitations

- The same extension can contain incompatible architectures or metadata versions.
- Conversion can lose unsupported layers, tokenizer details, or quality.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Model Formats expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../)
- [Numerical Precision](../numerical-precision/)
- [GPU Offloading](../gpu-offloading/)
