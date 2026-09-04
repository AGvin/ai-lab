# Documentation Requirements

## Requirements

- Teach tool design as creating bounded interfaces that models/agents can select and parameterize reliably while deterministic host code can validate, authorize, execute, and test independently.
- Prefer clear capability-specific names and descriptions that explain what the tool does, when to use it, important exclusions, and the meaning of its result without relying on hidden prompt conventions.
- Avoid unnecessarily overlapping tools whose descriptions differ only subtly. If two operations have materially different permissions, effects, failure modes, or acceptance rules, expose those differences explicitly rather than making the model infer them from vague names.
- Prefer the narrowest meaningful capability boundary over generic execution surfaces. A tool should make authorization/business-rule checks tractable and should not expose shell/SQL/filesystem/network or other broad privileged power when a bounded operation can satisfy the need.
- Design argument schemas around semantic domain inputs rather than implementation accidents where possible. Use typed fields, required/optional distinctions, enums and explicit ranges/constraints when they reduce ambiguity and improve deterministic validation.
- Keep argument descriptions concise enough for model context while preserving the distinctions required for correct selection and safe execution. Excessively large/duplicated schemas can increase context cost and selection confusion.
- Treat schema as an interface aid, not a security boundary. Validate identifiers, ownership/tenant/environment, current authoritative state, cross-field rules, business invariants, permissions, and side-effect policy in host code even when generation is schema-constrained.
- Avoid model-generated powerful free-form execution payloads unless a separate sandboxed/validated boundary is genuinely the intended capability. Prefer semantic parameters that the host translates into bounded implementation behavior.
- Declare idempotency/retry expectations, side-effect class, expected latency/resource envelope, and result/error contract when those properties affect how an agent can safely use the tool; link deeper behavior to the selected sibling/operations owners.
- Design result contracts so callers can identify stable outcome categories and authoritative identifiers/artifacts without requiring the model to parse incidental human-readable logs.
- Include enough provenance/version identity to diagnose behavior when tool implementation/schema/configuration changes can affect replay or continuation.
- Test tools both independently and under model/agent use: schema validation, semantic validation, permission failures, boundary values, ambiguous selections, hostile/untrusted arguments, error/result shapes, repeated invocation, and model selection across overlapping alternatives.
- Evaluate selection confusion, argument correction/validation failures, context/schema size, privilege exposed per task, invalid/unauthorized attempts, result usability, portability burden, and accepted task quality/cost.
- Keep concrete provider schema syntax, MCP/tool discovery protocols, generated SDKs, and product-specific capability catalogs with their applicable catalog/specification/evidence owners.

## Validation

- Tool interfaces are bounded around meaningful capabilities and do not expose generic privileged execution without explicit need.
- Schema conformance never replaces semantic validation or authorization.
- Names/descriptions/schemas reduce ambiguity without unnecessary context bloat.
- Result, side-effect, retry/idempotency, and permission expectations are explicit where they affect safe use.
- Provider-specific protocol syntax remains source-backed rather than universalized.
