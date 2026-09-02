# Function Calling

Legacy residual retained for practical function-interface design guidance that is intentionally outside the canonical Tool Use concept owner.

> **Migration note:** Function calling as a narrower structured tool-interface pattern, the fact that the exposed function need not map one-to-one to a programming-language function, host-owned authentication/authorization/validation/execution/error handling, and schema-valid-versus-safe/correct distinctions are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/tool-use/`. The remaining material below stays here until its exact learning, API/interface-design, execution-security, or project owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Function-style interfaces can support workflows such as:

- extracting typed arguments from natural-language requests;
- routing to bounded application capabilities;
- connecting conversational interfaces to business operations;
- producing structured records for a workflow step; and
- selecting among a small approved set of actions.

These are interface/application examples rather than part of the canonical tool-use definition.

## Interface-design residual

Use descriptive operation names and parameter descriptions. Prefer typed fields, enumerations, and explicit constraints where they improve validation and reduce ambiguity, but do not treat schema conformance as authorization or semantic correctness.

Keep function-like capabilities narrow enough that permission and business-rule checks are meaningful. Avoid passing model-generated file paths, SQL, shell commands, or similarly powerful free-form execution material directly into a privileged implementation unless a separate validated execution boundary explicitly permits it.

Return compact structured results whose contract can distinguish success, failure, partial completion, and relevant error state. Provider/runtime implementations can differ in schema strictness and tool/function protocol details, so recipes must be validated for the concrete interface rather than assumed portable.

These function-interface practices remain migration source material until their exact learning, API/interface-design, security, or project owners are verified.
