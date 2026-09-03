# Documentation Requirements

## Scenario Fit

- Present this scenario for one software engineer whose normal development workstation has a **useful local GPU or accelerator that has been verified for the intended inference runtime and model workload**.
- Do not define scenario membership from a vendor badge, nominal VRAM amount, TOPS figure, or the fact that a model can load. The accelerator must materially improve the user's actual coding/model workflow at acceptable context, latency, throughput, thermals, and quality.
- Distinguish this scenario from `software-engineer-without-local-gpu/`: that route treats hosted/API/temporary acceleration as the capability default and CPU-local inference as bounded fallback; this route makes local accelerated inference a first-order option worth comparing against hosted coding products.
- Distinguish it from `mac-developer-or-creator/`: Apple-Silicon unified-memory/MLX constraints have materially different memory/runtime behavior and own their own scenario.
- Keep generic coding-model ranking in `decision-guides/software-development/`, complete-loop agent evaluation in `decision-guides/agents-and-automation/`, and exact hardware fit in sibling `hardware/` selection. This scenario owns the **professional local-GPU coding route trade-off**.

## Start From the Exact Hardware and Runtime Boundary

- Identify the exact GPU/accelerator model, usable VRAM or shared-memory budget, host RAM, CPU, OS, driver/runtime stack, PCIe/interconnect topology where material, monitor/display reservation, and other concurrent developer workloads before selecting a model.
- Verify runtime support for the exact hardware generation rather than extrapolating from vendor family names. Current serving/runtime support differs across NVIDIA CUDA, AMD ROCm, Intel GPU, Apple/Metal, Vulkan, and other backends, and feature parity is not guaranteed.
- Treat quantization support as runtime-and-hardware-specific. Current vLLM documentation, for example, distinguishes AWQ, GPTQ, Marlin, FP8, INT8, bitsandbytes, GGUF, and other formats by GPU architecture; a quantization format that exists is not necessarily efficient or supported on the user's device.
- Treat GPU offload as a spectrum rather than a binary state. Current llama.cpp supports partial/full layer offload and multi-GPU splitting; when the model or KV/context does not fit fully in device memory, CPU fallback can materially change prompt processing and generation latency.
- Record the exact model artifact, precision/quantization, runtime version, context size, KV-cache format, batch/concurrency settings, and GPU-offload configuration used for any practical-fit conclusion.

## Separate the Engineering Workloads

- Classify recurring tasks before deciding how much local inference is worth operating:
  - inline completion and bounded edits;
  - code explanation and repository navigation;
  - multi-file implementation/refactoring;
  - debugging and failure diagnosis;
  - tests and test repair;
  - code review and security review;
  - architecture/design reasoning;
  - terminal/tool-driven agentic engineering;
  - long-running issue-to-PR work;
  - multimodal screenshot/UI/document work;
  - private or offline engineering workflows.
- Do not require one local model to serve all workloads. A small fast local model, larger local coding model, hosted capability model, direct API, deterministic static-analysis/test tools, and cloud coding agent can coexist when each has a measurable role.
- Preserve repository-native build/test/typecheck/lint/CI results as the acceptance evidence. Local inference changes the execution boundary, not the verification contract.

## Local-First Route

- Use local accelerated inference as the primary route when source-code privacy, offline availability, low marginal usage cost, provider independence, fast repeated bounded interactions, or experimentation materially outweigh the setup/maintenance burden.
- Prefer a local model only after measuring it on the user's actual repository tasks. Compare code correctness, repository understanding, tool use, recovery from failing tests, latency, context behavior, correction effort, and cost per accepted change.
- Keep local execution especially attractive for private repository exploration, code explanation, bounded refactors, local retrieval/reranking, test generation, review preprocessing, or agent workers whose tasks fit the verified capability tier.
- Do not assume local is automatically faster. Prompt processing for large repositories, long context, CPU fallback, constrained memory bandwidth, low-end GPUs, and concurrent IDE/build workloads can make a local route slower than a hosted model.
- Do not assume local is automatically private. The editor/agent client, telemetry, extensions, embeddings/indexing service, package tools, web search, MCP servers, remote storage, or fallback provider can still transmit source data.

## Candidate Local Coding Models

- Consume the concrete candidate shortlist from `decision-guides/software-development/` rather than creating a permanent ranking here.
- `Qwen3-Coder 30B-A3B Instruct` is a current self-hostable coding/agentic-coding evaluation candidate with 30.5B total / 3.3B active MoE scale and 262,144-token native context. Treat these as model identity/capability facts, not a statement that it fits any specific GPU.
- `Qwen3-Coder-Next` is a distinct larger 80B-total / 3B-active coding-agent model with 262,144-token native context. Do not infer that `3B active` implies 3B-dense storage/VRAM requirements or that it is automatically practical on a consumer GPU.
- Keep compact candidates such as `Qwen2.5-Coder 7B Instruct` available as reproducible lower-resource baselines when a larger model's accepted-result advantage does not justify its memory/latency cost.
- Retain another local/open coding model only when current first-party identity and runtime support are verified and the model materially changes the evaluation set for the user's hardware class.
- Provider benchmark results and coding-agent positioning establish eligibility for evaluation, not AI Lab proof that a candidate wins on the user's codebase.

## VRAM, Host RAM, and Context

- Treat model weights as only one part of memory demand. Include runtime buffers, KV cache, attention/workspace allocations, graph/backend overhead, multimodal encoders where applicable, and display/desktop reservations on shared GPUs.
- State context as an operating choice, not just the model's advertised maximum. Long context increases KV/cache and prompt-processing cost, and the useful context can be materially lower than the model's nominal maximum on a fixed GPU.
- Measure the exact context sizes used by real tasks: small-edit context, repository-context retrieval, large-file review, and agent-loop history can have different practical ceilings.
- If the runtime partially offloads a model, measure both prefill and token-generation behavior after offload. A configuration that technically fits through CPU fallback can fail the interactive latency target.
- On shared-memory or resizable-BAR/unified-host arrangements, distinguish addressable memory from high-bandwidth device memory. Do not equate host RAM availability with GPU-speed inference.

## Quantization and Precision

- Select quantization/precision from the exact runtime and GPU support matrix, then evaluate quality and performance on the target tasks.
- Do not assume lower-bit quantization is always faster. Kernel support, dequantization overhead, GPU architecture, batch size, memory bandwidth, runtime implementation, and model architecture can reverse the expected result.
- Preserve a higher-precision or alternate quantization baseline when evaluating whether memory savings introduce unacceptable code-quality, instruction-following, tool-call, or long-context regressions.
- Treat quantized artifact size as storage evidence only. It does not by itself predict total runtime VRAM or host-memory demand.
- Recheck runtime support when changing GPU generation or backend: a format optimized for one architecture may fall back or fail on another.

## NVIDIA, AMD, and Other GPU Routes

- Keep vendor paths separate when runtime/toolchain differences materially change usability.
- For NVIDIA, verify current CUDA compute-capability/runtime requirements, quantization kernels, flash-attention support, driver/CUDA compatibility, and the exact serving/inference stack.
- For AMD, verify current ROCm support for the exact consumer/workstation GPU and OS. Do not generalize from data-center MI-series support to every Radeon generation or from one runtime to another.
- For Intel or other GPU backends, verify model architecture, kernels, quantization format, and feature support from the selected runtime rather than inferring parity with CUDA.
- If the chosen runtime does not support a required model/operator/quantization efficiently, a theoretically capable GPU may still be the wrong local route.

## Multi-GPU and Partial Offload

- Consider multi-GPU only when the user already has the hardware and the workload justifies added complexity; do not turn this scenario into GPU purchasing advice.
- Current llama.cpp supports layer/row/tensor-style splitting with explicit device selection and notes that KV cache, interconnect speed, NCCL availability, and split mode can materially affect performance.
- Measure inter-GPU communication and PCIe/NVLink/topology effects rather than summing VRAM and assuming single-GPU-equivalent performance.
- Prefer the simplest configuration that passes acceptance. A smaller model fitting on one GPU can outperform a larger split model in latency, reliability, setup cost, or accepted-result economics.
- Keep unsupported or unmeasured multi-GPU combinations explicitly `Unknown`.

## Local Serving and Development Integration

- Distinguish one-process desktop inference from a persistent local API/server used by IDEs or agents.
- If exposing a local OpenAI-compatible or other inference endpoint, bind it safely, require authentication when it crosses a trusted-process boundary, and avoid exposing it broadly on LAN/WAN merely for convenience.
- Record which client constructs prompts and repository context. A local model server can still receive excessive secrets or unrelated files if the agent/editor context builder is misconfigured.
- For simultaneous editor completion, chat, embeddings, agent workers, and build/test activity, measure contention and concurrency rather than benchmarking the model alone on an idle machine.
- If the endpoint becomes multi-user, remotely accessible, or operationally persistent with quotas/monitoring/backups, route infrastructure concerns to the applicable server/home-lab/internal-platform owners.

## Agentic Local Coding

- Treat tool-using local agents as side-effecting systems even when the model inference never leaves the machine.
- Evaluate complete-loop reliability: task decomposition, correct file selection, patch quality, terminal commands, test execution, recovery from failures, context retention, stopping behavior, and final verification.
- A smaller local model may be useful as a bounded worker, classifier, reviewer, or preprocessor without being reliable enough as the primary autonomous coding agent.
- Do not promote a local coding model to long-running autonomous work solely because it supports tool-call syntax or performs well on provider coding benchmarks.
- Preserve least privilege, sandboxing, branch/worktree isolation where applicable, secret boundaries, and explicit human approval for destructive Git operations, publishing, deployment, access-control changes, or other high-impact actions.
- Prompt injection from repository files, issue text, documentation, generated artifacts, or retrieved web content remains relevant even with local inference.

## Hosted and Hybrid Fallback

- Keep a hosted coding assistant/API as a credible fallback when the local model repeatedly fails on large-repository reasoning, long context, difficult debugging, multimodal work, or complete-loop agent reliability.
- A hybrid route can keep private indexing/retrieval, source preprocessing, or bounded edits local while sending only the minimum necessary sanitized context to a stronger hosted model when policy allows.
- Compare the local-first route against hosted alternatives using the same acceptance suite. Local control is valuable only if the resulting engineering throughput and quality remain acceptable.
- If provider policy permits hosted code and the stronger hosted model consistently saves more developer review time than local inference saves subscription/API cost, hosted can be the lower total-cost route despite existing GPU ownership.

## Data Boundary and Secrets

- Classify source code, configuration, logs, issue data, generated artifacts, and test fixtures before allowing any component to send them outside the machine.
- Verify whether the editor/agent sends code context to hosted embeddings, rerankers, web tools, MCP servers, crash/telemetry services, or fallback models.
- Keep credentials, signing keys, cloud tokens, production configuration, customer exports, private keys, recovery codes, and other secrets out of model context unless explicitly required and safely bounded.
- A local model does not remove endpoint-security, disk-encryption, account isolation, malware, extension, dependency, or backup risks.

## Performance and Acceptance Measurements

- Measure at least time to first token, prompt-processing throughput for representative code context, sustained generation rate, end-to-end task latency, GPU/host memory usage, power/thermals, and correction/review burden.
- For agent workloads, also measure tool-call success, test/retry loops, commands executed, elapsed wall time, context growth, and proportion of runs that finish with verifiable acceptance evidence.
- Test under realistic developer load with the IDE, browser, containers/VMs, build tools, databases, and other normal services running when they compete for CPU/RAM/GPU resources.
- Repeat enough runs to distinguish warm-cache behavior from initial load and to expose thermal throttling or memory fragmentation.
- Preserve benchmark environment details so later runtime/model changes can be compared rather than remembered informally.

## Cost per Accepted Engineering Change

- Compare **total cost per accepted engineering change**: already-owned GPU opportunity/power cost, setup/maintenance time, local storage, runtime upgrades, failed attempts, developer correction/review time, hosted fallback spend, and hardware contention with other workloads.
- Do not treat owned hardware as zero-cost when it materially consumes power, blocks graphics/creative workloads, increases heat/noise, or requires substantial maintenance.
- Likewise, do not force the local route merely to justify existing hardware. If a hosted tool produces accepted changes more efficiently, use it for the workloads where it wins.
- A smaller local model can be optimal when its lower latency and lower correction burden beat a larger model that is slower or only marginally better on the actual task.

## Escalation Triggers

- Move to a stronger local model when the current candidate repeatedly fails capability acceptance and the exact hardware/runtime still has verified headroom.
- Move to a smaller or more aggressively quantized model when context, concurrency, latency, or VRAM pressure prevents interactive use, but revalidate code quality after the change.
- Move to hosted/API capability when local accepted-result quality or complete-loop reliability remains insufficient despite reasonable tuning.
- Move toward `software-engineer-without-local-gpu/` if the accelerator becomes unavailable or proves not useful for the intended workload.
- Move toward `mac-developer-or-creator/` when Apple-Silicon/MLX execution becomes the governing hardware boundary.
- Move toward `sensitive-data-professional/` or high-security organization routes when source-code classification or isolation requirements dominate beyond ordinary professional controls.
- Move to team/internal-platform scenarios when the local model service becomes shared infrastructure with standardized models, quotas, observability, policy, or multiple developers.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` for exact GPU/runtime/model-fit work.
- Continue into `../../../hardware/sub/computers/` for the workstation/laptop route and then the applicable accelerator/vendor specialization selected by the hardware tree.
- If the accelerator is in a dedicated remote machine rather than the developer workstation, continue through the applicable `../../../hardware/sub/servers/` route.
- Do not recommend purchasing another GPU from this scenario; compare the verified owned hardware against hosted, rented, remote, or hybrid routes instead.

## Canonical Links

- Link `Qwen3-Coder 30B-A3B Instruct` to `catalog/models/reference/producers/alibaba/qwen/qwen3-coder/models/qwen3-coder-30b-a3b-instruct` when named.
- Link `Qwen3-Coder-Next` to `catalog/models/reference/producers/alibaba/qwen/qwen3-coder/models/qwen3-coder-next` when named.
- Link compact baselines such as `Qwen2.5-Coder 7B Instruct` to their exact canonical Model Reference identities when retained.
- Link generic coding-model evaluation to `catalog/models/selection/decision-guides/software-development` and agent complete-loop evaluation to `catalog/models/selection/decision-guides/agents-and-automation` rather than duplicating their ranking/candidate ownership.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current official Qwen3-Coder model repositories, current vLLM installation/quantization hardware matrices, current llama.cpp GPU-offload/multi-GPU documentation, and canonical AI Lab coding/agent decision guides.
- Current runtime evidence confirms that GPU-vendor generation, backend, quantization, offload, context/KV configuration, and multi-GPU topology materially affect support and performance; nominal VRAM alone is insufficient practical-fit evidence.
- Current Qwen3-Coder 30B-A3B Instruct and Qwen3-Coder-Next model cards establish exact identity/architecture/context/provider positioning, not fit on a specific consumer/workstation GPU or independent repository-level quality.
- Driver/runtime versions, GPU support, quantization kernels, model artifacts, context behavior, serving features, and hosted fallback prices/limits are mutable; recheck them before rendering current recommendations.
- Keep unsupported, unbenchmarked, or topology-specific combinations `Unknown` rather than generalizing from another GPU generation or runtime.

## Validation

- Scenario membership depends on a **verified useful local accelerator**, not nominal GPU ownership.
- Exact GPU, runtime, model artifact, quantization/precision, context/KV, offload, and concurrent workload are part of every practical-fit conclusion.
- VRAM, parameter count, active MoE parameters, artifact size, and load success are not used as standalone fit proofs.
- NVIDIA/AMD/Intel/other backend differences remain explicit where they affect support.
- Multi-GPU capacity is not treated as simple additive single-GPU performance.
- Local inference is not equated with complete workflow privacy or security.
- Local agent tool use retains permission, sandbox, prompt-injection, secret, and verification controls.
- Hosted/hybrid fallback remains valid when local quality, context, or loop reliability is insufficient.
- Exact local model identities remain canonical and candidate ranking stays in the software-development decision guide.
- Hardware purchasing remains outside this scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
