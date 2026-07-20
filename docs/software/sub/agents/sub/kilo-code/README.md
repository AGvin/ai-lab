# Kilo Code

AI coding-agent platform with VS Code, JetBrains, CLI, gateway, and hosted-agent infrastructure surfaces.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Coding agent platform
Primary use case: Write, edit, understand, automate, and collaborate on code through coding-agent workflows across editor and CLI surfaces
Access model: Open-source and hosted platform components with account, gateway, and optional team or enterprise access
License: Mixed; verify component-specific licenses before adoption
Source model: Open source project with hosted platform services
Operational requirement: Kilo Code extension or CLI, selected model provider or Kilo Gateway access, repository workspace, configured rules, MCP or automation permissions, and optional KiloClaw hosted-agent infrastructure
Integration modes: VS Code, JetBrains, CLI, custom rules, modes, MCP, Kilo Gateway, KiloClaw, hosted agents, chat platforms, development tools, automation workflows
Source: https://kilo.ai/docs
Risk notes: High-trust coding-agent platform with editor, CLI, repository, model-gateway, MCP, automation, and hosted-agent access; review component licenses, provider credentials, repository permissions, generated diffs, automation scopes, hosted-agent boundaries, and human approval gates before use with sensitive repositories.
```

## Overview

Kilo Code is an AI coding-agent platform that spans editor extensions, CLI usage, model gateway access, collaboration, automation, and hosted-agent infrastructure.

It is broader than a single editor extension because the documented product surface includes VS Code, JetBrains, CLI, custom modes, rules, MCP, Kilo Gateway, and KiloClaw hosted agents.

## Fit for AI Lab

Kilo Code belongs under `agents/` because its main documented role is a coding-agent system rather than a standalone code editor.

Use it as a reference point for:

- coding-agent platforms with editor and CLI surfaces;
- multi-model gateway workflows;
- MCP-enabled coding automation;
- hosted-agent infrastructure adjacent to coding agents;
- comparison with Cline, Roo Code, Aider, and Goose.

## Evaluation notes

Evaluate before adoption:

- component-specific license and source model;
- editor, CLI, gateway, and hosted-agent scope;
- model provider and gateway credential handling;
- repository and filesystem permission boundaries;
- custom rules and mode trust boundaries;
- MCP and automation permission scopes;
- generated diff review before commit, push, or PR creation.

## References

- Kilo documentation: https://kilo.ai/docs
- Kilo Code GitHub: https://github.com/Kilo-Org/kilocode
