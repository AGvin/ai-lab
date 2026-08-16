# Documentation Requirements

## Requirements

- Identify Aider as an open-source terminal-based AI pair-programming and coding tool that works directly with local Git repositories.
- Preserve its tight Git integration: Aider edits repository files and can automatically commit its changes so users can inspect, diff, manage, and undo them with ordinary Git tooling.
- Preserve support for both cloud and local model backends at a high level without implying that Aider itself is a hosted agent service.
- Preserve useful legacy operational boundaries around source-code and secret exposure to model providers, local filesystem access, generated-code execution, provider credentials, and review of generated diffs before push or publication.
- Keep model recommendations, provider support, benchmark results, package versions, and other mutable implementation facts source-backed when expanded.
- Include current official Aider website, documentation, and repository references.
- Preserve Aider AI as the canonical producer identity through the `produced-by` relation.

## Validation

- The page presents Aider as a user-controlled terminal coding tool rather than a hosted agent service.
- Git integration is not generalized into unsupported repository-hosting behavior.
- Local model support is not described as making all Aider workflows offline or private by default.
- Official resource links match canonical entity metadata.
