# Tool Calling

Legacy residual retained for practical tool-interface design and application guidance that is intentionally outside the canonical Tool Use concept owner.

> **Migration note:** Tool-use identity, tool request versus validated execution, host-owned authorization/validation/side effects/error handling, tool-result versus success semantics, schema/interface variability, and the narrower function-calling boundary are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/tool-use/`. The remaining material below stays here until its exact learning, tool-design, execution-security, reliability, or project owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Tool interfaces can connect model-directed workflows to capabilities such as:

- search and retrieval;
- databases and internal services;
- calendars, email, and source control;
- code execution or file operations; and
- bounded business/application operations.

These are application examples rather than part of the universal tool-use definition.

## Tool-design residual

Prefer bounded capabilities with clear names, descriptions, argument contracts, permission scope, and result semantics over unnecessarily generic execution surfaces. Overlapping or ambiguous tools can reduce selection reliability, while very large tool descriptions/schemas can consume context and make routing harder.

Treat model-produced arguments as untrusted even when they satisfy a schema. Validate semantic constraints and authorization at execution time, and return compact structured results that distinguish successful completion, failure, partial completion, or ambiguous external state where the workflow needs those distinctions.

Network failures, timeouts, and side effects require explicit retry/idempotency/reconciliation handling. A proposed or accepted tool call is not evidence that the external operation completed.

These tool-interface and execution practices remain migration source material until their exact learning, engineering, security, reliability, or project owners are verified.
