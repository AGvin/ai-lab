# Concrete Model Portfolio Profiles

These profiles turn the [Combined Workloads](../..) framework into candidate model assignments for common hardware, cost, latency, and quality constraints.

## Translations

- English

## Status and evidence boundary

Initial candidate profiles verified on 2026-07-25.

The profiles are **evaluation starting points**, not universal rankings or production approvals. Exact artifact identity, access, license, file size, published API price, and documented modality support are provider facts where cited. Role suitability, quality ceiling, accepted-result cost, and fallback value remain recommendations that must be validated on the intended workload.

Do not transfer a result between:

- a base model and a quantized artifact;
- one runtime, prompt, context, or tool scaffold and another;
- local and hosted deployments;
- one quality tier, language, repository, modality, or risk class and another.

## Candidate artifacts and services used here

### Local language-model artifacts

- [`Qwen/Qwen3-8B-GGUF`](https://huggingface.co/Qwen/Qwen3-8B-GGUF), file `Qwen3-8B-Q4_K_M.gguf`: Apache-2.0, 5.03 GB published file size, native 32,768-token context with documented YaRN extension.
- [`Qwen/Qwen3-14B-GGUF`](https://huggingface.co/Qwen/Qwen3-14B-GGUF), file `Qwen3-14B-Q4_K_M.gguf`: Apache-2.0, 9 GB published file size, native 32,768-token context with documented YaRN extension.
- [`Qwen/Qwen3-30B-A3B-GGUF`](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF), file `Qwen3-30B-A3B-Q4_K_M.gguf`: Apache-2.0, 18.6 GB published file size.

Published GGUF file size is not peak VRAM. Runtime buffers, KV cache, context length, batching, GPU layers, drivers, and concurrent services require additional memory. Measure the exact runtime before declaring that an artifact fits.

### Hosted text and multimodal candidates

- `deepseek-v4-flash`: economical long-context reasoning and tool-use candidate; exact API identity and price snapshot are recorded on the [DeepSeek V4 Flash](../../../../../../../../../software/sub/models/sub/deepseek/sub/deepseek-v4/sub/flash/) page.
- `gpt-5.6-luna`, `gpt-5.6-terra`, and `gpt-5.6-sol`: fast, balanced, and flagship hosted tiers; exact family characteristics and price snapshot are recorded on the [GPT-5.6](../../../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/) page.
- `claude-sonnet-5`: hosted coding, agentic, reasoning, and knowledge-work candidate; exact access, context, and time-bounded price snapshot are recorded on the [Claude Sonnet 5](../../../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) page.
- `gemini-3.6-flash`: hosted text, image, video, audio, and PDF input candidate with text output; exact capabilities are recorded on the [Gemini 3.6 Flash](../../../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) page.

### Local and hosted specialists

- [`openai/whisper`](https://github.com/openai/whisper): MIT-licensed local ASR baseline; select and measure the exact checkpoint and runtime.
- [`pyannote/speaker-diarization-community-1`](https://huggingface.co/pyannote/speaker-diarization-community-1): CC-BY-4.0 local diarization candidate with gated access conditions.
- [`black-forest-labs/FLUX.1-schnell`](https://huggingface.co/black-forest-labs/FLUX.1-schnell): Apache-2.0 image-generation candidate; runtime, precision, memory, quality, and output-rights workflow still require assignment-level verification.
- OpenAI, Google Vertex AI, Adobe Firefly, Azure, Google Cloud, Deepgram, and other hosted specialists documented in the task guides remain candidate services only after exact endpoint, model, region, policy, retention, and price verification.

## Profile summary

| Profile | Resident core | Standard escalation | High-quality or specialist route | Primary constraint |
| --- | --- | --- | --- | --- |
| One 24 GB GPU | Qwen3-14B Q4_K_M | Qwen3-30B-A3B Q4_K_M sequentially or DeepSeek V4 Flash | GPT-5.6 Sol, Claude Sonnet 5, Gemini 3.6 Flash, or media specialist | VRAM headroom and model switching |
| Two 24 GB GPUs | Qwen3-30B-A3B Q4_K_M on one GPU | Second GPU for a separately measured specialist | Hosted flagship or another provider when local quality fails | Concurrency versus one larger sharded model |
| CPU-only | Qwen3-8B Q4_K_M | DeepSeek V4 Flash or GPT-5.6 Luna | GPT-5.6 Sol, Claude Sonnet 5, Gemini 3.6 Flash, or specialist | Latency and memory bandwidth |
| Cloud-only | DeepSeek V4 Flash or GPT-5.6 Luna | GPT-5.6 Terra and Gemini 3.6 Flash | GPT-5.6 Sol, Claude Sonnet 5, and specialist APIs | Provider cost, data boundary, and availability |
| Hybrid local and hosted | Qwen3-14B Q4_K_M | DeepSeek V4 Flash or GPT-5.6 Terra | GPT-5.6 Sol, Claude Sonnet 5, Gemini 3.6 Flash, or specialist | Privacy with selective capability escalation |
| Always-on local core | Qwen3-14B Q4_K_M | Hosted model selected by task and risk | Specialist generation, perception, speech, or flagship reasoning | Low idle cost and predictable local availability |
| Local orchestrator plus image POD | Qwen3-14B Q4_K_M | Temporary FLUX.1-schnell deployment | Hosted image API if the local artifact misses the gate | Verified startup, persistence, and teardown |
| Low-budget | Qwen3-8B Q4_K_M or Qwen3-14B Q4_K_M | DeepSeek V4 Flash | Human review or one bounded flagship call | Cost per accepted result |
| Low-latency | Qwen3-14B Q4_K_M or GPT-5.6 Luna | Gemini 3.6 Flash for multimodal input | Pre-warmed Terra or Sol only for declared cases | Tail latency and avoidance of cold starts |
| Maximum-quality | GPT-5.6 Sol | Claude Sonnet 5 and Gemini 3.6 Flash | Dedicated translation, media, speech, perception, and human specialists | Accepted-result quality rather than request price |

The table names candidates, not measured winners. Each detailed profile defines what must be verified before adoption.

## One 24 GB GPU

### Intended workload

A home lab or workstation with one RTX 3090-class 24 GB GPU serving private text work, coding, orchestration, occasional speech, and intermittent media tasks.

### Candidate portfolio

- **Resident local generalist and orchestrator:** `Qwen/Qwen3-14B-GGUF`, `Qwen3-14B-Q4_K_M.gguf`.
- **Higher-capacity local text candidate:** `Qwen/Qwen3-30B-A3B-GGUF`, `Qwen3-30B-A3B-Q4_K_M.gguf`, loaded sequentially after unloading the resident model.
- **Local ASR:** exact Whisper checkpoint selected from measured latency and accuracy; load sequentially unless measured concurrent residency is safe.
- **Local diarization:** `pyannote/speaker-diarization-community-1`, normally as a batch step rather than a permanently resident service.
- **Hosted routine escalation:** `deepseek-v4-flash` for eligible coding, reasoning, or tool work that exceeds the local profile.
- **Hosted production or exceptional escalation:** `gpt-5.6-sol` or `claude-sonnet-5`, selected by workload evidence rather than provider name.
- **Hosted multimodal escalation:** `gemini-3.6-flash` for eligible image, video, audio, or PDF input when local perception is absent or inadequate.
- **Image generation:** hosted API by default for infrequent work, or a separately measured local artifact after unloading the language model.

### Residency and routing

Keep the 14B artifact resident only when its measured acceptance rate justifies always-on VRAM. Use the 30B-A3B artifact as a sequential alternative, not a presumed concurrent companion: its 18.6 GB file leaves limited 24 GB headroom before KV cache and runtime overhead.

Route by explicit conditions:

1. deterministic tools before any model;
2. local 14B for private preprocessing, classification, draft work, routing, and low-risk automation that passed evaluation;
3. local 30B-A3B for measured tasks where it materially improves accepted-result quality without hosted data transfer;
4. DeepSeek V4 Flash for eligible economical escalation;
5. Sol, Sonnet 5, Gemini Flash, or a dedicated specialist for production, multimodal, or repeated local failure;
6. human approval for consequential output.

### Validation gates

- Measure peak VRAM at target context and batch size, not only weight size.
- Measure unload, load, warm-up, and first-token latency for every sequential transition.
- Preserve task state and artifacts before unloading a service.
- Test the local model's ability to route; use deterministic or independent escalation triggers where self-assessment is weak.
- Keep image, video, or large speech generation out of the critical path unless startup latency is accepted.

### Rejected default

Do not make `Qwen3-Coder-Next` the default one-GPU assignment from its base page alone. Its official guidance does not establish a consumer-GPU fit, and no validated quantized deployment is selected by the current documentation.

## Two 24 GB GPUs

### Intended workload

A workstation or server requiring concurrent local text work plus speech, perception, evaluation, or generation without unloading the primary model for every specialist call.

### Candidate portfolio

- **GPU 0 resident text core:** `Qwen3-30B-A3B-Q4_K_M.gguf`, after exact runtime verification.
- **GPU 1 specialist lane:** one exact specialist at a time, for example Whisper ASR, pyannote diarization, `FLUX.1-schnell`, or a separately evaluated vision-language artifact.
- **Hosted escalation:** DeepSeek V4 Flash for economical overflow, Gemini 3.6 Flash for multimodal cases not covered locally, and GPT-5.6 Sol or Claude Sonnet 5 for high-quality reasoning, review, or recovery.

### Topology decision

Compare two layouts on the complete workflow:

1. **Independent services:** one model per GPU, preserving concurrency and failure isolation.
2. **Sharded larger model:** both GPUs serve one artifact through tensor or pipeline parallelism.

Prefer independent services when text and specialist tasks overlap, queueing matters, or one failed service should not block the other. Prefer sharding only when the larger model's measured accepted-result gain exceeds lost concurrency, startup complexity, interconnect overhead, and operational cost.

### Validation gates

- Measure per-GPU and host RAM, PCIe transfer, context cache, concurrency, and cross-service contention.
- Verify that the specialist lane can unload and replace models without disturbing the core service.
- Test whether two independent smaller services outperform one larger sharded model at portfolio level.
- Preserve a hosted fallback because two local GPUs remain one power, host, storage, and software failure domain.

## CPU-only

### Intended workload

Offline or low-cost batch work on a system without usable GPU acceleration.

### Candidate portfolio

- **Local text core:** `Qwen3-8B-Q4_K_M.gguf`.
- **Optional larger local batch candidate:** `Qwen3-14B-Q4_K_M.gguf` only after acceptable measured latency and RAM usage.
- **Local speech:** a smaller Whisper checkpoint selected from measured real-time factor and accuracy.
- **Hosted fast route:** `gpt-5.6-luna` or `deepseek-v4-flash` for eligible latency-sensitive text work.
- **Hosted multimodal route:** `gemini-3.6-flash`.
- **Hosted high-quality route:** GPT-5.6 Sol or Claude Sonnet 5 after bounded lower-cost failure or for a pre-declared high-risk task.

### Operating rules

- Prefer deterministic parsers, search, diff, schema validation, OCR, and media tooling where a model is unnecessary.
- Queue local inference as background or batch work and set realistic timeouts.
- Limit context and concurrency from measured memory bandwidth and latency.
- Do not keep several CPU models resident merely because storage is available.
- Fail over to hosted service only for data permitted to leave the device.

### Quality ceiling

The CPU profile prioritizes availability, privacy, and cost. It should not be presented as a maximum-quality or interactive low-latency profile without measured evidence.

## Cloud-only

### Intended workload

No managed local inference; all model work uses hosted APIs or managed services.

### Candidate portfolio

- **Economical text, coding, and reasoning:** `deepseek-v4-flash`.
- **Fast general route:** `gpt-5.6-luna`.
- **Balanced OpenAI route:** `gpt-5.6-terra`.
- **Multimodal input route:** `gemini-3.6-flash`.
- **High-quality reasoning, coding, or review:** `gpt-5.6-sol` and `claude-sonnet-5` as independently evaluated candidates.
- **Dedicated task services:** exact translation, image, video, speech, OCR, or document APIs selected from the corresponding task guide.

### Routing policy

Use an auditable risk and capability matrix:

- routine, low-risk, text-only work starts on the least expensive validated route;
- image, video, audio, or PDF input goes only to a route whose exact model supports that modality;
- production or consequential work requires deterministic checks and a separately validated reviewer or human gate;
- repeated similar failure escalates to a different model family or specialist, not an unlimited retry loop;
- confidential data is routed only to providers, projects, regions, and retention modes approved for that data class.

### Provider resilience

A second provider is not a valid fallback until schemas, tools, prompts, rate limits, data terms, output quality, and failure behavior are tested. Preserve provider-neutral task records and normalized artifacts to reduce switching cost.

### Cost control

Track cache behavior, input and output tokens, images, pages, media seconds, tools, storage, transfer, retries, judge calls, and human review. Set monthly and per-task budgets and calculate accepted-result cost by route.

## Hybrid local and hosted

### Intended workload

Private or offline-capable routine work with selective hosted escalation for stronger reasoning, multimodal input, or specialist generation.

### Candidate portfolio

- **Local privacy and routing core:** `Qwen3-14B-Q4_K_M.gguf`.
- **Hosted economical escalation:** `deepseek-v4-flash`.
- **Hosted balanced escalation:** `gpt-5.6-terra`.
- **Hosted multimodal specialist:** `gemini-3.6-flash`.
- **Hosted high-quality reasoning or independent review:** `gpt-5.6-sol` or `claude-sonnet-5`.
- **Local or hosted task specialists:** exact Whisper, pyannote, FLUX, translation, document, or media assignment selected from task-level evidence.

### Data boundary

Classify input before routing:

1. **Local-only:** raw secrets, credentials, private identities, restricted source assets, or data whose policy forbids transfer.
2. **Sanitized eligible:** minimized content after deterministic redaction and verification that the removed context is not required.
3. **Hosted-approved:** data explicitly permitted for the selected provider, project, region, endpoint, retention, and use.

Sanitization does not create rights to upload a voice, face, copyrighted work, confidential design, or personal record.

### Degraded operation

When hosted services or network access fail:

- continue validated local tasks at the local quality ceiling;
- queue approved hosted work with expiry and revalidation;
- fail closed for tasks whose required quality cannot be met locally;
- preserve enough state to resume without duplicating billable or destructive actions.

## Always-on Local Generalist with Remote Specialists

### Intended workload

A home server or small private service that should remain useful without external access while avoiding permanent residency for rarely used specialists.

### Candidate portfolio

- **Always-on core:** `Qwen3-14B-Q4_K_M.gguf` as generalist, router, summarizer, and low-risk worker only for roles it passes.
- **Remote low-cost text specialist:** `deepseek-v4-flash`.
- **Remote multimodal specialist:** `gemini-3.6-flash`.
- **Remote high-quality specialist:** `gpt-5.6-sol` or `claude-sonnet-5`.
- **Remote media, speech, translation, or document specialists:** exact services selected by the task guides.

### Consolidation rule

Keep one local service rather than separate planner, router, reviewer, and worker models when the same artifact passes each required role. Split roles when:

- the local model cannot reliably identify its own failure;
- review must be independent;
- different permissions or data visibility are required;
- concurrency or latency suffers from one shared queue;
- a specialist materially lowers cost per accepted result.

### Health and fallback

Verify local service health, loaded artifact, context isolation, queue depth, disk, memory, and restart behavior. Remote specialists must have independent availability checks and bounded timeouts. The local core should expose a clear degraded state rather than pretending remote capability remains available.

## Local Orchestrator with On-Demand Image POD

### Intended workload

Local planning, prompt development, privacy checks, and artifact management with an image-generation GPU service started only for approved generation jobs.

### Candidate portfolio

- **Resident orchestrator:** `Qwen3-14B-Q4_K_M.gguf`.
- **Temporary image worker:** exact `black-forest-labs/FLUX.1-schnell` revision and measured runtime, or another exact licensed artifact selected by the [Generative Media](../../../generative-media/) guide.
- **Hosted image fallback:** exact OpenAI, Google, Adobe, or other image endpoint whose input, policy, retention, output, and price are approved.
- **Independent evaluator:** deterministic image validators plus a calibrated perception model or human reviewer; the generator does not approve itself.

### Required lifecycle

1. Validate task need, content policy, rights, consent, quality tier, and budget.
2. Select the exact worker artifact, runtime, GPU profile, storage, and timeout.
3. Request POD or service startup with an idempotency key.
4. Poll provider state until the service, endpoint, model, and required files are confirmed ready.
5. Execute a bounded candidate budget.
6. Persist prompts, parameters, seeds, masks, candidates, selected artifacts, and provenance outside ephemeral storage.
7. Run deterministic checks and independent review.
8. Request shutdown after the last approved dependent job.
9. Verify provider state and billing state independently from the worker response.
10. Retry cleanup or escalate when shutdown, volume cleanup, or endpoint deletion fails.

### Failure rules

- Do not start the POD when the expected cold-start cost or delay exceeds a validated hosted route.
- Stop repeated sampling when the defect is a model capability gap.
- Do not delete ephemeral storage before artifact integrity and persistence are verified.
- A worker reporting completion is not evidence that a billable resource stopped.

## Low-Budget

### Intended workload

Minimize total spend while preserving a defined working-result threshold.

### Candidate portfolio

- **Local baseline:** Qwen3-8B Q4_K_M on CPU or Qwen3-14B Q4_K_M on an available 24 GB GPU.
- **Hosted routine escalation:** `deepseek-v4-flash` under explicit token, tool, and retry budgets.
- **Fast alternative:** `gpt-5.6-luna` only when its measured accepted-result cost is lower for the task.
- **High-quality escalation:** one bounded GPT-5.6 Sol, Claude Sonnet 5, Gemini 3.6 Flash, specialist, or human-review step when the lower-cost route fails or risk requires it.

### Cost policy

- Use deterministic tools before model calls.
- Cache approved reusable inputs and outputs where provider terms and correctness permit it.
- Shorten context by retrieval and explicit evidence selection, not by dropping requirements.
- Cap candidate count, retries, tool loops, output length, and judge calls.
- Escalate when another low-cost retry has lower expected value than a stronger route.
- Measure human correction time and rejected outputs; free local inference is not zero-cost.

### Rejected default

Do not choose the lowest token price without measuring terminal acceptance. A cheap model that requires several retries, a stronger reviewer, and manual repair can be the most expensive route per accepted result.

## Low-Latency

### Intended workload

Interactive assistance, UI completion, routing, or voice workflows where tail latency and interruption response matter more than maximum reasoning depth.

### Candidate portfolio

- **Local zero-network route:** `Qwen3-14B-Q4_K_M.gguf`, preloaded with bounded context and concurrency.
- **Hosted fast text route:** `gpt-5.6-luna`.
- **Hosted fast multimodal route:** `gemini-3.6-flash` after modality-specific latency measurement.
- **Pre-warmed balanced route:** `gpt-5.6-terra` for tasks that exceed the fast route but remain latency-sensitive.
- **Exceptional route:** Sol, Sonnet 5, or a specialist only outside the critical interaction path or under a declared user-visible escalation.

### Latency policy

Measure:

- queue delay;
- input preparation and upload;
- time to first token, partial transcript, or first audio;
- tool and retrieval latency;
- completion or terminal artifact latency;
- p50, p95, p99, timeout, cancellation, and retry behavior.

Avoid on-demand GPU startup, model swapping, long deliberation, multi-judge councils, and synchronous high-quality media generation in the critical path. Precompute, preload, stream, or move expensive review after provisional output only when risk permits.

### Quality boundary

Fast output must remain labeled provisional until required validators and review finish. Do not execute consequential actions from unstable streaming text, partial ASR, or an unverified router decision.

## Maximum-Quality

### Intended workload

Production or exceptional-quality coding, research, multimodal analysis, publication, or high-value artifacts where accepted-result quality dominates request price and latency.

### Candidate portfolio

- **Primary planner, orchestrator, and complex worker candidate:** `gpt-5.6-sol`.
- **Independent text, coding, or reasoning reviewer candidate:** `claude-sonnet-5`.
- **Multimodal perception candidate:** `gemini-3.6-flash` for text, image, video, audio, and PDF input; use a stronger or specialized route if the exact assignment shows a higher ceiling.
- **Alternative economic or diversity candidate:** `deepseek-v4-flash`, not as proof of independent correctness but as a differently priced and deployed route to evaluate.
- **Dedicated specialists:** exact translation, OCR, document, image, video, speech, audio, or evaluation services selected from the corresponding guides.
- **Human approval:** qualified reviewer for consequential, rights-sensitive, safety-sensitive, or publication-critical output.

### Review topology

1. The primary model receives explicit acceptance criteria, tools, and evidence.
2. Deterministic validators run before model review.
3. A different model family reviews only the criteria it has been calibrated to judge.
4. Contradictions, close decisions, unsupported evidence, and high-risk output go to human adjudication.
5. Revision rounds are bounded and compared against previous artifacts to detect cycles and diminishing returns.

Do not call several correlated models and label the result consensus. Record each reviewer, model family, prompt, evidence, decision, disagreement, and residual uncertainty.

### Cost policy

Maximum quality is not unlimited cost. Stop when:

- every acceptance criterion is satisfied;
- remaining defects are accepted explicitly;
- the revision budget is exhausted;
- repeated changes do not improve measured quality;
- a qualified human determines that further model iteration has lower value than direct editing.

## Profile validation matrix

Before adopting any profile, complete this matrix with measured values:

| Dimension | Required record |
| --- | --- |
| Exact assignments | Model or service ID, artifact revision, runtime, quantization, endpoint, region, prompt, parameters, tools, and permissions |
| Workload | Task mix, frequency, modality, input distribution, language, context, quality tier, and failure severity |
| Residency | Concurrent and sequential services, peak VRAM and RAM, KV cache, load, unload, warm-up, and idle policy |
| Throughput | Concurrency, queueing, tokens or media units per second, saturation, and timeouts |
| Quality | First-pass and terminal acceptance, failure taxonomy, quality ceiling, subgroup results, and reviewer disagreement |
| Reliability | Retry budget, repeated-failure detection, escalation, fallback, degraded operation, and recovery |
| Cost | Hardware occupancy, API, storage, transfer, tools, failed attempts, review, correction, and cost per accepted result |
| Privacy and policy | Data classes, permitted routes, retention, region, rights, consent, biometric handling, and deletion |
| Evidence | Primary sources, evaluation suite, raw results, limitations, verification date, and re-evaluation triggers |

A profile becomes a recommendation only after the complete assignment passes its task-level gates. Until then, retain the label **candidate profile**.

## Related pages

- [Choosing Model Portfolios for Combined Workloads](../..)
- [AI Model Selection and Team Design](../../../..)
- [Choosing Models for Coding](../../../coding/)
- [Translation and Localization](../../../translation-and-localization/)
- [Generative Media](../../../generative-media/)
- [Speech and Conversation](../../../speech-and-conversation/)
- [Perception and Evaluation](../../../perception-and-evaluation/)
- [Agent Role Selection](../../../agent-role-selection/)
- [Defining Model Reliability Profiles](../../../reliability-profiles/)
- [Models](../../../../../../../../../software/sub/models/)
