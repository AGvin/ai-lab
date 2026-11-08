# Documentation Requirements

## Requirements

- Document current ChatGPT/OpenAI shared plugin catalog and workspace-facing plugin behavior as mutable service/product facts from official OpenAI documentation.
- Cover shared plugin discovery/catalog, installation or enablement, removal/management, supported plugin capabilities/components, workspace/admin boundaries, and availability only when current-source-backed.
- Record the documented shared ChatGPT/Codex plugin-system relationship without duplicating Codex-specific execution details here.
- Keep exact UI surfaces, availability, catalog behavior, supported components, admin controls, and product terminology current-source-backed because they may change.
- Link the formal Agent Plugins specification when OpenAI exposes portable Agent Plugins behavior rather than redefining the standard.
- Keep generic plugin lifecycle, trust, adoption, and portability teaching with the selected concept/learning owners.

## Validation

- Current shared ChatGPT/OpenAI plugin behavior is supported by current official OpenAI documentation.
- Codex-specific sandbox/approval/execution behavior is not owned here.
- Portable Agent Plugins normative fields are not duplicated as product truth.

## Scoped original-source qualification — 2026-11-08

- **ChatGPT Plugins** is OpenAI's shared plugin directory/install/usage surface in supported ChatGPT and Codex clients. Official developer documentation describes a universal plugin catalog, skills and MCP server capabilities, optional browser extensions and hooks, and account/workspace installation and service-connection boundaries. This does **not** make every plugin or connector a first-party OpenAI service or grant access to external accounts automatically.
- Plugins can be used in supported ChatGPT Chat/Work on web, desktop and mobile; Codex availability depends on its supported desktop and CLI surfaces, and IDE extension plugin support is not claimed. Desktop-only plugins cannot be used on mobile. Workspace admin permissions, plugin install state, third-party app authentication, hook execution/approval, data routing and vendor terms vary by environment.
- Original first-party docs: https://learn.chatgpt.com/docs/plugins and https://learn.chatgpt.com/docs/build-plugins (OpenAI, checked 2026-11-08). Portable Agent Plugins specification, specific third-party plugin packages, Codex-specific execution, independent external provider security/legal terms and host/runtime tests are **separate** scopes.
- Credit **one existing identity scoped original-source gate only**. No new entity/metadata, third-party plugin validation, live connector or paid service call, end-to-end permission/privacy/security/legal audit, renderer-wide/CI/clean/final acceptance.
