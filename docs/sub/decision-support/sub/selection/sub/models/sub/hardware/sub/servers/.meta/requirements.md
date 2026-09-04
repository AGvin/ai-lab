# Documentation Requirements

## Router Role

- Cover dedicated local/on-prem inference hosts and accelerator servers where service-style operation, sustained throughput, concurrency, topology, large model/KV working sets, and operational SLOs materially change model feasibility.
- Route by the **effective installed compute ecosystem**: `nvidia/`, `amd/`, `intel/`, or `cpu/`.
- Keep this page focused on cross-server model-selection constraints and delegate exact accelerator/runtime/model matrices to the children.
- Keep hardware acquisition, rack/network design, and full HA/failover architecture outside this journey; existing infrastructure is a fixed model-selection constraint.

## Route by Actual Serving Compute

- Use `nvidia/` for existing NVIDIA datacenter/server GPU inference stacks.
- Use `amd/` for existing AMD Instinct/ROCm inference stacks.
- Use `intel/` for existing Intel Gaudi 2/3 accelerator inference stacks.
- Use `cpu/` when dedicated server CPUs are the intended inference device and no accelerator route owns the workload.
- Do not route from server OEM/chassis/CPU vendor when an installed accelerator owns inference.
- Preserve mixed fleets as separate execution pools unless the selected serving stack explicitly supports the heterogeneous topology.

## Exact Server State

- Require exact accelerator/CPU SKU and generation, count, memory per device or NUMA node, host CPU/RAM, interconnect/NUMA/fabric, OS/kernel, drivers/firmware, runtime/container, model artifact/precision, context/KV cache, parallelism, batching/concurrency, and service SLO before assigning fit.
- Record single-device, single-host multi-device, and multi-node topology separately.
- Keep unsupported/unmeasured exact server/runtime/model/topology combinations `Unknown`.
- Recheck the relevant child support matrix before current recommendations.

## Capacity Is Topology-Specific

- Do not infer model capacity by summing HBM/VRAM/RAM across devices/nodes.
- Usable capacity depends on supported tensor/pipeline/data/expert parallelism, per-rank memory, interconnect, NUMA locality, KV cache, runtime workspaces, and communication buffers.
- Track peak memory per device/rank/node as well as aggregate infrastructure capacity.
- A cluster with enough aggregate memory but an unsupported or inefficient sharding topology does not fit.

## Runtime Is Part of Hardware Fit

- Treat runtime/backend/container versions as part of the compute target.
- NVIDIA NIM/vLLM/TensorRT-LLM, AMD ROCm/vLLM/SGLang/ATOM-AITER, Intel Gaudi vLLM plugin/Optimum/TGI, and CPU vLLM/llama.cpp/OpenVINO routes have different support and topology contracts.
- Do not transfer model/precision/parallelism support between ecosystems because they expose similar OpenAI-compatible APIs.
- Preserve exact model artifact and conversion/quantization with the runtime tuple.

## Service SLO Before Model Size

- Define interactive or batch service objective before comparing models: TTFT, inter-token latency, total request latency, throughput, concurrency, availability, and quality.
- Separate low-latency interactive serving from maximum-throughput batch serving.
- A model that fits memory but cannot satisfy p95/p99 latency does not fit the service.
- Preserve workload-specific thresholds rather than one generic tokens/s target.

## Prefill and Decode

- Measure prompt/prefill separately from autoregressive decode/inter-token latency.
- Record representative input/output length distributions, not only one short synthetic prompt.
- Long-context prompt ingestion can be the bottleneck even when decode throughput is acceptable.
- Preserve TTFT and ITL/p95/p99 under target concurrency.

## KV Cache and Context

- Treat KV/cache as a dynamic serving resource tied to context and concurrent sessions.
- Record max configured context, actual p50/p95 input/output lengths, KV precision, prefix-cache policy, and per-session growth.
- Do not present the base model's advertised context as serviceable at production concurrency without memory/latency evidence.
- Reduced context/concurrency remains an explicit conditional fit.

## Batching, Queueing, and Admission

- Measure the actual arrival pattern and scheduler/batching configuration.
- Track queue depth/time, active sequences, token budget, preemption, continuous batching, and backpressure/admission limits where applicable.
- Do not extrapolate one offline batch benchmark to an online service.
- A high-throughput configuration with unacceptable tail latency does not fit an interactive workload.

## Parallelism Is a Model/Runtime Contract

- Record TP/PP/DP/EP and any disaggregated prefill/decode or cache topology.
- Use only combinations supported by the exact model/runtime and existing hardware/fabric.
- Do not assume more devices improve latency or throughput linearly.
- Compare independent replicas/data parallelism with sharded execution when both are feasible.
- Keep unsupported topology `Unknown` rather than approximating from memory sums.

## Interconnect, Fabric, and NUMA

- Record NVLink/NVSwitch, XGMI/Infinity Fabric, Gaudi Ethernet/RDMA, PCIe, CPU NUMA, NIC placement, and storage locality as applicable.
- Measure collective/fabric/remote-memory behavior when multi-device or multi-node serving depends on it.
- Topology-aware placement is part of model fit even though physical network design belongs elsewhere.
- Revalidate after driver/runtime/communication-library upgrades because defaults can change.

## Host Resources

- Include tokenization, preprocessing, retrieval/vector databases, request routing, TLS/API, pinned memory, model loading, observability, logging, and CPU fallback.
- Reserve host CPU/RAM/storage for service functions rather than assigning every resource to model kernels.
- Include current and rollback model/container artifacts, caches, compiled engines/kernels, and indexes in storage planning.
- Measure cold model load from the actual storage path.

## Precision and Quantization

- Record exact BF16/FP16/FP8/FP4/INT8/INT4/AWQ/GPTQ/MXFP4/other precision and its runtime/model implementation.
- Hardware capability does not establish model/kernel support for a precision.
- Preserve quantization tool/version/calibration and exact artifact identity.
- Validate accepted-result quality after quantization.
- A smaller memory footprint that materially increases retries/corrections is not automatically better fit.

## MoE and Multimodal Workloads

- For MoE, include total/active parameters, expert count, EP topology, all-to-all communication, and imbalance.
- For VLM/audio/video/diffusion, include all encoders/decoders/pre/postprocessing and modality-specific memory/latency.
- Do not reuse dense text-LLM measurements for MoE or multimodal workloads.
- Verify exact model architecture support in the selected child runtime.

## Multi-Model / Multi-Tenant Serving

- Measure combined resident weights, KV/cache, adapters, scheduler isolation, model reload/eviction, and tenant request mix.
- Preserve per-model/tenant SLOs and access controls.
- Do not overcommit memory so model swaps dominate latency unless the workload explicitly accepts it.
- Compare static partitioning, replicas, and supported sharing mechanisms.

## Offline / High-Security Boundary

- For disconnected environments, pre-stage models, containers, runtimes, and dependencies and verify startup/steady-state with denied egress.
- Preserve artifact hashes/signatures/version provenance.
- Avoid hidden model-hub/package/licensing/telemetry dependencies.
- Link full security-boundary and cross-domain operational controls to the applicable user scenario rather than duplicating them here.

## Serving API Security

- Treat all inference endpoints as network services requiring authentication, authorization, TLS where applicable, rate/request limits, tenant separation, and audit.
- Do not expose an unauthenticated OpenAI-compatible endpoint merely because it is on-premises.
- Keep model serving separate from agent/tool execution authority.
- Minimize sensitive prompt/output logging and separate deployment/admin privileges from clients.

## Observability

- Monitor per-device/rank memory, utilization, KV/cache, communication/fabric/NUMA behavior, queue depth, TTFT/ITL, throughput, p50/p95/p99, errors/OOM/restarts, power/thermals, and exact model/runtime version.
- Service metrics are primary; accelerator/CPU utilization alone is not fit evidence.
- Detect repeated OOM, fallback, recompilation/warm-up, swapping, or communication failure as practical-fit signals.
- Include observability overhead in capacity tests.

## Reliability and Lifecycle

- Test process/container restart, model reload, cold/warm start, device/node failure where applicable, communication failure, overload, rolling update, and rollback.
- Treat driver/runtime/container/model changes as compatibility/performance events.
- Preserve a known-good deployment tuple for rollback.
- A benchmark-complete topology is not automatically production-fit.

## Benchmark Contract

- Record exact hardware/device counts/topology, host CPU/RAM/NUMA/storage, driver/runtime/container, model/artifact/precision, context/input/output distribution, parallelism, batching/concurrency, and cold/warm state.
- Measure TTFT/prefill, ITL/decode, total request latency, throughput, peak memory per rank, host memory, communication/NUMA behavior, power where material, and accepted-result quality.
- Do not compare results across different topology/model/context/precision/concurrency conditions as equivalent.

## Accepted-Result Economics

- Compare total cost per accepted result: power, server operations, idle capacity, storage, tuning/engineering, retries, human correction/review, and incident burden where material.
- Existing hardware can have low marginal acquisition cost but poor latency/energy/operations economics.
- Hosted/rented/hybrid execution remains valid when the fixed local server cannot meet quality/SLO/economic constraints.
- Hardware procurement remains outside this route.

## Practical Routing Outcomes

- `NVIDIA`: exact datacenter GPU + current NVIDIA runtime/profile/topology owns fit.
- `AMD`: exact Instinct + ROCm/runtime/topology owns fit.
- `Intel`: exact Gaudi + Gaudi software/runtime/topology owns fit.
- `CPU`: exact CPU/NUMA/runtime topology owns fit.
- `Hosted/hybrid/other existing pool`: local server route misses accepted model/context/SLO/economics and policy permits escalation.
- `Unknown`: exact current hardware/runtime/model/topology lacks support or measurement.

## Canonical Links

- Route exact ecosystem support to `nvidia/`, `amd/`, `intel/`, or `cpu/`.
- Link exact model facts to Model Reference and serving software to canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link internal-AI-platform/high-security/organization scenarios when operational/governance requirements become primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after current NVIDIA NIM/TensorRT/vLLM, AMD ROCm/vLLM/ATOM-AITER, Intel Gaudi/vLLM-plugin, and CPU vLLM/llama.cpp/OpenVINO child-route passes.
- Current child evidence confirms that exact runtime/profile, memory per rank, topology/communication, KV/concurrency, and service SLO are indispensable across server classes while support/precision/parallelism matrices remain ecosystem-specific.
- Drivers, firmware, runtimes, communication libraries, supported models/precisions/topologies, and model artifacts are mutable; recheck the selected child before rendering recommendations.
- Exact existing server/runtime/artifact/topology/workload measurement and accepted-result quality remain the fit authority.

## Validation

- Direct children remain `nvidia/`, `amd/`, `intel/`, and `cpu/`.
- Datacenter accelerator, CPU-server, PC, and SBC support boundaries are not conflated.
- Aggregate GPU/HPU/RAM capacity is never treated as usable model memory without supported topology and per-rank headroom.
- Runtime/profile, KV/context, prefill/decode, batching/concurrency, topology/fabric/NUMA, host resources, tail latency, and accepted quality are first-class.
- Hardware acquisition/full network/HA architecture remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
