# Development

Software used for AI-assisted software development, including code editors, development lifecycle tooling, code-review utilities, and application security tools.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Child nodes

- [`code-editors/`](./sub/code-editors/) — code editors and editor extension ecosystems used for AI-assisted development.
- [`development-workflows/`](./sub/development-workflows/) — tools that structure AI-assisted delivery through specifications, plans, tasks, validation, and implementation stages.
- [`code-review-tools/`](./sub/code-review-tools/) — non-agent tools for inspecting, navigating, annotating, and reviewing code changesets.
- [`application-security-tools/`](./sub/application-security-tools/) — AI-enabled tools for application security testing, vulnerability analysis, findings management, remediation, and verification.

## Scope

Use this node for software whose primary documented role is creating, structuring, inspecting, reviewing, or securing software changes in AI-assisted development workflows.

Keep standalone agent-like systems under [`agents/`](../agents/), even when their main use case is software development or security testing. Keep general workflow construction under [`workflow-engines/`](../workflow-engines/) and general automation under [`automation/`](../automation/).

Create additional development categories such as testing, debugging, or version-control tooling only when real documentation content requires them.
