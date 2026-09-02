# Structured Output

Legacy residual retained for application integration, schema-design, validation, retry, and consequential-action guidance that are intentionally outside the canonical Structured Output concept owner.

> **Migration note:** Structured-output identity, result-contract versus generation-mechanism separation, schema/parse/type/semantic/factual/authorization/safety validation layers, structured-output versus constrained-generation distinction, and tool-output versus actual execution boundaries are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/generation-controls/sub/structured-output/`. The remaining material below stays here until its exact learning, application-engineering, trustworthy-AI, or provider-specific owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application-integration residual

Structured outputs are commonly useful for entity extraction, classifications, workflow parameters, API inputs, required fields or enumerated values, and separating machine-readable results from reader-facing explanation.

Treat generated structured data as proposed application input. Validate it before using it in a consequential operation, and perform authorization or permission checks independently from schema compliance.

## Schema-design and provider residual

Useful implementation practices include:

- prefer a provider/runtime's native supported structured-output or schema-constrained mechanism when its guarantees fit the task, while verifying the exact supported schema subset;
- keep schemas no more complex than the task requires and avoid deeply ambiguous alternatives when they reduce generation reliability;
- define required and optional fields intentionally rather than treating arbitrary omission as acceptable;
- avoid depending on fragile parsing of unrestricted prose when a supported machine-readable contract is required.

These choices are implementation-specific rather than universal Structured Output semantics.

## Validation and recovery residual

After structural validation, apply domain validation appropriate to the application, such as allowed identifiers, date ranges, state transitions, path restrictions, or other business constraints.

When output is invalid, use a bounded repair, retry, or failure policy rather than silently accepting malformed or semantically invalid data. If a generated object will cause an external action, validate and authorize the action before execution even when the object is syntactically and structurally valid.

These integration, validation, and recovery practices remain migration source material until their exact learning, application-engineering, trustworthy-AI, or provider-specific owners are verified.
