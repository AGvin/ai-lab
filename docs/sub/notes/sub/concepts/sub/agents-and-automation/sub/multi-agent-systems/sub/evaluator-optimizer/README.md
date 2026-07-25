# Evaluator-Optimizer Architecture

An evaluator-optimizer architecture alternates between a generator or optimizer that creates or revises an artifact and an evaluator that checks it against explicit criteria.

## Translations

- English

## Status

Established agent workflow pattern.

## Core idea

The optimizer produces a candidate. The evaluator returns a structured decision and actionable findings. The optimizer revises only the accepted findings, and the loop stops when the artifact passes, a bounded budget is exhausted, progress stalls, or escalation is required.

```text
requirements -> optimizer -> candidate -> deterministic checks -> evaluator
                                      ^                         |
                                      |---- bounded feedback ---|
```

The evaluator should not modify the artifact silently. Generation, judgment, decision, and revision should remain inspectable stages.

## Required contracts

### Optimizer input

- authoritative requirements and acceptance criteria;
- current artifact and revision identifier;
- accepted unresolved issues;
- evaluator findings with stable issue identifiers;
- allowed tools, files, permissions, and revision budget;
- quality tier and stop conditions.

### Optimizer output

- revised artifact;
- change summary linked to issue identifiers;
- evidence for deterministic checks;
- limitations and rejected findings;
- next-review request.

### Evaluator output

```text
Decision: accept | revise | reject | escalate | insufficient-evidence
Criteria checked:
Passed criteria:
Issues:
  - ID:
    Severity:
    Criterion:
    Evidence:
    Required correction:
Remaining uncertainty:
Recommended next action:
```

The evaluator should separate objective defects, uncertain claims, preference-level suggestions, and out-of-scope requests.

## Bounded correction loop

Define before execution:

- maximum revision rounds;
- maximum evaluator calls and total cost;
- terminal acceptance rule;
- severity levels that block acceptance;
- minimum measurable improvement per round;
- repeated-issue and cycle detection;
- escalation model, human approver, or accepted-limitation path.

Stop or escalate when:

- the same issue remains after the useful retry limit;
- two revisions alternate between earlier states;
- evaluation scores change without corresponding artifact improvement;
- the evaluator introduces new criteria outside the contract;
- the optimizer lacks the capability or permission to correct the defect;
- additional iteration has lower expected value than direct human editing.

Do not run until an evaluator emits a vague positive statement. Acceptance should be tied to explicit criteria and evidence.

## Independence and evaluator quality

The evaluator may be:

- deterministic tests or validators;
- a different prompt and role on the same model;
- a different model or provider;
- a specialist perception, security, legal, language, or domain model;
- a qualified human reviewer;
- a combination of these stages.

A second model call is not automatically independent. Evaluate common model family, shared context, correlated training, prompt leakage, self-preference, and shared blind spots.

Calibrate evaluator false acceptance and false rejection on representative human-adjudicated cases. A weak evaluator can reward superficial changes, miss regressions, or create endless churn.

## Revision comparison

Preserve every revision and compare:

- issue resolution status;
- new regressions;
- changed files, regions, statements, tests, or metrics;
- criteria score movement;
- cost and latency;
- reviewer disagreement;
- distance from the last accepted or best-known artifact.

Do not discard a stronger earlier revision merely because the latest round is newer.

## Suitable uses

- translation refinement with terminology and protected-token checks;
- coding changes followed by tests and independent review;
- document or media generation with measurable compliance criteria;
- extraction or classification pipelines with deterministic validation;
- architecture proposals with risk and feasibility review;
- outputs where human feedback can be converted into actionable revision criteria.

## Poor fits

Avoid or simplify this pattern when:

- one deterministic transformation can solve the task;
- evaluation criteria are too vague to produce actionable feedback;
- revisions cannot materially improve the artifact;
- the evaluator and optimizer share the same unsupported assumption;
- the task is latency-critical and review has no safety or quality value;
- the artifact is irreversible before approval.

## Strengths

- separates creation from judgment;
- supports measurable iterative improvement;
- makes acceptance criteria explicit;
- permits specialist or human evaluation;
- provides a natural escalation boundary;
- preserves revision and evidence history.

## Limitations

- multiplies model and review cost;
- can oscillate or optimize for the evaluator rather than the real requirement;
- may amplify evaluator bias or false confidence;
- requires durable artifact and issue tracking;
- can stall when feedback is vague, contradictory, or impossible;
- correlated generator and evaluator errors can survive every round.

## Evaluation metrics

Record:

- first-pass and terminal acceptance;
- issues found, resolved, reopened, and introduced;
- revisions per accepted artifact;
- repeated-issue and cycle rate;
- evaluator false acceptance and false rejection;
- regressions per revision;
- accepted-result quality gain over one-pass generation;
- latency, model cost, human correction time, and cost per accepted result;
- escalation and accepted-limitation rate.

## Evidence and established usage

Anthropic documents evaluator-optimizer as a workflow in which one model generates a response and another evaluates and provides feedback in a loop, recommending it when clear criteria exist and iterative refinement provides measurable value.

Source:

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## Related concepts

- [Multi-Agent Systems](../..)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Human Approval Gates](../human-approval-gates/)
- [Verification and Reflection](../../../verification-and-reflection/)
- [Agent State](../../../agent-state/)
