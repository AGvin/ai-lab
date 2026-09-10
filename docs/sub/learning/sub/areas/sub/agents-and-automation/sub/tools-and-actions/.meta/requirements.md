# Documentation Requirements

## Requirements

- Present Tools and Actions as the Agents and Automation learning group for how models/agents discover/select/invoke external capabilities, design tool interfaces, interpret results/errors, and control consequential side effects/permissions.
- Use canonical `concepts/agents-and-autonomy/tool-use/` for reusable tool-use and function-calling semantics. This group teaches practical interface/execution design and agent-operation consequences rather than creating duplicate canonical concepts.
- Keep `function-calling/`, `tool-calling/`, `tool-design/`, `tool-results-and-errors/`, and `side-effects-and-permissions/` distinct selected learning topics because structured invocation, broader tool selection, interface design, result/error contracts, and consequential action control have different learning outcomes.
- Explain that the current materialized subset covers all five selected children because the legacy Tool Calling and Function Calling residuals contain source-backed material across those exact boundaries.
- Treat model-produced tool names/arguments as requests, not authoritative execution. Host/application layers own eligibility, validation, authentication/authorization, side-effect policy, execution, reconciliation, and trustworthy result construction.
- Keep MCP/protocol mechanics with Integration and Extensibility/Specifications, concrete tools/products with Catalog, generic idempotency/retries/recovery with Operations/Engineering, and project-specific execution policies with Project owners.
- Keep provider-specific tool/function message formats, schema strictness, streaming/protocol behavior, and API syntax source-backed rather than universalizing one interface.

## Validation

- Tool selection/request is distinguished from validated execution and successful external effects.
- Function calling remains a narrower structured interface pattern inside broader tool use.
- Interface design, results/errors, and side-effect permissions remain separate practical learning concerns.
- Current navigation exposes only materialized selected children backed by actual migration content.
- Concrete protocols/products and mutable provider APIs remain with their applicable owners.
