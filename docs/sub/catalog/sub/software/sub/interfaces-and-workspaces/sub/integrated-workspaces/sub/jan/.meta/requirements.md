# Documentation Requirements

## Requirements

- Identify Jan as an open-source, local-first AI desktop/workstation application for downloading and running local models, connecting cloud providers, managing assistants/conversations, and exposing local compatible APIs.
- Preserve its primary placement under `interfaces-and-workspaces/integrated-workspaces`; Jan Desktop combines model management, inference, chat/workspace, API, and MCP capabilities.
- Preserve Menlo Research Pte Ltd as the legal producer identity while allowing Menlo Research as its public-facing alias.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve the current release boundary: Cowork is a Desktop nightly preview that can work with files and run commands, not a stable Desktop feature.
- Since Desktop 0.8.5, the Jan Agent preview CLI is installed and updated separately; Desktop does not bundle it. The CLI uses an external model backend, including Desktop's Local API Server, and does not itself provide an inference engine. Legacy `jan launch`, `jan serve`, and `jan models load` commands are not current CLI commands.
- Keep supported backends, model/provider lists, agent integrations, endpoint details, and release-specific behavior source-backed when expanded.
- Include current official Jan documentation, repository, and legal/privacy references.

## Validation

- Desktop nightly Cowork, stable Desktop, and the separately installed Agent preview CLI are not presented as one uniformly available release surface.
- Jan's integrated workspace identity remains distinct from its underlying llama.cpp/MLX inference backends.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
