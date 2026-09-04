# Documentation Requirements

## Requirements

- Teach self-attention as attention where queries, keys, and values are derived from the same source sequence/set of representations; use the canonical Self-Attention concept for the stable semantic boundary.
- Build intuition with examples such as resolving a pronoun against earlier context, connecting code references across a function/module, or relating distant document sections whose interaction matters for the current representation.
- Explain that causal self-attention restricts access to future positions while bidirectional self-attention can use both directions, and that local/sparse/block or other connectivity patterns can deliberately restrict interaction structure.
- Explain multi-head self-attention as learning multiple projections/interaction subspaces without claiming each head has one stable human-readable meaning.
- Teach that stacking self-attention with nonlinear transformations can build progressively transformed contextual representations, while the exact internal features remain learned and are not guaranteed to align with human concepts.
- Distinguish self-attention from cross-attention according to source sets rather than model task labels; decoder-only generation commonly uses causal self-attention, but architecture/task associations are not universal guarantees.
- Explain runtime scaling qualitatively: full dense self-attention can become expensive as sequence length grows, while locality/sparsity, optimized kernels, caching, architecture changes, and runtime implementation can change practical cost. Route detailed kernel/runtime optimization to inference learning.
- Do not treat self-attention weights as proof of explanation, causality, retrieval, persistent memory, factual grounding, or model confidence.

## Validation

- Same-source query/key/value semantics distinguish self-attention from cross-attention.
- Causal/bidirectional and dense/local/sparse connectivity distinctions are explicit.
- Examples are pedagogical illustrations, not task guarantees.
- Attention-head or weight interpretation is not overstated.
