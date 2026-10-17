# LLM Compressor

LLM Compressor is an independently maintained model-compression library that prepares quantized and otherwise optimized LLM artifacts for subsequent inference in runtimes such as vLLM.

## Scope and product boundaries

Its optimization workflows cover weight and activation quantization, calibration and supported KV-cache quantization. Compressed checkpoint formats, specific kernels and downstream inference servers are separate integration or artifact concerns. Compression changes an existing model representation; it does not by itself create a new trained model identity.

## Compatibility and operational considerations

Pin the library, output serialization, target architecture, precision scheme, calibration data and intended runtime. Algorithm and hardware support depend on release; development-branch examples must not be taken as stable support. Evaluate output quality and throughput on the actual model and workload rather than extrapolating from a different configuration.

LLM Compressor originated with Neural Magic, whose team announced its initial public release in 2024 and continued compression work after joining Red Hat. The current project is part of the vLLM Project, with technical direction and contributions managed by its committers. This history is separate from the current repository-level producer relation.

## Relations

- Produced by: [vLLM Project](../../../../../../../producers/sub/v/sub/vllm-project/)

## Official resources

- [Source repository](https://github.com/vllm-project/llm-compressor)
- [Official documentation](https://docs.vllm.ai/projects/llm-compressor/en/latest/)
- [Current project governance](https://docs.vllm.ai/projects/llm-compressor/en/latest/developer/governance/)
- [Original release announcement](https://developers.redhat.com/articles/2024/08/14/llm-compressor-here-faster-inference-vllm)
- [Neural Magic joining Red Hat and subsequent model-compression work](https://developers.redhat.com/articles/2025/01/30/compressed-granite-3-1-powerful-performance-small-package)
