# Documentation Requirements

## Requirements

- Teach the practical distinction between agent-style control and deterministic/staged workflows without redefining the canonical agent identity owned by `concepts/agents-and-autonomy/`.
- Use agent-style control when later actions genuinely depend on newly observed state, tool results, ambiguous interpretation, flexible planning/classification/synthesis, or other conditions that cannot be specified and validated economically through fixed application logic alone.
- Use examples such as repository maintenance with observation-driven next steps, evidence-gathering research, administration across several external systems, adaptive multi-stage data processing, and support/operations workflows whose next action depends on validated current state.
- Prefer deterministic application logic when the correct next step, validation, transformation, routing, authorization, or side effect can be expressed directly and predictably. Model involvement is not automatically beneficial merely because a workflow has several steps.
- Teach hybrid control explicitly: deterministic code can own schemas, validation, permissions, budgets, state transitions, stopping conditions, retries, approvals, and side-effect enforcement while models handle interpretation, classification, synthesis, planning, or other bounded ambiguous decisions.
- Distinguish an agent from a fixed multi-step pipeline. Repetition or tool use alone does not make a system agentic when the sequence/control policy remains fully predetermined by the application.
- Distinguish autonomy from broad authority. A model-directed loop can still have narrow tools, bounded credentials, explicit state, time/cost limits, approval gates, and deterministic stopping/recovery controls.
- Do not use an `agent` label to justify broad credentials, unrestricted data access, open-ended loops, implicit permission escalation, or model-owned authorization. Capability and authority remain separately controlled by the surrounding system.
- Require explicit stopping/terminal conditions and resource envelopes for open-ended/adaptive loops. A model continuing to find possible actions is not by itself evidence that more work is valuable or authorized.
- Require deterministic validation/authorization around consequential effects where the required property can be checked directly. Model confidence, reasoning, or refusal is not a substitute for enforceable system controls.
- Treat observed external/tool state as authoritative over the agent's expectation or conversational memory. Adaptation should follow verified observations rather than hallucinated completion or assumed state changes.
- Compare agent-style control against simpler alternatives such as one deterministic operation, a fixed pipeline, routing, or a bounded workflow. Choose the agent form only when adaptive decision value justifies additional state, latency, cost, observability, permission, and recovery complexity.
- Evaluate accepted-result quality, number/value of adaptive decisions, unnecessary model decisions, invalid/unauthorized action attempts, loop/stopping failures, state-observation mismatches, human interventions, latency/cost/resource use, and failure/recovery behavior against simpler baselines.
- Link deeper topics to Agent Planning, Tools and Actions, Context/State/Memory, Workflows and Orchestration, and Operations and Control rather than duplicating their implementation-specific contracts here.

## Validation

- Deterministic logic is preferred for directly expressible/validatable control decisions and effects.
- Agent-style control is justified by useful adaptation to observations/ambiguity rather than by multi-step structure alone.
- Model capability, autonomy, permissions, credentials, and authorization remain distinct concepts.
- Open-ended loops have bounded stopping/resource controls and authoritative state validation.
- The learning page compares against simpler deterministic/workflow baselines before recommending agent-style control.
