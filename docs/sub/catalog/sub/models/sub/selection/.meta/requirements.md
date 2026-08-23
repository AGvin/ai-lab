# Documentation Requirements

## Requirements

- Present model selection through three distinct reader journeys rather than one flat list: `decision-guides/`, `user-scenarios/`, and `hardware/`.
- Use `decision-guides/` for task-, need-, constraint-, and model-portfolio-oriented choices; use the natural-intent test `I want a model to <task>` where task intent is governing.
- Use `user-scenarios/` when the reader's combined persona/scale, tasks, existing hardware, budget, skills, privacy/data boundary, deployment preference, and operational tolerance jointly change the model route.
- Use `hardware/` when the hardware target is already owned/fixed and the primary question is which models are practically viable on it. Keep hardware purchasing and canonical hardware facts outside this journey.
- Link canonical model facts from `../reference/` instead of duplicating full model descriptions.
- Require concrete recommendations to identify exact model/version/artifact scope, acceptance criteria, evidence basis, material runtime/deployment assumptions, and trade-offs.
- Define the assignment or route before candidate choice, including input/output contract, quality target, failure severity, modalities, privacy/data boundary, latency/throughput, budget, and access/deployment conditions when material.
- Compare exact model/version/artifact identities rather than vague family names when identity affects behavior or operation.
- Treat derived artifacts as separate evaluated selection units only when their behavior/operating constraints materially differ, while preserving their relationship to the base model.
- Use deterministic validators before model judgment when they directly prove an acceptance property.
- Keep provider-documented claims distinct from independent AI Lab task evidence.
- Preserve explicit evidence states such as provider-documented, AI Lab tested, external benchmark, community report, inference, and untested; keep conflicts visible.
- Do not collapse recommendation, evidence, deployment context, classification, price, benchmark, or reliability outcomes into one unsupported aggregate score.
- Use recommendation labels only as task- and evidence-bounded conclusions, never intrinsic model properties.
- Evaluate terminal acceptance and workload-specific failure modes rather than selecting from parameter count, one benchmark, token price, TOPS, or provider positioning alone.
- Treat reliability as assignment-specific and bound it to exact model/version/artifact or hosted snapshot, task class, quality tier, representative input distribution, acceptance criteria, verification design, and behavior-affecting runtime conditions.
- Require separate reliability evidence when material profile conditions change; do not transfer reliability across quantizations, hosted/local routes, unrelated tasks, or quality tiers without evidence.
- Preserve observable reliability dimensions where relevant: strengths, recurring failure signatures, omitted-requirement risk, premature-completion risk, correction behavior, useful retry count, quality ceiling, unsuitable tasks, failure-severity limits, and required independent validation.
- Treat worker self-report as insufficient terminal-acceptance proof when artifacts, deterministic checks, tool results, provider state, or independent QC can verify the claim.
- Treat repeated materially similar failures after targeted correction as possible capability-gap evidence rather than justification for unlimited retries.
- Keep model-team escalation logic under `decision-guides/model-teams/`; keep provider failover, infrastructure recovery, and service lifecycle outside model-selection ownership except as frozen constraints.
- When local resource fit affects a recommendation, require exact model/artifact/revision plus runtime, quantization/precision, context, batch/concurrency, auxiliary files, offload, and measured-memory conditions.
- State that published artifact/weight size is not peak runtime memory and successful loading does not prove useful context headroom, concurrency, latency, sustained behavior, or task quality.
- Treat unmeasured model/resource combinations as `Unknown`; do not infer fit from nominal VRAM/RAM, TOPS, or simple multi-device memory sums.
- Keep hardware purchase decisions, capacity-class buying guidance, sharding architecture, runtime product selection, resident-service scheduling, and host architecture outside model selection. `hardware/` may document these only as fixed conditions that affect model viability.
- Compare cost per accepted result, including material retries and verification/reviewer calls, rather than isolated request price or raw inference speed.
- Require material recommendations to record evaluation date, exact evaluated identity, runtime/hosted conditions, prompt/tool/context assumptions, limitations, conflicting evidence, and re-evaluation triggers.
- Recheck mutable pricing, availability, hosted features, limits, aliases, drivers/toolkits, runtime support, model exports, and provider terms when they materially affect a recommendation.
- Treat legacy model-selection pages as preservation/recycling input rather than destination-preserving source.

## Validation

- Every materialized child corresponds to an approved selected model-selection destination.
- `decision-guides/`, `user-scenarios/`, and `hardware/` answer distinct starting questions and do not duplicate ownership.
- Selection pages do not become alternate sources of canonical model or hardware identity/facts.
- Provider claims are not presented as independent AI Lab benchmark evidence.
- Recommendation/reliability labels are scoped to explicit task, conditions, constraints, and evidence.
- Published artifact size, nominal VRAM/RAM/TOPS, or successful load is not presented as practical local fit evidence.
- `hardware/` selects models for fixed hardware; it does not become a GPU/PC/SBC purchase guide or canonical hardware catalog.
- No broad infrastructure lifecycle/failover/solution architecture is migrated into model selection merely because models are components.
