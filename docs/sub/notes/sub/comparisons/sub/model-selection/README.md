# AI Model Selection Guides

Practical decision support for choosing AI models by workload, capability, access model, deployment constraints, and measured quality.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Draft. The selection framework and task taxonomy are defined here first. Concrete recommendations must be added only when the exact model version, evidence, access conditions, and evaluation date can be recorded.

## Purpose

There is no universally best model. A useful recommendation must identify the workload, minimum quality threshold, acceptable failure modes, deployment environment, cost constraints, and required modalities before comparing candidates.

This section complements the [Model Selection](../../../concepts/sub/evaluation-and-operations/sub/model-selection/) concept page. Canonical descriptions of model families and individual models belong under [Models](../../../../../software/sub/models/), while this comparison section owns task-oriented recommendations and cross-model decision matrices.

## Documentation model

Use three connected views instead of duplicating the same information:

1. **Task to models** — task guides shortlist suitable models and explain trade-offs.
2. **Model to details** — canonical model pages document capabilities, versions, deployment options, limitations, and evidence.
3. **Capability to models** — comparison matrices group models by features such as reasoning, tool use, vision, audio, structured output, or local deployment.

A task guide may recommend a model for several related workloads, but the canonical technical description remains on the model page.

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

Task guides may reference a recommended quantization only when hardware or latency is part of the recommendation.

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

A model should be called multimodal only when the relevant combination is explicit. For example, image understanding does not imply image generation, and speech recognition does not imply speech synthesis.

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

## Recommendation record

A recommendation entry may use the following compact fields when relevant:

```text
Model:
Version or artifact:
Primary workloads:
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
Strengths:
Limitations:
Evidence:
Verified:
```

Do not include empty fields merely to satisfy the template. Keep cost, source availability, and license separate.

## Recommendation levels

Use consistent labels across task guides:

- **Preferred** — strongest practical default for the stated constraints.
- **Alternative** — credible choice with a different quality, cost, privacy, or deployment trade-off.
- **Specialized** — recommended for a narrow subtask rather than general use.
- **Experimental** — promising but insufficiently verified or operationally unstable.
- **Not recommended** — fails a material requirement for the stated workload; the reason must be explicit.

A model may receive different labels in different task guides.

## Evidence and maintenance

Every concrete recommendation should identify:

- the exact model version, API snapshot, or downloadable artifact;
- the evaluation date;
- whether evidence is first-party documentation, an external benchmark, repository testing, or a reproducible local experiment;
- the hardware, runtime, prompts, parameters, and quantization when they affect the result;
- important limitations or conflicting evidence.

Do not rank models from one aggregate benchmark alone. Prefer task-specific evaluations and repeatable workflow tests. Re-check recommendations after material model, provider, runtime, or pricing changes.

## Task guides

The planned task-oriented guides are:

- [`agents/`](./sub/agents/) — agent reasoning, planning, tool use, structured output, and long-running workflows.
- [`coding/`](./sub/coding/) — code generation, modification, debugging, review, and repository-scale work.
- [`translation-and-localization/`](./sub/translation-and-localization/) — translation quality, terminology, formatting, and localization workflows.
- [`generative-media/`](./sub/generative-media/) — image, video, music, sound, speech, and voice generation.
- [`perception-and-evaluation/`](./sub/perception-and-evaluation/) — image, audio, video, and document understanding, including model-output evaluation.
- [`speech-and-conversation/`](./sub/speech-and-conversation/) — speech-to-text, speaker diarization, speaker identification, and conversational transcription.
- [`combined-workloads/`](./sub/combined-workloads/) — models selected for several workloads, such as coding plus localization.

Create each guide only with real evaluation criteria or recommendations; do not add empty category pages.

## High-risk synthetic media

Voice cloning, face replacement, impersonation, and other deepfake workflows require explicit consent, identity-protection controls, provenance or disclosure where applicable, and a review of legal and platform restrictions. A recommendation must not present technical capability while omitting these adoption constraints.

## Related pages

- [Models](../../../../../software/sub/models/)
- [Model Selection](../../../concepts/sub/evaluation-and-operations/sub/model-selection/)
- [Benchmarks](../../../benchmarks/)
- [Agentic Systems](../agentic-systems/)
- [Disclaimer](../../../../disclaimer/)
