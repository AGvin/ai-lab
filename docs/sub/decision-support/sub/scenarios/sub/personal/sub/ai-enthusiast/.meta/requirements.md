# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual whose primary goal is **hands-on AI experimentation**: comparing open and hosted models, runtimes, quantizations, modalities, tool use, local APIs, prompt formats, agent behavior, and deployment routes while accepting frequent ecosystem change.
- Keep this scenario experimentation-first. Persistent uptime, household service reliability, remote multi-user access, backups, monitoring, storage architecture, and hardened unattended operation belong in `home-lab-owner/` once those become first-class requirements.
- Do not require one permanent resident model or one preferred runtime. Easy replacement, reproducible comparison, and low switching cost are legitimate primary values for this user.
- Keep hardware purchasing outside this scenario. Exact owned hardware constrains experiments; if fixed-device fit becomes the main question, continue into sibling `../../../hardware/` selection.

## Experimental Method

- Require each meaningful experiment to begin with a question or hypothesis such as `Does a larger dense model improve my coding acceptance rate enough to justify latency?`, `How much quality do I lose moving from Q8 to Q4?`, or `Does this VLM's local audio path actually work in my runtime?`.
- Change **one major variable at a time** where practical. Do not compare a new model, new quantization, new runtime, larger context, different system prompt, and different hardware simultaneously and then attribute the result to model quality.
- Record enough experiment context to reproduce the result: exact canonical model identity/version/artifact, source, quantization/precision, runtime/backend/version, hardware target, accelerator/offload split, context configuration, prompt/template, sampling/reasoning settings, modalities/auxiliary files, tools, test input, and date.
- Where deterministic reproduction is impossible because a hosted service or stochastic model is mutable, preserve the service/model label exposed at test time, relevant settings, representative inputs/outputs or acceptance result, and the verification date instead of pretending the result is immutable.
- Use a stable **baseline workload set** across experiments. Include several real tasks the user actually values rather than relying only on public benchmark numbers or one attractive demo prompt.
- Evaluate accepted-result quality together with latency, peak memory, context behavior, retries, tool/schema failures, setup effort, and monetary/energy cost. A model that wins one benchmark but requires more correction or administration can lose the practical experiment.

## Route Matrix

- Treat managed assistant, direct hosted API, local interactive runtime, local API/server, temporary rented accelerator, and hybrid combinations as separate experiment routes rather than a maturity ladder.
- Use managed assistants for rapid capability reconnaissance when product tools/UI are themselves part of the question. Do not use a consumer assistant result as evidence for a raw model/API when the application adds retrieval, tools, hidden routing, memory, post-processing, or other product behavior.
- Use direct APIs when the experiment needs repeatable programmatic prompts, structured outputs, batch runs, tool calls, latency/cost logging, or access to hosted models without product-UI confounders. Apply spend caps and keep API credentials out of prompts, logs, repositories, and notebooks.
- Use a local interactive runtime when the question is model/artifact fit, privacy/offline behavior, quantization, or quick comparison and a GUI/desktop workflow minimizes setup friction.
- Use a local API/server when multiple clients or automated eval scripts need a stable endpoint; treat network exposure, authentication, model reloads, concurrency, and runtime version as experiment variables rather than assuming localhost results transfer to service operation.
- Use temporary rented GPU capacity when an open-weight experiment exceeds owned hardware or needs a short burst of repeatable accelerator time. Include image/container startup, model download/cache, storage, warm-up, idle billing, shutdown, and egress/persistence behavior in the experiment cost.
- Use hybrid experiments when local and hosted routes answer different questions. Apply data classification before any input crosses from local to hosted infrastructure.

## Current Local Baseline Ladder

- Use `Qwen3 8B` as a compact current general text/reasoning baseline when the target hardware supports the selected artifact. It is useful for establishing whether a larger experiment materially beats a relatively accessible local model.
- Use `Qwen3 14B` as a larger dense comparison when memory/headroom permits. Measure whether the accepted-result improvement justifies higher latency, memory, and power rather than assuming the larger parameter count is automatically worthwhile.
- Use `Qwen3 30B-A3B` and `Qwen3 32B` as larger experiments only with exact artifact/resource evidence. The MoE model's approximately 3B active parameters do **not** imply a 3B-class checkpoint or memory footprint.
- Use `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` as compact current multimodal experiments when text+image+audio understanding is relevant. Keep text-only and multimodal runtime paths separate because auxiliary/projector/encoder support can materially change compatibility and memory.
- Use `Mistral Small 4` as a current example of why **active parameter count is not a hardware class**. Its official specification describes 119B total parameters with about 6.5B active and a much larger GPU-memory range than a conventional 6–8B dense model. Do not infer local fit from `6.5B active`; evaluate the actual checkpoint/precision/runtime route.
- Treat these named models as **current baselines and experiment candidates**, not a complete or permanent 2026 leaderboard. The open-weight landscape changes faster than scenario architecture.
- When current research identifies a materially better candidate that lacks a canonical Model Reference identity, add/refresh that canonical owner before naming it as a durable scenario recommendation. Do not let the existing catalog silently constrain research to older models.

## Quantization and Artifact Experiments

- Treat quantization as an artifact-level experiment, not merely a smaller download. Record source model/version, quantization method and level, runtime/backend, context, accelerator residency/offload, and whether the artifact is official, upstream, or community-produced.
- When evaluating quantization quality, compare multiple precisions of the **same model** under otherwise equivalent conditions before comparing across different models.
- Measure peak device and system memory rather than using weight-file size as the memory result. Include KV/context state, runtime buffers, multimodal components, graph/engine allocations, fragmentation, and application/display reserve.
- Compare short and long-context workloads. Lower weight memory can create context headroom, but a nominal maximum context is not proof of usable long-context quality or acceptable KV/cache cost.
- Do not label Q4, Q5, Q8, FP8, NVFP4, MXFP4, INT4, or another precision as universally superior. Hardware support, kernel/backend path, calibration method, model family, and task sensitivity can change the result.
- Keep conversion reproducibility visible. A community conversion may be highly useful while still requiring separate provenance and compatibility evidence from the original upstream model.

## Runtime Experiments

- Compare runtimes only on routes they actually support. A model imported into LM Studio through GGUF/MLX, an Ollama package, a `llama.cpp` CLI/server build, a vLLM deployment, or a vendor-specific backend may expose different quantizations, templates, tool calling, multimodal support, cache behavior, and accelerator kernels.
- LM Studio is a useful low-friction experimentation surface because current versions can search/download GGUF or MLX variants, import external GGUF artifacts, load with configurable context/GPU offload, and expose local REST/OpenAI-compatible/Anthropic-compatible endpoints. Treat its runtime version and selected model artifact as part of every result.
- A convenient model catalog entry or runtime metadata field is discovery/configuration evidence, not independent proof that the model fits the user's exact machine or task.
- When the experiment concerns runtime performance, keep model artifact, context, prompt, hardware state, and sampling fixed enough that backend changes are the primary variable.
- When a runtime update materially changes kernels, model architecture support, context handling, tool templates, or memory behavior, invalidate old runtime-performance conclusions rather than carrying them forward silently.

## Hosted Model and Product Experiments

- Separate three questions: `Which model is better?`, `Which provider API route is better?`, and `Which assistant product is better?`. Do not compare them as if they were interchangeable.
- For direct API experiments, record exact exposed model/version alias where possible, input/output/tool usage, latency, accepted-result rate, and current price/rate-limit boundary. Mutable aliases require revalidation.
- For managed-assistant experiments, include product tools such as web search, file analysis, image generation, memory/projects, connectors, or hidden model routing in the tested product capability rather than attributing all value to the named underlying model.
- Use routing intermediaries only as explicit provider-chain experiments. Record intermediary, downstream provider/model when exposed, privacy/data-processing implications, pricing markup/discount, failover/routing behavior, and any feature differences.
- Do not upload confidential/employer/client/regulated data merely to compare providers. Use public/synthetic or explicitly permitted evaluation material unless the whole provider chain is approved for that data.

## Multimodal and Media Experiments

- Treat text, vision/document understanding, audio/speech, image generation, and video as separate capability paths. One multimodal model label does not prove equal quality or runtime support for every modality.
- For VLM/audio experiments, record preprocessing, image resolution/count, audio duration/format, auxiliary encoder/projector files, context consumption, and whether preprocessing runs on CPU or accelerator.
- For generative-media experiments, capture model/version, workflow graph or pipeline, sampler/scheduler/steps where applicable, resolution/duration, seed when meaningful, VRAM peak, generation time, and post-processing. Do not compare media models on prompt text alone when workflows differ.
- When a dedicated specialist beats the routine generalist materially, keep it as a measured specialist route rather than forcing all modalities into one resident model.

## Agents and Tool-Use Experiments

- Treat agent/tool performance as more than text quality. Measure tool-selection correctness, argument/schema validity, unnecessary calls, recovery from tool errors, looping, state handling, permission behavior, and final task success.
- Sandbox destructive or external side effects during experiments. Use read-only tools, disposable environments, mocks, test accounts, or explicit human approval before writes/payments/messages/deletions/system changes.
- Do not infer safe autonomy from a model's function-calling benchmark or provider claim. Capability and permission architecture are separate.
- Keep secrets outside model context where possible and scope credentials to the minimum resources/actions required for the test.
- If recurring agent workflows become persistent operational services, move the infrastructure/availability concern toward the home-lab/team/organization route as appropriate rather than hardening it inside this personal experimentation scenario.

## Temporary Cloud GPU Experiments

- Use rented accelerators to answer a bounded experiment that owned hardware cannot answer economically: a larger checkpoint, higher precision, multi-GPU/sharded route, batch eval, fine-tuning/adaptation experiment, or media workload.
- Pin accelerator SKU/count, VRAM, driver/runtime/container image, storage/cache arrangement, model artifact, precision, and region/provider when they affect reproducibility.
- Track **billable lifecycle**, not only active inference time: provisioning/cold start, image pull, model download, compilation/warm-up, idle wait, attached storage, snapshots, and cleanup/shutdown.
- Verify whether pausing/stopping preserves the endpoint, local disk, IP/URL, image cache, or accelerator availability. Do not design an experiment around a stable API endpoint unless the provider actually guarantees that lifecycle.
- Prefer disposable/reconstructable environments. Keep prompts/config/eval scripts and non-secret experiment metadata in version control while credentials and sensitive datasets remain outside it.
- If the same cloud route is used continuously enough to require uptime, autoscaling, monitoring, backups, stable endpoints, and cost governance, it has crossed from temporary enthusiast experimentation into an operational deployment scenario.

## Cost Accounting

- Compare **cost per useful experiment and accepted result**, not token/GPU-hour price alone.
- Local cost includes electricity, download/storage, hardware contention, runtime/model maintenance, conversion time, and the researcher's own setup/debugging time.
- Hosted API cost includes tokens, tools, storage/caching, retries, batch behavior, and human review/correction.
- Cloud GPU cost includes provision/warm-up/download/idle/storage/shutdown overhead in addition to listed accelerator price.
- A free/open-weight model is not zero-cost to evaluate or operate. Conversely, a paid hosted API can be the cheaper experiment when it avoids hours of local setup for a question that needs only a small number of runs.

## Experiment Promotion and Retirement

- Promote a model/runtime combination from `interesting experiment` to `routine local route` only after it repeatedly wins on a real workload and its setup/update cost is acceptable.
- Retire or archive an experiment when upstream is superseded, runtime support regresses, the workload disappears, accepted-result quality loses to a simpler route, or repeated maintenance outweighs learning value.
- Keep historical benchmark/eval evidence distinct from the current recommendation. A past result remains evidence for the tested version, not a timeless ranking.
- If a routine route becomes uptime-sensitive, shared, remotely accessible, storage-heavy, or automation-critical, escalate to `home-lab-owner/` or the appropriate professional/team scenario.

## Canonical Links

- Link current Qwen3 candidates to canonical Model Reference identities: `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b`, `.../qwen3-14b`, `.../qwen3-30b-a3b`, and `.../qwen3-32b`.
- Link compact multimodal baselines to `catalog/models/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/google/gemma/gemma-4/models/e4b-instruct`.
- Link the MoE anti-shortcut/current larger experiment to `catalog/models/mistral-ai/mistral-small/models/mistral-small-4` when named.
- Link runtimes, hosted services, and temporary cloud services to their canonical catalog owners when named; do not duplicate complete product/runtime profiles here.
- Route task-specific model ranking to the relevant `decision-guides/` owner and exact fixed-hardware analysis to `../../../hardware/` rather than recreating either taxonomy inside this scenario.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current official Qwen3, Gemma 4, Mistral Small 4, OpenAI open-weight landscape, and LM Studio/runtime documentation plus canonical AI Lab model owners.
- The current broader open-weight landscape includes material models not yet necessarily represented by the current canonical reference tree. Scenario research must continue to consider current external releases; a model selected for durable recommendation must receive a canonical identity before the scenario names it as an owned recommendation.
- Model releases, artifacts, runtime architecture support, tool templates, quantizations, hosted aliases/pricing, and cloud-GPU availability/lifecycle are mutable. Recheck the exact route before rendering a current recommendation.
- Provider model cards and benchmark tables are provider evidence. They do not replace independent or AI Lab measurement of latency, memory, tool reliability, quantization loss, or accepted-result quality on the user's workload.

## Validation

- The scenario remains experimentation-first and distinct from persistent home-lab operation.
- Every recommendation is framed as a testable route with exact model/artifact/runtime conditions rather than a permanent winner.
- Current research is not artificially limited to models already materialized in the catalog; missing canonical identity is resolved before a new model becomes a durable named recommendation.
- MoE active parameters are never treated as checkpoint/memory size; `Mistral Small 4` and `Qwen3 30B-A3B` preserve that distinction.
- Quantization experiments separate model quality, artifact method, runtime support, and memory/performance effects.
- Managed assistant, direct API, local runtime, local server, cloud GPU, and hybrid experiments remain distinct comparison routes.
- Tool/agent experiments include side-effect isolation and permission boundaries.
- Temporary cloud capacity includes full lifecycle/billing/reproducibility constraints and does not silently become permanent infrastructure.
- No hardware purchase or permanent service architecture is prescribed from experimentation alone.
- Mutable current claims carry the 2026-08-23 evidence boundary.
