# Concrete Model Portfolio Profiles

Candidate model assignments for common hardware, cost, latency, privacy, and quality constraints.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status and evidence boundary

Verified on 2026-07-27.

These profiles are **evaluation starting points**, not universal rankings or production approvals. Exact model identity, access, license, context, published price, modality support, and artifact size are provider facts where cited on the canonical model pages. Role suitability, quality ceiling, deployment fit, and cost per accepted result remain recommendations that must be validated on the intended workload.

Do not transfer a result between:

- a base model and a quantized or converted artifact;
- one runtime, prompt, context, tool scaffold, or provider deployment and another;
- one language, repository, modality, quality tier, or risk class and another.

## Canonical candidates

### Local language and multimodal models

- [Gemma 4 E2B Instruct](../../../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) — compact local multimodal SLM; current profiles use the official QAT Q4_0 GGUF as a planning artifact.
- [Gemma 4 E4B Instruct](../../../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) — stronger compact local multimodal SLM; current profiles use the official QAT Q4_0 GGUF as a planning artifact.
- [Qwen3 8B](../../../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/8b/) — economical local text baseline; current profiles evaluate the official `Q4_K_M` GGUF artifact.
- [Qwen3 14B](../../../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/14b/) — resident local text generalist candidate; current profiles evaluate the official `Q4_K_M` GGUF artifact.
- [Qwen3 30B-A3B](../../../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/30b-a3b/) — higher-capacity local text candidate; current profiles evaluate the official `Q4_K_M` GGUF artifact.

Published weight or file size is not peak VRAM. Runtime buffers, KV cache, context, batching, offload, drivers, multimodal projections, encoders, and concurrent services require separate measurement. See [Local Model Selection by VRAM](../../../local-models-by-vram/).

### Hosted text and multimodal models

- [DeepSeek V4 Flash](../../../../../../../../../software/sub/models/sub/deepseek/sub/deepseek-v4/sub/flash/) — economical hosted reasoning and tool-use candidate.
- [GPT-5.6 Luna](../../../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/luna/) — fast, lower-cost GPT-5.6 tier.
- [GPT-5.6 Terra](../../../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/) — balanced GPT-5.6 tier.
- [GPT-5.6 Sol](../../../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) — flagship GPT-5.6 tier.
- [Claude Sonnet 5](../../../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) — hosted coding, reasoning, and agent-work candidate.
- [Gemini 3.6 Flash](../../../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) — hosted text, image, video, audio, and PDF input candidate with text output.

### Local specialists

- [Whisper](../../../../../../../../../software/sub/models/sub/openai/sub/whisper/) — local ASR family; choose and measure an exact checkpoint and runtime.
- [pyannote Community-1](../../../../../../../../../software/sub/models/sub/pyannote/sub/speaker-diarization/sub/community-1/) — gated local diarization candidate.
- [FLUX.1-schnell](../../../../../../../../../software/sub/models/sub/black-forest-labs/sub/flux/sub/flux-1-schnell/) — local or temporary image-generation candidate requiring exact runtime measurement.

## Profile summary

| Profile | Resident or primary route | Standard escalation | Primary constraint |
| --- | --- | --- | --- |
| One 24 GB GPU | Qwen3 14B text core with optional Gemma 4 compact multimodal lane | Qwen3 30B-A3B sequentially or hosted model | VRAM headroom and switching |
| Two 24 GB GPUs | Qwen3 30B-A3B on one GPU | Gemma 4 or another specialist on the second GPU, or hosted route | Concurrency versus sharding |
| CPU-only | Gemma 4 E2B or Qwen3 8B according to modality | Luna or DeepSeek V4 Flash | Latency and memory bandwidth |
| Cloud-only | Luna or DeepSeek V4 Flash | Terra, Gemini, Sol, Sonnet, or specialist | Provider cost and data boundary |
| Hybrid local and hosted | Qwen3 14B text core plus optional Gemma 4 multimodal route | DeepSeek, Terra, Gemini, Sol, Sonnet | Privacy with selective escalation |
| Always-on local | Qwen3 14B or compact Gemma 4 according to workload | Remote task specialist | Predictable availability and idle cost |
| Local orchestrator plus image POD | Qwen3 14B Q4_K_M | Temporary FLUX.1-schnell deployment | Verified lifecycle and billing stop |
| Low-budget | Gemma 4 E2B, Qwen3 8B, or Qwen3 14B | DeepSeek, then one bounded stronger route | Cost per accepted result |
| Low-latency | Preloaded compact local route, Qwen3 14B, or Luna | Pre-warmed Terra or multimodal Flash | Tail latency and cold starts |
| Maximum-quality | GPT-5.6 Sol | Independent Sonnet, Gemini, specialists, human | Accepted-result quality |

The table names candidates, not measured winners.

## One 24 GB GPU

### Intended workload

Private text work, coding, local multimodal analysis, orchestration, occasional speech processing, and intermittent media tasks on RTX 3090- or RTX 4090-class hardware.

### Candidate assignment

- **Resident text generalist:** Qwen3 14B Q4_K_M.
- **Compact local multimodal route:** Gemma 4 E2B or E4B official QAT artifact, resident only when combined peak memory and context are measured safe.
- **Higher-capacity local text route:** Qwen3 30B-A3B Q4_K_M, loaded only after unloading conflicting resident services.
- **ASR:** exact Whisper checkpoint, loaded sequentially unless concurrent residency is measured safe.
- **Diarization:** Community-1 as a batch stage.
- **Economical hosted escalation:** DeepSeek V4 Flash or GPT-5.6 Luna.
- **Balanced or production escalation:** GPT-5.6 Terra, Sol, or Claude Sonnet 5 according to workload evidence.
- **Hosted multimodal escalation:** Gemini 3.6 Flash when the required modality or quality is not covered locally.
- **Image generation:** hosted endpoint for infrequent work, or a separately measured local worker after unloading conflicting models.

### Operating rules

- Treat Qwen3 30B-A3B as **Constrained** on 24 GB until peak VRAM is measured at the target context and batch.
- Treat Gemma model and projection files, modality encoders, context, and runtime buffers as separate memory consumers.
- Measure unload, load, warm-up, and first-token latency for every transition.
- Preserve task state and artifacts before replacing a resident service.
- Use deterministic or independent escalation triggers when the local model cannot assess its own failure reliably.
- Do not keep speech, perception, or image services resident merely because one test request succeeded.

### Quality and fallback

Use each local route only for quality tiers and modalities it passes. Escalate repeated omission, perception, tool, factuality, or completion failures to a different model family or human review rather than repeating the same route indefinitely.

## Two 24 GB GPUs

### Intended workload

Concurrent local text work plus multimodal analysis, speech, perception, evaluation, or generation without unloading the primary service for every specialist call.

### Candidate assignment

- **GPU 0:** Qwen3 30B-A3B Q4_K_M as the text core after exact validation, or Qwen3 14B when latency and headroom are more important.
- **GPU 1:** one measured lane at a time, such as Gemma 4 E2B or E4B, Whisper, Community-1, FLUX.1-schnell, or another exact specialist.
- **Hosted overflow:** DeepSeek or Luna for economical capacity, Gemini for unsupported modalities, and Sol or Sonnet for high-quality reasoning and review.

### Topology decision

Compare:

1. **Independent services** — one service per GPU for concurrency and failure isolation.
2. **Sharded model** — both GPUs serve one larger artifact.

Prefer independent services when tasks overlap or one failure must not block the other. Prefer sharding only when the larger model's measured acceptance gain exceeds lost concurrency, startup complexity, interconnect overhead, and operational cost.

### Validation

Measure per-GPU VRAM, host RAM, PCIe or interconnect transfer, context cache, multimodal components, concurrency, queueing, and cross-service contention. Preserve a hosted fallback because two local GPUs remain one host, power, storage, and software failure domain.

## CPU-only

### Intended workload

Offline or low-cost batch work without usable GPU acceleration.

### Candidate assignment

- **Compact multimodal baseline:** Gemma 4 E2B official QAT artifact when bounded image, document, or short-audio input is required and runtime support is validated.
- **Text baseline:** Qwen3 8B Q4_K_M.
- **Optional larger batch route:** Gemma 4 E4B or Qwen3 14B only after latency and RAM validation.
- **Local ASR:** smaller Whisper checkpoint selected by error rate and real-time factor.
- **Hosted fast route:** Luna or DeepSeek V4 Flash.
- **Hosted multimodal route:** Gemini 3.6 Flash.
- **High-quality route:** Sol, Sonnet, or a specialist after bounded lower-cost failure or for a declared high-risk task.

### Operating rules

Prefer deterministic parsers, search, diff, schema validation, OCR, and media tools where a model is unnecessary. Queue local inference as batch work, cap context and concurrency, and fail closed when the local quality ceiling is below the requirement and data cannot leave the device.

## Cloud-only

### Intended workload

All model work uses hosted APIs or managed services.

### Candidate assignment

- **Economical text and reasoning:** DeepSeek V4 Flash or GPT-5.6 Luna.
- **Balanced route:** GPT-5.6 Terra.
- **Multimodal input:** Gemini 3.6 Flash.
- **High-quality reasoning, coding, or review:** GPT-5.6 Sol and Claude Sonnet 5 as independently evaluated candidates.
- **Dedicated tasks:** exact translation, media, speech, OCR, or document services selected from the task guides.

### Routing and resilience

Route by task capability, risk, data class, region, retention, and quality tier. A second provider is not a valid fallback until schemas, tools, prompts, rate limits, data terms, output quality, and failures are tested. Preserve provider-neutral task records and normalized artifacts.

### Cost

Track tokens, cached input, media units, pages, tools, storage, transfer, retries, judge calls, and human review. Enforce per-task and monthly budgets and calculate cost per accepted result.

## Hybrid local and hosted

### Intended workload

Private or offline-capable routine work with selective hosted escalation.

### Candidate assignment

- **Local text and routing core:** Qwen3 14B Q4_K_M.
- **Local compact multimodal route:** Gemma 4 E2B or E4B for bounded image, document, UI, or short-audio work.
- **Economical escalation:** DeepSeek V4 Flash or Luna.
- **Balanced escalation:** GPT-5.6 Terra.
- **Multimodal escalation:** Gemini 3.6 Flash.
- **High-quality reasoning or independent review:** GPT-5.6 Sol or Claude Sonnet 5.
- **Specialists:** exact Whisper, Community-1, FLUX, translation, document, or media assignment.

### Data boundary

Classify every input as:

1. **Local-only** — transfer is prohibited.
2. **Sanitized eligible** — deterministic redaction is verified and removed context is not required.
3. **Hosted-approved** — provider, project, region, endpoint, retention, and use are explicitly permitted.

Sanitization does not create rights to upload a voice, face, copyrighted work, confidential design, or personal record.

### Degraded operation

Continue only validated local tasks during network or provider failure. Queue approved hosted work with expiry and revalidation, fail closed when required quality cannot be met locally, and preserve state so retries do not duplicate billable or destructive actions.

## Always-on Local Generalist with Remote Specialists

### Candidate assignment

- **Always-on text core:** Qwen3 14B Q4_K_M as generalist, router, summarizer, and low-risk worker only for roles it passes.
- **Alternative compact multimodal core:** Gemma 4 E4B when local image, document, UI, and short-audio inputs dominate and measured text quality remains sufficient.
- **Remote economical route:** DeepSeek V4 Flash or Luna.
- **Remote multimodal route:** Gemini 3.6 Flash.
- **Remote high-quality route:** GPT-5.6 Sol or Claude Sonnet 5.
- **Remote task specialists:** exact services selected by the task guides.

Keep one local service rather than separate planner, router, reviewer, worker, and perception models when the same artifact passes each role. Split roles when review must be independent, permissions differ, concurrency suffers, modality support differs, or a specialist materially improves cost per accepted result.

Monitor loaded artifact, projection or encoder files, context isolation, queue depth, disk, memory, restart behavior, remote health, and timeouts. Expose a clear degraded state instead of pretending remote capability remains available.

## Local Orchestrator with On-Demand Image POD

### Candidate assignment

- **Resident orchestrator:** Qwen3 14B Q4_K_M.
- **Optional local multimodal preparation:** Gemma 4 E2B or E4B for bounded image understanding and prompt or reference preparation.
- **Temporary image worker:** exact FLUX.1-schnell revision and measured runtime.
- **Hosted fallback:** exact approved image endpoint.
- **Independent evaluator:** deterministic validators plus calibrated perception model or human reviewer.

### Required lifecycle

1. Validate task need, rights, consent, quality tier, and budget.
2. Select exact artifact, runtime, GPU profile, storage, and timeout.
3. Start with an idempotency key.
4. Confirm provider state, endpoint, model, and files are ready.
5. Execute a bounded candidate budget.
6. Persist prompts, parameters, seeds, masks, outputs, and provenance outside ephemeral storage.
7. Run deterministic checks and independent review.
8. Request shutdown after the last dependent job.
9. Verify provider and billing state independently.
10. Retry cleanup or escalate when teardown fails.

A worker reporting completion is not evidence that a billable resource stopped.

## Low-Budget

### Candidate assignment

- **Compact multimodal local baseline:** Gemma 4 E2B on a validated CPU, GPU, or unified-memory runtime.
- **Text local baseline:** Qwen3 8B on CPU or Qwen3 14B on an available GPU.
- **Routine hosted escalation:** DeepSeek V4 Flash under explicit token, tool, and retry budgets.
- **Fast alternative:** Luna only when measured accepted-result cost is lower.
- **Final bounded escalation:** one Sol, Sonnet, Gemini, specialist, or human-review step.

Use deterministic tools first, cache only when correct and permitted, shorten context through retrieval rather than dropping requirements, cap candidates and retries, and measure human correction time. Free local inference is not zero-cost.

## Low-Latency

### Candidate assignment

- **Local compact multimodal route:** preloaded Gemma 4 E2B or E4B with bounded modality, context, and concurrency.
- **Local text route:** preloaded Qwen3 14B with bounded context and concurrency.
- **Hosted fast text route:** GPT-5.6 Luna.
- **Hosted fast multimodal route:** Gemini 3.6 Flash after modality-specific measurement.
- **Pre-warmed balanced route:** GPT-5.6 Terra.
- **Exceptional route:** Sol, Sonnet, or specialist outside the critical interaction path.

Measure queue delay, upload, modality preprocessing, time to first token or audio, tool latency, terminal artifact latency, p50, p95, p99, timeout, cancellation, and retry. Avoid model swapping, on-demand GPU startup, long deliberation, councils, and synchronous media generation in the critical path.

Treat streaming output as provisional until required validators and review finish.

## Maximum-Quality

### Candidate assignment

- **Primary planner, orchestrator, and complex worker candidate:** GPT-5.6 Sol.
- **Independent text, coding, or reasoning reviewer candidate:** Claude Sonnet 5.
- **Multimodal perception candidate:** Gemini 3.6 Flash.
- **Private compact multimodal evidence route:** Gemma 4 E4B only for bounded work it passes; do not treat it as the maximum-quality judge.
- **Economic or diversity candidate:** DeepSeek V4 Flash.
- **Dedicated specialists:** exact translation, OCR, document, media, speech, or evaluation services.
- **Human approval:** qualified reviewer for consequential, rights-sensitive, safety-sensitive, or publication-critical work.

### Review topology

1. Provide explicit acceptance criteria, tools, and evidence.
2. Run deterministic validators before model review.
3. Use a different calibrated model family for independent review.
4. Send contradictions, close decisions, unsupported evidence, and high-risk output to human adjudication.
5. Bound revisions and compare versions to detect cycles and diminishing returns.

Do not call correlated models and label the result consensus. Record reviewer, model, prompt, evidence, decision, disagreement, and residual uncertainty.

Maximum quality is not unlimited cost. Stop when criteria pass, limitations are accepted, the budget is exhausted, revisions stop improving measured quality, or direct expert editing has higher value.

## Profile validation record

Before adoption, record:

| Dimension | Required record |
| --- | --- |
| Exact assignment | Model or service ID, artifact revision, runtime, quantization, endpoint, region, prompt, tools, and permissions |
| Workload | Task mix, frequency, modality, language, context, quality tier, and failure severity |
| Residency | Concurrent and sequential services, peak VRAM and RAM, KV cache, load, warm-up, unload, and idle policy |
| Throughput | Concurrency, queueing, throughput, saturation, cancellation, and timeouts |
| Quality | First-pass and terminal acceptance, failures, quality ceiling, subgroup results, and reviewer disagreement |
| Reliability | Retry budget, repeated-failure detection, escalation, fallback, degraded operation, and recovery |
| Cost | Hardware occupancy, API, storage, transfer, tools, failed attempts, review, correction, and accepted-result cost |
| Privacy and policy | Data classes, permitted routes, retention, region, rights, consent, biometric handling, and deletion |
| Evidence | Primary sources, evaluation suite, raw results, limitations, verification date, and re-evaluation triggers |

A profile becomes a recommendation only after the complete assignment passes its task-level gates. Until then, retain the label **candidate profile**.

## Related pages

- [Choosing Model Portfolios for Combined Workloads](../..)
- [AI Model Selection and Team Design](../../../..)
- [Local Model Selection by VRAM](../../../local-models-by-vram/)
- [Coding](../../../coding/)
- [Translation and Localization](../../../translation-and-localization/)
- [Generative Media](../../../generative-media/)
- [Speech and Conversation](../../../speech-and-conversation/)
- [Perception and Evaluation](../../../perception-and-evaluation/)
- [Agent Role Selection](../../../agent-role-selection/)
- [Reliability Profiles](../../../reliability-profiles/)
- [Gemma 4](../../../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/)
- [Models](../../../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../../../disclaimer/)

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B QAT Q4_0 GGUF](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf)
- [Gemma 4 E4B QAT Q4_0 GGUF](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf)
