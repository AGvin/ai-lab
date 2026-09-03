# Documentation Requirements

## Requirements

- Teach function calling as the narrower structured tool-interface pattern in which a model selects a declared named function-like capability and emits structured arguments for host-side validation/execution.
- Make clear that an exposed `function` is an interface abstraction, not necessarily a one-to-one programming-language function. It may represent an API call, workflow operation, search, database operation, job, code-execution request, device action, or other bounded host capability.
- Use examples such as extracting typed arguments from natural-language requests, routing into bounded application operations, connecting conversational interfaces to business capabilities, producing structured records for workflow steps, and selecting among a small approved action set.
- Keep operation names/descriptions clear enough that the model can distinguish capabilities, but route reusable naming/schema/granularity rules to `tool-design/` rather than treating function calling as the owner of all tool-interface design.
- Prefer typed fields, enums, required/optional distinctions, and explicit constraints when they improve validation and reduce ambiguity. Schema conformance is only syntactic/structural evidence; it does not prove semantic correctness, current-state validity, authorization, or safety.
- Avoid exposing unnecessarily generic privileged operations. A function-like capability should be narrow enough that business rules and permission checks can be enforced meaningfully by the host.
- Do not pass model-generated file paths, SQL, shell commands, templates, code, or other powerful free-form material directly into privileged implementations unless a separate validated/sandboxed execution boundary explicitly permits and constrains it.
- Treat all arguments as untrusted input even under strict schema generation. Validate identifiers, ownership/tenant/environment, ranges, cross-field rules, current authoritative state, authorization, and domain-specific invariants at execution time.
- Return compact structured results under a declared contract and link detailed success/failure/partial/ambiguous-result handling to `tool-results-and-errors/`.
- Keep side-effect authorization, approvals, idempotency/reconciliation, and least privilege with `side-effects-and-permissions/` and applicable Operations/Engineering owners rather than assuming a function schema makes execution safe.
- Distinguish function calling from structured output: a function call includes intended host invocation semantics; structured output alone may simply produce data without execution.
- Distinguish function calling from broader tool calling: not every tool protocol or capability is best modeled as a named function-like operation, and exact provider tool/function protocols vary.
- Validate recipes against the actual provider/runtime. Schema strictness, supported types/constraints, call/result message formats, parallel-call behavior, streaming, and error semantics are mutable interface facts rather than universal function-calling properties.
- Compare model-produced function calls against deterministic parsing/routing or direct application invocation. Use model interpretation only where natural-language variability/ambiguity materially benefits the interface.
- Evaluate argument validity/correction, wrong-function selection, invalid/unauthorized execution attempts, semantic business-rule failures, result interpretation, provider/interface portability failures, latency/cost, and accepted workflow outcome.

## Validation

- Function calling remains a narrower practical interface pattern inside broader tool use.
- An exposed function need not map directly to a programming-language function.
- Schema-valid arguments are never presented as authorized, semantically correct, or safe by themselves.
- Privileged free-form execution inputs require a separate validated/sandboxed boundary.
- Provider/runtime function-calling syntax and strictness remain mutable source-backed facts.
