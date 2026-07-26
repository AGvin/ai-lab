# AI Model Selection and Team Design

Choose an AI model or the smallest practical model portfolio for a concrete task, quality target, environment, and budget.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Start here

| Need | Open |
| --- | --- |
| Select one model for a bounded task | Use the matching [task guide](#task-guides) |
| Select models for several connected tasks | [Combined Workloads](./sub/combined-workloads/) |
| Choose a local model by available GPU memory | [Local Model Selection by VRAM](./sub/local-models-by-vram/) |
| Assign orchestrator, worker, reviewer, or other agent roles | [Agent Role Selection](./sub/agent-role-selection/) |
| Define retries, escalation, and unsuitable-task boundaries | [Reliability Profiles](./sub/reliability-profiles/) |
| Design decomposition, scheduling, and resource control | [Orchestration](./sub/orchestration/) |
| Understand comparison labels, evidence, and cost accounting | [Model Selection Methodology](./sub/methodology/) |
| Understand SLM, LLM, frontier, dense, sparse, MoE, and ecosystem labels | [Model Classification](../../../concepts/sub/model-classification/) and [Model Architectures](../../../concepts/sub/model-architectures/) |
| Inspect canonical provider, family, version, and artifact facts | [Models](../../../../../software/sub/models/) |

## Classification fields

Comparison tables may use the following independent fields when they improve the decision:

| Field | Canonical documentation |
| --- | --- |
| Scale class: SLM or LLM | [Small and Large Language Models](../../../concepts/sub/model-classification/sub/language-model-scale/) |
| Architecture: dense, sparse, or MoE | [Dense and Sparse Architectures](../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) and [Mixture of Experts](../../../concepts/sub/model-architectures/sub/mixture-of-experts/) |
| Frontier status | [Frontier Models](../../../concepts/sub/model-classification/sub/frontier-models/) |
| Ecosystem status: experimental, emerging, mainstream, or legacy | [AI Glossary](../../../glossary/#model-ecosystem-status) |

These fields are orthogonal. Do not infer deployment, access, hardware fit, quality, licensing, or safety from one classification label. Link table headings, legends, or the first meaningful use to the canonical concept page instead of repeating complete definitions in each comparison.

## Fast decision path

1. Define the exact task or complete workload portfolio.
2. Set acceptance criteria, quality tier, failure severity, privacy boundary, latency, and budget.
3. Run deterministic tools and validators before assigning work to a model.
4. Shortlist exact model versions, API snapshots, or downloadable artifacts.
5. Prefer one generalist when it covers several roles without unacceptable quality loss.
6. Add specialists only when their measured improvement justifies memory, switching, API, and orchestration cost.
7. Define bounded retries, independent verification, escalation, and human approval before execution.
8. Compare terminal acceptance and cost per accepted result, not only benchmark score, token price, or parameter count.

## Portfolio shapes

| Shape | Use when | Main risk |
| --- | --- | --- |
| Single generalist | Simplicity, privacy, or one resident model matters most | Capability gaps and self-review bias |
| Generalist with specialist fallback | Most work is routine but some tasks need stronger or different capability | Incorrect escalation policy |
| Specialist team | Specialization produces material accepted-result gains | Residency, switching, and service complexity |
| Router with quality tiers | High-volume work can start on a cheaper validated route | Routing errors can erase savings |
| Hybrid local and hosted | Private routine work stays local while difficult work escalates | Data classification and provider dependency |

Concrete starting portfolios for one or two 24 GB GPUs, CPU-only, cloud-only, hybrid, always-on local, on-demand image POD, low-budget, low-latency, and maximum-quality environments are listed under [Environment Profiles](./sub/combined-workloads/sub/environment-profiles/).

## Task guides

| Workload | Guide |
| --- | --- |
| Agent reasoning, planning, tool use, and long-running execution | [Agents](./sub/agents/) |
| Orchestrator, planner, router, worker, reviewer, verifier, evaluator, advisor, memory, and context roles | [Agent Role Selection](./sub/agent-role-selection/) |
| Decomposition, scheduling, delegation, lifecycle, verification, and stopping | [Orchestration](./sub/orchestration/) |
| Code generation, modification, debugging, review, tests, and repository-scale work | [Coding](./sub/coding/) |
| General translation, technical documentation, UI strings, terminology, and multilingual review | [Translation and Localization](./sub/translation-and-localization/) |
| Image, video, music, sound, speech, voice generation, and editing | [Generative Media](./sub/generative-media/) |
| ASR, transcription, diarization, TTS, and real-time voice systems | [Speech and Conversation](./sub/speech-and-conversation/) |
| Image, document, video, and audio understanding plus output evaluation | [Perception and Evaluation](./sub/perception-and-evaluation/) |
| Teams of models for connected tasks and constrained environments | [Combined Workloads](./sub/combined-workloads/) |

## Evidence boundary

A concrete recommendation must identify the exact model or artifact, deployment assumptions, evidence type, limitations, and verification date. Mutable facts such as API price, access, license, context limits, and provider availability must be rechecked before adoption.

Use categorical recommendation, deployment-fit, and evidence labels from the [methodology guide](./sub/methodology/). Do not convert one leaderboard score directly into a recommendation or treat a quantization as an unrelated base model.

Canonical technical descriptions belong under [Models](../../../../../software/sub/models/). Selection guides should contain only workload-specific trade-offs, assignments, routing, and validation requirements.

## Reliability and operations

Use [Reliability Profiles](./sub/reliability-profiles/) to record omission risk, premature-completion risk, useful retry count, review requirements, unsuitable tasks, escalation, degraded operation, quality ceiling, and cost per accepted result.

Use [Resource Lifecycle Orchestration](./sub/orchestration/sub/resource-lifecycle/) when models or GPU services are resident, lazy-loaded, mutually exclusive, temporary, hosted, or started on demand. A worker reporting completion is not proof that a billable resource stopped.

## High-risk media

Voice cloning, face replacement, impersonation, and other deepfake workflows require explicit consent, identity protection, provenance or disclosure where applicable, and review of legal and platform restrictions. See [Generative Media](./sub/generative-media/) for the operational boundaries.

## Related pages

- [Model Classification](../../../concepts/sub/model-classification/)
- [Model Architectures](../../../concepts/sub/model-architectures/)
- [AI Glossary](../../../glossary/)
- [Model Selection concept](../../../concepts/sub/evaluation-and-operations/sub/model-selection/)
- [Benchmarks](../../../benchmarks/)
- [Agentic Systems](../agentic-systems/)
- [Repository-Original Content and Research Candidates](../../../repository-original-content/)
- [General repository disclaimer](../../../../../disclaimer/)
