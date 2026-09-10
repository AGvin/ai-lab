# Documentation Requirements

## Scenario Fit

- Present this scenario for a person who already owns a gaming-oriented desktop or laptop with a discrete GPU and wants to reuse that hardware for local AI before considering dedicated AI hardware, a separate server, or recurring rented accelerator capacity.
- Start from the **exact existing machine**, not from generic labels such as `gaming PC`, `RTX`, `Radeon`, `Arc`, or an `8–16 GB GPU`. Identify GPU vendor and exact SKU/architecture, physical VRAM, OS, driver stack, intended inference runtime/backend, system RAM, CPU, storage, display topology, and the applications/games that normally consume GPU memory.
- Keep hardware purchasing outside this scenario. The first objective is to discover what the existing card can do reliably and where the measured bottleneck actually is.
- If the reader's dominant question becomes hardware-first fit rather than combined user context, continue into `../../../hardware/`, `../../../hardware/sub/computers/`, and the applicable `computers/nvidia/`, `computers/amd/`, `computers/intel/`, or other selected compute route.

## Starting Decision Order

- First define the recurring workloads: general text/reasoning, coding, document work, image/audio understanding, image generation, speech, embeddings/RAG, or a mixed workflow. Do not select one local model merely because it fits VRAM if it does not cover the required modality or accepted-result quality.
- Separate **interactive desktop use** from an always-on local service. A gaming PC may be excellent for opportunistic inference while still being a poor always-on server because of sleep/reboot cycles, driver/game updates, user logoff, noise, thermals, power consumption, and resource contention.
- Benchmark the machine in two states when relevant: a clean inference session and a representative normal-desktop state with browser, display compositor, game launcher, creative software, or other usual GPU consumers active. Use the latter when judging practical headroom.
- Start with one or two model artifacts that plausibly fit the exact target and workload; measure them before broad model collecting. Expand the shortlist only when the first candidates fail a material requirement.

## Practical VRAM and Artifact Shortlisting

- Treat VRAM as a **budget that must include more than model weights**. Account for KV/cache or equivalent context state, runtime buffers, temporary workspaces, multimodal encoders/projectors, CUDA/ROCm/OpenVINO allocations, graph/engine memory, batch/concurrency, fragmentation, display usage, and application/game contention.
- Use official artifact size only as a lower-bound planning input. A model file fitting inside nominal VRAM does not prove full accelerator residency, useful context, stable latency, or accepted-result quality.
- For an approximately **8 GB VRAM** card, current Qwen3 8B low-bit artifacts are a reasonable text/reasoning experiment when the exact runtime supports them. The official Q4_K_M artifact is about 5 GB by weights, while Q8_0 is about 8.7 GB; therefore Q8_0 alone already exceeds an 8 GB full-residency budget before context/runtime/display overhead. Do not describe `Qwen3 8B fits 8 GB` without naming quantization, runtime, context, and measured peak allocation.
- `Gemma 4 E4B Instruct` is a current compact multimodal experiment for image/document/audio-oriented local use. Google's official QAT Q4_0 GGUF route is roughly 5.15 GB for model weights plus a separate multimodal projection artifact around 1 GB; treat those as artifact sizes, not a total VRAM requirement. `Gemma 4 E2B Instruct` is the lighter sibling when lower resource use matters more than the larger E4B route.
- For an approximately **12 GB VRAM** card, current Qwen3 14B Q4_K_M weights are roughly 9 GB and can be evaluated with bounded context/headroom. Higher-bit artifacts consume materially more space, so 12 GB must not be described as a blanket `14B class` guarantee.
- For an approximately **16 GB VRAM** card, do not present current Qwen3 30B-A3B or Qwen3 32B Q4_K_M artifacts as full-VRAM routes: their official Q4_K_M weight files are roughly 18.6 GB and 19.8 GB respectively before context/runtime/display overhead. Partial CPU/system-RAM offload may make them runnable, but it changes latency, bandwidth pressure, power use, and practical interactivity and must be measured as a different execution route.
- For an approximately **24 GB VRAM** card, current Qwen3 30B-A3B and Qwen3 32B Q4-class weights become plausible full-accelerator experiments by weight size, but context/KV state, runtime buffers, display occupancy, and fragmentation still need explicit headroom. `24 GB` is not a guarantee of useful context or stable concurrency.
- Do not infer memory fit from **active MoE parameter count**. Sparse models may activate only a subset of parameters per token while still requiring a much larger total checkpoint to be resident or accessible. Use the exact artifact and runtime memory behavior rather than active-parameter marketing shorthand.
- Do not infer task quality from parameter count or quantization level alone. A smaller model that produces accepted results with fewer retries may be the better route than a larger artifact that barely fits or spills to CPU.

## Current Candidate Roles

- Keep `Qwen3 8B` as a current compact general text/reasoning candidate for smaller gaming GPUs and as a baseline against which heavier Qwen3 models are judged.
- Add `Qwen3 14B` as the next current dense Qwen3 evaluation step when the exact VRAM/runtime/context budget supports it; do not jump directly from 8B to a much larger artifact without measuring whether 14B materially improves the user's accepted results.
- Treat `Qwen3 30B-A3B` and `Qwen3 32B` as larger current local candidates only when exact artifact residency/offload and performance are demonstrated. The MoE `30B-A3B` architecture does not make its checkpoint behave like a 3B memory footprint.
- Keep `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` as compact multimodal candidates when local text+image+audio understanding is a real requirement. Evaluate their multimodal projection/runtime path explicitly; do not assume a text-only backend configuration enables every advertised modality.
- Do not keep `Qwen2.5-Coder 7B Instruct` as the scenario's default coding recommendation merely because it was present in the legacy page. Coding-specific selection changes quickly and belongs primarily in the coding decision guide; the scenario may use current Qwen3 8B/14B as general local baselines and link the coding guide for a fresh task-specific shortlist.
- Do not force one local model to cover every workload. A user may reasonably keep a compact general LLM plus a separate image/speech/media model or escalate selected tasks to hosted models.

## NVIDIA Route

- For an NVIDIA gaming GPU, pin the exact card generation/SKU, VRAM, NVIDIA driver, CUDA compatibility, runtime/backend, model artifact/precision, context, and any multimodal auxiliary models before claiming support.
- Treat CUDA-capable execution and TensorRT/TensorRT for RTX execution as different compatibility claims. A model working through `llama.cpp`, another CUDA backend, or a framework does not prove that its exact operators/export are supported by TensorRT for RTX.
- Current TensorRT for RTX targets supported RTX generations including Turing/RTX 20-series and later families, but engine portability, precision features, and model/operator coverage vary by architecture and runtime version. Keep exact support as a mutable hardware/runtime fact rather than a scenario-level universal promise.
- Measure peak VRAM and latency under normal desktop contention. NVIDIA's ability to run compute and graphics concurrently does not eliminate resource contention with the display stack or a game.
- If a game or creative workload is expected to remain active during inference, benchmark that coexistence directly and preserve enough VRAM/thermal/power headroom for both rather than using an idle-desktop measurement.

## AMD Route

- For AMD Radeon/Ryzen-AI systems, require an exact **GPU/APU + OS + ROCm/Radeon Software/other backend + runtime version** support check before selecting a model.
- Do not generalize `ROCm supports AMD GPUs`. Current official support differs across Linux and Windows, consumer Radeon and datacenter Instinct, architecture generations, and ROCm releases; unsupported/unlisted combinations remain `Unknown` until validated through another explicitly supported backend.
- Distinguish discrete GPU, integrated GPU, NPU, and CPU execution. Record any partition/offload/fallback behavior that moves significant work away from the intended accelerator.
- When a community backend can run a combination outside AMD's official matrix, label that evidence separately from first-party support and require local measurement before recommending it as the stable starting route.

## Intel Route

- For Intel Arc/Core Ultra systems, pin exact GPU/NPU/CPU generation, OS, graphics/NPU drivers, OpenVINO/Windows ML/other backend, model export or GGUF route, precision/compression, and device assignment.
- Do not equate an `AI PC`, Arc GPU, or NPU TOPS figure with LLM/VLM compatibility. Current OpenVINO model and NPU paths depend on model architecture, export/compression, operator support, and runtime version.
- Distinguish CPU, iGPU/dGPU, and NPU execution and record fallback or partitioning when it materially changes latency or power.
- Treat vendor examples for one validated model/export as evidence for that exact route, not permission to generalize every GGUF or model family to the same accelerator.

## Context, Performance, and Quality Acceptance Test

- For each shortlisted artifact, record: exact model identity/version/artifact; quantization/precision; runtime/backend/version; accelerator/offload configuration; configured context; prompt size; peak GPU and system memory; first-token latency; sustained decode/generation rate or task latency; power/thermals; and accepted-result quality on the user's real tasks.
- Test at least one **short interactive** prompt and one **representative long/context-heavy** task. A model that is fast at short prompts can become unusable once KV/cache or multimodal state expands.
- If CPU/system-RAM offload is used, state the offload amount and measure the resulting latency. Do not compare a partially offloaded larger model with a fully GPU-resident smaller model as if they were the same execution class.
- If multiple applications or users will call a local service, test realistic concurrency/batch behavior; single-user benchmark numbers do not establish multi-client fit.
- Require accepted-result evaluation, not only tokens/second. Track retries, factual/source errors, coding test failures, formatting/schema failures, and the human correction time that materially affects the workload.

## Local Application and Local API Route

- A desktop GUI/runtime is the lowest-administration local starting point when only one person uses the model interactively.
- A local OpenAI-compatible or other local API can be useful when the same measured model should serve editors, coding tools, personal automations, or multiple local applications, but the API introduces an operational/security boundary.
- Bind local services to loopback by default when remote access is unnecessary. If LAN or remote access is required, use explicit authentication, firewall/network scoping, TLS or a trusted tunnel where applicable, and least exposure. Do not recommend an unauthenticated model endpoint on a broad network merely because the underlying model is local.
- Account for model reload time, process supervision, runtime/model updates, logs, power/sleep behavior, and driver restarts. A gaming desktop used opportunistically is not operationally equivalent to a managed hosted service or dedicated always-on inference server.
- If availability for other household devices or automations becomes important, compare keeping the desktop awake against a separate home-lab/self-hosted route rather than silently turning the gaming machine into infrastructure.

## Hybrid Hosted Escalation

- Preserve a hybrid route in which permitted routine/private-enough work stays local while harder, latency-sensitive, large-context, or unsupported-modality tasks can escalate to an approved hosted model.
- Make data classification **before** escalation. Do not send local/private material to a hosted route merely because the local model failed without checking whether that data may leave the device and what provider chain will receive it.
- Use hosted escalation when the accepted-result economics are better: for example, a stronger hosted model may cost less overall than waiting for a heavily offloaded local model and correcting weak output.
- Do not require a hosted fallback if offline/privacy constraints prohibit it; instead state the quality/capability ceiling and consider another local artifact/hardware class only when the gap is real and recurring.

## Power, Thermals, and Gaming Coexistence

- Include electricity, heat, fan/noise, and opportunity cost in total local cost when sustained inference is frequent. A sunk-cost GPU is not free to operate.
- Distinguish short interactive use from long batch generation/training-like workloads. Sustained power/thermal limits can reduce clocks and change throughput relative to a short benchmark.
- When the user also games on the machine, define whether inference must stop during games, share the GPU concurrently, or run only while idle. Each policy produces a different practical service/availability expectation.
- Do not recommend aggressive overclocking, undervolting, or thermal tuning as a prerequisite for model fit; hardware tuning is a separate operational/hardware topic and should follow vendor-safe practices.

## Cost and Upgrade Decision

- Compare **total cost per accepted result** across the existing-GPU route, hosted assistant/API, temporary rented accelerator, and—only after a demonstrated persistent gap—another hardware class.
- Include the existing GPU's electricity and time cost, local setup/maintenance, retries/correction time, and any productivity loss from game/desktop contention. The GPU's purchase price is sunk for this scenario, but operation and opportunity cost are not.
- Do not recommend buying another GPU merely because a larger model exists. Establish which real workload fails, why it fails (capacity, bandwidth, runtime compatibility, modality, context, throughput, availability, or quality), and whether hosted/rented execution solves the gap more economically.
- If a larger GPU would still not solve the dominant problem—for example model quality, unsupported modality, provider-only tool access, or need for managed availability—do not frame hardware purchase as the escalation path.

## Escalation Triggers

- Escalate from the smallest plausible local artifact to a larger local model only when measured accepted-result quality improves enough to justify additional memory, latency, and power cost.
- Escalate from full-GPU residency to partial CPU/RAM offload only when the resulting latency remains acceptable; otherwise prefer a smaller fully resident model or hosted route.
- Escalate to hosted/API execution when local quality, context, modality, runtime support, or latency cannot meet the real workload and the data boundary allows it.
- Escalate to temporary rented GPU capacity for bounded heavy workloads when local hardware is insufficient but persistent new hardware or a permanent server is not justified.
- Escalate to a dedicated home-lab/server scenario when always-on availability, multiple clients, orchestration, storage/RAG services, monitoring, or unattended operation become first-class requirements.
- Consider hardware purchasing only after exact existing-hardware measurements demonstrate a repeated capability/resource gap and alternatives have been compared.

## Hardware-Specific Model Selection Continuation

- Link the complete sibling journey `../../../hardware/` and `../../../hardware/sub/computers/`.
- Route NVIDIA systems to `../../../hardware/sub/computers/sub/nvidia/`, AMD systems to `../../../hardware/sub/computers/sub/amd/`, Intel systems to `../../../hardware/sub/computers/sub/intel/`, and another selected compute child when that is the actual inference accelerator.
- Keep detailed hardware/runtime support matrices in those hardware-first owners. This scenario owns the combined user decision and the conditions under which the reader should use those matrices.

## Canonical Links

- Link named current general models to canonical Model Reference identities: `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b`, `catalog/models/alibaba/qwen/qwen3/models/qwen3-14b`, `catalog/models/alibaba/qwen/qwen3/models/qwen3-30b-a3b`, and `catalog/models/alibaba/qwen/qwen3/models/qwen3-32b`.
- Link current compact multimodal candidates to `catalog/models/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/google/gemma/gemma-4/models/e4b-instruct`.
- Route coding-specific model choice to the canonical coding decision guide rather than freezing a legacy coder-model recommendation in this scenario.
- Link local runtime/software products to canonical catalog owners when named; do not duplicate their installation, backend, or complete compatibility documentation here.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current first-party NVIDIA TensorRT for RTX/CUDA compatibility documentation, AMD ROCm Radeon/Ryzen support matrices, Intel OpenVINO documentation, current official Qwen3/Gemma 4 artifacts, and canonical AI Lab model/hardware owners.
- GPU/OS/driver/runtime support matrices, model artifacts, quantization availability, backend operator coverage, and vendor runtime prerequisites are mutable. Recheck the exact route before rendering a current recommendation.
- Official artifact sizes and model cards establish checkpoint/capability facts; they do not establish measured VRAM consumption, tokens/second, thermals, or accepted-result quality on the reader's machine.
- Community runtime success outside a vendor support matrix is separate evidence and must not be presented as first-party support.

## Validation

- The scenario starts from already-owned hardware and never becomes a GPU purchase guide.
- No generic `8–16 GB` class, nominal VRAM figure, parameter count, MoE active-parameter count, artifact size, or successful model load is treated as practical-fit proof.
- Exact artifact/quantization/runtime/context/display contention and measured peak allocation are required for local fit claims.
- Qwen3 30B-A3B/32B Q4-class artifacts are not described as full-residency 16 GB routes; partial offload is clearly a different performance class.
- Vendor support claims remain exact to GPU/OS/runtime/version; NVIDIA, AMD, and Intel paths are not generalized across unsupported configurations.
- A local API has explicit exposure/authentication/availability boundaries and a gaming desktop is not treated as a managed server by default.
- Hybrid escalation applies the data boundary before content leaves the device.
- Power, thermals, desktop/game contention, correction time, and accepted-result quality participate in cost/fit evaluation.
- The hardware-specific continuation links sibling hardware owners instead of recreating their complete compatibility matrices.
- Mutable current claims carry the 2026-08-23 evidence boundary.
