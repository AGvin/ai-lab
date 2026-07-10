# Function Calling

Function calling is a structured form of tool calling in which a model selects a named function and supplies arguments that match a declared schema.

## Core idea

The word “function” describes the interface exposed to the model; the underlying implementation may call an API, queue a job, query a database, or invoke local code. The host application remains responsible for authentication, authorization, validation, execution, and error handling.

## Practical use

- Extract typed arguments from natural-language requests.
- Route requests to application capabilities.
- Connect chat interfaces to business operations.
- Produce structured data for a workflow step.
- Let a model choose among a small set of approved actions.

## Design guidance

Use descriptive names and precise parameter descriptions. Prefer enumerations and typed fields over free-form strings. Keep functions narrow enough that permission checks are meaningful. Return compact, structured results that distinguish success, failure, and partial completion.

## Trade-offs and limitations

A valid function-call object does not mean the intent is safe or correct. Function schemas can become large, and many similar functions may reduce selection accuracy. Provider implementations differ in how strictly they enforce schemas.

## Common mistakes

- Treating the model as the authorization layer.
- Passing generated file paths, SQL, or commands directly to execution.
- Failing to report tool errors back to the workflow.
- Confusing a proposed function call with completed execution.

## Related concepts

- [Agents and Automation](../../)
- [Tool Calling](../tool-calling/)
- [Structured Output](../../../model-usage-and-generation/sub/structured-output/)
- [Guardrails](../../../safety-privacy-and-reliability/sub/guardrails/)
