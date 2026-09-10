# Documentation Requirements

## Requirements

- Teach reasoning budgets as explicit limits or control choices for additional inference-time effort, such as provider reasoning/thinking levels, token/step budgets, wall-clock time, latency targets, monetary/compute budget, sampling/search attempts, or external tool/verification work where the execution path exposes those dimensions.
- Select the budget from task value, difficulty, acceptance criteria, failure/consequence cost, latency objective, and available resources rather than maximizing reasoning effort by default.
- Establish a simpler baseline before increasing effort where practical. Compare the marginal accepted-result improvement from additional compute against added latency, token/compute consumption, tool cost, and failure/retry behavior.
- Treat extra reasoning as an option with diminishing, noisy, or non-monotonic returns. Define stop, timeout, escalation, fallback, or route-change behavior instead of allowing unbounded deliberation or repeated failed strategies.
- Keep the complete task objective, material constraints, relevant context/evidence, and required output/acceptance criteria stable enough for meaningful effort comparisons. A larger budget cannot repair missing evidence, denied permissions, unsupported capability, or an invalid task definition by itself.
- Distinguish model-side reasoning budget from external workflow budget. Internal inference effort, repeated sampling, tool calls, search, verification, agent loops, and human review can consume different resources and should be accounted separately when they are controlled by different components.
- Evaluate budgets using accepted-result quality plus latency, token/compute use, external/tool cost, failure/retry rate, and any operational deadline or service objective that matters to the workload.
- For consequential outputs, allocate enough budget for required verification or route the result to deterministic checks, tools, external evidence, or human review rather than treating internal deliberation as proof of correctness.
- Do not require visible or hidden chain-of-thought as an audit artifact. Preserve externally inspectable evidence, calculations, tool results, validation outcomes, citations, decision records, or concise explanations when reviewability is required.
- Treat hidden/visible reasoning exposure as independent from budget adequacy. A platform can spend more internal compute without revealing it, and revealing more reasoning text does not prove that a larger or better-validated budget was used.
- Keep provider-specific effort labels, exact token accounting, prices, hard limits, API semantics, hidden-reasoning behavior, and measured quality/cost curves with catalog/evidence owners.

## Validation

- Maximum reasoning effort is not the default recommendation.
- Budget choice is tied to task value, acceptance/failure cost, latency, and measured marginal benefit.
- Internal reasoning effort is distinguished from external tools/search/agent-loop/human-review budgets.
- More effort is not treated as proof of correctness, factuality, safety, or authorization.
- Auditability does not require disclosure of private chain-of-thought.
- Mutable provider controls and measured curves remain evidence/catalog-owned.
