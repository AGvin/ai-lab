# Model Loading

Model loading moves model artifacts from storage into RAM, VRAM, accelerator memory, or memory-mapped address space so inference can begin.

## Core idea

Loading includes reading files, allocating memory, initializing runtime structures, transferring layers to devices, and sometimes compiling kernels. The amount of required memory is larger than the model file alone because the runtime also needs buffers, caches, metadata, and temporary workspaces.

## Practical considerations

- Storage speed affects cold-start time.
- Memory mapping can avoid copying the full model into anonymous RAM.
- GPU transfer time grows with model size and bus bandwidth.
- Multiple processes may or may not share mapped weights.
- Some runtimes compile optimized graphs on first use.

## Practical use

Measure cold start, warm start, and first-request latency separately. Leave memory headroom for the operating system, context cache, and concurrent requests. For containers, verify memory limits and persistent cache locations.

## Trade-offs and limitations

Keeping a model resident reduces latency but consumes memory continuously. Loading on demand saves resources but creates long startup delays. Memory mapping depends on operating-system caching and can still cause page faults under pressure.

## Common mistakes

- Estimating memory from file size only.
- Running several model processes that duplicate weights.
- Ignoring temporary conversion or compilation storage.
- Benchmarking only after the model is fully warmed.

## Related concepts

- [Inference and Serving](../../)
- [Inference](../inference/)
- [GPU Offloading](../gpu-offloading/)
- [Context Caching](../context-caching/)
