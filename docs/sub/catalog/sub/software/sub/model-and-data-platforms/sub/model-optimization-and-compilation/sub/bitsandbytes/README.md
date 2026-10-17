# bitsandbytes

bitsandbytes is an independently released PyTorch-oriented library for low-bit quantization and memory-efficient optimization, enabling large-model inference and QLoRA-style fine-tuning.

## Scope and product boundaries

Its core functionality includes LLM.int8 8-bit inference, 4-bit quantization and 8-bit optimizers. Quantization backends, wheels, numeric formats, Hugging Face integration and QLoRA workflows are components or applications of one library, not separate software products or trained checkpoints.

## Compatibility and operational considerations

CPU and GPU support, precision formats, driver/toolchain requirements and prebuilt packages vary by release and architecture. Do not assume NVIDIA, AMD, Intel or Apple compatibility from the name alone; verify the exact device and installation matrix. Benchmark claims require an identified model, dataset, quantization mode, accelerator, kernel, software build and runtime.

## Relations

- Produced by: [bitsandbytes Foundation](../../../../../../../producers/sub/b/sub/bitsandbytes-foundation/)

## Official resources

- [Upstream source](https://github.com/bitsandbytes-foundation/bitsandbytes)
- [Documentation](https://huggingface.co/docs/bitsandbytes/main/)
