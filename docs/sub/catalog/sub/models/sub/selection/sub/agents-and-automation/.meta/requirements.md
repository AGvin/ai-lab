# Documentation Requirements

## Requirements

- Define agent-model selection around complete-loop reliability rather than conversational quality or provider positioning.
- Cover the selected task families: tool/function calling, general agents, computer use, voice agents, planning/execution, long-running execution, and orchestrator/manager model roles.
- Preserve the useful legacy agent-evaluation dimensions: planning, tools, structured output, recovery, context retention, loop control, permissions, terminal acceptance, retries, corrections, time, and accepted-result cost.
- Require equivalent tools, permissions, environment state, context, and stopping rules for comparative evaluation.
- Include degraded/adversarial cases such as tool failures, stale instructions, prompt injection, and failed verification where applicable.
- Preserve useful concrete candidate hypotheses from the legacy agent guide only after current first-party identity/capability verification; present them as candidates to evaluate for explicit agent workloads, not as a copied quick-pick ranking.
- For every retained candidate, state the intended agent workload, provider-documented capability basis, and the limitation or missing AI Lab evidence that prevents the provider claim from becoming an automatic recommendation.
- Distinguish hosted tool availability, model capability, and application-level agent controls; recheck mutable tool surfaces, aliases, limits, prices, and access at decision time.
- Do not promote small/open/cheap models to primary long-running agent roles without complete-loop evidence.
- Compact models may remain bounded worker/router/preprocessor candidates when their assigned role is narrower than primary orchestration and their evidence supports that scope.
- For orchestrator models, evaluate goal-to-deliverable translation, task decomposition, dependency/conflict recognition, worker/model/tool assignment, concise state retention, evidence-based worker monitoring, targeted correction, failure classification, stopping, and escalation decisions.
- Treat strong worker performance as insufficient evidence of orchestrator suitability.
- Evaluate orchestrator-specific failure modes including dependency mistakes, false or unsafe parallelism recommendations, bad worker/tool assignment, missed constraints, unnecessary expensive escalation, repeated correction loops, and premature completion.
- Require orchestrator completion claims to pass observable acceptance/verification evidence rather than worker or manager self-report alone.
- Require explicit quality target, retry/review bounds, terminal stopping conditions, and escalation conditions for orchestrator evaluation.
- Link model-team topology/routing/escalation guidance from `../model-teams/` rather than duplicating portfolio design here.
- Keep workflow-engine design, orchestration software selection, branch/workspace mechanics, service/resource lifecycle, GPU residency, provider startup/teardown, billing reconciliation, and infrastructure fault recovery outside model-selection ownership.
- Allow operational conditions to be recorded only as frozen evidence context when they materially affect the evaluated model behavior.
- Link canonical model facts from `../../../reference/`.

## Validation

- The page contains no dated quick-pick ranking copied from legacy guidance.
- Useful legacy candidate hypotheses are not discarded merely because they were embedded in legacy model-reference or mixed comparison pages.
- Agentic marketing claims are not treated as reliability evidence.
- Every candidate is an evaluation starting point with explicit scope and evidence boundary, not an unsupported current winner.
- Worker quality is not treated as proof of manager/orchestrator quality.
- Application-level controls remain separate from model capability claims.
- Operational orchestration architecture is not migrated into the model-selection subtree.
