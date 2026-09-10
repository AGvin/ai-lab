# Documentation Requirements

## Requirements

- Teach constrained generation as restricting the valid continuation/output space during decoding according to a machine-checkable constraint such as allowed values, grammar, schema, structured syntax, or other runtime-supported rule; use the canonical Constrained Generation concept for stable identity and implementation boundaries.
- Use application examples such as typed API payloads, grammar-defined languages, enumerated classifications, parseable configuration, or tool arguments that will still undergo application validation before use.
- Keep the constraint no more complex than required by the task and the exact runtime's supported feature set. A formal schema/grammar being expressible in theory does not prove one runtime/provider implements every feature or tokenizer interaction correctly.
- Account for tokenizer/runtime compatibility when character/byte/grammar/schema/permitted-value constraints must map to valid token continuations. Avoid assuming a text-level rule translates trivially to token-level decoding.
- Prefer explicit bounded forms for consequential identifiers, commands, paths, operations, or enumerations where feasible instead of generating unrestricted strings that are later executed or interpreted with broad authority.
- Avoid unnecessary ambiguity or deeply nested alternatives when they create avoidable dead ends or make reliable population of the allowed structure harder; evaluate the concrete grammar/schema behavior rather than assuming more constraint complexity is safer.
- Apply semantic/domain validation after constrained decoding. A structurally valid date, path, identifier, query, configuration, tool argument, or API payload can still be invalid, unsafe, unauthorized, stale, or inappropriate for the intended action.
- Keep authorization, business invariants, policy checks, trust boundaries, and consequential side-effect controls outside the probabilistic decoding mechanism. Passing syntax/grammar validation never expands authority.
- Define explicit failure/fallback behavior for dead ends, unsupported constraints, runtime inability to satisfy the rule, timeout/exhaustion, or an allowed output that fails application validation. Do not silently execute merely because syntax passed.
- Distinguish constrained generation from prompting for a format and from post-hoc parsing. Constraints can restrict generation-time continuations, but the exact guarantee is limited to the runtime's supported subset and does not imply factual/semantic correctness.
- Keep provider/runtime-specific grammar/schema feature support, tokenizer quirks, APIs, implementation limits, benchmark results, and tool/action policies with catalog/evidence/project owners.

## Validation

- Constrained generation is distinguished from prompting-only formatting and post-hoc parsing.
- Text/schema constraints account for tokenizer/runtime implementation boundaries where material.
- Structural validity is never equated with semantic validity, safety, authorization, or correctness.
- Failure/dead-end and application-validation fallback behavior is explicit.
- Mutable provider/runtime support remains evidence/catalog-owned.
