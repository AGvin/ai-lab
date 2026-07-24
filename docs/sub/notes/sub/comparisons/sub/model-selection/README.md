# AI Model Selection and Team Design

Practical decision support for choosing individual AI models or an economical team of models for a defined workload portfolio.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Draft. The selection framework and task taxonomy are defined here first. Concrete recommendations must be added only when the exact model version, evidence, access conditions, and evaluation date can be recorded.

## Purpose

There is no universally best model, and the best model for one isolated task may not produce the best overall system.

A useful recommendation must identify:

- the complete set of tasks that must be covered;
- minimum quality thresholds and acceptable failure modes for each task;
- whether tasks run sequentially or concurrently;
- deployment, privacy, latency, and cost constraints;
- available RAM, VRAM, storage, and model-loading time;
- whether one generalist model can replace several specialists without unacceptable quality loss.

The primary objective is therefore not only to answer **which model is best for a task**, but also **which smallest and most economical model set covers the required workload**.

This section complements the [Model Selection](../../../concepts/sub/evaluation-and-operations/sub/model-selection/) concept page. Canonical descriptions of model families and individual models belong under [Models](../../../../../software/sub/models/), while this comparison section owns task-oriented recommendations, workload portfolios, and cross-model decision matrices.

## Selection units

Use two connected selection units.

### Individual task

Choose the best practical model for one bounded task, such as:

- translating repository files;
- modifying code;
- reviewing an image against a generation prompt;
- transcribing a multi-speaker recording;
- generating an image or voice sample.

This view is useful for measuring model strengths and minimum acceptable quality.

### Workload portfolio

Choose a complete model team for a set of tasks that will be executed by one system or infrastructure environment.

The portfolio decision may prefer a slightly weaker generalist model if it:

- covers several required tasks;
- remains resident in memory;
- avoids repeated model loading and unloading;
- reduces orchestration complexity;
- lowers total hardware or API cost;
- preserves enough quality for every covered task.

A specialist should be added only when its measurable improvement justifies the extra memory, latency, cost, routing, and maintenance overhead.

## Documentation model

Use four connected views instead of duplicating the same information:

1. **Task to models** — task guides shortlist suitable models and explain trade-offs.
2. **Portfolio to team** — combined-workload guides select the smallest practical set of models for several tasks and constraints.
3. **Model to details** — canonical model pages document capabilities, versions, deployment options, limitations, and evidence.
4. **Capability to models** — comparison matrices group models by features such as reasoning, tool use, vision, audio, structured output, or local deployment.

A task or portfolio guide may recommend one model for several workloads, but the canonical technical description remains on the model page.

## Team topologies

Compare at least these system shapes when selecting a model team.

### Single generalist

One model performs every supported task.

Prefer this when model residency, simplicity, privacy, or limited hardware matters more than achieving the absolute best result for each task.

### Generalist with specialist fallback

One resident model handles most work. A specialist is loaded or called only for tasks where the generalist misses a required quality threshold.

This is often the practical default for constrained local hardware or mixed local and hosted operation.

### Specialist team

Different models handle different task classes.

Prefer this only when specialist quality gains are material and the system can absorb additional model residency, switching, API, and orchestration costs.

### Router with quality tiers

A low-cost model handles routine work and escalates difficult or high-risk cases to a stronger model.

The router itself must be evaluated because incorrect routing can erase the expected savings.

## Total system cost

Do not compare only per-token API prices or isolated inference speed. Measure the complete system cost.

### Hosted models

Include:

- input, cached-input, output, tool, storage, and grounding charges;
- retries and verification calls;
- minimum billing units or subscription costs;
- provider rate limits and concurrency;
- expensive escalation frequency;
- data-handling and regional constraints.

### Local models

Include:

- model weights and runtime memory;
- KV-cache growth at the required context size;
- simultaneous model residency;
- model loading, unloading, and warm-up time;
- CPU and GPU offloading behavior;
- quantization quality loss;
- throughput under concurrent agents;
- power, storage, and operational overhead.

The largest single model that fits in VRAM is not automatically optimal. A smaller resident model may complete the full workflow faster than repeatedly loading several stronger specialists.

## Model residency and scheduling

Record how the proposed team uses memory:

- **concurrent residency** — several models must remain loaded because tasks run in parallel;
- **sequential residency** — one model can be unloaded before another is needed;
- **shared generalist** — several agents use one loaded model with different prompts, tools, or roles;
- **remote specialist** — a local model handles common work and calls a hosted specialist only when required;
- **CPU or storage standby** — inactive models remain available but incur reload latency.

A recommendation should state whether its memory estimate is for one active model, several simultaneous models, or a sequential schedule.

## Model-level and quantization-level decisions

Recommendations should normally name an exact model or model version without treating each quantization as a separate model.

Quantization belongs on the canonical model page because it changes deployment behavior rather than the model's identity. The model page should record, when relevant:

- full-precision and reduced-precision variants;
- recommended quantizations;
- expected quality loss or task-specific regressions;
- RAM and VRAM requirements;
- inference speed and context constraints;
- runtime and format compatibility;
- the best-quality option and the practical default.

Task and portfolio guides may reference a recommended quantization when hardware, latency, or simultaneous residency is part of the recommendation.

## Selection dimensions

Record only dimensions that materially affect the decision.

### Workload quality

- task success rate and failure severity;
- reasoning depth and consistency;
- instruction following;
- factuality and grounding;
- output style and language quality;
- domain-specific performance.

### Agent and automation suitability

- suitability as the reasoning model inside an agent;
- tool-calling and function-calling reliability;
- structured-output reliability;
- planning and multi-step execution;
- recovery from tool failures;
- context retention across long workflows;
- whether the model is itself agentic or only suitable as an agent component.

### Modalities

Record supported input and output modalities separately:

- text;
- images;
- audio and speech;
- video;
- documents or mixed multimodal context.

A model should be called multimodal only when the relevant combination is explicit. Image understanding does not imply image generation, and speech recognition does not imply speech synthesis.

### Access, cost, and deployment

- free, paid, usage-limited, or enterprise access;
- API, hosted application, downloadable weights, or local runtime;
- source model and license as separate fields;
- offline capability;
- privacy and data-handling implications;
- hardware requirement, latency, throughput, and concurrency;
- provider availability, regional restrictions, and version stability.

### Content-policy profile

When relevant to the use case, record whether a model or deployment is commonly described as:

- provider-moderated or policy-restricted;
- self-hosted with configurable safeguards;
- permissive, abliterated, or marketed as uncensored;
- unknown or not independently verified.

Do not infer this label from marketing language alone. Record the exact artifact or deployment because the same base model may have differently aligned fine-tunes, system prompts, provider filters, or runtime controls.

## Model recommendation record

A model recommendation entry may use these compact fields when relevant:

```text
Model:
Version or artifact:
Primary workloads:
Secondary workloads:
Modalities:
Reasoning:
Agent suitability:
Tool and structured-output support:
Access model:
Cost model:
Source model:
License:
Deployment modes:
Content-policy profile:
Hardware requirement:
Residency role:
Strengths:
Limitations:
Evidence:
Verified:
```

Do not include empty fields merely to satisfy the template. Keep cost, source availability, and license separate.

## Team recommendation record

A portfolio recommendation should additionally state:

```text
Workload portfolio:
Required quality thresholds:
Selected models and assigned roles:
Tasks covered by each model:
Fallback and escalation rules:
Concurrent or sequential residency:
Peak RAM and VRAM:
Expected switching or loading overhead:
Hosted API cost assumptions:
Why one generalist is or is not sufficient:
Rejected alternatives:
Evidence:
Verified:
```

## Recommendation levels

Use consistent labels across task guides:

- **Preferred** — strongest practical default for the stated constraints.
- **Alternative** — credible choice with a different quality, cost, privacy, or deployment trade-off.
- **Specialized** — recommended for a narrow subtask rather than general use.
- **Experimental** — promising but insufficiently verified or operationally unstable.
- **Not recommended** — fails a material requirement for the stated workload; the reason must be explicit.

A model may receive different labels in different task guides. A preferred single-task model may still be excluded from a preferred team when its marginal benefit does not justify another active model or API dependency.

## Evidence and maintenance

Every concrete recommendation should identify:

- the exact model version, API snapshot, or downloadable artifact;
- the evaluation date;
- whether evidence is first-party documentation, an external benchmark, repository testing, or a reproducible local experiment;
- the hardware, runtime, prompts, parameters, and quantization when they affect the result;
- important limitations or conflicting evidence.

Do not rank models from one aggregate benchmark alone. Prefer task-specific evaluations and repeatable workflow tests. Re-check recommendations after material model, provider, runtime, hardware, or pricing changes.

For a model team, evaluate the complete end-to-end workflow rather than summing isolated benchmark scores.

## Task guides

The task-oriented guides are:

- [`agents/`](./sub/agents/) — agent reasoning, planning, tool use, structured output, and long-running workflows.
- [`coding/`](./sub/coding/) — code generation, modification, debugging, review, and repository-scale work.
- [`translation-and-localization/`](./sub/translation-and-localization/) — translation quality, terminology, formatting, and localization workflows.
- [`generative-media/`](./sub/generative-media/) — image, video, music, sound, speech, and voice generation.
- [`perception-and-evaluation/`](./sub/perception-and-evaluation/) — image, audio, video, and document understanding, including model-output evaluation.
- [`speech-and-conversation/`](./sub/speech-and-conversation/) — speech-to-text, speaker diarization, speaker identification, and conversational transcription.
- [`combined-workloads/`](./sub/combined-workloads/) — portfolio-level team design, role assignment, model residency, routing, and cost optimization across several tasks.

Create each guide only with real evaluation criteria or recommendations; do not add empty category pages.

## High-risk synthetic media

Voice cloning, face replacement, impersonation, and other deepfake workflows require explicit consent, identity-protection controls, provenance or disclosure where applicable, and a review of legal and platform restrictions. A recommendation must not present technical capability while omitting these adoption constraints.

## Related pages

- [Models](../../../../../software/sub/models/)
- [Model Selection](../../../concepts/sub/evaluation-and-operations/sub/model-selection/)
- [Benchmarks](../../../benchmarks/)
- [Agentic Systems](../agentic-systems/)
- [Disclaimer](../../../../disclaimer/)
