# GitHub Spec Kit

GitHub Spec Kit is an open-source toolkit and CLI for Spec-Driven Development (SDD) with AI coding agents. It turns product intent into durable specifications, technical plans, task breakdowns, validation artifacts, and implementation workflows instead of relying on one-shot coding prompts.

## Metadata

```text
Resource type: Spec-driven software development toolkit and CLI
Primary use case: Structure AI-assisted software delivery from requirements through planning, tasks, validation, implementation, and iteration
Access model: Open-source local CLI and repository templates used with a supported AI coding agent
Cost model: Spec Kit is free under the MIT License; selected coding agents, model providers, hosted services, and infrastructure may introduce separate costs
License: MIT
Source model: Open source
Operational requirement: Python 3.11+, uv recommended or pipx, a supported AI coding agent, and optional Git functionality when the Git extension is enabled
Integration modes: Slash commands, agent skills, Bash or PowerShell scripts, extensions, presets, bundles, and project-local template overrides
Source: https://github.com/github/spec-kit
Risk notes: Initialization writes workflow files and templates into the target repository. Generated specifications, plans, tasks, and implementation changes remain model-assisted output and require review, testing, permission controls, and normal source-control discipline.
Last verified: 2026-07-11
```

## Overview

Spec Kit implements a development process in which specifications remain first-class project artifacts. The coding agent is guided through explicit stages rather than being asked to infer requirements, architecture, implementation order, and acceptance criteria from one prompt.

The toolkit supplies the `specify` CLI, project templates, scripts, commands or skills for supported agents, and a conventional `specs/` workspace for feature artifacts.

Spec Kit is not itself a coding agent, code editor, or general-purpose agent orchestrator. It is the development workflow layer used around a selected coding agent.

## Core workflow

A typical workflow uses these stages:

1. **Initialize the project integration.** `specify init` installs the selected agent integration, templates, and supporting scripts.
2. **Define project principles.** `/speckit.constitution` records durable engineering and governance principles.
3. **Specify the feature.** `/speckit.specify` captures what should be built and why, without prematurely fixing the implementation.
4. **Clarify ambiguity.** `/speckit.clarify` identifies underspecified requirements before technical planning.
5. **Create the implementation plan.** `/speckit.plan` records architecture, technology choices, data models, contracts, research, and operational constraints.
6. **Generate executable tasks.** `/speckit.tasks` creates an ordered task breakdown with dependencies, paths, optional test-first work, and parallel markers.
7. **Check consistency.** `/speckit.analyze` and `/speckit.checklist` can validate coverage, consistency, and requirement quality before implementation.
8. **Implement.** `/speckit.implement` asks the selected coding agent to execute the tasks according to the approved artifacts.
9. **Reconcile remaining work.** `/speckit.converge` can compare the codebase with the specification, plan, and tasks, then append unresolved work.

Additional commands can convert tasks into GitHub issues or support installed extensions and custom workflows.

## Typical project artifacts

The exact generated structure depends on the Spec Kit version, integration, enabled extensions, and feature complexity. A project commonly includes:

```text
.specify/
  memory/
    constitution.md
  scripts/
    bash/
    powershell/
  templates/

specs/
  001-feature-name/
    spec.md
    plan.md
    tasks.md
    research.md
    data-model.md
    quickstart.md
    contracts/
```

Key artifact responsibilities:

- `constitution.md` — project-wide principles and governance constraints;
- `spec.md` — user scenarios, requirements, scope, and acceptance expectations;
- `plan.md` — implementation architecture and technical decisions;
- `tasks.md` — ordered, actionable implementation work;
- `research.md` — evidence and decisions for unresolved technical questions;
- `data-model.md` — domain entities and relationships when relevant;
- `contracts/` — API, protocol, schema, or interface contracts;
- `quickstart.md` — validation or execution guidance for the implemented feature.

These files are intended to remain inspectable and version-controlled rather than disappearing after code generation.

## Installation

The maintainers recommend installing a tagged release directly from the official GitHub repository with `uv`:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Initialize a new project with an explicit integration:

```bash
specify init my-project --integration copilot
cd my-project
```

Initialize the current repository when appropriate:

```bash
specify init . --integration copilot
```

Useful maintenance commands include:

```bash
specify version
specify self check
specify self upgrade --dry-run
specify self upgrade
```

Use a release tag instead of copying the development branch installation example unchanged into production workflows.

The official installation guide warns that similarly named packages on PyPI are not maintained by the Spec Kit project. Install from the official GitHub repository or from a locally built package derived from that repository.

## Platform and integration support

The official project supports Linux, macOS, and Windows. Current installation documentation includes native PowerShell script support on Windows without requiring WSL, while Bash scripts remain available for other environments or explicit selection.

Spec Kit integrates with many CLI-based and IDE-based AI coding agents. The installed CLI can show the integrations supported by that version:

```bash
specify integration list
```

Most integrations expose `/speckit.*` commands. Integrations that support skills mode can install equivalent agent skills instead of slash-command prompt files.

Compatibility should be checked against the exact Spec Kit release and coding-agent version. A documented integration does not guarantee identical command behavior, tool permissions, model quality, or execution isolation across agents.

## Extensions, presets, and bundles

Spec Kit has several customization layers:

- **Project-local overrides** change templates for one repository.
- **Presets** customize how existing Spec Kit workflows and artifacts are produced.
- **Extensions** add commands, templates, integrations, or development phases.
- **Bundles** package a versioned role-oriented set of extensions, presets, steps, and workflows.

Use a preset when the organization wants to change specification, planning, or task conventions. Use an extension when a genuinely new capability or workflow phase is required. Use a bundle when a repeatable team or role setup should be provisioned as one unit.

Customization increases flexibility but also creates another versioned configuration surface. Pin versions, review installed components, and test upgrades before applying them broadly.

## Strengths

- Converts vague feature intent into reviewable artifacts before implementation.
- Separates product requirements from architecture and implementation choices.
- Makes assumptions, constraints, dependencies, and acceptance criteria easier to inspect.
- Supports several coding agents instead of binding the workflow to one provider.
- Encourages staged clarification and validation rather than one-shot generation.
- Keeps feature specifications and plans in source control alongside code.
- Supports greenfield development and iterative work on existing codebases.
- Provides extension points for organization-specific standards and processes.

## Trade-offs and limitations

- The artifact workflow can be excessive for tiny, obvious, low-risk changes.
- Poor initial requirements can still produce detailed but incorrect specifications and plans.
- Generated artifacts may drift from the implementation unless the team updates and validates them.
- More documents do not automatically produce better architecture, security, or product decisions.
- Agent quality, context limits, tool access, and provider behavior materially affect implementation results.
- `/speckit.implement` can cause consequential repository and local-environment changes through the selected coding agent.
- Templates and commands evolve, so teams should pin releases and review upgrade changes.
- Spec Kit complements tests, code review, CI, security controls, and project management; it does not replace them.

## Recommended adoption approach

1. Pilot Spec Kit on a bounded feature with clear acceptance criteria.
2. Record project principles before generating feature artifacts.
3. Run clarification before planning when requirements contain ambiguity.
4. Review the specification and plan as human-owned engineering artifacts.
5. Require explicit approval before consequential implementation or publication steps.
6. Run tests, linters, security checks, and normal code review after agent implementation.
7. Compare artifact maintenance cost with the reduction in rework and ambiguity.
8. Pin a known release and test upgrades in a non-critical repository first.

## Evaluation checklist

Evaluate the toolkit against the actual development environment:

- Does the selected coding agent have a maintained integration?
- Are generated specifications complete, testable, and understandable by the team?
- Do plans respect existing architecture and repository conventions?
- Are tasks small enough to review and recover when an implementation step fails?
- Can the workflow preserve human approval boundaries for high-impact changes?
- Do generated scripts and commands work on the required operating systems?
- Are extensions, presets, and bundles reviewed and version-pinned?
- Can specification changes be traced to implementation and tests?
- Does the workflow improve delivery quality enough to justify the added artifacts?

## Fit for AI Lab

Spec Kit belongs under `development-workflows/` because its primary role is structuring AI-assisted software delivery. It integrates coding agents, but it does not primarily act as an agent, editor, or agent orchestration runtime.

Use this page as a reference for:

- specification-driven coding-agent workflows;
- requirements-to-implementation pipelines;
- durable AI-assisted development artifacts;
- comparisons with direct prompting, standalone coding agents, and agent orchestration platforms;
- evaluating governance and approval gates around AI-generated code.

## References

- Spec Kit repository: https://github.com/github/spec-kit
- Official documentation: https://github.github.io/spec-kit/
- Installation guide: https://github.com/github/spec-kit/blob/main/docs/installation.md
- Spec-Driven Development methodology: https://github.com/github/spec-kit/blob/main/spec-driven.md
- Supported integrations: https://github.github.io/spec-kit/reference/integrations.html
- CLI reference: https://github.github.io/spec-kit/reference/overview.html
- Extensions: https://github.github.io/spec-kit/reference/extensions.html
- Presets: https://github.github.io/spec-kit/reference/presets.html
- License: https://github.com/github/spec-kit/blob/main/LICENSE
