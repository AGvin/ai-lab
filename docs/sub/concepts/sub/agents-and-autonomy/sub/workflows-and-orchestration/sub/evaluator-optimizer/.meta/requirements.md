# Documentation Requirements

## Requirements

- Use the reader-facing title `Evaluator-Optimizer`.
- Define the pattern as a bounded workflow loop in which an optimizer/generator produces or revises a candidate, an evaluator assesses that candidate against declared criteria/evidence, feedback is returned to the optimizer, and the workflow either accepts, revises again, escalates, or terminates under explicit stop rules.
- Keep the workflow architecture distinct from the identity of any concrete evaluator model, judge prompt, benchmark, rubric, or scoring service. Those remain with their applicable evaluation/catalog/evidence owners.
- Distinguish evaluator-optimizer from generic `verification-and-reflection/`. Verification/reflection owns reusable checking/reconsideration semantics; evaluator-optimizer owns the explicit two-role/phase iterative control loop that uses evaluation feedback to drive another candidate revision.
- Distinguish evaluator-optimizer from `evaluation-and-measurement/methods/llm-as-a-judge/`. An LLM judge can be one evaluator implementation, while the workflow can also use deterministic validators, tests, humans, specialized models, or combinations; judge methodology and measured judge performance remain evaluation-owned.
- Distinguish evaluator-optimizer from ordinary retries. A retry repeats or reattempts work after failure; an evaluator-optimizer iteration should carry actionable evaluation evidence/feedback that materially informs the next revision.
- Distinguish evaluator-optimizer from manager-worker orchestration. A manager can delegate many heterogeneous subtasks and integrate results; evaluator-optimizer centers on a recurrent candidate-evaluation-feedback relation even when separate agents implement the roles.
- Distinguish evaluator-optimizer from advisory councils/review boards. Multi-reviewer deliberation or voting can feed an evaluator stage, but the canonical loop does not require multiple evaluators or governance authority.
- Define the candidate contract where material: stable candidate/artifact identity/version, task/requirements, expected output schema, source/evidence references, optimizer identity/configuration, and known constraints/uncertainty.
- Define the evaluation contract where material: criteria/rubric, evaluator identity/version, evidence available, allowed tools, output schema, severity/priority, decision classes, confidence/uncertainty, requested correction, and unsupported/insufficient-evidence outcomes.
- Keep evaluation feedback structured enough to drive a targeted revision. Prefer issue identifiers, criterion references, evidence, severity, requested correction, and residual uncertainty over vague `make it better` feedback.
- Preserve candidate and evaluation versions across iterations so the workflow can tell which findings apply to which artifact and whether a change resolved, preserved, superseded, or regressed a prior issue.
- Require explicit acceptance semantics. A passing evaluator decision is evidence under the evaluator's tested limitations, not proof of correctness, safety, factual truth, legal compliance, or user acceptance unless independent controls establish those properties.
- Require deterministic validators outside model judgment where the acceptance property is exactly machine-checkable, such as schema, syntax, compilation, tests, calculations, identifiers, permissions, or other critical invariants.
- Bound the loop with maximum iterations, elapsed time/cost, repeated-state or repeated-finding detection, minimum improvement/change expectations where useful, escalation/fallback, and terminal failure/accepted-limitation states.
- Detect oscillation and non-improvement. Repeating the same two candidate states, receiving materially identical findings, or changing style without resolving blocking criteria should trigger escalation or termination rather than unlimited iterations.
- Treat optimizer and evaluator independence as an empirical property, not a naming convention. Different prompts/roles on the same model can share blind spots; when independence matters, record model/provider/evidence/prompt/tool overlap and calibrate against human/deterministic ground truth.
- Treat evaluated content as potentially adversarial/untrusted. Separate evaluator instructions from candidate/source content, restrict evaluator tools and side effects, and prevent embedded instructions from changing criteria, leaking secrets, or granting authority.
- Keep the optimizer from silently changing requirements/acceptance criteria to make evaluation easier. Criteria changes require the declared decision owner or policy path rather than model convenience.
- Preserve disagreement and insufficient evidence. An evaluator may abstain, return `unknown`, or request additional evidence rather than force pass/fail when the criterion cannot be established.
- Explain multi-evaluator composition as optional. Independent reviewers, ensemble judges, deterministic checks, or human review can contribute to an evaluation stage, but aggregation rules and authority must remain explicit and should not hide minority blocking findings.
- Keep side effects outside the candidate-revision loop unless explicitly controlled. Optimizers should normally revise artifacts/plans before irreversible external actions; consequential execution should follow separate authorization/approval policy.
- Evaluate the full loop, including first-pass quality, issues found/missed, revisions per accepted result, non-improving cycles, false passes/rejections, human overrides, latency, cost, and final externally adjudicated quality.
- Keep concrete candidate artifacts, evaluator prompts/models, rubric versions, scores, traces, benchmark results, thresholds, project acceptance criteria, and run-level feedback with their applicable evidence/evaluation/project owners.
- Use the canonical entity references as research inputs for the reusable generate-evaluate-improve loop while keeping evaluator implementations and measured results outside concept ownership.

## Validation

- The concept is an explicit candidate-evaluation-feedback-revision loop, not a synonym for retries, generic self-reflection, LLM-as-a-judge, or multi-agent review boards.
- Evaluation feedback is versioned/traceable enough to connect findings to revisions.
- Evaluator pass is not treated as proof beyond the evaluator's validated scope.
- Loops have bounded stop/escalation/non-improvement behavior.
- Exact machine-checkable properties use deterministic validation where appropriate rather than model judgment alone.
- Concrete rubrics, judges, candidates, scores, thresholds, traces, and run results remain outside the reusable concept owner.
