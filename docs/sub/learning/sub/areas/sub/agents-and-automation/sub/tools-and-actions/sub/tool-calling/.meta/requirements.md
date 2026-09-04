# Documentation Requirements

## Requirements

- Teach tool calling as the broader practical pattern in which a model/agent selects and requests a declared external capability, while the host/runtime validates and executes that request under explicit interface and authority boundaries.
- Use examples such as search/retrieval, databases/internal services, calendars/email/source control, code or file operations, and bounded business/application actions without implying those concrete capabilities are part of the universal tool-calling definition.
- Treat model-selected tool names and arguments as untrusted requests. Tool availability and schema-conforming arguments do not prove the chosen tool is appropriate, authorized, semantically correct, safe, or executable in the current state.
- Require the host to filter eligible tools according to user/tenant/environment/data/policy/runtime state before or after model selection as appropriate; the model must not discover privilege merely by naming a tool.
- Teach tool selection quality separately from execution success. Common failures include wrong tool choice, omitted required call, invalid or unsafe arguments, stale assumptions, misinterpreted results, repeated calls, and selection among overlapping ambiguous capabilities.
- Use bounded, clearly differentiated tools where possible and link detailed naming/schema/granularity guidance to `tool-design/` rather than embedding every interface-design rule here.
- After a request is accepted for execution, rely on `tool-results-and-errors/` for result/error contracts and `side-effects-and-permissions/` for consequential action authorization/reconciliation rather than treating the call request as completion.
- Feed tool results back into agent state/context only after the host has constructed a trustworthy result record. A proposed or accepted tool call is not evidence that the external operation occurred.
- Distinguish tool calling from function calling: function calling is a narrower structured named-function-like interface pattern; broader tool calling can represent other declared tool/request protocols and abstractions.
- Distinguish tool calling from structured output: both can use schemas, but a tool call carries intended invocation semantics and still requires host-side execution/authorization.
- Compare tool calling with deterministic application calls. When the application already knows exactly which capability and arguments should be used, direct deterministic invocation can be simpler, safer, cheaper, and easier to test than model-based selection.
- Evaluate tool-selection accuracy/utility, unnecessary or omitted calls, invalid/unauthorized requests, argument correction rate, result interpretation failures, repeated/looping calls, latency/cost, and accepted task outcome versus simpler deterministic baselines.
- Keep concrete tool catalogs, provider message formats, MCP mechanics, credentials, sandbox/runtime behavior, and project-specific policies with their applicable owners.

## Validation

- A tool request is never equated with successful execution or external effect.
- Model tool selection cannot create authority outside the host's eligible tool/permission boundary.
- Tool calling is distinguished from narrower function calling and from structured output.
- Detailed interface/result/side-effect concerns are linked to their selected sibling learning owners.
- Deterministic direct invocation remains preferred when model selection adds no material value.
