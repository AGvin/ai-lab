# Continue

Continue is Continue Dev, Inc.'s open-source coding agent exposed through CLI, VS Code, and JetBrains plugin surfaces. It is represented as a Local Agent rather than as a VS Code-only extension because the same agent/runtime concept spans terminal and multiple editor clients.

## Editor client surfaces

For Visual Studio Code, Continue is distributed through its [Visual Studio Marketplace listing](https://marketplace.visualstudio.com/items?itemName=Continue.continue), which exposes the VS Code agent, chat, edit, and autocomplete experience. This is a client/distribution surface of the same Continue product rather than a separate canonical VS Code-only identity.

## Lifecycle and execution boundary

The official `continuedev/continue` repository currently states that it is read-only and no longer actively maintained after the final 2.0.0 release. Treat Continue as a retained software identity with an explicit maintenance boundary, not as evidence of an actively evolving current product unless upstream status changes.

Continue can use repository context, configurable models/providers, rules, tools, skills, MCP servers, and file/shell actions. The agent client runs in a user-controlled environment while selected model inference may be local or remote; using a hosted model API alone does not create a first-party hosted agent-execution surface.

Review repository/file permissions, shell/tools, project rules, plugins, skills, MCP servers, provider credentials, telemetry/data handling, and generated changes before use on sensitive projects.

## Related

- [Visual Studio Code](../../../../../development-tools/sub/code-editors/sub/vs-code/) — one supported editor host for Continue's VS Code client.
- [Continue Dev, Inc.](../../../../../../../producers/sub/c/sub/continue-dev-inc/) — canonical producer organization.

## Official resources

- [Continue](https://continue.dev/)
- [Documentation](https://docs.continue.dev/)
- [Visual Studio Marketplace: Continue](https://marketplace.visualstudio.com/items?itemName=Continue.continue) — VS Code client/extension surface.
- [Repository](https://github.com/continuedev/continue)
