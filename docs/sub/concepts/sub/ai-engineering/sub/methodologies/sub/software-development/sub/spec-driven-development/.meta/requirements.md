# Documentation Requirements

## Requirements

- Use the reader-facing title `Spec-Driven Development` and define it as a software-development methodology in which an explicit specification captures intended behavior and constraints before implementation details are selected, then drives planning and implementation through structured refinement.
- Explain the core distinction from prompt-only or one-shot generation: requirements are made durable and reviewable, implementation planning is derived from them, and changes are reconciled back through the specification rather than relying only on transient chat context.
- Treat the specification as an engineering artifact that can include acceptance criteria, constraints, interfaces, invariants, and decision boundaries; do not prescribe one file format, template, command set, or vendor tool.
- Explain a practical loop as: clarify intent -> write/review the specification -> derive an implementation plan/tasks -> implement in bounded increments -> verify against the specification -> evolve the specification when requirements change.
- Keep Spec Kit and other concrete SDD tools with their software catalog owners. They may illustrate the methodology but do not define the only valid implementation of it.
- Distinguish SDD from Test-Driven Development and Eval-Driven Development. Tests and evals can operationalize parts of a specification, but neither is a complete substitute for explicit requirements and design intent.
- Preserve brownfield evolution: existing systems require the specification to reflect current constraints and intended change rather than pretending the project starts from an empty state.

## Validation

- Spec-Driven Development is presented as a methodology, not as a synonym for GitHub Spec Kit.
- The page does not prescribe one template, tool, model, or repository layout.
- Specifications remain reviewable engineering artifacts rather than disposable prompt scaffolding.
- Verification is tied back to explicit specified outcomes and constraints.
