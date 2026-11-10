# Documentation Requirements

## Requirements

- Present Agent Plugins as the open, vendor-neutral, versioned portable plugin package standard defined by the upstream specification.
- Treat the current `agent-plugins.org` specification and upstream repository as authoritative research sources. Re-check live sources before changing manifest fields, component rules, schema constraints, version claims, or extension behavior.
- Describe the package contract at a source-backed level, including the required plugin manifest and the standard's portable component/reference surfaces; exact filenames, fields, and validation rules remain versioned specification facts.
- Treat referenced Agent Skills and MCP artifacts as separate specifications with their own canonical owners rather than redefining those contracts here.
- Explain the client-extension boundary only as defined by the Agent Plugins specification; vendor/client-specific extensions must not be generalized into portable standard behavior.
- Do not claim that every ecosystem using the word `plugin` conforms to Agent Plugins. Claude Code, Cursor, OpenCode, OpenAI/ChatGPT/Codex, and other hosts may expose additional or different package, marketplace, command, hook, permission, or lifecycle contracts.
- Keep concrete host discovery, installation, execution, permissions, marketplaces, compatibility, update behavior, and current supported components with the corresponding product integration owner.
- Keep generic plugin concept, lifecycle, trust, adoption, and portability teaching with selected concept/learning owners.

## Validation

- Exact manifest/component/version statements are traceable to the current upstream Agent Plugins specification.
- Vendor-specific plugin behavior is not misrepresented as portable Agent Plugins behavior.
- Agent Skills and MCP are linked as external formal contracts rather than duplicated.

## Scoped original-source qualification — 2026-11-07

- Agent Plugins is the published vendor-neutral portable plugin package specification v1.0.0. A plugin is a rooted directory with a required root `plugin.json` manifest; `$schema`, name, version and package components have normative versioned validation rules. Paths defined as plugin-relative are constrained to the root, including symlink/junction resolution.
- The portable specification explicitly separates referenced Agent Skills and MCP artifacts from the plugin envelope. A client's custom commands, hooks, marketplace, installation, permission approvals, runtime isolation or extension namespaces are host-defined; a package conforming to the format is not inherently trusted or safe to run.
- Verified first-party source 1: https://agent-plugins.org/specification
- Verified first-party source 2: https://github.com/agentplugins/agent-plugins-spec
- Existing format identity/source gate only; no plugin installed, manifest validated by a conformant runtime, client tested, security/license audit, root-wide schema/cache/CI/render, clean pass or final gate.
