# Documentation Requirements

## Route Fit

- Cover existing AMD Instinct server/datacenter GPU hosts where local/self-hosted model inference is the intended workload and the installed accelerator topology is fixed.
- Require exact Instinct SKU/architecture/count/HBM per device, host CPU/RAM, ROCm/amdgpu/RCCL versions, serving/runtime stack, model artifact, precision/quantization, context/KV cache, parallelism topology, interconnect, concurrency, and service SLO before assigning fit.
- Keep Radeon/Ryzen client hardware in the computer route; Instinct compatibility must come from the current ROCm/runtime matrix for the exact server accelerator.
- Keep accelerator purchasing, rack/network design, and full HA architecture outside this route.

## Current Instinct Generations

- Treat MI300-class and MI350-class Instinct accelerators as related but materially different architecture/runtime targets.
- Current ROCm documentation identifies MI300X/MI325X as `gfx942` CDNA3-class devices and MI350X/MI355X as `gfx950` CDNA4-class devices with different HBM capacities and precision/kernel capabilities.
- Do not transfer MI350/MI355 FP4/AITER behavior to MI300/MI325 without explicit support.
- Do not transfer one Instinct SKU's benchmark or supported runtime/model combination to another merely because both are officially ROCm-supported.
- Pin exact GPU target (`gfx*`) where custom kernels/builds depend on it.

## Current ROCm Boundary

- Use the current ROCm compatibility matrix as the first authority for OS, driver, framework, and exact Instinct support.
- Current ROCm 7.14-era documentation supports current MI300/MI325/MI350/MI355 families and updates supported inference frameworks independently.
- Preserve ROCm version, kernel/OS, amdgpu driver, Python/framework/runtime image, and exact GPU target with every deployment claim.
- Do not infer current support from an older ROCm release that happened to list the same GPU.
- Keep unsupported or unlisted exact combinations `Unknown`.

## Current Serving Routes

- Separate at least:
  - AMD-supported vLLM on ROCm;
  - SGLang on supported ROCm releases;
  - AMD ATOM/AITER-optimized serving where the exact GPU/model/backend is supported;
  - llama.cpp/HIP for supported compact or alternate artifact routes;
  - direct PyTorch/Transformers/model-specific engines when explicitly supported.
- Do not collapse these into generic `ROCm inference`.
- Preserve exact container/image/tag, runtime version, AITER/attention backend, model artifact, precision, and launch parameters.
- Current ROCm releases can change supported vLLM/SGLang/PyTorch versions; recheck before rendering recommendations.

## vLLM on ROCm

- Treat AMD's current vLLM documentation as a hardware/runtime-specific route rather than assuming upstream CUDA behavior carries over unchanged.
- Current AMD guidance covers MI300X, MI325X, MI350X, and MI355X with ROCm-specific attention, AITER, RCCL, quantization, and parallelism tuning.
- Preserve vLLM version and whether the deployment uses upstream ROCm support, AMD-published container/wheel, or another build.
- Do not use NVIDIA/CUDA-specific vLLM flags/kernels as evidence for ROCm support.
- Reproduce the complete workload on the selected Instinct SKU before assigning fit.

## ATOM / AITER Boundary

- Treat AMD ATOM as a separate current LLM serving engine/plugin path built around AITER kernels, not as a synonym for vLLM.
- Current ATOM documentation exposes an OpenAI-compatible server and a vLLM-plugin backend for selected Instinct devices.
- Preserve exact ATOM/AITER/vLLM/ROCm image versions and supported GPU/model matrix.
- Do not assume ATOM supports every model supported by ordinary vLLM, or vice versa.
- Keep experimental/new ATOM paths conditional until the exact production workload is validated.

## AITER and Attention Backend Selection

- Record whether AITER is enabled and which attention/MoE/GEMM backend actually executes the model.
- Current AMD vLLM guidance exposes AITER MHA/MLA/unified-attention, ROCm attention, Triton fallbacks, and model/shape-specific behavior.
- Do not assume the nominally fastest backend supports every head size/model architecture.
- Preserve fallback behavior because an unsupported optimized kernel can materially change decode latency.
- Benchmark the selected backend under the intended context and concurrency.

## Precision and Quantization

- Record BF16/FP16/FP8/FP4/MXFP4/AWQ/other exact quantization and its implementation.
- Current AMD vLLM guidance supports multiple FP8/FP4 routes across current Instinct families, but specific AITER FP4 kernels require MI350X/MI355X-class hardware.
- Do not infer FP4 acceleration from generic ROCm or Instinct branding.
- Preserve Quark/llm-compressor/other quantization tool, model revision, calibration, and runtime backend.
- Validate accepted-result quality after every precision/quantization transformation.

## HBM Is a Per-Device Working Set

- Account for weights, KV/cache, runtime/AITER workspaces, communication buffers, attention/temp tensors, multimodal encoders, adapters, speculative decoding, batch/concurrency, and allocator fragmentation.
- Reserve operational HBM headroom; do not plan service operation at nominal maximum capacity.
- Current MI300X/MI325X/MI350X/MI355X have materially different HBM capacities; use exact current device specifications rather than family averages.
- Do not sum HBM across accelerators without a supported sharding/parallelism topology.
- Track memory per rank/device as well as aggregate memory.

## KV Cache and Context

- Record configured max model length, actual input/output distributions, concurrency, KV dtype, prefix-cache behavior, and GPU memory-utilization settings.
- Current AMD vLLM guidance explicitly treats GPU memory utilization/KV-cache allocation as a throughput/concurrency tuning variable.
- Measure short and long context separately.
- Do not present advertised model context as simultaneously serviceable context under production concurrency without KV evidence.
- Reduced-context fit remains conditional fit.

## Single-GPU vs Multi-GPU

- Prefer the simplest topology that meets the workload; a model that fits one high-memory Instinct GPU can avoid communication overhead compared with unnecessarily spanning devices.
- Current AMD performance guidance notes that multiple independent single-GPU instances can outperform one instance stretched across all GPUs for smaller models.
- Use tensor/pipeline/data/expert parallelism only when the model/workload requires it and the runtime supports it.
- Do not assume `TP=N` is automatically faster than independent replicas.
- Measure both capacity and accepted service throughput for realistic traffic.

## Parallelism Is Part of Compatibility

- Record tensor parallelism, pipeline parallelism, data parallelism, expert parallelism, and any disaggregated serving topology explicitly.
- Preserve model-specific constraints for MoE, MLA, speculative decoding, and multimodal workloads.
- A topology that starts does not prove efficient RCCL communication or acceptable tail latency.
- Keep unsupported parallelism combinations `Unknown`.
- Do not infer linear throughput/capacity scaling from GPU count.

## RCCL and Fabric

- Treat RCCL/fabric/NUMA topology as part of multi-GPU and multi-node model fit.
- Record XGMI/Infinity Fabric/PCIe/NIC topology, RCCL version, channel/tuning settings where material, and CPU/NIC locality.
- Current RCCL documentation includes release/GPU-specific channel behavior for MI350X/MI355X multi-node workloads, demonstrating that communication defaults can change across ROCm releases.
- Preserve the actual RCCL tuning used in benchmarks rather than comparing results with hidden defaults.
- Revalidate collective performance after ROCm/RCCL updates.

## Multi-Node Serving

- Treat multi-node inference as a separate deployment route with explicit node/GPU/fabric/orchestration constraints.
- Record nodes, GPUs/node, RDMA/fabric, runtime/Ray or scheduler, TP/PP/DP/EP strategy, model placement, and recovery behavior.
- Benchmark cross-node communication, startup, warm-up, failure/rejoin, and p95/p99 service latency.
- Do not infer multi-node support from successful single-node vLLM inference.
- Keep network/cluster architecture ownership outside this model-selection page while representing topology as a fixed constraint.

## MoE Models

- Record total and active parameters, expert count, routing, expert-parallel topology, all-to-all communication, and memory placement.
- Current AITER/vLLM ROCm routes include optimized MoE kernels for selected current model families, but kernel activation/support remains model and release specific.
- Do not generalize one DeepSeek/Qwen/Mixtral/Kimi-class example to arbitrary MoE checkpoints.
- Measure expert imbalance and RCCL/fabric pressure.
- Keep unsupported kernels/topologies `Unknown`.

## Multimodal and Media Models

- Include encoders/decoders/preprocessing, vision/audio/video tensors, media transfer, and runtime support for the exact architecture.
- Verify ROCm kernels/runtime support for every material component rather than only the language backbone.
- Measure full request latency and HBM under realistic media sizes/concurrency.
- Do not reuse text-only LLM benchmark results for VLM/diffusion/media routes.
- Preserve CPU or alternate-backend fallback where components are unsupported.

## Multi-Model Serving

- Measure combined resident weights, KV/cache, adapters, scheduler isolation, and model load/eviction behavior when several services share the node.
- Compare independent GPU replicas, static partitioning, and supported multi-model serving rather than forcing one stretched topology.
- Preserve per-model/tenant SLOs and admission limits.
- Do not overcommit HBM so model reload or host offload dominates latency unless explicitly acceptable.

## GPU Partitioning / Virtualization

- Treat SR-IOV/compute/memory partition modes as explicit resource topologies.
- Current ROCm releases add/expand partitioning support on current MI350-class accelerators; exact modes and runtime behavior are release-specific.
- Verify the selected partition exposes the required HBM/compute/runtime features.
- Do not reuse full-GPU benchmark numbers for a partitioned virtual function.
- Measure isolation, concurrency, communication, and service latency on the actual partition.

## Host CPU, RAM, NUMA, and Storage

- Account for tokenization, preprocessing, retrieval, request handling, pinned host memory, model loading, observability, and CPU fallback.
- Record NUMA locality between CPU sockets, GPUs, NICs, and NVMe.
- Include current+rollback model artifacts, containers, compiled/tuned kernels, and caches in local storage planning.
- Do not treat HBM as the only capacity constraint.
- Verify cold-start/warm-up behavior from the actual storage path.

## Container and Dependency Discipline

- Prefer current AMD-published/validated containers where they materially reduce ROCm/PyTorch/vLLM/AITER dependency ambiguity.
- Pin image digest/tag, ROCm, PyTorch, vLLM/SGLang/ATOM/AITER, Python, and model tooling.
- Current AMD documentation warns that dependency resolution can pull incompatible transitive versions; preserve a reproducible environment.
- Revalidate after container/runtime updates rather than mutating production images in place.
- Record deviations from supported matrices.

## Offline / Controlled Environments

- Prestage models, containers, ROCm/runtime packages, tuned artifacts, and dependencies when outbound access is restricted.
- Verify startup and steady-state with denied egress.
- Preserve artifact hashes/signatures and exact runtime versions across transfer.
- Avoid hidden model-hub/package downloads during service startup.
- Link high-security operational controls to the scenario owner while keeping hardware/runtime compatibility here.

## Serving API Security

- Treat vLLM/ATOM/SGLang/OpenAI-compatible endpoints as network services requiring authentication, TLS where applicable, authorization, rate/size limits, tenant separation, and audit.
- Do not expose an unauthenticated endpoint merely because it is inside the datacenter.
- Keep model-server access separate from agent/tool execution authority.
- Minimize sensitive prompt/output logging.
- Separate deployment/admin permissions from inference-client permissions.

## Observability

- Monitor HBM/utilization, power/thermals, clocks, XGMI/fabric/RCCL traffic, KV/cache, queue depth, TTFT/ITL, request/token throughput, OOM/errors, and exact model/runtime version.
- Use service-level latency/throughput metrics rather than accelerator utilization alone.
- Preserve p50/p95/p99 and representative concurrency.
- Treat repeated kernel fallback, OOM, process restart, or long warm-up as practical-fit signals.
- Include monitoring overhead in capacity measurements.

## Reliability and Upgrade Behavior

- Test runtime/container restart, GPU/reset/failure behavior, model reload, RCCL/fabric failure, node loss where applicable, cache warm-up, and rollback.
- Treat ROCm/runtime upgrade as a compatibility event because kernels, attention backends, RCCL defaults, and supported frameworks can change.
- Preserve a known-good rollback tuple of ROCm + container/runtime + model/artifact + launch settings.
- Do not call a topology production-fit because one benchmark succeeds.

## Benchmark Contract

- Record at minimum:
  - exact Instinct SKU/count/architecture/HBM/topology;
  - host CPU/RAM/NUMA/storage;
  - ROCm/amdgpu/RCCL;
  - container/runtime/AITER/attention backend;
  - model/artifact/precision/quantization;
  - context/input/output distribution;
  - TP/PP/DP/EP topology;
  - concurrency/batching/scheduler settings;
  - cold/warm state.
- Measure TTFT, inter-token/decode latency, total request latency, input/output/total token throughput, peak HBM, host RAM, GPU/fabric utilization, power where material, and accepted-result quality.
- Do not compare benchmark numbers that differ in model/context/precision/topology/concurrency without normalizing the conditions.

## Accepted-Result Quality

- Evaluate the exact served/quantized artifact against representative task acceptance criteria.
- Track retries, corrections, refusals, structured/tool-call accuracy, multimodal quality, and failure severity.
- Provider statements such as `minimal accuracy loss` for a quantization method remain provider evidence until the target workload is validated.
- Optimize cost/throughput per accepted result, not raw tokens/s alone.

## Practical Fit Outcomes

- `Fits well`: exact Instinct/ROCm/runtime/backend/model/precision/context/topology/concurrency passes current support, HBM/KV headroom, TTFT/ITL/throughput, accepted quality, and sustained reliability targets.
- `Fits conditionally`: requires a specific ROCm/container/backend, alternate attention kernel, reduced context/concurrency, supported quantization, particular multi-GPU topology, partition mode, or another accepted constraint.
- `Does not fit`: exact route fails hardware/runtime/model support, memory, communication, latency/throughput, quality, or reliability requirements.
- `Unknown`: exact GPU/ROCm/runtime/model/topology lacks current support or measurement.
- Do not assign fit from aggregate HBM, Instinct family name, GPU count, TOPS/TFLOPS, or load success alone.

## Hosted / Other Existing Compute Escalation

- Preserve hosted/API, another existing accelerator pool, CPU serving, or hybrid routing when the fixed Instinct fleet cannot meet model/context/SLO requirements.
- Compare local power/operations/tuning/idle capacity and human correction against hosted accepted-result economics.
- Do not turn this route into accelerator procurement advice; expose the exact support/resource/topology gap.

## Canonical Links

- Link exact model facts to Model Reference and ROCm/vLLM/SGLang/ATOM/AITER/RCCL software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Keep Radeon/Ryzen client hardware in `computers/amd/`.
- Link internal-AI-platform/high-security/organization scenarios when service operations or governance becomes primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current ROCm 7.14 compatibility/release documentation, current AMD Instinct GPU specifications, current AMD vLLM inference/optimization guidance for MI300X/MI325X/MI350X/MI355X, current AITER/ATOM serving documentation, and current RCCL multi-GPU/multi-node guidance.
- Current evidence establishes distinct CDNA3/CDNA4 Instinct targets, exact ROCm/framework matrices, current vLLM/SGLang and ATOM/AITER serving routes, model/backend-specific FP8/FP4 behavior, and release-specific RCCL/parallelism tuning. These do not establish practical fit for arbitrary model/topology combinations.
- ROCm/amdgpu/RCCL, vLLM/SGLang/ATOM/AITER, supported GPUs/models/precisions, attention kernels, partition modes, and model artifacts are mutable; recheck them before rendering recommendations.
- Exact Instinct/ROCm/runtime/artifact/context/topology/concurrency measurement and accepted-result quality remain the fit authority.

## Validation

- Exact Instinct SKU/architecture/count/HBM/topology, ROCm/amdgpu/RCCL, runtime/backend, model artifact/precision, context, and concurrency are pinned.
- Instinct and Radeon/Ryzen client support boundaries remain separate.
- MI300/MI325 and MI350/MI355 precision/kernel assumptions are not silently transferred.
- vLLM, SGLang, ATOM/AITER, llama.cpp, and direct framework routes remain distinct.
- Multi-GPU/multi-node fit follows supported parallelism and RCCL topology rather than aggregate HBM arithmetic.
- KV/cache, prefill/decode, attention fallback, batching/concurrency, host NUMA/resources, fabric, and service tail latency are measured.
- Quantization/provider benchmarks do not replace accepted-result quality measurement.
- Hardware acquisition remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
