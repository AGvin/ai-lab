# Documentation Requirements

## Requirements

- Use the reader-facing title `Tool Use`.
- Define tool use as an AI model or agent selecting, requesting, parameterizing, or otherwise invoking an external capability whose execution or authoritative result is provided by an environment, host application, service, device, or other system component.
- Distinguish a model/tool request from execution. The model can propose a tool/action and arguments, but the execution layer owns validation, authorization, side effects, error handling, result integrity, and any consequential-action policy.
- Explain `tool calling` as a common interface pattern in which the model emits a structured request for a declared tool. Preserve `function calling` as a narrower API/interface pattern where a named function-like capability and structured arguments are exposed to the model; do not create separate canonical children for either merge source.
- Make clear that an exposed `function` does not have to map one-to-one to a programming-language function. It may represent an API call, workflow operation, database query, job, search, code execution, device action, or another bounded host capability.
- Distinguish tool use from structured output. Tool arguments can be schema-constrained structured output, but tool use additionally carries intended invocation/execution semantics and still requires execution-layer validation and authorization.
- Distinguish tool availability from tool selection quality and task success. A model can choose the wrong tool, produce valid-but-wrong arguments, omit a needed call, misinterpret results, or request an unauthorized/unsafe action.
- Explain that tool results become model context/state only when the surrounding system returns or records them; a tool request alone is not evidence that the operation ran or succeeded.
- Treat tool names, descriptions, schemas, permission scopes, result formats, and discovery mechanisms as interface contracts whose exact form varies by provider/framework; do not universalize one API's message format or schema features.
- Keep tool design recipes, provider-specific API syntax, MCP mechanics, concrete tool catalogs, credentials/permissions, sandboxing, retry/idempotency logic, and project-specific execution policies with their applicable catalog, specification, security, engineering, or learning owners.
- Use the canonical entity references as research inputs for action/tool interaction and the narrower function-calling boundary when reader-facing rendering is activated.

## Validation

- The page does not create canonical `tool-calling` or `function-calling` child leaves from the merge sources.
- Tool selection/request is distinguished from validated execution and successful side effects.
- Function calling is preserved as a narrower interface pattern rather than treated as a synonym for every form of tool use.
- Schema-valid arguments are not presented as authorized, semantically correct, or safe by themselves.
- The page does not assume one provider's role/message/schema contract is universal.
- MCP, concrete tool implementations, credentials, and execution security remain with their own selected owners.
