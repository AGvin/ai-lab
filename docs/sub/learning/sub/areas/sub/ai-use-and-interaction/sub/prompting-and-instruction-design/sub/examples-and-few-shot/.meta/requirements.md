# Documentation Requirements

## Requirements

- Teach Examples and Few-Shot as designing demonstrations that communicate task behavior and boundaries without changing model weights.
- Choose examples that are representative of the real task rather than only easy or ideal cases; include relevant edge, invalid, or failure cases when they materially affect acceptance.
- Use positive and negative examples when the contrast communicates an important boundary, and keep labels/formatting internally consistent.
- Treat example similarity, diversity, ordering, count, and label balance as task-specific variables to evaluate rather than universal rules.
- Inspect demonstrations for accidental instruction-like content, contradictions, leakage, or sensitive/confidential information before use.
- Prefer synthetic or appropriately sanitized examples when they satisfy the teaching objective and reduce data-handling risk.
- Compare few-shot behavior against simpler zero-shot or one-shot baselines when useful, and evaluate representative held-out cases, context consumption, and cost/quality trade-offs.
- Re-run relevant checks after material model, provider, prompt, context, or example-set changes.

## Validation

- Adding examples is not presented as automatically improving performance.
- Demonstrations are evaluated on held-out representative cases.
- Sensitive example data is not assumed safe merely because it is embedded in a prompt.
