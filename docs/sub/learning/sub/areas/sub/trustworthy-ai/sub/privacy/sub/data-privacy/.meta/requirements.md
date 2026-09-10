# Documentation Requirements

## Requirements

- Teach Data Privacy through what sensitive information is collected, exposed to a model/tool/provider, retained, logged, disclosed, or made available to later users/processes.
- Prefer task-relevant minimum disclosure over copying unrestricted prompts, internal policies, source documents, or intermediate reasoning-like traces into durable artifacts merely for completeness.
- When auditability is required, preserve the minimum externally inspectable evidence needed for the decision: structured state, tool results, calculations, approvals, source references, or concise explanations can be safer and more reliable than unrestricted trace prose.
- Treat prompts, model context, logs, traces, caches, files, tool inputs/results, and generated outputs as potential sensitive-data surfaces subject to the applicable retention/access rules.
- Keep concrete provider data-retention behavior, legal requirements, organizational policy, and product settings source-backed with their current owners.

## Validation

- Sensitive information is not retained solely because it appeared in an intermediate reasoning process.
- Audit requirements are balanced against minimization and access boundaries.
- Concrete retention/access rules are not invented as timeless learning facts.
