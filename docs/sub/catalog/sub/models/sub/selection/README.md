# Model Selection

Choose models or model portfolios for a concrete task using explicit acceptance criteria, evidence boundaries, and deployment constraints.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Current task areas

- [`software-development/`](./sub/software-development/) — coding, debugging, testing, review, architecture, and repository-scale software work.
- [`language-and-research/`](./sub/language-and-research/) — language work, research, writing, translation, summarization, and related text tasks.
- [`agents-and-automation/`](./sub/agents-and-automation/) — tool use, planning, long-running execution, computer use, and agent workloads.
- [`media-creation/`](./sub/media-creation/) — image, video, speech, music, sound, and other generative-media tasks.
- [`content-understanding/`](./sub/content-understanding/) — image, video, speech, audio, and document understanding.
- [`evaluation-and-quality-control/`](./sub/evaluation-and-quality-control/) — independent model-assisted evaluation and QC tasks.
- [`model-teams/`](./sub/model-teams/) — model portfolios, role assignment, routing, ensembles, and consensus.

## Decision boundary

Start from the task: `I want a model to <task>`. Compare exact model identities, versions, or artifacts that could perform that task. Link canonical technical facts from [Model Reference](../reference/) instead of copying full model profiles here.

A recommendation must state the workload, acceptance criteria, evidence basis, important deployment assumptions, and material trade-offs. Mutable facts such as pricing, API availability, hosted features, context limits, and provider terms must be checked at decision time.

Broader solution selection that chooses software, services, hardware, runtimes, deployment topology, or operational processes in addition to models does not belong here merely because models are involved.

## Selection method

Define the assignment before naming candidates. Record the relevant input/output contract, quality target, failure severity, modalities, data/privacy boundary, latency or throughput requirements, budget constraint, and any model-specific access or deployment condition that can change the decision.

Shortlist exact model identities, versions, or materially distinct artifacts. Do not compare a vague family name when the decision actually depends on a concrete model, hosted ID, revision, fine-tune, quantization, or conversion. A derived artifact remains related to its base model; it becomes a separately evaluated selection unit only when its behavior or operating constraints materially differ.

Use deterministic validators before model judgment when they can directly prove a required property. Evaluate terminal acceptance on representative work rather than converting one leaderboard score, parameter count, token price, or provider claim into a recommendation.

### Evidence states

Keep the evidence basis visible. Useful states include:

- **Provider-documented** — an official model card, specification, documentation, or provider measurement; useful for identity and provider claims but not independent task validation.
- **AI Lab tested** — a reproducible AI Lab evaluation under recorded assignment conditions.
- **External benchmark** — an independent evaluation with methodology and scope that can be inspected.
- **Community report** — operational signal that still requires validation before material adoption decisions.
- **Inference** — an explicitly labeled conclusion derived from cited facts rather than a directly measured result.
- **Untested** — no qualifying evidence for the stated assignment.

Conflicting evidence should remain visible rather than being flattened into a single confidence-free score.

### Recommendation states

Use compact decision labels only after the assignment and evidence are explicit:

- **Preferred** — strongest practical default for the stated constraints and evidence.
- **Alternative** — credible option with a materially different trade-off.
- **Specialized** — appropriate for a narrower task or subtask rather than general default use.
- **Experimental** — promising but insufficiently verified or operationally unstable for the target quality level.
- **Not recommended** — fails a material requirement; state the failed requirement.

A recommendation label is not an intrinsic model property and must not be copied across tasks or environments.

### Quality and acceptance

When useful, distinguish exploration, concept-draft, working-result, production-quality, and exceptional-quality targets. The same model may be acceptable at one quality tier and fail another.

Measure the dimensions that actually determine acceptance: task success, omissions, unsupported output, factual grounding where relevant, structured-output or tool-call reliability, recovery behavior, useful retry count, required independent review, quality ceiling, and unsuitable tasks. Add modality-specific dimensions on the corresponding task page.

### Reliability profile

Treat reliability as an **assignment-specific evidence profile**, not a universal model score. A profile binds an exact model/version/artifact or hosted snapshot to one bounded task class, target quality tier, representative input distribution, acceptance criteria, verification design, and the runtime/hosted conditions that materially affect behavior.

Create a separate profile when a material part of that unit changes. Do not transfer reliability from one quantization to another, from hosted to local execution, from one task class to another, or from a lower quality tier to production use without evidence that the result still applies.

Record observable behavior that changes a model-selection decision, including:

- demonstrated strengths under the stated assignment;
- recurring error signatures rather than vague impressions;
- omitted-requirement risk against an explicit checklist;
- premature-completion risk when the model claims success before required artifacts or checks exist;
- useful retry count observed before additional same-assignment attempts stop improving acceptance;
- correction/recovery behavior after targeted feedback;
- quality ceiling under the recorded conditions;
- forbidden or unsuitable tasks and failure-severity limits;
- required deterministic validators, independent reviewer, or human approval gate.

Worker self-report is not completion evidence. Verify acceptance against produced artifacts, deterministic checks, tool results, provider state when relevant, or an independent QC/reviewer path.

Repeatedly similar failures after targeted correction should be treated as evidence of a capability gap rather than justification for unlimited retries. Model-team escalation rules belong under [Model Teams](./sub/model-teams/); infrastructure retry/backoff, provider failover, GPU/runtime degradation, and service recovery belong outside model-selection ownership.

### Cost and trade-offs

Compare total cost **per accepted result**, not isolated request price or raw inference speed. Include model calls, retries, verification/reviewer calls, failed attempts, and any model-specific switching or access overhead that materially changes the candidate comparison. Broader infrastructure ownership and lifecycle economics remain outside this subtree.

Prefer the smallest or cheapest candidate only when it still passes the required acceptance gate. Conversely, a stronger model is not automatically preferred if its measured improvement does not justify the additional cost, latency, privacy exposure, or operational dependency for the stated task.

## Evidence maintenance

Every material recommendation should record the exact evaluated model/version/artifact, evaluation date, relevant runtime or hosted configuration when it affects results, prompt/tool/context assumptions, limitations, conflicting evidence, and re-evaluation triggers.

Re-evaluate when the exact model or artifact changes, a provider silently changes an alias or hosted surface, pricing/access materially changes the decision, the workload or acceptance criteria change, or new evidence invalidates a prior conclusion.

## Recycled legacy guidance

The earlier model-selection section is an input corpus, not the target taxonomy. Broad legacy pages may split across several task areas, and stale recommendations are not carried forward without current evidence. Practical user-scenario material is intentionally outside this migration scope.
