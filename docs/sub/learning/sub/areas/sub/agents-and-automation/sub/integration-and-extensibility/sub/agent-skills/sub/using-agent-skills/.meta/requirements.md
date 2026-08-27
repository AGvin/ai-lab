# Documentation Requirements

## Requirements

- Use the reader-facing title `Using Agent Skills` and preserve the source guide's complete adoption lifecycle: evaluate a skill, install it through an appropriate mechanism, verify discovery/activation, invoke it explicitly or automatically where supported, compose it carefully, update it, disable/remove it, and troubleshoot portability/runtime failures.
- Before installation, require readers to confirm target-client support, inspect the skill instructions and bundled scripts/resources, review license/maintenance/compatibility/update mechanism, identify required tools/credentials/network destinations/writable paths, and choose project-local versus user-global scope deliberately.
- Explain project-local versus user-global installation as a scope/review decision, not a universal path rule. Project-local is appropriate for repository-owned reviewed workflow; user-global for safe personal workflows across projects, subject to host support.
- Preserve three installation models: copy the complete skill directory, use an installer, or install a plugin/managed bundle that contains skills. Explain that copying only the entrypoint can break referenced resources and that installers/marketplaces do not make a source trusted.
- Current examples such as `npx skills@latest add owner/repository`, skill-root paths, plugin commands, or UI mechanisms must be marked platform/install-tool-specific and freshness-sensitive rather than timeless requirements.
- Teach explicit invocation versus model/host automatic discovery. Preserve representative explicit examples such as a command-style invocation and a natural-language request to use a named skill, while noting exact syntax is host-specific.
- Explain when explicit invocation is preferable: high-impact tasks, ambiguous multiple matches, broad orchestration flows, testing new skills, or unreliable automatic discovery.
- For automatic activation, teach testing with realistic task language rather than naming the skill; the observable process defined by the skill should appear instead of merely a similar-looking answer.
- Preserve activation-verification techniques: host UI indicator where available, inspect/ask what instructions loaded, observe required workflow steps, inspect logs/tool calls where available, temporarily add a harmless unmistakable test instruction, and compare with the skill disabled. Do not use answer similarity alone as proof.
- Teach skill composition through clear responsibility boundaries. Preserve the example of a staged engineering flow using requirement/design, spec, TDD, and code-review skills as illustration while avoiding hard dependency on those exact skill names. Warn against multiple skills claiming the same workflow stage.
- Preserve update models: managed subscription, pinned reviewed copy, and forked copy. For consequential workflows, record immutable source/revision and review diffs because Markdown instruction changes can change commands, permissions, and data handling.
- Preserve disable/removal responsibilities: remove/disable directory/plugin/UI/permission rule as appropriate, reload host if required, verify discovery metadata disappears, remove bundled hooks/MCP configuration, and revoke credentials created only for the skill.
- Preserve troubleshooting coverage for: not discovered; not automatically activated; over-activation; script failure; different behavior across clients. Include checks for location/current spec requirements, discovery description quality, runtime/working directory/dependencies/env/network, permissions, invocation syntax, supported metadata/extensions, and host-specific differences.
- When teaching current structural facts such as the uppercase entrypoint filename, YAML/frontmatter fields, directory-name constraints, or host-specific metadata, source them from the current Agent Skills specification/platform documentation and clearly separate normative specification from learning guidance.
- Preserve the safe-adoption checklist: source/revision, instruction review, script/dependency review, minimized permissions, positive and negative activation tests, failure/rollback test, and selected update policy.
- Cross-link the Agent Skills learning root, creating tutorial, portability/platform-support continuation, abstract concept, formal specification, and concrete catalog sources where applicable.

## Validation

- The guide can be followed by a first-time skill user without assuming one host-specific directory/UI.
- It gives observable tests for discovery/activation rather than relying on subjective answer similarity.
- Installation/update/removal and permission/trust boundaries remain explicit.
- Current specification and platform facts are freshness-bound/source-backed.
