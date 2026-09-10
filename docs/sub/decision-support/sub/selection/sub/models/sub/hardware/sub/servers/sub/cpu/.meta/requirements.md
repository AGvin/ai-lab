# Documentation Requirements

## Route Fit

- Cover existing dedicated CPU-server inference where no GPU/NPU/HPU accelerator is the intended execution path.
- Require exact CPU architecture/microarchitecture, sockets/NUMA topology, ISA flags, physical cores/threads, memory channels/capacity/bandwidth per NUMA node, OS, runtime/backend/build, model artifact/quantization, context/KV cache, batch/concurrency, and service SLO before assigning fit.
- Keep desktop CPU use in `computers/cpu/`; this route owns multi-socket/NUMA/service-serving constraints.
- Keep accelerator/CPU purchasing outside this route. Existing server resources are fixed constraints.

## Current CPU Runtime Routes

- Separate at least:
  - vLLM CPU backend for supported x86/Arm/other current architectures;
  - `llama.cpp`/GGUF CPU serving;
  - OpenVINO GenAI/OpenVINO Model Server for supported Intel CPU/model routes;
  - ONNX Runtime/oneDNN/BLAS/model-specific optimized engines where current support justifies them.
- Do not preserve one permanent CPU runtime default; choose by exact CPU ISA, model/artifact, service pattern, and measured accepted result.
- Record exact runtime/build/container version and CPU feature detection.
- Keep unsupported model/runtime/ISA combinations `Unknown`.

## Exact CPU Architecture and ISA

- Record x86-64, AArch64, IBM Z/s390x, or another supported architecture and exact instruction capabilities.
- Current vLLM CPU documentation supports Intel/AMD x86 and Arm AArch64 as current server-capable CPU paths, with current x86 guidance recommending AVX-512 and treating AVX2 as limited-feature support.
- Current `llama.cpp` supports x86 AVX/AVX2/AVX512/AMX and Arm NEON/SVE-class paths, plus other architectures according to its current feature matrix.
- Do not infer optimized-kernel availability from `x86-64` or `ARM64` alone.
- Pin the binary/build so it actually contains the intended ISA kernels.

## Vendor / Generation-Specific CPU Paths

- Keep vendor/generation assumptions explicit when the runtime has optimized paths.
- Current vLLM CPU documentation notes that its AMD x86 path requiring AVX-512 targets Zen 4/Genoa-class or newer CPUs for that route and exposes a Zen-optimized build target.
- Intel Xeon generations with AVX-512/AMX can have materially different OpenVINO/oneDNN/vLLM kernel behavior from older Xeons.
- Do not transfer a benchmark from one Xeon/EPYC generation to another solely by core count.
- Keep unmeasured older-generation or alternate-ISA behavior `Unknown`.

## NUMA Is Part of Model Fit

- On multi-socket servers, treat NUMA node memory and CPU locality as first-class model resources.
- Record socket count, NUMA nodes, cores per node, local memory per node, memory interleaving policy, process/thread affinity, and model/KV placement.
- Current vLLM CPU guidance explicitly treats each NUMA node as a TP/PP rank when multi-socket NUMA is used for tensor/pipeline parallel CPU serving.
- Keep each rank's CPU threads and memory allocations local to its NUMA node where the runtime requires it.
- Do not use total system RAM as one flat pool when the runtime/rank incurs remote-NUMA access.

## Per-NUMA Weight and KV Budget

- Calculate memory per serving rank/node, not only per server.
- Current vLLM CPU guidance defines each TP rank's memory as its weight shard plus configured CPU KV-cache space and warns that exceeding a NUMA node's capacity can terminate the worker.
- Include runtime buffers, allocator overhead, tokenizer/preprocessing, OS/services, and other co-resident applications in the local-node budget.
- Reserve headroom for traffic/context variance.
- A server with enough aggregate RAM but insufficient local-node memory does not fit that topology.

## Memory Bandwidth, Not Capacity Alone

- Treat CPU LLM decode as frequently memory-bandwidth-sensitive and measure effective bandwidth under the actual model/runtime/thread topology.
- Record memory channels populated, DIMM topology/speed, NUMA locality, and concurrent memory consumers where material.
- Do not publish universal `RAM → model size` or `core count → tokens/s` tables.
- A model can fit easily in RAM and still miss service latency/throughput because memory bandwidth is the bottleneck.
- Measure prompt and decode separately because their compute/memory behavior differs.

## Threading and Affinity

- Record physical cores, SMT, thread count, OpenMP/threadpool settings, CPU affinity, NUMA binding, and process count.
- Do not assume all logical threads maximize throughput.
- Current vLLM CPU guidance exposes explicit OpenMP thread binding and requires tuning with NUMA locality.
- Current `llama.cpp` also exposes threadpool/NUMA strategies and warns through its implementation/support surface that topology matters.
- Benchmark thread counts for both latency and throughput rather than using `nproc` blindly.

## vLLM CPU Boundary

- Treat vLLM CPU as its own backend with CPU-specific installation, ISA, NUMA, KV-cache, and batching constraints.
- Current x86 support covers FP32/FP16/BF16 basic inference/serving with AVX-512 recommended; feature/quantization support varies by architecture.
- Preserve exact vLLM version/build and CPU wheel/container variant.
- Do not transfer CUDA/ROCm vLLM kernel/precision/parallelism assumptions to CPU.
- Recheck the current CPU backend before making model/quantization feature claims.

## vLLM CPU KV Cache

- Record `VLLM_CPU_KVCACHE_SPACE` or current equivalent per rank/node when vLLM CPU is used.
- Larger KV space can enable longer context or more concurrent requests but consumes local NUMA memory.
- Measure actual average/p95 context and concurrency rather than maximizing cache blindly.
- Keep KV cache separate from weight and OS/application memory.
- Treat worker OOM/exit due to local-node memory as a practical fit failure.

## CPU Tensor / Pipeline Parallelism

- Use CPU TP/PP only when the runtime/topology supports it and measurement shows benefit or necessity.
- Current vLLM NUMA guidance maps ranks to NUMA nodes; preserve exact rank/core/memory binding.
- Do not assume splitting a model across sockets increases throughput; remote communication and memory access can reduce performance.
- Compare one-process-per-node/replica versus sharded topology where the model fits locally.
- Preserve topology in every benchmark.

## `llama.cpp` Route

- Treat `llama.cpp` as a mature cross-platform CPU/GGUF route with extensive quantization and ISA support.
- Pin exact commit/release, GGUF model/revision/quantization, build flags, NUMA strategy, thread counts, context, batch, and server settings.
- Current CPU backend exposes NUMA strategies including disabled/distribute/isolate/numactl/mirror; benchmark the mode appropriate to the server.
- Do not assume the same GGUF quantization has equal performance across AVX2/AVX512/AMX/NEON CPUs.
- Evaluate quantized artifact quality independently from memory/speed.

## OpenVINO GenAI Route

- Treat OpenVINO GenAI/OpenVINO Model Server as an Intel-oriented CPU serving route when the exact model/export/CPU generation is supported.
- Current OpenVINO GenAI supports CPU `LLMPipeline`, weight-compressed INT4 exports, streaming, speculative decoding, and scheduler/continuous-batching configuration.
- Preserve OpenVINO/GenAI/Optimum-Intel version, source model, exported artifact, weight format, CPU generation, thread/NUMA settings, and scheduler configuration.
- Do not generalize Intel-optimized OpenVINO performance to AMD/Arm CPU servers.
- Validate task quality after conversion/compression.

## Model Artifact and Quantization

- Record exact model producer/revision, runtime-native artifact, quantization/weight compression, tokenizer, adapters, and conversion tool.
- CPU-friendly GGUF, OpenVINO INT4/INT8, AWQ/GPTQ/compressed-tensors or another format can have very different kernel support by runtime/ISA.
- Do not infer performance or quality from nominal bits per weight alone.
- Preserve source→converted artifact provenance and hashes.
- Keep unsupported quantization/runtime combinations `Unknown`.

## Prompt Processing vs Decode

- Measure prompt/prefill throughput separately from autoregressive decode/inter-token latency.
- CPU prompt processing can scale differently with cores/batch than decode, which can be bandwidth-bound.
- Report TTFT, inter-token latency, and total request latency for interactive service.
- Do not optimize prompt throughput while ignoring unusable decode speed.
- Preserve representative input/output lengths.

## Batching and Concurrency

- Tune batch size and scheduler against the service objective.
- Current vLLM CPU guidance notes larger batches can raise throughput while smaller batches can improve latency.
- Measure request mix, arrival rate, queueing, p50/p95/p99 latency, and throughput at accepted quality.
- Do not extrapolate one offline batch benchmark into production concurrency.
- Define admission/backpressure behavior for overload.

## Continuous Batching

- Use continuous batching only when supported by the selected runtime/model and it materially improves the workload.
- Current OpenVINO GenAI exposes scheduler configuration for continuous batching; vLLM provides its own scheduler/batching semantics.
- Preserve scheduler/block/cache/batch settings with benchmark evidence.
- Measure tail latency as concurrency rises.
- Do not assume the same batching configuration is optimal across models or CPU generations.

## Context and KV Growth

- Record configured model length, actual input/output distributions, KV dtype/implementation, per-session cache growth, and concurrency.
- Do not advertise the base model's maximum context as serviceable at target concurrency unless memory/latency are measured.
- Long context increases RAM and prefill latency even when weights fit comfortably.
- Measure short/long context separately.
- Reduced context remains an explicit conditional fit.

## Speculative Decoding

- Treat speculative decoding as an optional route with a second draft model or current runtime-specific mechanism.
- Current OpenVINO GenAI and other CPU runtimes expose speculative decoding support for selected paths.
- Measure additional memory, draft-model latency, acceptance rate, TTFT/decode improvement, and quality stability.
- Do not assume it improves every CPU/model/workload.
- Preserve both target and draft artifact/version.

## MoE Models

- Record total/active parameters, expert count, memory residency, expert routing, thread/NUMA placement, and runtime kernel support.
- Active parameter count alone does not determine memory footprint or memory bandwidth.
- Measure expert/router overhead and NUMA traffic.
- Keep unsupported MoE architectures/quantizations `Unknown`.
- Compare accepted service performance against a smaller dense alternative when practical.

## Multimodal / Media Workloads

- Include image/audio/video preprocessing, encoders, projectors, decoders, media libraries, and memory copies in CPU resource budgets.
- Do not infer VLM/media performance from text LLM tokens/s.
- Verify exact model/runtime support for all components.
- Measure end-to-end request latency and concurrency with representative media sizes.
- Escalate to an existing accelerator/hosted route when CPU media latency is unacceptable.

## Host Service Overhead

- Account for API/reverse proxy, TLS, tokenization, retrieval/vector/database access, observability, logging, model download/load, decompression, and application logic.
- These workloads compete for the same CPU cores/memory bandwidth as inference.
- Reserve cores/RAM for OS/service functions rather than assigning every logical CPU to the model.
- Measure with the actual service stack active.
- Do not use a bare benchmark process as the only production fit evidence.

## Storage and Model Loading

- Include current/rollback model artifacts, quantized variants, container/runtime images, caches, indexes, and logs.
- Measure cold model load and page-cache warm behavior from actual NVMe/storage.
- mmap/page-cache behavior can change apparent RAM use and first-request latency.
- Do not use swap as ordinary capacity expansion for latency-sensitive serving.
- Preserve offline artifact staging when internet-independent service is required.

## Power and TCO

- Measure package/system power where CPU serving runs continuously or competes economically with hosted/accelerated alternatives.
- Include sockets, memory channels/DIMMs, cooling, idle capacity, and service utilization.
- Compare cost per accepted result/request at required SLO, not only hardware already-owned sunk cost.
- A CPU route can be operationally attractive for compact/private workloads even when accelerator raw throughput is higher.
- Escalation remains valid when energy/latency economics are poor.

## Offline / Controlled Environments

- Prestage model/runtime/container/package artifacts and verify no hidden downloads are required after startup.
- Preserve hashes/signatures/version provenance.
- Disable/route telemetry according to the environment.
- Verify service restart and model loading fully offline.
- Link high-security operational controls to the relevant scenario owner.

## Serving API Security

- Treat vLLM/llama-server/OpenVINO Model Server/OpenAI-compatible endpoints as network services requiring authentication, TLS where applicable, authorization, rate/size limits, audit, and tenant isolation.
- Do not expose unauthenticated CPU inference merely because it runs on an internal server.
- Keep model-server access separate from agent/tool authority.
- Minimize sensitive prompt/output logging.
- Separate admin/deployment privileges from inference clients.

## Observability

- Monitor per-socket/core utilization, memory bandwidth where available, NUMA local/remote traffic, RAM/KV use, queue depth, TTFT/ITL, throughput, page faults/swap, power/thermals, and exact model/runtime version.
- Use p50/p95/p99 service metrics rather than CPU utilization alone.
- Detect thread migration, remote NUMA traffic, OOM, swapping, repeated model reload, or thermal/power throttling as practical-fit signals.
- Include observability overhead in capacity testing.

## Reliability and Upgrade Behavior

- Test process/container restart, cold/warm model load, NUMA/rank failure behavior, OOM, service overload, runtime/model upgrade, and rollback.
- Treat runtime/compiler/model conversion changes as behavior/performance changes.
- Preserve a known-good runtime/build/artifact/thread/NUMA configuration.
- Do not call a CPU route production-fit because one benchmark succeeds.
- Define hosted/accelerated fallback if service SLO cannot be maintained.

## Benchmark Contract

- Record at minimum:
  - CPU vendor/model/generation/ISA;
  - sockets/NUMA nodes/cores/SMT;
  - memory channels/capacity/bandwidth per node;
  - OS/kernel/runtime/build/container;
  - model/artifact/quantization;
  - context/input/output distribution;
  - thread/affinity/NUMA/rank configuration;
  - KV cache per rank;
  - batch/concurrency/scheduler;
  - cold/warm state.
- Measure TTFT/prefill, inter-token/decode, total request latency, throughput, peak/local RAM, memory bandwidth/NUMA behavior, CPU utilization, power where material, and accepted-result quality.
- Do not compare results that differ in ISA/thread/NUMA/model/context/batch conditions as equivalent.

## Accepted-Result Quality

- Evaluate the exact quantized/converted artifact on representative tasks.
- Track retries, corrections, refusals, structured/tool-call accuracy, and failure severity.
- A compact CPU model can be the best route when its accepted-result latency/quality is better than a larger model that technically fits RAM.
- Optimize cost and latency per accepted result rather than raw tokens/s alone.

## Practical Fit Outcomes

- `Fits well`: exact CPU/NUMA/runtime/artifact/context/batch/concurrency passes current support, local-node memory/KV headroom, TTFT/ITL/throughput, accepted quality, and sustained service targets.
- `Fits conditionally`: requires a specific ISA-optimized runtime/build, NUMA binding, lower quantization, reduced context/concurrency, batch-only use, or another explicit accepted constraint.
- `Does not fit`: exact route fails runtime/ISA support, local memory/bandwidth, latency/throughput, quality, power, or reliability requirements.
- `Unknown`: exact CPU/runtime/artifact/topology lacks current support or measurement.
- Do not assign fit from total RAM, socket/core count, parameter count, or load success alone.

## Accelerator / Hosted Escalation

- Preserve another existing GPU/HPU/NPU pool, hosted/API, rented capacity, or hybrid routing when CPU serving cannot meet accepted SLO/quality/economics.
- Keep CPU-local execution for privacy/offline/bounded workloads when it meets acceptance.
- Do not turn this route into accelerator purchasing advice; expose the measured capability/resource gap.

## Canonical Links

- Link exact model facts to Model Reference and vLLM/llama.cpp/OpenVINO GenAI/OVMS software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Keep personal/workstation CPU use in `computers/cpu/`.
- Link organization/internal-AI-platform/high-security scenarios when service operation or data boundary dominates.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current vLLM CPU installation/tuning documentation, current `llama.cpp` CPU/NUMA/ISA feature implementation and feature matrix, and current OpenVINO 2026 GenAI CPU/continuous-batching/quantized-LLM documentation.
- Current evidence establishes explicit x86/Arm CPU runtime boundaries, AVX-512/AVX2/NEON and NUMA requirements, per-NUMA rank/KV budgeting in vLLM, current llama.cpp NUMA/ISA support, and current OpenVINO CPU LLM/INT4/continuous-batching paths. It does not establish universal RAM/core/model tiers.
- vLLM CPU, llama.cpp, OpenVINO/GenAI/OVMS, CPU ISA kernels, quantization formats, NUMA behavior, and model support are mutable; recheck them before rendering recommendations.
- Exact CPU/NUMA/runtime/artifact/context/concurrency measurement and accepted-result quality remain the fit authority.

## Validation

- Exact CPU generation/ISA, sockets/NUMA, memory per node/bandwidth, runtime/build, artifact/quantization, context/KV, batching, and concurrency are pinned.
- Server CPU and desktop CPU routes remain separate.
- Aggregate system RAM is not treated as flat per-rank memory on NUMA systems.
- vLLM CPU, llama.cpp, OpenVINO, and other runtime support boundaries remain distinct.
- AVX-512/AMX/NEON/vendor-optimized assumptions are not transferred to unsupported CPUs.
- Prompt/decode, batching/tail latency, thread affinity, NUMA traffic, host service overhead, power, and accepted quality are measured.
- RAM/core count/parameter count/load success do not replace practical fit evidence.
- Hardware purchasing remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
