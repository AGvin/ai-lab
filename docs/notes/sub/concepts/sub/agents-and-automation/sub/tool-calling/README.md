# Tool Calling

Tool calling allows a model to select a registered external operation and produce arguments for that operation.

## Core idea

The model does not execute the tool directly. It emits a structured request, the host application validates and executes it, and the result is returned to the model or workflow. This separation is essential because model output is untrusted input to the execution layer.

## Typical flow

1. The application exposes tool names, descriptions, and argument schemas.
2. The model chooses a tool or responds without one.
3. The application validates permissions and arguments.
4. The tool runs in a controlled environment.
5. The result is added to state or context.
6. The model decides whether more work is required.

## Practical use

Tool calling connects models to search, databases, calendars, email, source control, code execution, and internal services. Tools should be narrow, clearly named, and designed around business capabilities rather than unrestricted shell access.

## Trade-offs and limitations

Tool descriptions consume context, and overlapping tools can confuse selection. Even valid arguments may be semantically wrong or unsafe. Network failures and partial side effects require explicit recovery logic.

## Common mistakes

- Executing model arguments without validation.
- Exposing powerful generic tools instead of bounded operations.
- Returning huge unfiltered tool results to the model.
- Assuming a tool call means the requested action succeeded.

## Related concepts

- [Agents and Automation](../../)
- [Function Calling](../function-calling/)
- [Least Privilege](../../../safety-privacy-and-reliability/sub/least-privilege/)
- [Structured Output](../../../model-usage-and-generation/sub/structured-output/)
