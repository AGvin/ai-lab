# Documentation Requirements

## Requirements

- Identify Jan as an open-source, local-first AI desktop/workstation application for downloading and running local models, connecting cloud providers, managing assistants/conversations, and exposing local compatible APIs.
- Preserve its primary placement under `interfaces-and-workspaces/integrated-workspaces`; Jan combines model management, inference, chat/workspace, API, MCP, and CLI capabilities rather than being only an inference engine or only a model client.
- Preserve Menlo Research Pte Ltd as the legal producer identity while allowing Menlo Research as its public-facing alias.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve the current agent boundary: after removal of the in-app OpenClaw integration in Jan v0.7.9, Jan does not run external coding agents inside the desktop app; `jan launch` starts/serves a local model and wires separately installed agent programs such as Claude Code or OpenClaw to that backend.
- Keep supported backends, model/provider lists, agent integrations, endpoint details, and release-specific behavior source-backed when expanded.
- Include current official Jan documentation, repository, and legal/privacy references.

## Validation

- The page does not claim that current Jan Desktop embeds or executes external coding agents internally.
- Jan's integrated workspace identity remains distinct from its underlying llama.cpp/MLX inference backends.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
