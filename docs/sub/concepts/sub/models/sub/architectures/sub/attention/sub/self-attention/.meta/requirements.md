# Documentation Requirements

## Requirements

- Use the reader-facing title `Self-Attention`.
- Define self-attention as attention in which the querying representations and the source representations being attended over are derived from the same input sequence, set, or representation collection, allowing elements to condition their updated representations on other permitted elements of that same collection.
- Explain that queries, keys, and values can be different learned projections even though they originate from the same underlying representation collection; `self` describes the source relationship, not identical Q/K/V vectors.
- Distinguish self-attention from cross-attention, where queries and attended source representations originate from different sequences, modalities, or representation sets.
- Explain causal masking as one self-attention pattern that prevents access to disallowed future positions, while bidirectional/full, local, sliding-window, sparse, blockwise, or other masks/connectivity patterns permit different interaction sets.
- Do not imply that every position attends to every other position, to itself, or to the entire advertised context; masking, architecture, context construction, and sparse/local patterns can restrict direct interactions.
- Treat multi-head self-attention as a common Transformer design rather than a universal requirement of self-attention.
- Qualify complexity statements: standard full self-attention has pairwise sequence interactions and quadratic scaling in sequence length for the attention matrix, while alternative attention structures can alter this cost.
- Keep positional representation conceptually separate: self-attention can use position information supplied by the surrounding architecture, but position encoding is not itself the self-attention mechanism.
- Inherit the parent attention boundary that attention weights are internal computation and are not automatically faithful explanations, causal attributions, or proof that information was used correctly.
- Keep concrete masking layouts, context-window limits, KV-cache/runtime behavior, attention kernels, model-specific variants, and performance claims with their applicable architecture, inference, catalog, or evidence owners.
- Use the canonical entity references as research inputs for definition and masking/connectivity distinctions when reader-facing rendering is activated.

## Validation

- The page distinguishes same-source self-attention from cross-attention.
- `Self` is not described as requiring identical query, key, and value projections.
- The page does not assume every self-attention layer is bidirectional, causal, full-context, or multi-head.
- Quadratic complexity is scoped to standard full self-attention rather than all variants.
- Self-attention is not conflated with positional encoding, persistent memory, or context-window guarantees.
- Legacy application examples and runtime/model-selection conclusions are not duplicated into this canonical child concept.
