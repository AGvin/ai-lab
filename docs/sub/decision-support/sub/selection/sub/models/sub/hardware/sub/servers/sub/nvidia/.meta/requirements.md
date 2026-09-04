# Documentation Requirements

## Route Fit

- Cover existing NVIDIA datacenter/server GPU hosts where local/self-hosted model inference is the primary workload and the installed GPU topology is fixed.
- Require exact GPU SKU/architecture/count/memory per device, host CPU/RAM, driver, CUDA/NCCL, serving/runtime stack, model artifact, precision/quantization, context/KV cache, parallelism topology, interconnect, concurrency, and service latency/SLO target before assigning fit.
- Distinguish datacenter/server NVIDIA accelerators from desktop GeForce/RTX PC routes; current server support must come from the exact runtime/profile matrix for the installed hardware.
- Keep hardware acquisition, rack/network design, and full HA architecture outside this route. Existing infrastructure is a frozen model-selection constraint.

## Current Runtime Routes

- Separate at least:
  - NVIDIA NIM model-specific validated profiles;
  - NVIDIA model-free NIM/vLLM-backed serving;
  - direct vLLM/SGLang/TensorRT-LLM or another supported serving engine;
  - TensorRT engines for supported non-LLM/model-specific workloads;
  - explicit distributed serving through Ray/Dynamo/other current supported orchestration.
- Do not label all NVIDIA serving `TensorRT-LLM` or `NIM`; preserve the actual backend/container/profile.
- Current NIM LLM documentation exposes both current 2.x and 3.x lines, with the newer line targeting Dynamo-based distributed inference where independently scaled workers are needed.
- Treat every runtime/container/profile/version as mutable and recheck current support before rendering recommendations.

## Profile-Specific Support Is the Authority

- Use the current NIM support matrix or the selected runtime's current hardware/model matrix for exact compatibility.
- Current NIM support is expressed as model + GPU SKU + tensor-parallel degree + precision + profile rather than a generic `NVIDIA GPU supported` statement.
- The current matrix includes multiple Blackwell, Hopper/Grace Hopper, Ampere, and selected server/workstation-class GPUs, but support varies materially by model/profile.
- Do not transfer one NIM model's verified GPU/TP/precision profile to another model.
- Keep an unlisted or unmeasured exact GPU/model/profile combination `Unknown` even when a neighboring architecture is supported.

## NIM Model-Specific vs Model-Free

- Treat model-specific NIMs as validated container/profile combinations with explicit model identities and supported configurations.
- Treat `model-free-nim` as a separate route whose practical support follows the bundled underlying backend and its current verified GPU/runtime boundaries.
- Do not infer that model-free NIM has the same performance tuning, profile coverage, or enterprise lifecycle guarantees as a model-specific NIM.
- Preserve exact NIM image/tag, model identity/revision, backend, profile, precision, TP/PP configuration, and cache/artifact source.
- Revalidate after NIM/backend updates because current releases can change bundled vLLM/TensorRT-LLM versions and supported profiles.

## GPU Architecture and Exact SKU

- Record exact GPU SKU and architecture rather than only `A100`, `H100`, `B200`, or `Blackwell` family shorthand when memory/topology/form factor differs.
- Distinguish PCIe, SXM/NVL/NVLink/NVSwitch-connected variants where interconnect or memory differs.
- Current server stacks span Ampere, Hopper/Grace Hopper, and Blackwell-class systems; exact feature/precision/runtime support still varies by architecture and model.
- Do not infer FP8/FP4/NVFP4/MXFP4/INT4 support from architecture branding alone; verify the selected runtime/model implementation.
- Preserve compute capability and exact driver/CUDA requirements for custom/runtime paths.

## VRAM Is a Per-Topology Working Set

- Measure model weights, KV/cache, runtime workspaces, CUDA graphs, attention/sampling buffers, multimodal encoders, adapters/LoRAs, speculative-decoding models, batching/concurrency, fragmentation, and communication buffers.
- Reserve operational headroom rather than planning to 100% nominal HBM.
- Do not sum GPU memory across devices and call it usable model memory without a supported sharding/parallelism topology.
- Track memory per rank/device as well as aggregate memory.
- A model that fits only by eliminating KV/cache or service headroom does not fit the intended serving workload.

## Parallelism Is Part of Compatibility

- Distinguish tensor parallelism, pipeline parallelism, data parallelism, expert parallelism, context/sequence parallelism, and disaggregated prefill/decode where the selected stack supports them.
- Use only parallelism combinations supported by the exact runtime/model and current topology.
- Preserve TP/PP/DP/EP values with every benchmark or fit claim.
- Do not assume doubling GPU count halves latency or doubles usable capacity.
- Measure communication overhead and load imbalance under the intended topology.

## Interconnect and Topology

- Record PCIe/NVLink/NVSwitch/fabric topology, NUMA affinity, NIC placement, and host memory locality where they affect multi-GPU or multi-node serving.
- Use NCCL topology/debug evidence when communication behavior is material.
- A multi-GPU host with poor peer topology can underperform a smaller but better-connected topology.
- Preserve heterogeneous GPU fleets as separate pools unless the runtime explicitly supports the intended heterogeneous placement.
- Do not build one tensor-parallel group from unlike GPUs merely because their memory sums to the target size.

## Multi-Node Serving

- Treat multi-node inference as a separate operational/runtime route, not a simple extension of one host.
- Current NIM supports Ray-based multi-node tensor-parallel serving and newer NIM 3.x guidance introduces Dynamo-based distributed inference patterns; direct vLLM/SGLang/TensorRT-LLM have their own distributed constraints.
- Record worker/node count, GPUs per node, fabric, rendezvous/orchestration, parallelism mode, model placement, failure behavior, and version coupling.
- Measure network/fabric saturation, cross-node collective latency, startup/recovery time, and p95/p99 service latency.
- Keep unsupported multi-node model/runtime combinations `Unknown` even if single-node inference works.

## NIM 3 / Dynamo Boundary

- Treat Dynamo-style distributed inference as an architecture option for workloads that benefit from independently scaled inference workers or disaggregated components.
- Do not assume Dynamo is required for ordinary single-node or small multi-GPU serving.
- Preserve backend choice (vLLM/SGLang/TensorRT-LLM), frontend/router/planner/cache components, worker topology, and scheduling policy.
- Evaluate the operational complexity and service objective before selecting disaggregation.
- Do not import Dynamo performance assumptions into non-Dynamo NIM or direct-runtime deployments.

## TensorRT / TensorRT-LLM Engine Portability

- Treat serialized/compiled engines as version/platform/hardware-coupled deployment artifacts unless current compatibility modes explicitly cover the target.
- Current TensorRT documentation states that serialized engines are not inherently portable across platforms and that version/hardware compatibility depends on how the engine was built.
- Preserve TensorRT/TensorRT-LLM version, CUDA, build flags, GPU architecture, model revision, precision, plugins, and engine/profile identity.
- Rebuild/revalidate after major runtime, driver, CUDA, model, or target-architecture changes when required.
- Do not copy an engine from H100 to B200/A100 or across OS/platforms and assume correctness/performance.

## Model Architecture Support

- Verify exact model family/revision and every required architecture feature in the selected serving stack.
- Current NIM/TensorRT-LLM/vLLM coverage evolves rapidly for MoE, multimodal, speculative decoding, structured outputs, adapters, long context, and new attention architectures.
- A runtime supporting the base model family does not prove support for every derivative checkpoint, custom architecture, tokenizer, adapter, or multimodal component.
- Keep custom `trust_remote_code`/plugin dependencies explicit and security-reviewed.
- Unsupported architecture/operator/backend combinations remain `Unknown`.

## Precision and Quantization

- Record BF16/FP16/FP8/FP4/NVFP4/MXFP4/INT8/INT4/AWQ/GPTQ/other exact precision/quantization as implemented by the selected runtime/model.
- Do not infer acceleration from datatype name alone.
- Preserve quantized artifact producer/tool/version/calibration and model revision.
- Evaluate accepted-result quality and any model-specific accuracy regressions after quantization.
- A quantization that enables memory fit but materially raises retry/correction rate does not fit the workload.

## KV Cache and Context

- Treat KV/cache as a dynamic service resource rather than a static model-size add-on.
- Record maximum model context, configured service context, average/p95 input and output lengths, concurrency, prefix-cache policy, KV precision, and memory utilization settings.
- Benchmark short and long-context workloads separately.
- Do not present the model's advertised context as concurrently serviceable capacity without KV/cache measurements.
- Preserve reduced-context fit as a conditional constraint rather than a full base-model capability claim.

## Prefill and Decode

- Measure time-to-first-token/prefill throughput separately from inter-token/decode throughput.
- Track p50/p95/p99 TTFT and inter-token latency where interactive SLOs matter.
- Measure batch/throughput-oriented workloads separately from low-latency interactive serving.
- A configuration optimized for throughput can be unsuitable for latency even when aggregate tokens/s is high.
- Preserve runtime scheduler/batching parameters with benchmark results.

## Continuous Batching and Concurrency

- Measure the intended request mix and arrival pattern rather than a single synthetic batch.
- Record max concurrent sequences, token budgets, batch scheduler policy, queueing, preemption, chunked prefill, prefix caching, and speculative decoding where used.
- Include p95/p99 queue time and tail latency.
- Do not infer production throughput from one offline benchmark.
- Define admission/backpressure thresholds so overload fails predictably.

## Speculative Decoding

- Treat speculative decoding as a separate model/runtime configuration with additional draft/verification model resources and support constraints.
- Current NIM releases can expose profile-specific speculative-decoding defaults/overrides; preserve the exact profile/configuration.
- Measure TTFT/decode gain, extra memory, acceptance rate, and quality/behavior stability.
- Do not assume speculative decoding improves every model/workload.
- Revalidate when NIM/backend/profile changes.

## MoE Models

- Record total parameters, active parameters, expert count, expert routing, EP/TP topology, all-to-all communication, and memory placement for MoE models.
- Do not compare MoE fit to dense models from active parameter count alone.
- Measure expert imbalance and fabric/collective overhead at real concurrency.
- Preserve expert-parallel/runtime support matrix as part of compatibility.
- Unsupported MoE kernels/parallelism remain `Unknown`.

## Multimodal Models

- Include vision/audio/video encoders, projectors, media preprocessing, frame/image limits, decoders, and modality-specific caches/workspaces.
- Verify the selected serving backend supports the exact multimodal architecture and request schema.
- Measure media transfer/decode/preprocessing plus model inference end to end.
- Do not assign text-only GPU/context measurements to VLM/video workloads.
- Evaluate concurrency with realistic media payloads.

## Multi-Model Serving

- When several models share GPUs, measure resident weights, per-model KV/cache, adapters, scheduler isolation, and eviction/load overhead.
- Compare static partitioning, independent replicas, and supported multi-model serving rather than assuming one large process is best.
- Preserve SLOs per model/tenant.
- Do not overcommit HBM so model swaps dominate latency unless the workload explicitly tolerates it.
- Keep cross-tenant/model isolation and rate controls explicit.

## MIG and Partitioned GPU Resources

- Treat MIG or other GPU partitioning as an explicit resource topology.
- Verify the exact GPU generation, MIG profile, runtime/container support, and model memory/compute needs.
- Do not use full-GPU benchmark numbers for a MIG slice.
- Measure isolation, KV/cache capacity, concurrency, and scheduler overhead on the actual partition.
- Keep unsupported serving/runtime combinations `Unknown`.

## Host CPU, RAM, and Storage

- Include tokenization, preprocessing, request handling, networking, model loading, pinned memory, offload, retrieval, and observability in host resource planning.
- Record NUMA locality between CPUs, GPUs, NICs, and storage where material.
- Model downloads/caches/engines can consume substantial local NVMe; include rollback/current+next model headroom.
- Do not treat HBM capacity as the only server resource constraint.
- Verify cold-start/model-load behavior from the actual storage path.

## Container and Driver Compatibility

- Pin NVIDIA driver, CUDA compatibility mode/toolkit where relevant, NVIDIA Container Toolkit, container image/tag, runtime libraries, and orchestrator GPU plugin/operator versions.
- Use the current support matrix rather than an old driver/CUDA heuristic.
- Revalidate after driver/container/backend upgrades.
- Do not mix host/runtime libraries ad hoc when the supported container already carries a validated stack unless there is a documented reason.
- Record deviations from vendor-supported container configurations.

## Offline / Air-Gapped Deployment

- For disconnected environments, pre-stage containers/models/caches and verify startup/steady-state with outbound networking denied.
- Keep registry/model-hub/API credentials out of the isolated runtime when local artifacts remove the need for them.
- Preserve artifact hashes/signatures and exact versions across transfer.
- Verify telemetry/licensing/update behavior under the actual boundary.
- Route high-security operational controls to the relevant user scenario while keeping hardware/runtime compatibility here.

## Serving API Security

- Treat OpenAI-compatible/NIM/vLLM endpoints as network services requiring authentication, authorization, TLS where applicable, rate limits, request-size limits, tenant isolation, and audit.
- Do not expose an unauthenticated inference endpoint to an entire network because it is internal.
- Keep tool execution/agent authority outside the model server unless explicitly designed and bounded.
- Minimize sensitive prompt/output logging and define retention.
- Separate model-deployment/admin privileges from inference-consumer privileges.

## Observability

- Record GPU memory/utilization, SM activity, power/thermals, PCIe/NVLink/fabric traffic, KV/cache use, queue depth, request/token rates, TTFT/ITL, errors/OOMs, and per-model/version identity.
- Use service-level metrics rather than GPU utilization alone.
- Preserve p50/p95/p99 latency and throughput at representative concurrency.
- Detect repeated OOM/preemption/restart/model-reload events as practical-fit failures.
- Keep observability stack overhead in capacity measurements.

## Reliability and Failure Behavior

- Test process/container restart, GPU reset/failure, node loss, model reload, NCCL/fabric failure, cache warm-up, and rolling update behavior appropriate to the deployment.
- Multi-node or disaggregated serving should have explicit degraded/failure semantics.
- Do not call a topology production-fit because a benchmark completes once.
- Preserve rollback to a known-good model/runtime/container combination.
- Define workload fallback/escalation when the fixed GPU fleet cannot meet availability or latency.

## Benchmark Contract

- Record at minimum:
  - exact GPU SKU/count/topology/interconnect;
  - host CPU/RAM/NUMA and storage;
  - driver/CUDA/NCCL;
  - container/runtime/backend versions;
  - model/artifact/precision/quantization;
  - context/input/output distribution;
  - TP/PP/DP/EP/disaggregation;
  - concurrency/batching/scheduler settings;
  - cold/warm state.
- Measure TTFT, inter-token latency/decode, request latency, input/output/total token throughput, peak HBM, host RAM, GPU/fabric utilization, power where material, and accepted-result quality.
- Do not compare results across different context/concurrency/model/precision/topology conditions as if they were the same benchmark.

## Accepted-Result Quality

- Validate the exact served/quantized artifact on representative tasks, not only upstream benchmark scores.
- Track retries, corrections, refusals, tool/function-call accuracy, multimodal quality, and failure severity according to workload.
- Compare accepted-result throughput/cost, not raw tokens/s alone.
- Preserve stronger model or hosted escalation when a smaller/faster local artifact misses quality thresholds.

## Practical Fit Outcomes

- `Fits well`: exact GPU topology/runtime/profile/model/precision/context/concurrency passes current support, HBM/KV headroom, TTFT/ITL/throughput, accepted quality, and sustained reliability targets.
- `Fits conditionally`: requires a specific NIM/runtime profile, reduced context/concurrency, alternate quantization, supported multi-GPU topology, MIG partition, or another explicit accepted constraint.
- `Does not fit`: exact route fails model/runtime/GPU support, memory, topology, latency/throughput, quality, or reliability requirements.
- `Unknown`: exact GPU/runtime/model/profile/topology lacks current first-party or measured evidence.
- Do not assign fit from aggregate HBM, GPU count, architecture name, TFLOPS/TOPS, or load success alone.

## Hosted / Other Existing Compute Escalation

- Preserve hosted/API, another existing accelerator pool, CPU serving, or hybrid routing when the fixed NVIDIA fleet cannot meet the selected model/context/SLO.
- Compare local energy/operations/tuning/idle capacity and human correction against hosted accepted-result economics.
- Do not turn this page into GPU procurement guidance; expose the exact capability/resource/topology gap.

## Canonical Links

- Link exact model facts to Model Reference and NIM/vLLM/SGLang/TensorRT-LLM/TensorRT/Dynamo software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Keep desktop NVIDIA PC guidance in `computers/nvidia/` and Jetson guidance in `single-board/jetson/`.
- Link organization/internal-AI-platform/high-security scenarios when operations/security/governance becomes primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current NVIDIA NIM for LLM support matrices and release documentation, current NIM model-free/model-specific and multi-node serving guidance, current NIM 3/Dynamo notices, current NVIDIA TensorRT 11.x support/engine-portability documentation, and current NVIDIA/vLLM distributed-serving guidance.
- Current evidence establishes profile-specific model/GPU/TP/precision validation, current Blackwell/Hopper/Ampere server coverage, distinct model-specific/model-free NIM paths, Ray/Dynamo distributed serving options, and explicit TensorRT engine portability/version constraints. These do not establish practical fit for arbitrary models/topologies.
- NIM/TensorRT-LLM/TensorRT/vLLM/SGLang/Dynamo, supported GPU/model/profile matrices, precision kernels, drivers/CUDA/NCCL, parallelism/disaggregation, and model artifacts are mutable; recheck them before rendering recommendations.
- Exact GPU topology/runtime/profile/artifact/context/concurrency measurement and accepted-result quality remain the fit authority.

## Validation

- Exact GPU SKU/count/topology/interconnect, driver/CUDA/NCCL, runtime/profile, model artifact/precision, context, and concurrency are pinned.
- Datacenter/server and desktop RTX/Jetson routes are not conflated.
- NIM model-specific/model-free and direct runtime paths remain distinct.
- NIM verified profile matrices are not generalized to unlisted model/GPU/precision/topology combinations.
- Multi-GPU/multi-node capacity follows supported TP/PP/DP/EP/disaggregation rather than aggregate HBM arithmetic.
- KV/cache, prefill/decode, batching/concurrency, fabric/NUMA, host resources, and service tail latency are measured.
- TensorRT/TensorRT-LLM engine/version/hardware portability is explicit.
- Quantization/precision and provider benchmarks do not replace accepted-result quality measurement.
- Hardware acquisition remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
