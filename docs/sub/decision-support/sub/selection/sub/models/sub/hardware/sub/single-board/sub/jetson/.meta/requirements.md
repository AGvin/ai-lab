# Documentation Requirements

## Route Fit

- Cover NVIDIA Jetson developer kits/modules as integrated embedded CUDA edge-AI platforms where exact module, JetPack/Jetson Linux generation, shared system memory, power mode, thermal design, sensors/media pipelines, and ARM64 software support determine model fit.
- Require exact Jetson module/SKU, installed memory, carrier/dev-kit context where material, JetPack/Jetson Linux release, CUDA/TensorRT/vLLM/TensorRT-LLM/other runtime, model artifact/precision, context, concurrency, power mode, and sustained cooling before assigning fit.
- Do not model Jetson as a miniature desktop RTX PC or as a datacenter GPU with lower VRAM.
- Keep module/hardware purchasing outside this route.

## Current JetPack Generation First

- Treat JetPack/Jetson Linux as part of the hardware compatibility key.
- Current JetPack 7 is the current generation and now supports Jetson Orin and Jetson Thor, with Ubuntu 24.04/Linux 6.8-era base and the current NVIDIA AI compute stack.
- Current JetPack 6 remains a sustaining/production Orin route with a different Jetson Linux/CUDA/TensorRT generation.
- Do not transfer a container, TensorRT engine, CUDA wheel, driver assumption, or framework from JetPack 6 to 7 or vice versa without current support evidence.
- Record exact L4T/Jetson Linux build as well as the marketing JetPack release.

## Thor and Orin Are Related but Not Interchangeable

- Keep Thor and Orin in one ecosystem page while content can remain clear, but treat them as distinct compatibility/performance families.
- Current Jetson Thor uses Blackwell-class GPU architecture, much larger memory/power envelopes on AGX Thor, current SBSA-aligned software, and CUDA 13-era JetPack 7 integration.
- Orin modules span AGX Orin, Orin NX, and Orin Nano with different GPU/DLA/memory/power capabilities and current JetPack 6/7 support paths.
- Do not use a Thor benchmark/runtime feature as evidence for Orin unless the exact software/model is documented on both.
- Do not transfer Orin DLA or power-mode assumptions to Thor without exact platform evidence.

## Exact Module and Memory SKU

- Record the exact module, not only `Orin` or `Thor`.
- Orin Nano/NX/AGX Orin and Thor T4000/T5000/AGX Thor-class systems have materially different memory, memory bandwidth, GPU, power, and sensor/IO envelopes.
- Treat system memory as **shared CPU/GPU/system memory**, not dedicated GPU VRAM.
- Reserve headroom for Linux, desktop/services when present, containers, cameras/media buffers, model weights, KV/cache, runtime workspaces, embeddings/VLM encoders, and other processes.
- Do not infer usable model size from nominal installed memory alone.

## Shared Memory and Unified Working Set

- Measure peak whole-system memory under the complete application.
- Include pageable/pinned CUDA memory, TensorRT/vLLM caches, KV cache, vision/audio tensors, camera buffers, zero-copy/shared memory, container overhead, and CPU-side preprocessing.
- A model that barely loads with no sensors/services running is not practical edge fit.
- Avoid aggressive swapping on storage as a substitute for memory fit; measure latency/endurance/availability consequences if swap is intentionally used.
- Track memory pressure during concurrent sensor + model + agent/service workloads.

## CUDA Compatibility Is Necessary but Not Sufficient

- JetPack includes NVIDIA CUDA/TensorRT/cuDNN and other Jetson-specific components, but exact model/runtime packages still require ARM64/aarch64 support.
- Verify container image architecture, Python wheels, custom CUDA extensions, tokenizers, FlashAttention/quantization kernels, Triton kernels, and dependent libraries.
- A project supporting NVIDIA CUDA on x86 does not automatically support Jetson aarch64.
- Preserve exact CUDA/TensorRT/framework/container versions in fit evidence.
- Keep unsupported aarch64 dependencies `Unknown` rather than assuming source-build success.

## TensorRT and TensorRT-LLM Route

- Use TensorRT/TensorRT-LLM only when the exact model/operator/precision and Jetson release are supported.
- Preserve source model, export/build process, TensorRT/TensorRT-LLM version, architecture target, precision/quantization, engine profiles, and context/batch limits.
- Do not assume a TensorRT engine built on x86/another GPU architecture is portable to the target Jetson without documented compatibility.
- Include engine-build time, disk/cache footprint, and rebuild requirements in operational fit.
- Verify any plugins/custom kernels on aarch64 and the target GPU generation.

## vLLM and Generative Serving

- Treat vLLM or Jetson-specific optimized containers as separate serving routes with exact JetPack/module support.
- Current NVIDIA Jetson Thor generative-AI benchmarks use vLLM for LLM/VLM workloads under explicitly stated sequence length, output length, concurrency, precision, and MAXN conditions; preserve these conditions rather than copying tokens/s as a generic Jetson result.
- Verify current Orin/Thor container support separately.
- Measure the user's own model revision, quantization, context, concurrency, and power mode.
- Do not infer a larger/sibling model's fit from one NVIDIA benchmark table.

## llama.cpp and Lightweight Local Runtimes

- `llama.cpp` can remain a lower-complexity CUDA/aarch64 route when current builds support the target Jetson/model.
- Preserve exact build/CUDA flags, GGUF quantization, GPU offload, context, and host-memory use.
- Compare prompt/decode and quality against NVIDIA-optimized routes rather than assuming either framework is universally faster.
- Lightweight runtime availability does not remove JetPack/CUDA/aarch64 compatibility constraints.

## DLA Is Not a Generic LLM Accelerator

- On Jetson models that include NVIDIA Deep Learning Accelerators, treat DLA as a model/operator-specific inference target, not extra CUDA cores or generic LLM capacity.
- Verify exact TensorRT/DLA operator and precision support for the model graph.
- Keep unsupported layers/fallback to GPU explicit.
- Do not infer that DLA TOPS can accelerate transformer decode unless the exact graph/runtime supports it.
- Use DLA where validated CNN/vision pipelines benefit and GPU capacity needs to be reserved for other work.

## Power Modes Are Part of the Benchmark

- Record `nvpmodel`/selected power mode, clock policy, fan/cooling configuration, input voltage/power supply, and sustained temperature.
- Current Jetson families expose materially different configurable power envelopes; Thor can reach much higher power than Orin Nano/NX-class systems.
- NVIDIA provider benchmarks often use MAXN; do not translate them to a lower-power deployed mode.
- Measure workload performance-per-watt at the power mode the application will actually use.
- A model fitting only at MAXN with unacceptable thermal/power behavior is conditional fit for constrained edge deployments.

## Sustained Thermals and Cooling

- Measure long enough to reach steady thermal behavior.
- Developer kits, passive modules, custom carrier/enclosures, and deployed robots/edge boxes can have different cooling.
- Record GPU/CPU clocks, temperature, throttling, fan state, and throughput over time.
- Do not use a short open-bench dev-kit test as proof of enclosed production performance.
- Treat thermal design as part of the fixed deployment boundary, not an afterthought.

## Prompt and Decode Measurement

- For LLMs record:
  - cold/warm model load;
  - TTFT;
  - prompt/prefill latency or tokens/s at representative context;
  - sustained decode/TPOT/tokens/s;
  - context/output lengths;
  - peak shared memory;
  - power mode/thermal state;
  - accepted-result quality.
- Do not report output tokens/s alone for an interactive VLM/agent route.
- Compare models/runtimes only under labeled equivalent precision/context/concurrency settings.

## Current NVIDIA Benchmarks Are Conditional Evidence

- NVIDIA publishes current Jetson generative-AI/MLPerf benchmarks and Jetson AI Lab measurements.
- Preserve exact module, model, quantization/precision, sequence length, concurrency, runtime, and power mode when citing them.
- Current Thor-vs-Orin generative benchmark examples use sequence length 2048, output 128, maximum concurrency 8 and MAXN for the stated results.
- Treat NVIDIA results as candidate/performance evidence, not independent proof of fit for a user's device/application.
- Reproduce accepted workloads locally before assigning fit.

## Multimodal and Physical-AI Workloads

- Jetson is often used for VLM/VLA/robotics/vision/speech workloads where sensor processing competes with generative inference.
- Include camera ingestion, codecs, CUDA/VPI preprocessing, detection/tracking, VLM encoders, LLM/VLA reasoning, speech, control loops, and logging in the whole-system measurement.
- Do not reserve all memory/GPU compute for the language model when the device must also process sensors in real time.
- Measure deadline/jitter for the safety/control pipeline separately from generative throughput.
- Link physical-AI/robotics decision guidance when task design becomes primary.

## Video and Media Engines

- Treat hardware video encode/decode and ISP/media paths as distinct resources that can reduce CPU/GPU load but still consume memory/bandwidth.
- Verify codec/resolution/stream-count support for the exact Jetson generation.
- Include camera buffers and zero-copy pipelines in memory pressure.
- Do not infer vision-model throughput from media-engine capability alone.

## Multiple Models and Agents

- Measure concurrent resident models for embeddings, detection, VLM, LLM, speech, control, and agent tools.
- NVIDIA Jetson is explicitly positioned for multiple concurrent AI pipelines, but concurrency fit remains module/model-specific.
- Record per-model memory/cache and p50/p95 latency under actual concurrency.
- Avoid summing standalone benchmark throughput as if all models can run concurrently without contention.
- Define model unload/scheduling when memory cannot hold the whole portfolio.

## MIG and Isolation

- Current JetPack 7 advertises Multi-Instance GPU support in the current Jetson stack; verify exact Thor/Orin hardware/software eligibility before using it.
- Treat MIG as an isolation/resource-partition route, not extra compute.
- Measure partition sizing, supported workloads, memory allocation, and inter-service contention.
- Do not claim MIG on a Jetson SKU solely because JetPack 7 contains MIG-capable software.

## Containers and Jetson Platform Services

- Record container architecture/base, NVIDIA Container Runtime/toolkit integration, device permissions, camera/device mounts, and JetPack compatibility.
- Current JetPack 6/7 can support cloud-native/Jetson Platform Services patterns, but service availability differs by release/module.
- Do not use an x86 NGC container without a current aarch64/Jetson build.
- Keep container startup/storage and OTA/update behavior in operational fit.

## Software Lifecycle and JetPack Archive

- Use the current Jetson Linux archive/support matrix to verify which Jetson Linux releases support the exact module.
- Current August 2026 archive shows current 39.x Jetson Linux support across Thor and Orin families, while 36.x remains an Orin line.
- Treat BSP/JetPack upgrades as compatibility changes requiring runtime/model regression tests.
- Avoid keeping an old JetPack solely because one model environment works if the platform is outside accepted security/support lifecycle; make the trade-off explicit.
- Preserve rollback/recovery procedure for production edge devices.

## Storage and Model Assets

- Include internal NVMe/eMMC/SD or attached storage performance/capacity, containers, engines, model weights, quantization variants, caches, datasets, logs, and OTA update headroom.
- A large model can fit memory but create impractical boot/load/update/storage pressure.
- Preserve artifact versions/checksums and local/offline availability where network independence matters.
- Do not use microSD/storage paging as a normal substitute for insufficient memory.

## ARM64 Ecosystem Constraints

- Verify all non-NVIDIA dependencies on aarch64: databases/vector stores, browser automation, robotics middleware, audio libraries, Python native extensions, package managers, and agent tools.
- Source availability is not the same as stable aarch64 package support.
- Record source-build patches/toolchains when they become part of the deployment.
- Keep a missing critical dependency as a route blocker even when the model itself benchmarks well.

## Offline and Edge Reliability

- Test operation with network unavailable when edge/offline capability is required.
- Prestage containers/models/packages and avoid hidden model-hub/runtime downloads.
- Define degraded behavior if the generative model fails while safety/robot/control functions must continue.
- Keep critical deterministic/control loops operable independently from optional LLM/VLM services where consequence requires it.

## Prompt Injection and Physical Actions

- Treat camera OCR/signs, web/docs, voice, messages, files, sensor metadata, and tool results as untrusted when an agent can act on the physical world.
- Do not allow VLM/LLM output to bypass deterministic safety interlocks.
- Use least privilege, sandboxing, explicit tool/action boundaries, confirmation/approval where needed, and local audit.
- A local Jetson model does not authorize machinery/robot/network actions.

## Quality and Quantization

- Evaluate the exact optimized/quantized artifact against an accepted reference.
- Current Thor Blackwell can expose new low-precision paths such as FP4 in supported runtimes; Orin precision support differs.
- Do not transfer FP4 speed/quality behavior to Orin or unsupported models.
- Track retries/correction/safety failures with performance.
- A faster lower-precision model that fails the task-quality threshold does not fit.

## Practical Fit Outcomes

- `Fits well`: exact module/JetPack/runtime/artifact/context/concurrency/power/cooling workload passes support, shared-memory headroom, quality, latency, sustained thermals, and application deadlines.
- `Fits conditionally`: requires a specific JetPack generation, lower precision, reduced context/concurrency, MAXN/higher cooling, selective model loading, or another explicit acceptable constraint.
- `Does not fit`: exact route fails software support, memory, latency, quality, thermal/power, ARM64 dependency, or edge-reliability thresholds.
- `Unknown`: exact module/JetPack/runtime/model combination lacks current support or measurement.
- Do not assign fit from TOPS, installed memory, or generic `Jetson` branding alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when fixed Jetson hardware cannot meet reasoning/model/context requirements and connectivity/data policy permits it.
- Keep low-latency/safety/local sensor processing on-device when cloud round trips are inappropriate.
- Compare network availability/cost, local power, model storage, engineering effort, retries, and accepted-result quality.
- Do not turn this route into advice to buy a larger Jetson module.

## Canonical Links

- Link exact model facts to Model Reference and JetPack/TensorRT/vLLM/llama.cpp software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first selection.
- Link robotics/physical-AI user/decision guidance when the workload rather than hardware fit becomes primary.
- Keep desktop NVIDIA and server/datacenter NVIDIA routes separate.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current NVIDIA JetPack 7/7.2 documentation, current Jetson Linux 39.2.1/36.5.2 archive matrix, current Jetson module/developer-kit specifications, current Jetson generative-AI benchmark/AI Lab material, and current NVIDIA runtime support matrices.
- Current evidence establishes JetPack 7 support across current Thor and Orin platforms, separate sustaining JetPack 6 Orin paths, Thor SBSA/CUDA 13-era differences, shared-memory/power-mode constraints, and current generative-AI benchmark routes. Provider benchmarks remain configuration-specific rather than universal model-fit proof.
- JetPack/Jetson Linux, CUDA/TensorRT/vLLM/containers, supported models/precisions, module power modes, and ARM64 package availability are mutable; recheck them before rendering recommendations.
- Exact module/BSP/runtime/artifact/context/concurrency/power/cooling measurements and accepted-result quality remain the fit authority.

## Validation

- Exact Jetson module and JetPack/Jetson Linux generation are pinned.
- JetPack 6/7 and Thor/Orin assumptions are not silently transferred.
- Shared system memory is not labeled dedicated VRAM or treated as fully available.
- Desktop RTX/datacenter CUDA assumptions are not imported without aarch64/Jetson support evidence.
- DLA is not treated as a generic LLM accelerator.
- NVIDIA benchmark results retain model/context/concurrency/precision/runtime/MAXN conditions.
- Sensor/media/multi-model contention, power mode, sustained cooling, storage, and ARM64 dependencies are included.
- Physical-agent actions retain deterministic safety/tool boundaries.
- Hardware purchasing remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
