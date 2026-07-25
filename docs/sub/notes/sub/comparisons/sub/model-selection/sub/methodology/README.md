# Model Selection Methodology

Detailed methodology for comparing individual AI models and complete model portfolios without reducing the decision to one benchmark score.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Selection units

Use two connected units.

### Individual task

Choose a model for one bounded task with explicit inputs, outputs, quality requirements, failure severity, data boundaries, latency, and cost constraints.

### Workload portfolio

Choose the smallest practical model set that covers the complete workload. A slightly weaker generalist may be preferable when it replaces several resident specialists, reduces cold starts, lowers orchestration complexity, and still satisfies every acceptance threshold.

Add a specialist only when its measured improvement justifies the additional memory, latency, routing, maintenance, and provider dependency.

## Decision sequence

1. Define the workload and acceptance criteria.
2. Identify deterministic tools and validators that should run before a model.
3. Set the required quality tier and failure severity.
4. Record modality, privacy, licensing, access, latency, concurrency, and budget constraints.
5. Shortlist exact model versions or artifacts.
6. Test whether one model can cover several compatible tasks or roles.
7. Define fallback, retry, escalation, and human-approval rules.
8. Measure terminal acceptance and total cost on the complete workflow.
9. Record evidence, limitations, and a verification date.

## Comparison vocabulary

Use compact categorical labels instead of star-heavy matrices or unsupported aggregate scores.

### Recommendation

- **Preferred** — strongest practical default for the stated constraints.
- **Alternative** — credible choice with a different quality, cost, privacy, or deployment trade-off.
- **Specialized** — appropriate for a narrow subtask rather than general use.
- **Experimental** — promising but insufficiently verified or operationally unstable.
- **Not recommended** — fails a material requirement for the stated workload; state the reason.

### Deployment fit

- **Comfortable** — expected to leave practical runtime and context headroom under the stated assumptions.
- **Constrained** — may fit only with limited context, batching, offload, or other explicit compromises.
- **Sequential only** — usable after unloading another model or service.
- **Impractical** — does not fit or misses the required latency, quality, or operational threshold.
- **Unknown** — evidence is insufficient; do not infer fit from parameter count or weight size alone.

### Evidence state

- **Provider-documented** — supported by official documentation, model cards, pricing, or specifications.
- **Repository-tested** — supported by a reproducible AI Lab experiment.
- **External benchmark** — supported by an independently published evaluation with known methodology.
- **Community report** — useful operational signal that still requires validation.
- **Inference** — a clearly labeled conclusion derived from cited facts.
- **Untested** — not yet evaluated for the stated assignment.

Do not collapse these dimensions into a single score. A model can have high capability but poor deployment fit, weak evidence, or unacceptable data handling for a particular task.

## Team topologies

### Single generalist

One model covers every supported task. Prefer this when simplicity, privacy, residency, or limited hardware matters more than the absolute best result for each task.

### Generalist with specialist fallback

One resident model handles routine work. A specialist is loaded or called only when the generalist misses a declared capability or quality threshold.

### Specialist team

Different models handle different task classes. Use this only when the specialist gains are material and the system can absorb additional services, memory, switching, and orchestration cost.

### Router with quality tiers

A low-cost route handles routine cases and escalates difficult or high-risk cases. Evaluate the router independently because incorrect routing can erase expected savings.

## Total system cost

Measure cost per accepted result, not only token price or isolated throughput.

### Hosted deployments

Include:

- input, cached-input, output, tool, storage, media, and grounding charges;
- retries, verification, and escalation calls;
- subscriptions or minimum billing units;
- rate limits and concurrency;
- regional, retention, and data-handling constraints;
- provider failure and migration cost.

### Local deployments

Include:

- model files, runtime memory, KV cache, and host RAM;
- concurrent and sequential residency;
- load, unload, warm-up, and first-token latency;
- CPU or GPU offload;
- quantization quality loss;
- throughput under realistic concurrency;
- power, storage, maintenance, and operator time.

A smaller resident model may complete a portfolio faster and more cheaply than repeatedly loading stronger specialists.

## Residency and scheduling

Record whether the design uses:

- **concurrent residency** — several services remain loaded simultaneously;
- **sequential residency** — one service is unloaded before another starts;
- **shared generalist** — several agents use one loaded model through different prompts, tools, or roles;
- **remote specialist** — a local route calls a hosted model only when required;
- **CPU or storage standby** — inactive artifacts remain available but incur reload latency.

Every memory estimate must state whether it covers one active model, concurrent services, or a sequential schedule.

## Model and artifact identity

Compare the base model first. Treat a quantization, hosted alias, fine-tune, runtime conversion, or provider deployment as a separate evaluated artifact only when it materially changes behavior or operation.

A concrete recommendation should record:

```text
Model:
Version or artifact:
Primary workloads:
Secondary workloads:
Modalities:
Reasoning and agent suitability:
Tool and structured-output support:
Access and cost model:
License and source model:
Deployment modes:
Content-policy profile:
Hardware requirement:
Residency role:
Strengths:
Limitations:
Evidence:
Verified:
```

Do not include empty fields merely to satisfy the template.

## Portfolio record

A model-team recommendation should additionally record:

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

## Selection dimensions

Record only dimensions that materially affect the decision.

### Quality and reliability

- task success and failure severity;
- instruction following and omission risk;
- factuality and grounding;
- reasoning consistency;
- structured-output and tool-call reliability;
- recovery from tool failures;
- premature-completion risk;
- useful retry count and escalation point;
- independent-review requirements;
- quality ceiling and unsuitable tasks.

### Modalities

Record supported inputs and outputs separately: text, image, audio, speech, video, documents, and mixed multimodal context. Image understanding does not imply image generation, and speech recognition does not imply speech synthesis.

### Access and policy

Record:

- free, paid, usage-limited, or enterprise access;
- API, hosted application, downloadable weights, or local runtime;
- license and usage restrictions;
- offline and privacy capability;
- provider moderation, configurable safeguards, or an exact permissive or abliterated artifact where relevant;
- regional and version-stability constraints.

Do not infer an uncensored or policy profile from marketing language alone. The same base model may have differently aligned fine-tunes, system prompts, provider filters, and runtime controls.

## Quality tiers

Use the repository quality tiers consistently:

1. **Exploration** — feasibility and direction.
2. **Concept draft** — meaningful draft for discussion.
3. **Working result** — functionally acceptable with known limitations.
4. **Production quality** — verified, maintainable, documented, and ready for use.
5. **Exceptional quality** — additional depth or polish justified by output value.

A cheaper or local model may be sufficient for lower tiers while a hosted flagship, specialist, independent reviewer, or human gate is required for higher tiers.

## Evidence and maintenance

Every concrete recommendation should identify:

- the exact model, API snapshot, or downloadable artifact;
- the evaluation date;
- the evidence type;
- hardware, runtime, prompt, parameters, tools, context, and quantization when relevant;
- limitations, conflicting evidence, and re-evaluation triggers.

Do not convert one leaderboard score directly into a recommendation. Evaluate the complete end-to-end workflow and preserve raw results where practical.

## High-risk synthetic media

Voice cloning, face replacement, impersonation, and other deepfake workflows require explicit consent, identity protection, provenance or disclosure where applicable, and review of legal and platform restrictions. Technical capability is not sufficient adoption guidance.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Local Model Selection by VRAM](../local-models-by-vram/)
- [Reliability Profiles](../reliability-profiles/)
- [Combined Workloads](../combined-workloads/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../disclaimer/)
