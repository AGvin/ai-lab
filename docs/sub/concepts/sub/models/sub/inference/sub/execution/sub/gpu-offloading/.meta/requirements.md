# Documentation Requirements

## Requirements

- Use the reader-facing title `GPU Offloading`.
- Define this repository's `GPU offloading` concept as heterogeneous model placement in which selected parameters, layers, operations, caches, or other execution state are placed on or executed by a GPU while other model state or computation remains on CPU, another accelerator, unified/system memory, or disk-backed storage.
- Explicitly note terminology direction when necessary. Some runtimes use `offload to GPU` for moving work from a CPU/system-memory baseline onto GPU, while other ecosystems use `CPU offload` or `disk offload` for moving state away from GPU. Always state source and destination instead of relying on the word `offload` alone.
- Distinguish partial GPU offloading from full GPU residency and from multi-GPU model parallelism. A heterogeneous CPU/GPU split can exist on one GPU, while multi-GPU execution can use separate parallelism/placement strategies.
- Explain that offloading can target weights, individual modules/layers, operations, activations, caches, or other state depending on runtime capabilities; a configured `number of GPU layers` is one implementation pattern rather than the universal abstraction.
- Make clear that more GPU-resident state does not monotonically guarantee better performance. Transfers, synchronization, CPU fallback, device-memory pressure, cache placement, batch/context shape, and runtime scheduling can create different optima.
- Distinguish GPU memory capacity from weight-placement capacity. VRAM must also accommodate required activations, caches, runtime workspaces, kernels/graphs, outputs, and concurrency; filling VRAM with weights can make the actual workload fail or perform worse.
- Explain that host-device interconnect bandwidth/latency matters when data crosses separate memory domains, while integrated/unified-memory systems can reduce or reshape explicit transfer boundaries without eliminating bandwidth, contention, residency, or capacity constraints.
- Distinguish offloading from model loading. Loading can dispatch weights to devices as part of initialization, but offloading owns the resulting heterogeneous placement/execution strategy rather than the persistence/loading mechanism.
- Distinguish offloading from quantization or compression. Smaller representations can make more state GPU-resident, but changing representation and changing placement are separate operations.
- Keep concrete layer counts, device-map syntax, unified-memory implementation details, PCIe/NVLink measurements, runtime-specific offload algorithms, hardware compatibility, benchmark curves, and practical deployment recommendations with their applicable catalog, runtime, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for heterogeneous device placement and directional offload terminology when reader-facing rendering is activated.

## Validation

- The page explicitly states offload direction when terminology could be ambiguous.
- GPU offloading is not equated with full GPU inference, multi-GPU parallelism, model loading, or quantization.
- More offloaded/GPU-resident layers are not presented as universally faster.
- Weight residency is not allowed to consume all VRAM in the conceptual feasibility model while ignoring caches/workspaces/concurrency.
- Unified memory is not presented as eliminating bandwidth, placement, or capacity constraints.
- Concrete runtime layer counts, device maps, and hardware recommendations remain outside the canonical concept.
