# Documentation Requirements

## Requirements

- Identify Pi as a minimal local terminal coding harness whose core intentionally stays small while workflow-specific behavior is added through TypeScript extensions, Agent Skills, prompt templates, themes, and Pi packages.
- Preserve its normal interactive terminal use plus programmatic/non-interactive surfaces such as print/JSON modes, SDK embedding, RPC/JSONL integration, and custom interfaces without turning those surfaces into separate product identities.
- Preserve project-local instructions/context and the distinction between Pi's small core and executable extensions/packages that can add tools, commands, UI, hooks, subagents, or other behavior.
- Preserve current stewardship accurately: Pi moved to the Earendil Works organization and `@earendil-works` package scope in May 2026 while retaining the same product identity and direction.
- Preserve OMP as a separate derived product in reader-facing lineage context rather than a Pi version or alias.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve useful legacy trust boundaries around shell/file access, project instructions, provider credentials, extensions, skills, prompt templates, packages, custom tools, and programmatic/non-interactive operation.
- Reflect the current project-trust boundary: project-local extensions, skills, prompts, themes, and package-managed extensions are code/content trust inputs; non-interactive modes do not present the ordinary interactive project-trust prompt, so automation requires explicit environment/repository trust controls.
- Make clear that third-party Pi packages can execute code and influence agent behavior; package availability does not imply trust or sandboxing.
- Keep provider/model lists, package inventories, exact versions, installation commands, and other mutable implementation details source-backed and time-scoped when expanded.
- Keep Pi distinct from unrelated products using the Pi name and from OMP, which is a separate derived product.
- Include current official Pi site, documentation, repository, and stewardship announcement references.

## Validation

- Pi is represented as a minimal extensible coding-agent harness rather than a full IDE or fixed hosted assistant.
- SDK/RPC/JSON modes are represented as integration surfaces of the same Pi identity.
- Extensions, skills, templates, themes, and packages remain distinct mechanisms and executable package/extension trust is not understated.
- Non-interactive operation is not described as inheriting an interactive project-trust prompt that it does not show.
- The OMP derived product remains a separate sibling identity.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
