# Documentation Requirements

## Scenario Fit

- Present this scenario for one professional using an Apple-Silicon Mac for software development, technical knowledge work, design, media, or multimodal creation where **unified-memory behavior and Apple-native runtime support materially change local model fit**.
- Keep the scenario about model-route selection on Apple Silicon, not Mac purchasing. Exact hardware buying, chip comparisons, memory-tier procurement, and upgrade advice belong outside this scenario.
- Distinguish this scenario from `software-engineer-with-local-gpu/`: discrete-GPU VRAM/offload/backend assumptions do not transfer directly to Apple unified memory.
- Distinguish it from `software-engineer-without-local-gpu/`: Apple Silicon can provide useful local GPU acceleration even without a discrete GPU, but only when the exact runtime/model/workload is measured.
- Keep creator-specific modality/tool selection bounded. If image/video/audio generation becomes the dominant decision, route to the applicable modality decision guide/content rather than turning this page into a complete creative-software guide.

## Unified Memory Is the Governing Constraint

- Treat Apple unified memory as one shared pool used by CPU, GPU, macOS, applications, model weights, runtime buffers, context/KV cache, multimodal components, and other active workloads.
- Current MLX documentation confirms that CPU and GPU directly access the same memory pool and MLX arrays do not require explicit CPU↔GPU copies. Treat that architecture as a runtime property, not proof that any model fitting numerically in unified memory is practical.
- Replace legacy `16 GB`, `24–32 GB`, and `32 GB+` model tiers with **usable-memory measurement on the exact Mac**. Retain historical examples only as evaluation context when needed, never as guaranteed fit boundaries.
- Measure memory pressure with the real professional workload open: IDE/editor, browser, containers/VMs, design/media applications, local databases, build tools, and communication clients can materially reduce model headroom.
- Leave operating-system and application reserve rather than targeting 100% nominal memory occupancy. Swap/compression or heavy memory pressure can make an otherwise loadable model unacceptable for interactive work.

## Native Runtime Route

- Prefer Apple-native or Apple-optimized runtimes when they materially improve support/performance for the chosen model and workload.
- MLX is the current Apple machine-learning framework to evaluate first for supported local workflows. Current MLX/MLX-LM supports Apple-Silicon CPU/GPU execution, Hugging Face model loading, model quantization, generation, fine-tuning, and distributed inference/fine-tuning for supported architectures.
- Do not assume every Hugging Face model works correctly merely because MLX-LM integrates with the Hub. Verify the exact architecture, conversion/artifact, tokenizer/chat template, quantization, modality path, and runtime version.
- Keep llama.cpp or another runtime as a credible alternative when GGUF support, specific quantizations, application integrations, or model architecture support are better for the selected workload. Compare measured results rather than assuming one runtime is universally best on Apple Silicon.
- Treat runtime conversion/community artifacts as separate evidence from the original model. Verify the artifact producer, quantization method, model revision, and any conversion caveats before recommending it.

## Separate Professional Workloads

- Classify recurring work before selecting one model/runtime:
  - code completion and bounded edits;
  - repository understanding, debugging, tests, and code review;
  - writing, summarization, translation, and research assistance;
  - private document/image/audio understanding;
  - multimodal screenshot/UI/design analysis;
  - local embeddings/retrieval or personal/project knowledge support;
  - image/media generation or editing when a supported local pipeline exists;
  - agentic terminal/tool use;
  - fine-tuning/LoRA experimentation when relevant.
- Do not require one local model to own all modalities. A compact text model, coding model, multimodal model, diffusion/media model, hosted assistant, and deterministic development/creative tools can coexist.
- Preserve professional source-of-truth systems: repository/tests for code, original documents/assets for content, and native project files for design/media. Model output remains generated assistance rather than authoritative state.

## Local Text and Coding Route

- Use local accelerated text/coding models when privacy, offline availability, fast repeated bounded work, provider independence, or experimentation justifies local setup.
- Keep `Phi-4 Mini Instruct` and `Qwen3 8B` as compact local evaluation candidates where their task quality is sufficient. Keep `Qwen3 14B` or coding-specific larger models only when exact MLX/alternate-runtime artifacts and measured memory/latency justify them.
- For software engineering, consume current candidate selection from `decision-guides/software-development/`; do not create a Mac-specific universal coding-model ranking.
- Compare small/fast and larger/slower candidates on accepted-result quality and end-to-end professional throughput. A larger model is not automatically preferable if it causes memory pressure, slower prompts, reduced context headroom, or blocks normal applications.
- For coding agents, measure complete-loop performance—file selection, edits, commands, tests, recovery, stopping, and final diff—not only single-prompt coding quality.

## Local Multimodal Route

- Use local multimodal models when private image/document/audio understanding materially matters and the exact Apple runtime supports the complete modality path.
- `Gemma 4 E2B Instruct` is a current compact multimodal candidate to evaluate first for constrained Apple-Silicon environments; `Gemma 4 E4B Instruct` is a larger alternative when measured memory/performance supports it.
- Do not infer that text-only runtime support implies image/audio support. Verify preprocessing, vision/audio encoder support, prompt format, artifact conversion, context behavior, and output quality for the exact runtime.
- Account for additional memory and latency from multimodal encoders, image/audio preprocessing, large attachments, and long contexts.
- For design/UI work, verify model observations against the real source image/application state. Visual description is not a pixel-accurate regression test or design measurement.

## Creative Media Route

- Treat local image/audio/video generation as a separate workload class from LLM inference. Runtime and memory fit can differ radically even on the same Mac.
- Current MLX includes examples and ecosystem support for machine-learning workloads beyond text, including image-generation and speech-oriented experimentation; do not interpret framework capability as support for every current creative model.
- Verify exact model architecture, runtime implementation, resolution/duration, precision, peak memory, iteration time, and project integration before recommending local creative generation.
- Compare local generation against hosted creative services by accepted output quality, iteration time, privacy/IP boundary, asset transfer friction, rights/provenance requirements, and cost—not only whether a pipeline runs.
- If media generation becomes the dominant decision, continue into the modality-specific model-selection owner.

## Memory, Context, and Quantization

- Treat weights as only part of runtime memory. Include context/KV cache, temporary buffers, graph allocations, modality encoders, prompt cache, concurrent generation, and other applications.
- Treat context length as a tunable operating point. A model's advertised maximum context can be unusable on a fixed-memory Mac because memory and prompt-processing time grow materially.
- Test the context actually needed for codebase work, long documents, multimodal files, and agent history instead of maximizing context by default.
- Quantization reduces model-weight memory but can change speed and accepted-result quality. Verify the exact MLX/other runtime quantization implementation and artifact rather than relying on nominal bit width.
- Do not convert artifact size directly into `required unified memory`. Runtime allocations and professional application reserve remain separate.

## MLX Quantization and Model Artifacts

- Current MLX-LM supports quantization workflows and use of quantized model artifacts. Treat the quantization method, group size/format where relevant, model revision, and conversion source as part of reproducibility.
- Prefer official model weights plus a well-defined reproducible conversion/quantization path when practical. Community-converted artifacts can be useful, but their identity and provenance must remain explicit.
- Evaluate at least one quality baseline when changing quantization materially. Code generation, tool-call formatting, multilingual behavior, reasoning, and multimodal accuracy can degrade differently.
- Recheck runtime/model compatibility after major MLX or model-family updates rather than assuming an old converted artifact remains the best route.

## Performance Measurements

- Measure time to first token, prompt-processing throughput, sustained generation rate, peak/steady memory use, end-to-end task time, device temperature/power behavior where observable, and correction/review burden.
- Run measurements with normal professional applications open so unified-memory contention is represented.
- Separate cold model load from warm repeated interaction; both can matter to desktop usability.
- For long tasks, observe whether memory pressure/swap increases over the session and whether performance degrades as context or tool history grows.
- For creative/multimodal work, measure complete iteration time including preprocessing/loading and output generation, not only model-core throughput.
- Record Mac chip/model, total memory, macOS version, runtime version, model artifact/quantization, context, and workload so results remain reproducible.

## Fine-Tuning and Adaptation

- Present local LoRA/fine-tuning as an advanced optional route when the user has a clear repeated domain/style/task gap and a proper evaluation set.
- Current MLX-LM supports low-rank and full-model fine-tuning, including quantized-model workflows for supported architectures. This capability does not mean fine-tuning is automatically better than prompting, retrieval, examples, or a stronger model.
- Include dataset preparation, rights/privacy, overfitting, evaluation, checkpoint storage, training time, memory pressure, and rollback/reproducibility in the decision.
- Do not fine-tune on employer/client/private material unless the data boundary and resulting checkpoints/artifacts are explicitly permitted.

## Local Agent and Tool Boundary

- A local model can power an agent while still creating side effects through shell, filesystem, browser, MCP, Git, or external APIs.
- Preserve sandboxing, least privilege, secret isolation, recoverable Git/worktree state, explicit high-impact approvals, and repository-native verification.
- Do not equate local inference with safe autonomous execution. Prompt injection from repository files, documents, web content, issues, or tool output still applies.
- A compact local model may be an effective bounded worker/router/reviewer without being reliable as a primary long-running orchestrator.
- Escalate difficult agent loops to a stronger local or approved hosted model only when the data-routing rule permits it and accepted-result measurements justify the change.

## Hosted and Hybrid Route

- Preserve hosted managed assistants/APIs as a first-class alternative even when the Mac can run useful local models.
- Use hybrid routing when private/routine workloads succeed locally but difficult long-context, research, coding-agent, or multimodal tasks materially benefit from hosted capability.
- Define an explicit data-routing rule before hybrid use: which source/code/assets may leave the Mac, which must be sanitized, and which remain local-only.
- Do not silently fall back to cloud inference from a local application. Surface remote provider use and treat it as a separate data boundary.
- Compare local versus hosted using the same acceptance tasks and total cost, including correction time and local workflow disruption.

## Professional Data and IP Boundary

- Classify employer/client source code, design assets, media, documents, unpublished work, model-training data, and customer information before choosing hosted/local routes.
- A local model keeps model inference local only if the complete client/runtime/tool path stays local. Extensions, cloud sync, telemetry, remote search, embeddings, MCP servers, and connected services can still transmit data.
- Keep credentials, signing keys, cloud tokens, private keys, production config, customer datasets, and recovery codes out of model context unless explicitly necessary and safely bounded.
- Local checkpoints, caches, prompt histories, converted models, fine-tunes, and generated assets can themselves become sensitive artifacts requiring normal access control and backup policy.

## Cost per Accepted Professional Outcome

- Compare routes by **total cost per accepted outcome**: subscription/API spend, local power, storage, setup/update time, conversion/quantization effort, memory pressure on paid professional applications, correction/review time, and failure/retry cost.
- Do not treat owned Mac hardware as zero marginal cost when heavy local inference materially interferes with builds, containers, design/video workloads, battery life, thermals, or responsiveness.
- Do not force a larger local model merely to use available unified memory. A compact model can be the better route when it preserves interactive performance and still passes acceptance.
- Conversely, a hosted service can be cheaper overall when it avoids sustained local memory pressure and substantially reduces human review/correction time.

## Escalation Triggers

- Move from compact to larger local models only when the current model repeatedly fails accepted quality and measured memory/performance headroom exists.
- Move to a smaller/quantized model when memory pressure, swap, context headroom, latency, or application contention prevents productive use; then revalidate quality.
- Move to hosted/API capability when local quality, context, modality support, or agent-loop reliability remains insufficient.
- Move toward `software-engineer-with-local-gpu/` when a discrete non-Apple accelerator becomes the governing local inference target.
- Move toward `software-engineer-without-local-gpu/` when local Apple acceleration is not useful for the intended workload and hosted/CPU routes dominate.
- Move toward `sensitive-data-professional/` or high-security organization routes when confidentiality/isolation requirements dominate beyond ordinary professional controls.
- Move to team/internal-platform scenarios when the Mac-hosted endpoint becomes shared multi-user infrastructure.

## Hardware-Specific Model Selection Continuation

- Link the complete `../../../hardware/` journey whenever exact Mac hardware materially constrains the route.
- Use `../../../hardware/sub/computers/sub/apple/` as the canonical Apple-Silicon hardware continuation for current chip, unified-memory, runtime, and exact model-fit analysis.
- Do not infer hardware purchase recommendations from a scenario fit result. The current Mac may simply imply a hosted, compact-local, or hybrid route.

## Canonical Links

- Link `Phi-4 Mini Instruct` to `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct` when named.
- Link `Qwen3 8B` and `Qwen3 14B` to their exact canonical Qwen3 model identities when named.
- Link `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` to their exact canonical Gemma 4 model identities when named.
- Link coding candidate selection to `catalog/models/selection/decision-guides/software-development` rather than duplicating a Mac-specific coding ranking.
- Link modality-specific decision guides when creative/media generation becomes dominant.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Apple MLX unified-memory documentation, current MLX/MLX-LM capabilities, canonical AI Lab model owners, and the selected Apple hardware continuation.
- Current MLX evidence establishes Apple-Silicon shared CPU/GPU memory behavior and current framework/LLM runtime capabilities such as quantization, generation, fine-tuning, and distributed execution. It does not establish exact fit or accepted-result quality for a particular Mac/model/workload.
- Remove legacy fixed-memory tiers as recommendation boundaries. Any retained memory number is evidence context only and must be tied to an exact Mac, runtime, artifact, context, applications, and measured outcome.
- MLX/model architecture support, converted artifacts, quantization methods, macOS/runtime behavior, hosted-service features/pricing, and model aliases are mutable; recheck them before rendering current guidance.
- Keep unmeasured Mac/model/modality combinations `Unknown` rather than extrapolating from another chip or memory configuration.

## Validation

- Unified memory is treated as a shared system resource, not GPU VRAM plus separately available system RAM.
- Legacy 16/24/32 GB thresholds are not presented as guaranteed model tiers.
- Exact runtime/model/quantization/context/application load and measured performance determine local fit.
- MLX capability is not treated as proof that every Hub model or modality is supported.
- Local text, coding, multimodal, creative, fine-tuning, and agent workflows remain distinct where their runtime/memory/evaluation needs differ.
- Local inference is not equated with complete workflow privacy or autonomous safety.
- Hybrid fallback uses an explicit data-routing rule.
- Hardware fit is delegated to `hardware/computers/apple/` and hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
