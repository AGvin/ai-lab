# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual who operates or plans **persistent personal AI services** on a workstation, dedicated server, mini PC, NAS-adjacent host, SBC/developer board, or mixed home-lab infrastructure and accepts ongoing systems administration.
- Distinguish it from `ai-enthusiast/`: here the primary question is not how easily models can be swapped for experiments, but which model/runtime portfolio can remain available, maintainable, recoverable, and economically sensible as a continuing service.
- Keep full network/security architecture, hardware purchasing, storage-platform design, cluster orchestration, UPS design, and backup implementation in their canonical owners. This scenario records only the operational conditions that materially change model selection.
- If the primary question is exact fixed-hardware compatibility, continue into sibling `../../../hardware/` selection, especially `../../../hardware/sub/servers/` and `../../../hardware/sub/single-board/`.

## Define the Service Before Selecting the Model

- Require a small service envelope before choosing a resident model: intended users/clients, concurrent requests, modalities, routine task classes, latency target, accepted-result quality, normal and peak context, uptime expectation, offline requirement, data boundary, power/noise constraints, and acceptable recovery time after failure/update.
- Separate **interactive availability** from high-throughput serving. A model that is comfortable for one user at one request may fail when several clients hold long contexts or tool/agent workflows remain active concurrently.
- Separate the model service from optional surrounding services such as embeddings, reranking, OCR, speech, image generation, RAG/vector storage, web retrieval, automation, and agent tools. Their memory/process/storage requirements reduce the resources available to the resident LLM and may justify specialist separation.
- Do not start with `largest model that can load`. Start with the smallest route that meets accepted-result and modality needs under the real service envelope, then measure whether a larger model improves enough to justify operational cost.

## Resident Generalist Portfolio

- Preserve `Qwen3 14B` as a current **resident-generalist hypothesis**, not as a universal home-lab default. Treat it as resident-fit only after exact artifact/quantization/precision, runtime/backend, configured context, number of concurrent slots/sequences, KV/cache allocation, auxiliary components, and peak-memory evidence are measured on the intended host.
- Keep `Qwen3 8B` as a lower-resource fallback/baseline when 14B consumes too much memory, latency, or power for the service envelope or when reserving capacity for other persistent services creates more total value.
- Consider `Qwen3 30B-A3B` or `Qwen3 32B` only when the host can support their exact checkpoint/runtime route and they materially improve accepted results. MoE active parameter count does not make the 30B-A3B checkpoint a 3B memory class.
- Do not assume that a model's advertised maximum context should be configured as the service default. Larger context reserves or consumes more KV/cache capacity and can reduce concurrency/headroom. Configure the context actually required by workloads and validate a separate maximum/exception route when needed.
- Treat resident choice as a portfolio decision: a smaller always-on model plus a larger on-demand model may be better than keeping the largest candidate permanently loaded.

## Multimodal and Specialist Services

- Preserve `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` as compact current multimodal-service candidates when local image/document/audio understanding is a recurring workload and the exact runtime supports the required modality path.
- Account for model weights plus multimodal encoders/projectors, preprocessing, context expansion, and any separate OCR/media processes. A compact language-decoder label does not define the whole resident memory footprint.
- Keep a specialist resident only when its recurring use justifies memory and update burden. For infrequent workloads, on-demand loading or hosted escalation can be more efficient than multiple permanently loaded services.
- Keep image generation, speech synthesis/transcription, embeddings/rerankers, and other specialists independent when their runtime/hardware requirements differ materially from the resident generalist. Do not force one `multimodal` label to become the whole home-lab stack.

## Residency, Loading, and Switching

- Compare three operational patterns explicitly:
  1. **single resident model** — simplest, predictable warm latency, limited specialization;
  2. **multiple simultaneous resident services** — better immediate capability coverage but higher VRAM/RAM fragmentation, idle power, process/update burden, and lower concurrency headroom;
  3. **resident generalist + on-demand specialists/larger model** — saves resident memory but adds load/unload/warm-up/recovery delay.
- For on-demand switching, measure model unload/load time, storage read throughput, initialization/compilation/warm-up, context/cache loss, first-request latency, and failure recovery. Do not call a route practical merely because a script can swap models.
- If the runtime supports idle unloading/retention controls, treat them as runtime-specific behavior and test actual memory reclamation and reload latency. Do not infer identical lifecycle behavior across Ollama, LM Studio, llama.cpp, vLLM, or other engines.
- Keep model files reproducibly recoverable. Large weights that can be re-downloaded need not be backed up the same way as unique configs, prompts, adapters, evaluation data, indexes, or user-generated state.

## Concurrency and Context Capacity

- Treat **concurrency as a model-fit dimension**, not merely a web-server setting. Each simultaneous sequence/slot can consume KV/cache and runtime state; the usable model/context combination therefore depends on expected parallel requests.
- Measure at the actual concurrency target. Record per-request context, prompt/prefill latency, decode latency/throughput, queueing behavior, peak device/system memory, and failure/preemption/eviction behavior where applicable.
- For `llama.cpp` server routes, current serving exposes parallel slots and continuous batching; the configured context and slot count materially change cache/resource use. Benchmark the chosen `--parallel`/context route rather than transferring a single-client desktop result.
- For vLLM routes, GPU memory allocation and KV-cache capacity are explicit serving controls; current vLLM exposes GPU-memory utilization, KV-cache sizing/types, prefix caching, batching/scheduling, and other knobs that directly affect model/context/concurrency fit. Treat defaults as starting points, not validated home-lab settings.
- Prefix caching can materially reduce repeated prefill work for shared prefixes, but it is not a substitute for sufficient cache capacity or accepted-result testing and should not be included in capacity assumptions until the actual workload shares reusable prefixes.
- Do not sum aggregate accelerator memory and assume a larger model fits. Multi-GPU execution requires exact supported tensor/pipeline/expert parallel or other sharding topology, interconnect behavior, runtime support, and measured overhead.

## Runtime Selection Boundary

- Select the runtime from the **service need and hardware route**, not personal popularity.
- `llama.cpp` is a relevant resident/home-lab route for GGUF-based serving and modest deployments where flexible CPU/GPU offload, local server slots, and broad consumer hardware support fit the target.
- vLLM is relevant when supported GPU hardware/models and higher serving throughput/concurrency make its scheduler/KV-management model useful. It is not automatically a better route for every single-user home server.
- Other canonical inference engines such as SGLang, TensorRT-LLM, MLX-LM, MLC-LLM, or distributed-serving layers are candidates only when their exact hardware/model and operational benefits justify the additional complexity.
- Keep runtime installation/compatibility details in canonical software owners. This scenario owns only why a runtime class materially changes resident model fit and operations.

## Service Exposure and Authentication Constraint

- Treat a persistent inference endpoint as a network service even when it runs at home. Bind to loopback/private interfaces by default and expose it only to the clients that need access.
- Require authenticated/private access before LAN/WAN use. Prefer an authenticated reverse proxy, private overlay/VPN, or another explicit access-control boundary when the inference engine itself does not protect all reachable endpoints.
- Do not assume an engine's `API key` switch secures the whole process. Current vLLM documentation explicitly notes that its API-key authentication protects selected API path prefixes but not every exposed endpoint, so deployment hardening must be evaluated outside the model server itself.
- Keep raw inference ports off the public Internet by default. Public exposure, TLS termination, identity/access management, rate limiting, audit logging, and external ingress are infrastructure/security decisions outside this page but become mandatory constraints if remote/public access is required.
- Do not put reusable credentials, API keys, private keys, or infrastructure secrets into model prompts or ordinary conversation logs.

## Data, Logs, and Persistent State

- Separate **model service state** from user/data-service state. Model weights/cache are usually reconstructable; chat history, user documents, RAG indexes, embeddings, adapters, configuration, evaluation baselines, and automation state may be unique and need a different retention/recovery policy.
- Apply the shared data-boundary rule before storing prompts/responses or adding hosted fallback. Personal confidential material may justify local service operation, but local hosting still requires endpoint security, filesystem permissions, backups, update discipline, and safe disposal.
- Treat inference logs as potentially sensitive because prompts, tool arguments, filenames, URLs, and model outputs can contain personal data. Minimize logging to what is operationally useful and protect/rotate it according to the data class.
- RAG does not convert private or untrusted source material into verified truth. Preserve source provenance and use deterministic validation/qualified review where the task consequence requires it.

## Availability and Recovery

- Define whether the service is `best effort`, `available while host is awake`, or expected to recover automatically after reboot/power/runtime failure. Model choice may change when automatic recovery and warm-up time are important.
- Measure cold boot/service start/model load/warm-up time and first usable request after restart. A fast steady-state model with a long fragile recovery path can be worse for the home-lab service than a slightly smaller model.
- Pin or deliberately control model artifact and runtime versions for a stable resident route. Do not auto-update every model/runtime dependency immediately if an update can break templates, operators, quantization, multimodal support, or memory behavior.
- Test updates on a bounded path and retain a rollback/recovery mechanism appropriate to the host. This scenario does not own container/orchestrator design, but model recommendations must not assume zero-cost upgrades.
- Monitor enough signals to know whether the service still meets its model-selection assumptions: process health, request failures, queueing/latency, device/system memory pressure, thermals/power where material, storage capacity, and model/runtime version.

## Power, Heat, Noise, and Idle Cost

- Include idle and active service power, cooling/fan noise, room heat, and host availability in the resident-model decision. A large model that forces the main workstation or high-power GPU to remain active continuously can lose to a smaller resident model plus hosted escalation.
- Measure sustained rather than only burst performance when the service is expected to operate for long requests or many clients; thermal/power limits may reduce throughput over time.
- Distinguish a dedicated server from a shared gaming/workstation host. The latter has display/application contention and may be unavailable during gaming/reboots, while the former has higher always-on infrastructure cost.
- Treat an SBC/low-power host as useful only when the exact model/runtime/accelerator route meets the workload. Low watts or advertised NPU TOPS do not establish LLM/VLM compatibility or accepted-result quality.

## SBC and Edge Nodes in the Home Lab

- Route Raspberry Pi, Jetson, Rockchip, and other selected boards through `../../../hardware/sub/single-board/` when they run inference directly. Require exact board/SoC/RAM/accelerator/toolkit/runtime and sustained cooling/storage conditions.
- Do not assume an SBC must host the main LLM. A small board can instead act as a client, sensor/media front end, automation node, gateway, or control-plane component while a stronger local/hosted model performs inference.
- Distinguish CPU-only SBC inference from GPU/NPU/AI-accelerator paths. Converted/compiled accelerator models may have a much narrower supported model/operator set than general CPU/GPU GGUF inference.
- If several SBCs are present, do not infer that aggregating their RAM/TOPS creates one larger model target unless a concrete distributed runtime supports that topology and its communication overhead is measured.

## Hosted and Temporary Cloud Escalation

- Preserve hosted model/API escalation for tasks whose quality, context, modality, or managed-tool needs exceed the resident stack and whose data may leave the home lab.
- Preserve temporary rented GPU as a bounded route for large open-weight models, evaluation/fine-tuning, media generation, or other bursts that do not justify permanent local residency.
- Apply data classification before escalation and evaluate the complete provider chain. A routing intermediary or rented VM changes who can process/store the data.
- Include cold start, image/container pull, model download/cache, storage, idle billing, shutdown, persistence, and endpoint lifecycle in temporary-cloud cost; advertised GPU-hour price alone is not the experiment/service cost.
- Do not treat a paused/preemptible/ephemeral cloud instance as a stable fallback service unless its provider actually guarantees the required endpoint/storage/availability behavior.

## Total Cost of Ownership

- State explicitly that self-hosting is not automatically cheaper than a managed assistant/API.
- Compare **cost per accepted request/service outcome** using hardware already owned plus incremental electricity, storage, backups, replacement/maintenance reserve, operator time, update/recovery effort, and idle capacity.
- Compare that local TCO with managed assistant/API spend and temporary rented accelerators at the actual workload volume and quality requirement.
- Avoid sunk-cost reasoning: existing hardware lowers acquisition cost but does not eliminate energy, noise, failure, administration, or opportunity cost.
- Avoid premature hardware upgrades. A new accelerator is justified only when a repeated measured capability/capacity gap cannot be solved more economically by a smaller resident model, on-demand specialist, hosted model, temporary GPU, or workload redesign.

## Escalation and Portfolio Change Triggers

- Move from Qwen3 8B to 14B or from 14B to a larger resident candidate only when accepted-result quality gains justify higher memory, latency, power, and lower concurrency headroom.
- Move a specialist from on-demand to resident only when its request frequency and load latency justify the idle memory/power/update burden.
- Move a large model from local sequential loading to hosted/rented execution when load/offload/recovery time or partial-offload latency makes accepted-result economics worse.
- Move from one host to a dedicated service host when availability/resource contention—not model quality—is the recurring failure mode; hardware/deployment design then belongs in the applicable canonical hardware/infrastructure owner.
- Move from this personal home-lab scenario toward a team/organization platform scenario when multiple independent users, shared governance, service-level commitments, budgets, compliance, centralized identity, audit, or formal platform ownership become first-class requirements.
- Move back toward `ai-enthusiast/` for temporary experimentation that does not need resident availability; do not over-engineer a hobby experiment into a permanent platform.

## Hardware-Specific Model Selection Continuation

- Link the complete sibling `../../../hardware/` journey.
- Use `../../../hardware/sub/servers/` when a dedicated inference host or accelerator server determines model fit, including exact accelerator topology, memory, sharding, concurrency, and sustained-serving constraints.
- Use `../../../hardware/sub/single-board/` for Raspberry Pi, Jetson, Rockchip, or another selected SBC/developer-board model route.
- Use `../../../hardware/sub/computers/` when the persistent service actually runs on a shared personal/workstation-class machine rather than a dedicated server.
- Do not reproduce platform-specific compatibility matrices in the scenario.

## Canonical Links

- Link resident/generalist model candidates to canonical Model Reference identities such as `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b`, `.../qwen3-14b`, `.../qwen3-30b-a3b`, and `.../qwen3-32b` when named.
- Link compact multimodal candidates to `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/reference/producers/google/gemma/gemma-4/models/e4b-instruct`.
- Link named inference engines to canonical software owners such as `catalog/software/inference-runtimes/inference-engines/llama-cpp`, `.../vllm`, `.../sglang`, or `.../tensorrt-llm` rather than copying runtime documentation here.
- Link hosted services, storage/RAG software, orchestration layers, networking/security tools, and hardware to their canonical owners when they materially affect the route.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current official llama.cpp server, vLLM serving/KV-cache, Qwen3/Gemma 4 model evidence and canonical AI Lab hardware/runtime owners.
- Model artifacts, runtime support, server authentication behavior, cache/scheduler features, hardware drivers, and cloud lifecycle/pricing are mutable; recheck the exact serving route before rendering a current recommendation.
- Runtime documentation establishes supported mechanisms, not the throughput, reliability, or security of the user's actual deployment. Those properties require configuration-specific measurement and appropriate infrastructure controls.
- Provider/model benchmark claims do not replace home-lab measurement of concurrency, queueing, context/cache pressure, recovery time, power, and accepted-result quality.

## Validation

- Persistent reliable service operation clearly distinguishes this scenario from experimentation-first `ai-enthusiast/`.
- Resident model fit is bound to exact artifact/runtime/context/**concurrency** evidence rather than nominal VRAM/RAM or active parameter count.
- Single-resident, multi-resident, and on-demand specialist portfolios are evaluated separately.
- Maximum advertised context is not used as the service default without cache/concurrency evidence.
- A local inference endpoint is treated as a network/security boundary; runtime-local authentication is not assumed to secure every endpoint.
- Recovery/update/monitoring, power/heat/noise, storage/log state, and operator time participate in the route decision without turning this page into full infrastructure architecture.
- SBCs are routed by exact hardware/runtime support and are not assumed to aggregate into a larger server.
- Hosted/cloud escalation includes data-boundary and full lifecycle/billing considerations.
- Total cost includes electricity, idle capacity, storage, administration, failures/recovery, and operator time.
- Hardware-specific fit is delegated to sibling hardware selection.
- Mutable current claims carry the 2026-08-23 evidence boundary.
