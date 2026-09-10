# Documentation Requirements

## Requirements

- Use the reader-facing title `Structured Output`.
- Define structured output as model-generated content intended to conform to an explicit machine-consumable structure or data contract, such as a typed object, JSON/JSON Schema instance, grammar-backed record, function/tool argument object, XML document, CSV row set, or another defined representation.
- Distinguish the desired structured-output contract from the mechanism used to achieve it. Prompt instructions, constrained decoding, tool/function-call interfaces, specialized model training, post-generation parsing/repair, retries, or combinations can all contribute to structured output with different guarantees.
- Explain that syntactic parseability, schema conformance, type validity, semantic/domain validity, factual correctness, authorization, and safety are separate validation layers. Passing a schema does not prove that generated values are true, permitted, safe, or internally consistent beyond what the schema actually expresses.
- Treat a schema as a formal structural/validation contract, not as a substitute for task instructions, evidence, business rules, or application authorization unless those semantics are genuinely encoded and enforced by the schema system.
- Explain that schemas and constrained-output mechanisms can reduce structural failure modes but can also change model behavior, latency, token selection, supported schema coverage, or content quality; claims about guarantees must be scoped to the exact implementation and supported constraint subset.
- Distinguish structured output from `constrained-generation/`: structured output is the target form/contract, while constrained generation is one inference mechanism that restricts the allowed generation space.
- Distinguish structured output from tool execution: a valid tool-argument object is still proposed model output until the application validates and authorizes the action and the tool/system actually executes it.
- Keep provider-specific schema dialects, unsupported keywords, function/tool APIs, repair policies, retry logic, business validation, and consequential-action controls with their applicable catalog, engineering, trustworthy-AI, or learning owners.
- Use the canonical entity references as research inputs for schema-compliance versus content-quality and implementation-guarantee boundaries when reader-facing rendering is activated.

## Validation

- The page distinguishes output structure from the decoding or prompting mechanism used to produce it.
- Schema validity is not presented as factual, semantic, business-rule, authorization, or safety validity.
- Structured output is distinguished from constrained generation and from actual tool execution.
- Guarantee claims are scoped to the exact supported schema/constraint implementation rather than generalized to all JSON Schema or all structured formats.
- The page does not assume JSON is the only structured-output representation.
- Legacy implementation recipes are not duplicated as universal canonical guidance.
