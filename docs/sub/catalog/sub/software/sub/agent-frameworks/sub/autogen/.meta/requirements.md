# Documentation Requirements

## Requirements

- Identify AutoGen as Microsoft's open-source framework for creating agentic and multi-agent applications.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- State the current upstream lifecycle accurately: AutoGen is in maintenance mode, is community managed, and is expected to receive bug fixes, security fixes, and documentation improvements rather than new feature development.
- Distinguish AutoGen from Microsoft Agent Framework. Explain that Microsoft Agent Framework is the production-ready successor recommended by Microsoft for new projects, while AutoGen remains available for existing users and migration.
- Describe the current layered framework at a high level: Core for message passing and local/distributed agent runtime, AgentChat for higher-level multi-agent patterns, and Extensions for model/tool integrations.
- Mention AutoGen Studio only as a prototyping/developer surface and do not present it as a production-ready application.
- Preserve the framework's multi-agent, tool-use, code-execution, event-driven, and human-in-the-loop roles without reproducing obsolete v0.2-era API details as current behavior.
- Keep package versions, supported providers, runtime requirements, release state, and other mutable implementation facts source-backed when expanded.
- Keep the maintained AutoGen Core/AgentChat/Extensions package distribution separate from obsolete v0.2 instructions: maintained documentation requires Python 3.10+, `autogen-core` or `autogen-agentchat` plus optional `autogen-ext` integrations, while historic 0.2 documentation has different imports and compatibility.
- For code execution explicitly distinguish `LocalCommandLineCodeExecutor` (executes on the application host) from `DockerCommandLineCodeExecutor` (executes inside a Docker container with selected working-directory binds). Never imply Docker is an unconditional security boundary: restrict workdir mounts, Docker socket, network, credentials, resource limits and cleanup.
- Distinguish maintenance-mode bug/security/documentation support from active feature development; cross-check current release and MAF migration guides before planning upgrades. The successor is a separate framework with non-drop-in workflow and API changes, not a renamed AutoGen release.
- Include current official AutoGen documentation and repository references.
- Link the related Microsoft Agent Framework profile.

## Validation

- The page does not present AutoGen as Microsoft's recommended framework for new production projects.
- The page does not imply that maintenance mode means the project is unavailable or abandoned.
- Microsoft Agent Framework is described as a distinct successor rather than as the same software identity.
- AutoGen Studio is not described as a production-ready end-user application.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
