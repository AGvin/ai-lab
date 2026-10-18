# Documentation Requirements

## Requirements

- Identify Cline as the open-source coding agent represented by one product identity across IDE/editor, desktop app, CLI, SDK, Kanban, automation, and managed Cloud Agents surfaces.
- Preserve its ability to inspect project context, edit files, execute terminal commands, use browser/network-capable tools, connect MCP servers and other extensions, and apply user approval controls.
- Preserve the relationship between local interactive/headless use and Cline-managed Cloud Agents as supported surfaces of one product; classify this material local-plus-managed execution envelope under Hybrid Agents.
- Distinguish operator-selected remote hubs/SSH hosts from Cline-managed Cloud Agents. The former remain self-managed; the latter execute in Cline-hosted per-session sandboxes and repositories and can continue after the browser tab closes.
- Preserve the current Cloud Agents boundary: repository access is scoped to the selected repository; agents commit and push on their own branch and changes are reviewed through pull requests. Do not imply current cloud support for local rules, skills, MCP servers, or connectors; verify client parity against current documentation.
- Preserve useful legacy operational boundaries around repository instructions/rules, shell execution, generated diff review, provider credentials, MCP/tool permissions, browser/network access, filesystem access, sandboxing, hub/remote exposure, and unattended/headless execution.
- Keep Cline product identity distinct from individual SDK/runtime/component identities and do not describe optional automation surfaces as mandatory.
- Keep model-provider support, plans, integration availability, preview states, package versions, and other mutable product-state claims source-backed when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official Cline site, documentation, and repository references.

## Validation

- One Cline software identity owns both local/self-managed and Cline-managed execution under Hybrid Agents; no duplicate Local alias node remains.
- IDE, desktop app, CLI, SDK, Kanban, scheduled/headless automation, and Cloud Agents are represented as surfaces of the same Cline product identity.
- Operator-controlled remote hubs are distinguished from the separately documented Cline-managed Cloud Agents surface.
- Approval controls are described as product behavior without promising a universal security guarantee.
- MCP, browser/network, shell, filesystem, hub/remote exposure, and unattended execution are treated as explicit trust boundaries.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
