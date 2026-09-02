# Evaluator-Optimizer Architecture

Legacy residual retained for practical pattern-selection guidance that is intentionally outside the canonical Evaluator-Optimizer concept owner.

> **Migration note:** Evaluator-optimizer identity, candidate/evaluation contracts, actionable structured feedback, revision traceability, deterministic validation, bounded correction loops, independence/correlation caveats, oscillation/non-improvement detection, escalation, side-effect boundaries, and full-loop evaluation are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/sub/evaluator-optimizer/`. The exact Anthropic `Building effective agents` source cited by the legacy page is also preserved in canonical entity metadata. The remaining material below stays here until its exact learning or workflow-decision owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Pattern-selection residual

Evaluator-optimizer can be a useful fit when an artifact can materially improve through targeted feedback and the acceptance criteria are specific enough to produce actionable findings. Example workflows include:

- translation refinement with terminology or protected-token checks;
- code changes followed by deterministic tests and independent review;
- document/media generation with measurable compliance criteria;
- extraction or classification with machine-checkable validation; and
- design or architecture proposals where risk/feasibility review can drive a concrete revision.

Prefer a simpler transformation or one-pass workflow when deterministic logic already solves the task, criteria are too vague to direct revision, additional revisions cannot materially improve the artifact, review latency/cost has little value, or the artifact becomes irreversible before evaluation can influence it.

Do not add an evaluator loop merely to create a second model opinion. The pattern is justified when evaluation evidence can change the next candidate in a bounded, inspectable way and final accepted-result quality improves enough to justify extra calls, state, latency, and review complexity.

These pattern-selection fragments remain migration source material until their exact learning or workflow-decision owner is verified.
