# Documentation Requirements

## Route Fit

- Cover existing Intel Gaudi 2 / Gaudi 3 server accelerator hosts where model inference/serving is the intended workload and the installed accelerator topology is fixed.
- Require exact Gaudi generation/SKU/count/HBM per device, host CPU/RAM, Intel Gaudi software/driver/firmware, serving/runtime stack, model artifact, precision/quantization, context/KV cache, tensor/data/expert parallel topology, networking, concurrency, and service SLO before assigning fit.
- Keep general Xeon CPU inference in sibling `cpu/` and Intel PC NPU/iGPU paths in `computers/intel/`.
- Keep accelerator purchasing and full cluster/network/HA architecture outside this route.

## Gaudi 2 and Gaudi 3 Are Distinct Targets

- Treat Gaudi 2 and Gaudi 3 as related but distinct compatibility/performance generations.
- Pin the exact accelerator generation in every model/runtime/benchmark claim.
- Do not transfer validated Gaudi 3 model/precision/plugin behavior to Gaudi 2 unless the current support matrix explicitly covers both.
- Do not transfer Gaudi 2-only examples/firmware assumptions to Gaudi 3.
- Preserve per-generation HBM/network/topology characteristics rather than using a generic `Gaudi` capacity number.

## Current Intel Gaudi Software Boundary

- Use the current Intel Gaudi support matrix as the authority for supported OS, kernel, Python, PyTorch, firmware, container, orchestration, and framework combinations.
- Current 1.24.1-era documentation supports Gaudi 2 and Gaudi 3 with specific OS/runtime combinations and an evolving upstream-plugin model for vLLM.
- Pin Intel Gaudi software version, driver, firmware/SPI firmware, container/PyTorch image, and exact accelerator generation.
- Current backward/forward compatibility rules constrain driver/container/firmware combinations; do not mix versions by intuition.
- Keep unsupported tuples `Unknown` until validated by the current matrix.

## Current Serving Routes

- Separate at least:
  - vLLM Hardware Plugin for Intel Gaudi;
  - older Intel/Habana-maintained vLLM fork paths when an existing deployment still uses them;
  - Optimum for Intel Gaudi / Transformers;
  - Text Generation Inference where supported;
  - direct PyTorch/model-specific inference routes.
- Do not describe these as one interchangeable `SynapseAI` serving stack.
- Prefer the current upstream-oriented vLLM Hardware Plugin for new current vLLM serving evaluations unless the exact model/runtime requirement points elsewhere.
- Preserve exact runtime/plugin/container versions and model support evidence.

## vLLM Hardware Plugin Compatibility Matrix

- Treat the current vLLM Gaudi compatibility matrix as an exact version-pair contract.
- Current documentation identifies vLLM **0.26.0** with Intel Gaudi software **1.24.1** as the latest validated pair at the 2026-08-24 evidence boundary.
- Earlier plugin releases map to different Gaudi software versions; a vLLM version that works with 1.23/1.24.0 is not automatically validated with 1.24.1.
- Pin both vLLM and Gaudi software/plugin versions in every deployment record.
- Recheck the matrix before upgrades rather than updating vLLM independently.

## Validated Model Matrix

- Use the current vLLM Gaudi `Validated Models` table as provider compatibility evidence for exact model + TP size + dtype + accelerator generation.
- Do not generalize from a family name such as Llama, Qwen, Gemma, DeepSeek, GPT-OSS, or Granite.
- A configuration not listed may work but remains unvalidated/`Unknown` until tested on the exact Gaudi generation/runtime.
- Preserve exact checkpoint/revision, tensor-parallel degree, dtype/quantization, and accelerator generation.
- Provider validation confirms functional support, not the user's accepted-result quality or service SLO.

## HBM Is Per Device and Per Rank

- Include weights, KV/cache, graph-compile/runtime buffers, attention/sampling tensors, communication buffers, multimodal encoders, adapters, speculative models, batching/concurrency, and allocator headroom.
- Track peak HBM per device/rank, not only aggregate host HBM.
- Do not sum HBM across Gaudi cards without a supported tensor/expert/pipeline topology.
- A model that fits weights but leaves insufficient KV/cache or service headroom does not fit the production workload.
- Preserve host RAM and pinned/shared-memory requirements separately.

## Tensor Parallelism and Device Count

- Treat tensor-parallel size as part of model compatibility and validation.
- Current validated-model tables explicitly attach supported TP sizes to named checkpoints.
- Do not assume any divisor of the installed card count is supported or efficient.
- Measure communication, graph compilation, memory distribution, and p95/p99 latency for the chosen TP degree.
- Independent replicas/data-parallel service can be preferable to stretching a smaller model across all HPUs; benchmark both when relevant.

## Expert Parallelism and MoE

- Record total/active parameters, expert count, expert-parallel topology, TP/EP interaction, calibration strategy, and inter-device traffic for MoE models.
- Current vLLM Gaudi releases add model-specific MoE/MLA support over time; do not infer arbitrary MoE compatibility from one validated family.
- Quantization calibration for MoE can require per-rank expert coverage/unification; preserve the exact workflow where used.
- Measure expert imbalance and network pressure.
- Keep unsupported EP/model combinations `Unknown`.

## Graph Compilation and Warm-Up

- Treat Gaudi graph compilation/warm-up as a service lifecycle cost rather than ignoring it after a hot benchmark.
- Record cold model load, graph compilation, warm-up, and steady-state latency separately.
- Current Gaudi/vLLM releases continue to optimize compile and multimodal warm-up behavior; version changes can materially alter startup time.
- Measure restart/scale-out behavior under operational conditions.
- A low steady-state latency does not compensate for unacceptable restart/warm-up if the service must recover quickly.

## Eager / torch.compile / Runtime Mode

- Preserve the actual PyTorch/Gaudi execution mode and compilation settings.
- Current Intel Gaudi software supports evolving public-PyTorch/`torch.compile` integration alongside Gaudi-specific runtime/lowering.
- Do not compare benchmarks across different eager/compiled/lazy paths without identifying the mode.
- Revalidate custom ops/kernels after PyTorch/Gaudi software upgrades.
- Keep unsupported custom extension/ABI combinations explicit.

## Precision and Quantization

- Record BF16/FP8/INT8/MXFP4/other exact precision/quantization and how it is implemented.
- Current vLLM Gaudi releases include evolving FP8, INT8, MXFP4, dynamic quantization, and model-specific optimized paths; support differs by model and accelerator generation.
- Do not infer a precision path from Gaudi hardware capability alone.
- Preserve Intel Neural Compressor/other calibration tool, dataset, scale generation, checkpoint revision, and runtime version.
- Validate accepted-result quality after quantization.

## KV Cache and Context

- Record configured max model length, actual input/output distribution, concurrency, KV-cache dtype/quantization, prefix caching, and any external/offloaded cache path.
- Current vLLM Gaudi releases evolve KV-cache, hybrid-model cache, LMCache/NIXL integration, and memory-defragmentation behavior.
- Do not present advertised model context as concurrently serviceable capacity without HBM/KV measurement.
- Benchmark short and long-context workloads separately.
- Reduced-context fit remains an explicit conditional constraint.

## Prefill and Decode

- Measure TTFT/prefill separately from inter-token/decode latency.
- Report p50/p95/p99 for interactive workloads and throughput under representative concurrent request mixes.
- Preserve batch/token scheduler settings and graph bucket/configuration that materially affect results.
- Do not use one offline tokens/s result as a production serving claim.
- Track queueing and overload behavior separately from model compute.

## Multimodal Models

- Include vision/audio encoders, media preprocessing, model-specific warm-up resolutions, projectors, decoders, and HBM impact.
- Current vLLM Gaudi releases add validated multimodal model families incrementally; verify the exact model and Gaudi generation.
- Do not assume a supported text backbone implies its VLM derivative is supported.
- Measure end-to-end media request latency and quality.
- Keep unsupported vision tower/operators `Unknown`.

## Networking and Scale-Out

- Treat Gaudi's integrated networking/RDMA path as a topology that must be configured and measured, not free linear scaling.
- Record HPU count, NIC topology, direct routing/switch fabric, libfabric/verbs configuration, OpenMPI/Ray/Slurm or other orchestration, and node count.
- Current Gaudi documentation has specific scale-out requirements for Gaudi 2/3 networking and Gaudi Direct/verbs.
- Verify ACS/hugepage/fork-safety/environment requirements where the selected multi-node stack needs them.
- Do not infer multi-node serving performance from a single-host TP benchmark.

## Multi-Node Serving

- Treat multi-node inference as a separate operational route.
- Record nodes, HPUs/node, TP/DP/EP topology, model placement, fabric, runtime version, launch/orchestration, and failure/recovery semantics.
- Measure cross-node communication, startup/compile, warm-up, tail latency, and throughput.
- Keep a single-node model marked `Unknown` for multi-node service until the exact topology is verified.
- Full cluster architecture ownership remains outside this model-selection page.

## Host CPU, RAM, NUMA, and Storage

- Include tokenization, preprocessing, request/API handling, retrieval, model loading, compilation cache, observability, and any CPU fallback.
- Record NUMA locality between CPU sockets, Gaudi cards/NICs, and NVMe when material.
- Include current+rollback containers/models/cache artifacts in storage capacity.
- Measure cold startup from the actual storage path.
- Do not treat HBM as the only resource constraint.

## Container / Driver / Firmware Discipline

- Prefer current validated Gaudi containers for reproducibility where possible.
- Pin image tag/digest, driver, Gaudi software, firmware, PyTorch, plugin/runtime, Python, and model tooling.
- Follow current driver/container/firmware compatibility rules; the driver generally must be at least as new as the container according to current support guidance.
- Do not upgrade only one layer of the stack without verifying the current matrix.
- Preserve a known-good rollback tuple.

## Offline / Controlled Environments

- Prestage containers, model artifacts, plugin/runtime packages, and dependencies for disconnected operation.
- Verify startup/steady-state without external model-hub/package downloads.
- Preserve hashes/signatures/version provenance.
- Keep remote telemetry/support access within the organization's approved boundary.
- Link full high-security controls to the relevant scenario owner.

## Serving API Security

- Treat vLLM/TGI/OpenAI-compatible endpoints as network services requiring authentication, reverse proxy/network controls, TLS where applicable, rate limits, request limits, tenant separation, and audit.
- Current vLLM Gaudi security guidance inherits upstream vLLM threat assumptions and explicitly recommends endpoint/network hardening.
- Do not expose development-mode services broadly.
- Keep model-server access separate from agent/tool authority.
- Minimize sensitive prompt/output logs.

## Observability

- Monitor HBM, HPU utilization, clocks/power/thermals, network/RDMA traffic, KV/cache, graph compilation/warm-up, queue depth, TTFT/ITL, request/token throughput, OOM/errors, and exact model/runtime versions.
- Use service-level metrics rather than accelerator utilization alone.
- Preserve p50/p95/p99 at representative concurrency.
- Detect repeated graph recompilation, OOM, warm-up regression, or communication errors as fit signals.
- Include observability overhead in capacity measurement.

## Reliability and Upgrade Behavior

- Test process/container restart, HPU/node failure, graph cache loss, model reload, scale-out failure, network failure, and rollback appropriate to the service.
- Treat Gaudi software/vLLM-plugin/PyTorch upgrades as compatibility events.
- Preserve a validated rollback image/runtime/model tuple.
- Do not call a topology production-fit because one hot benchmark succeeds.
- Define fallback/escalation when the fixed Gaudi fleet cannot meet availability/SLO requirements.

## Benchmark Contract

- Record at minimum:
  - Gaudi generation/SKU/count/topology;
  - host CPU/RAM/NUMA/storage;
  - Gaudi software/driver/firmware;
  - container/PyTorch/vLLM plugin or alternate runtime versions;
  - model/artifact/precision/quantization;
  - context/input/output distribution;
  - TP/DP/EP topology;
  - concurrency/batching/scheduler settings;
  - cold/compile/warm state.
- Measure TTFT, inter-token/decode latency, request latency, input/output/total throughput, peak HBM, host RAM, HPU/network utilization, compilation/warmup time, and accepted-result quality.
- Do not compare results across different model/TP/precision/context/runtime states as equivalent.

## Accepted-Result Quality

- Evaluate the exact served/quantized checkpoint on representative tasks.
- Track retries, corrections, refusals, structured/tool-call accuracy, multimodal quality, and failure severity.
- Provider validation means functional compatibility, not independent AI Lab quality endorsement.
- Optimize throughput/cost per accepted result rather than raw tokens/s alone.

## Practical Fit Outcomes

- `Fits well`: exact Gaudi generation/software/plugin/runtime/model/precision/context/topology/concurrency passes current support, HBM/KV headroom, TTFT/ITL/throughput, accepted quality, and sustained reliability targets.
- `Fits conditionally`: requires an exact validated plugin/software pair, particular TP/EP size, alternate quantization, reduced context/concurrency, compile/warm-up allowance, or another accepted constraint.
- `Does not fit`: exact route fails accelerator/runtime/model support, memory, networking, latency/throughput, quality, or reliability requirements.
- `Unknown`: exact Gaudi generation/runtime/model/topology lacks current validation or measurement.
- Do not assign fit from aggregate HBM, HPU count, Gaudi branding, theoretical throughput, or load success alone.

## Hosted / Other Existing Compute Escalation

- Preserve hosted/API, another existing accelerator pool, CPU route, or hybrid execution when the fixed Gaudi fleet cannot meet model/context/SLO requirements.
- Compare local operations/compile/warm-up/power/idle capacity and correction cost against hosted accepted-result economics.
- Do not turn this page into accelerator procurement advice; expose the exact compatibility/resource/topology gap.

## Canonical Links

- Link exact model facts to Model Reference and Intel Gaudi software/vLLM Gaudi plugin/Optimum/TGI software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Keep Xeon CPU-only serving in `servers/cpu/` and PC NPU/iGPU in `computers/intel/`.
- Link organization/internal-AI-platform/high-security scenarios when service operation/governance dominates.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Intel Gaudi 1.24.1 support/installation/networking documentation and current vLLM Hardware Plugin for Intel Gaudi compatibility, validated-model, installation, security, and 0.26.0 release documentation.
- Current evidence establishes an exact Gaudi-software/vLLM-plugin matrix with vLLM 0.26.0 validated on Gaudi software 1.24.1, model+TP+dtype+Gaudi-generation validation, evolving FP8/INT8/MXFP4/MoE/multimodal support, and explicit Gaudi networking/scale-out requirements. These do not establish practical fit for arbitrary models/topologies.
- Intel Gaudi software/driver/firmware, PyTorch, vLLM Gaudi plugin, Optimum/TGI, validated models/TP/dtypes, quantization, networking, and model artifacts are mutable; recheck them before rendering recommendations.
- Exact Gaudi/software/runtime/artifact/context/topology/concurrency measurement and accepted-result quality remain the fit authority.

## Validation

- Exact Gaudi generation/count/HBM/topology, software/driver/firmware, runtime/plugin, model artifact/precision, context, and concurrency are pinned.
- Gaudi 2/Gaudi 3, Xeon CPU, and Intel PC NPU/iGPU routes are not conflated.
- vLLM plugin compatibility follows exact Gaudi-software version pairs.
- Validated model support retains exact TP/dtype/accelerator conditions and is not generalized by family.
- Multi-HPU/multi-node fit follows supported TP/DP/EP and measured networking rather than aggregate HBM arithmetic.
- KV/cache, prefill/decode, graph compile/warmup, quantization, host NUMA/resources, networking, and service tail latency are measured.
- Provider compatibility benchmarks do not replace accepted-result quality measurement.
- Hardware acquisition remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
