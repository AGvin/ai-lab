# Model Selection Methodology

Detailed methodology for comparing individual AI models and complete model portfolios without reducing the decision to one benchmark score.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Selection units

### Individual task

Choose a model for one bounded task with explicit inputs, outputs, quality requirements, failure severity, data boundaries, latency, and cost constraints.

### Workload portfolio

Choose the smallest practical model set that covers the complete workload. A slightly weaker generalist may be preferable when it replaces several resident specialists, reduces cold starts, lowers orchestration complexity, and still satisfies every acceptance threshold.

Add a specialist only when its measured improvement justifies additional memory, latency, routing, maintenance, and provider dependency.

## Decision sequence

1. Define the workload and acceptance criteria.
2. Identify deterministic tools and validators that should run before a model.
3. Set the required quality tier and failure severity.
4. Record modality, privacy, license, access, latency, concurrency, and budget constraints.
5. Shortlist exact model versions or artifacts.
6. Record scale, architecture, frontier status, and ecosystem status only when those fields materially improve the decision.
7. Test whether one model can cover several compatible tasks or roles.
8. Define fallback, retry, escalation, and human-approval rules.
9. Measure terminal acceptance and total cost on the complete workflow.
10. Record evidence, limitations, and a verification date.

## Comparison vocabulary

Use compact categorical labels instead of star-heavy matrices or unsupported aggregate scores.

### Recommendation

- **Preferred** — strongest practical default for the stated constraints.
- **Alternative** — credible choice with a different quality, cost, privacy, or deployment trade-off.
- **Specialized** — appropriate for a narrow subtask rather than general use.
- **Experimental** — promising but insufficiently verified or operationally unstable.
- **Not recommended** — fails a material requirement; state the reason.

### Deployment fit

- **Comfortable** — measured to leave practical runtime and context headroom under stated assumptions.
- **Constrained** — meets the minimum only with explicit compromises.
- **Sequential only** — usable after unloading another model or service.
- **Impractical** — does not fit or misses a required latency, quality, or operational threshold.
- **Unknown** — evidence is insufficient; do not infer fit from parameter count or weight size.

### Evidence state

- **Provider-documented** — official documentation, model card, pricing, or specification.
- **Repository-tested** — reproducible AI Lab experiment.
- **External benchmark** — independent evaluation with known methodology.
- **Community report** — operational signal that still requires validation.
- **Inference** — clearly labeled conclusion derived from cited facts.
- **Untested** — not evaluated for the stated assignment.

### Model classification fields

Classification fields describe independent model properties. Use them only when they help distinguish candidates, and link the table heading, legend, or first meaningful use to the canonical concept page.

| Field | Values | Canonical meaning |
| --- | --- | --- |
| Scale class | `SLM`, `LLM`, `Unclear` | Relative language-model scale in the stated comparison context. There is no universal parameter threshold. See [Small and Large Language Models](../../../../../concepts/sub/model-classification/sub/language-model-scale/). |
| Architecture | `Dense`, `Sparse — MoE`, `Other sparse`, `Unknown` | Parameter activation architecture, independent from scale and deployment. See [Dense and Sparse Architectures](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) and [Mixture of Experts](../../../../../concepts/sub/model-architectures/sub/mixture-of-experts/). |
| Frontier status | `Supported`, `Not supported`, `Unclear`, `Not assessed` | Date- and scope-bounded evidence that a model is near the current capability frontier. See [Frontier Models](../../../../../concepts/sub/model-classification/sub/frontier-models/). |
| Ecosystem status | `Experimental`, `Emerging`, `Mainstream`, `Legacy`, `Unclear` | Adoption, tooling support, documentation maturity, and operational familiarity. See the [AI Glossary](../../../../../glossary/#model-ecosystem-status). |

Do not infer one field from another:

- SLM does not mean local-only, and LLM does not mean provider-hosted-only.
- Quantization changes representation and resource requirements but does not reclassify an underlying LLM as an SLM.
- Dense does not mean small, and MoE does not automatically mean faster, frontier, or locally practical.
- Frontier does not mean mainstream, safest, most reliable, or best for the task.
- Mainstream does not mean frontier or highest quality.

For an MoE model, record total and active parameters separately when reliable values are available. Active parameters must not be used as a storage or VRAM estimate, and undocumented active counts must not be derived from expert count or naming conventions.

Do not collapse recommendation, deployment fit, evidence state, or classification fields into a single score. A capable model may still have poor deployment fit, weak evidence, immature tooling, or unacceptable data handling.

## Team topologies

- **Single generalist** — one model covers all validated tasks; useful when simplicity, privacy, or residency dominates.
- **Generalist with specialist fallback** — one resident route handles routine work and escalates declared gaps.
- **Specialist team** — separate models handle task classes when measured gains justify additional services and switching.
- **Router with quality tiers** — routine cases start on a cheaper validated route and escalate by explicit policy.

Evaluate the router independently because incorrect routing can erase expected savings.

## Total system cost

Measure cost per accepted result, not only token price or isolated throughput.

### Hosted deployments

Include input, cached-input, output, media, tool, storage, and grounding charges; retries and verification; subscriptions or minimum units; rate limits; regional and retention constraints; and provider-failure or migration cost.

### Local deployments

Include model files, runtime memory, KV cache, host RAM, concurrent and sequential residency, load and warm-up time, CPU or GPU offload, quantization loss, realistic concurrency, power, storage, maintenance, and operator time.

A smaller resident model may complete a portfolio faster and more cheaply than repeatedly loading stronger specialists.

## Residency and scheduling

Record whether the design uses:

- **concurrent residency** — several services remain loaded;
- **sequential residency** — one service unloads before another starts;
- **shared generalist** — several agents share one model with different roles or tools;
- **remote specialist** — a local route calls a hosted service only when required;
- **CPU or storage standby** — inactive artifacts remain available but incur reload latency.

Every memory estimate must state whether it covers one active model, concurrent services, or a sequential schedule.

## Model and artifact identity

Compare the base model first. Treat a quantization, hosted alias, fine-tune, conversion, or provider deployment as a separate evaluated artifact only when it materially changes behavior or operation.

A concrete recommendation may record:

```text
Model and exact version or artifact:
Primary and secondary workloads:
Modalities:
Scale class and comparison context:
Architecture:
Total and active parameters, when applicable:
Frontier status, scope, evidence, and verification date:
Ecosystem status and verification date:
Reasoning and agent suitability:
Tool and structured-output support:
Access, cost, license, and source model:
Deployment modes and hardware requirement:
Content-policy profile:
Residency role:
Strengths and limitations:
Evidence and verification date:
```

A model-team recommendation should additionally record:

```text
Workload portfolio and quality thresholds:
Selected models, roles, and task coverage:
Fallback and escalation rules:
Concurrent or sequential residency:
Peak RAM and VRAM:
Loading and switching overhead:
Hosted cost assumptions:
Why one generalist is or is not sufficient:
Rejected alternatives:
Evidence and verification date:
```

Do not include empty fields merely to satisfy a template.

## Selection dimensions

### Quality and reliability

Record task success, failure severity, omission risk, factual grounding, reasoning consistency, structured-output and tool-call reliability, recovery behavior, premature-completion risk, useful retry count, escalation point, independent-review requirement, quality ceiling, and unsuitable tasks.

### Modalities

Record supported inputs and outputs separately: text, image, audio, speech, video, documents, and mixed multimodal context. Image understanding does not imply image generation, and speech recognition does not imply synthesis.

### Access and policy

Record free, paid, limited, or enterprise access; API, hosted, downloadable, or local deployment; license and usage restrictions; privacy and offline capability; provider moderation or exact permissive artifact; region; retention; and version stability.

Do not infer an uncensored or policy profile from marketing language. The same base model can have differently aligned fine-tunes, system prompts, provider filters, and runtime controls.

## Quality tiers

1. **Exploration** — feasibility and direction.
2. **Concept draft** — meaningful draft for discussion.
3. **Working result** — functionally acceptable with known limitations.
4. **Production quality** — verified, maintainable, documented, and ready for use.
5. **Exceptional quality** — additional depth or polish justified by output value.

A cheaper or local route may satisfy lower tiers while a flagship, specialist, independent reviewer, or human gate is required for higher tiers.

## Evidence and maintenance

Every concrete recommendation must identify the exact model, API snapshot, or artifact; evaluation date; evidence type; relevant hardware, runtime, prompt, tools, context, and quantization; limitations; conflicting evidence; and re-evaluation triggers.

Do not convert one leaderboard score directly into a recommendation. Evaluate the complete workflow and preserve raw results where practical.

## High-risk synthetic media

Voice cloning, face replacement, impersonation, and other deepfake workflows require explicit consent, identity protection, provenance or disclosure where applicable, and review of legal and platform restrictions. Technical capability is not sufficient adoption guidance.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Model Classification](../../../../../concepts/sub/model-classification/)
- [Small and Large Language Models](../../../../../concepts/sub/model-classification/sub/language-model-scale/)
- [Frontier Models](../../../../../concepts/sub/model-classification/sub/frontier-models/)
- [Model Architectures](../../../../../concepts/sub/model-architectures/)
- [AI Glossary](../../../../../glossary/)
- [Local Model Selection by VRAM](../local-models-by-vram/)
- [Reliability Profiles](../reliability-profiles/)
- [Combined Workloads](../combined-workloads/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)