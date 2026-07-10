# FlashAttention

FlashAttention is a family of attention implementations designed to reduce memory traffic and improve accelerator efficiency while computing exact attention results within supported numerical behavior.

## Core idea

Standard attention may materialize large intermediate matrices in high-bandwidth memory. FlashAttention reorganizes the computation into tiles that fit in faster on-chip memory, reducing reads and writes. The improvement is primarily an implementation optimization rather than a different model architecture.

## Practical use

- Speed up prompt processing for long sequences.
- Reduce temporary memory use during attention.
- Enable larger batches or contexts on supported GPUs.
- Improve training and inference efficiency in compatible runtimes.

## Trade-offs and limitations

Benefits depend on sequence length, hardware, data type, head dimensions, and kernel support. Short requests or unsupported architectures may see little improvement. Different FlashAttention generations and vendor kernels have different compatibility requirements.

## Common mistakes

- Treating FlashAttention as a model quantization method.
- Assuming enabling a flag guarantees the optimized kernel is used.
- Comparing performance without checking sequence length and batch size.
- Expecting it to eliminate KV-cache memory.

## Related concepts

- [Inference and Serving](../../)
- [KV Cache](../kv-cache/)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)
- [Performance Metrics](../performance-metrics/)
