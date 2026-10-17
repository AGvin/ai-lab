# Documentation Requirements

## Requirements

- Identify ONNX Runtime GenAI as Microsoft's released generative-AI inference extension/runtime for executing generative models with ONNX Runtime.
- Preserve its inference-engine boundary across model loading, preprocessing/postprocessing, decoding/sampling, KV-cache management, batching, speculative decoding, constrained/tool-call generation, multimodal/audio support, and model-building/export helpers where released.
- Keep ONNX Runtime GenAI distinct from ONNX as a model format, base ONNX Runtime, Windows ML, Foundry Local, VS Code AI Toolkit, concrete exported model artifacts, and model producers.
- Treat supported model architectures, execution providers/hardware, APIs/languages, runtime profiles, quantization formats, cache/attention modes, package artifacts, release versions, and performance results as freshness-sensitive.
- Do not treat under-development or roadmap support matrices as released capability.
- Attribute performance comparisons to Microsoft or the cited evaluator and preserve hardware/model/precision/configuration.
- Preserve Microsoft producer provenance.

## Validation

- The node remains a generative inference engine rather than the ONNX format or a model family.
- Roadmap/under-development rows are not presented as current support.
- Producer provenance resolves bidirectionally to Microsoft.
