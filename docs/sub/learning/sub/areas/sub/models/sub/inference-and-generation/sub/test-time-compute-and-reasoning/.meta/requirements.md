# Documentation Requirements

## Requirements

- Present Test-Time Compute and Reasoning as the model-inference learning group for strategies that spend additional inference-time computation, sampling, search, verification, or adaptive reasoning effort to improve accepted-result quality on suitable workloads.
- Use canonical Reasoning Models and related inference concepts for stable semantic boundaries; this learning group teaches workload selection, operating budgets, evidence/verification, and quality-versus-resource trade-offs rather than defining a model category by provider label.
- Distinguish model-side test-time reasoning from external workflow/agent orchestration. A model may spend more internal inference effort without an external search loop, while an application can add tools, search, verification, or multi-step control around any eligible model.
- Route reasoning-oriented modes where representative evaluation shows useful improvement for difficult, multi-step, constraint-rich, analytical, coding, mathematical, planning, or review tasks; do not make them the default merely because additional compute is available.
- Prefer a lower-effort mode, smaller model, direct deterministic operation, or simpler workflow for extraction, classification, transformation, or latency-sensitive work when it satisfies the acceptance criteria more efficiently.
- Give the model/system the complete objective, material constraints, relevant evidence/context, and output/acceptance contract before interpreting more reasoning effort as useful. Additional inference work does not repair a missing requirement, stale source, unavailable capability, denied permission, or invalid task definition by itself.
- Explain that more test-time compute is not guaranteed to improve results monotonically. Extra reasoning can pursue a wrong premise, amplify stale or incorrect evidence, add latency/cost, repeat a failed strategy, or produce a more elaborate unsafe answer.
- Keep consequential calculations, tool actions, external facts, and high-impact outputs independently verifiable when the application requires it. Concise final explanations, evidence, calculations, tool results, test outputs, or other externally inspectable artifacts can support review without exposing private hidden chain-of-thought.
- Evaluate routing and effort choices using accepted-result quality together with latency, token/compute use, tool/external-service cost, failure/retry rate, and operational constraints rather than quality in isolation.
- Explain that the current materialized subset focuses on `reasoning-budgets/` because the legacy Reasoning Models source contains source-backed effort/time/token/cost budgeting and routing guidance ready for migration.
- Do not imply that unmaterialized selected siblings `self-consistency-and-sampling/` or `search-and-verification/` are absent from the logical architecture; standard navigation reflects only physical children.
- Keep concrete provider effort controls, token accounting, prices, hidden-reasoning exposure behavior, APIs, measured improvements, and model recommendations with catalog/evidence/decision owners.

## Validation

- Test-time reasoning is not conflated with a provider label, external agent orchestration, or chain-of-thought visibility.
- More compute is not presented as monotonically improving correctness or safety.
- Simpler/deterministic routes remain valid when they satisfy the workload acceptance criteria.
- Consequential outputs can be verified through external evidence/artifacts without requiring hidden chain-of-thought.
- Current navigation exposes only materialized selected children.
- Mutable provider controls and measured benefits remain evidence/catalog-owned.
