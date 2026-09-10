# Documentation Requirements

## Requirements

- Teach Structured Outputs as using an explicit machine-readable result contract when downstream consumers depend on fields, types, enumerated values, classifications, extraction results, workflow parameters, or API inputs.
- Prefer a provider/runtime's native supported structured-output or schema-constrained mechanism when its guarantees fit the task, while verifying the exact current supported schema subset.
- Keep schemas only as complex as the task requires; define required and optional fields intentionally and avoid fragile parsing of unrestricted prose when a reliable machine-readable contract is required.
- Treat generated structured data as proposed application input. Apply structural validation first, then domain/semantic validation such as allowed identifiers, ranges, state transitions, paths, or other business constraints.
- Keep authorization and consequential-action permission checks independent from schema compliance; a valid object does not authorize its execution.
- Use bounded repair, retry, or failure handling for malformed or semantically invalid output rather than silently accepting it.
- Keep provider-specific guarantees and schema subsets current and source-backed rather than presenting them as universal Structured Output semantics.

## Validation

- Syntactic/schema validity is not treated as semantic correctness or authorization.
- Consequential actions are validated and authorized independently before execution.
- Recovery behavior is bounded and explicit rather than unlimited silent retries.
