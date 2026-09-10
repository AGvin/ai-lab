# Documentation Requirements

## Requirements

- Teach evaluator-optimizer as a bounded generate/evaluate/revise workflow used only when evaluation evidence can materially improve the next candidate under explicit acceptance criteria.
- Start from an inspectable candidate contract, evaluation criteria, evaluator output schema, revision contract, iteration bound, and terminal acceptance/escalation rule instead of relying on an open-ended conversation between models.
- Require evaluator feedback to be actionable and attributable: identify the failed criterion, supporting evidence, severity/impact, and concrete revision target rather than returning only a score or vague preference.
- Preserve candidate/revision identity and evaluation trace so each change can be tied to the feedback that caused it and regressions/oscillation can be detected.
- Use deterministic validation before or alongside model evaluation whenever the criterion is machine-checkable, such as tests, schemas, protected-token checks, format validation, constraints, or policy rules.
- Teach bounded correction loops. Stop on acceptance, explicit iteration/cost/time limits, repeated non-improvement, oscillation, contradictory feedback, or a failure class requiring escalation/human review rather than continuing indefinitely.
- Explain evaluator independence carefully: a separate model/context/prompt/evidence path can reduce some shared failure modes but does not guarantee independence or correctness. Correlated blind spots and shared source errors remain possible.
- Keep irreversible or consequential side effects outside the revision loop until the candidate passes required validation/approval. An evaluator cannot safely improve an artifact after an irreversible effect has already occurred.
- Teach pattern fit with examples where targeted feedback can produce a concrete next revision: translation refinement with terminology/protected-token checks; code changes with tests and review; document/media generation with measurable compliance criteria; extraction/classification with machine-checkable validation; and design/architecture proposals where risk/feasibility findings can drive a specific revision.
- Prefer a simpler transformation or one-pass workflow when deterministic logic already solves the task, criteria are too vague to guide revision, extra revisions cannot materially improve the artifact, evaluation latency/cost has little value, or the artifact becomes irreversible before evaluation can influence it.
- Do not add an evaluator merely to obtain a second model opinion. The loop is justified only when evaluation evidence changes the next candidate in an inspectable way and accepted-result quality improves enough to justify extra calls, state, latency, and operational complexity.
- Evaluate the full loop rather than only evaluator agreement: acceptance rate, improvement per iteration, regressions/oscillation, deterministic-check failures, iteration count, escalation/manual-review rate, latency/cost/resource use, evidence quality, and cost per accepted result.
- Use the exact Anthropic reference in entity metadata as pattern evidence and the canonical Evaluator-Optimizer concept for stable semantics. Mutable framework APIs and concrete judge/model choices remain source-backed/evidence-owned.

## Validation

- Every revision can be traced to explicit evaluation evidence or a deterministic validation failure.
- The loop has bounded stop conditions and does not continue on non-improvement indefinitely.
- Machine-checkable criteria are not delegated to subjective model judgment without reason.
- Consequential side effects occur only after required acceptance/approval boundaries.
- A second model opinion alone is never treated as sufficient justification for the pattern.
- Pattern-selection guidance distinguishes evaluator-optimizer from one-pass transformation, human review, and generic verification.
