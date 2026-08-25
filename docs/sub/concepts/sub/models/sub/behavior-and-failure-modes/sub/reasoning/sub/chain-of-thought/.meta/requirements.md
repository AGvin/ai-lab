# Documentation Requirements

## Requirements

- Use the reader-facing title `Chain of Thought (CoT)`.
- Define chain of thought as an explicit sequence of intermediate reasoning-like steps represented in model context or generated during problem solving before or alongside a final answer; treat it as a reasoning representation/behavior, not as proof of the model's complete internal causal process.
- Distinguish a CoT trace from `chain-of-thought prompting`, which is a prompting technique that supplies or requests intermediate-step demonstrations/instructions to elicit such traces.
- Explain that a visible CoT can influence later generation and can improve performance on some multi-step tasks, but the effect is model-, scale-, task-, prompt-, and evaluation-dependent rather than universal.
- Make clear that fluent intermediate reasoning can be incorrect, post-hoc, incomplete, selectively reported, or unfaithful to factors that actually influenced the answer. A detailed rationale is therefore evidence to evaluate, not automatic transparency into internal computation.
- Distinguish visible/generated CoT from hidden or private model computation. When a system does not expose internal reasoning, do not infer that an external explanation is a verbatim transcript of hidden states or require disclosure of hidden reasoning as a correctness/audit mechanism.
- Distinguish CoT from externally verifiable workflow artifacts such as structured plans, tool calls/results, code execution, retrieved evidence, calculations, or state transitions. Those artifacts can support auditing even when internal reasoning remains inaccessible.
- Explain that intermediate steps can propagate assumptions and errors as well as correct them; verification of the final result and material intermediate claims remains separate from producing more reasoning text.
- Keep concrete provider policies on hidden reasoning, reasoning-token accounting, model-specific reasoning modes, benchmark gains, prompting recipes, and agent/workflow traces with their applicable catalog, evaluation, learning, or system owners.
- Keep the unselected `reasoning-models/` classification separate; CoT usage or visibility does not by itself define a model as a canonical `reasoning model` class.
- Use the canonical entity references as research inputs for CoT elicitation, performance, and faithfulness boundaries when reader-facing rendering is activated.

## Validation

- The page does not equate visible CoT with a faithful transcript of the model's internal causal reasoning.
- Chain-of-thought as a trace is distinguished from chain-of-thought prompting as an elicitation technique.
- CoT is not presented as universally improving accuracy or as proof of correctness, interpretability, or safety.
- Hidden/private reasoning is not treated as something that must be disclosed for auditing; externally verifiable evidence and workflow artifacts remain separate.
- CoT does not implicitly create or define the blocked `reasoning-models` classification leaf.
- Legacy practical guidance is preserved only as conceptual verification boundaries rather than a universal instruction to expose or lengthen reasoning traces.
