# GGUF

GGUF is the upstream GGML model file format for storing models for inference with GGML and GGML-based executors. It succeeds the earlier GGML, GGMF, and GGJT file-format line.

## Format boundary

The format is designed for single-file deployment, extensibility, memory-mapping-friendly access, and self-describing model metadata. Its structure includes a header, typed key-value metadata, tensor descriptors, required alignment or padding, and the tensor-data region. Structural versions, metadata vocabulary, alignment rules, endianness, tensor type identifiers, and quantization-version metadata are versioned specification concerns and must be read from the current upstream contract.

GGUF validity does not imply that a runtime supports a particular model, that conversion preserved model semantics, that a model is appropriately licensed, or that it is suitable for a workload. Runtime compatibility, converter behavior, device support, benchmarks, and model-selection guidance remain separate concerns.

## Official resources

- [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md)
- [GGML repository](https://github.com/ggml-org/ggml)
