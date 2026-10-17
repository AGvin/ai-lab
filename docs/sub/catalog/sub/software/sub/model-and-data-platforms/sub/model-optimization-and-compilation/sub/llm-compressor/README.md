# LLM Compressor

LLM Compressor is an independently maintained model-compression library that prepares quantized and otherwise optimized LLM artifacts for subsequent inference in runtimes such as vLLM.

## Scope and product boundaries

Its optimization workflows cover weight and activation quantization, calibration and supported KV-cache quantization. Compressed checkpoint formats, specific kernels and downstream inference servers are separate integration or artifact concerns. Compression changes an existing model representation; it does not by itself create a new trained model identity.

## Compatibility and operational considerations

Pin the library, output serialization, target architecture, precision scheme, calibration data and intended runtime. Algorithm and hardware support depend on release; development-branch examples must not be taken as stable support. Evaluate output quality and throughput on the actual model and workload rather than extrapolating from a different configuration.

## Relations

- Produced by: [vLLM Project](../../../../../../../producers/sub/v/sub/vllm-project/)

## Official resources

- [Source repository](https://github.com/vllm-project/llm-compressor)
- [Official documentation](https://docs.vllm.ai/projects/llm-compressor/en/latest/)
