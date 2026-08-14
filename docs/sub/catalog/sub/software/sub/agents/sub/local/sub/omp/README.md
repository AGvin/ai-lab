# OMP (Oh My Pi)

OMP, also known as **Oh My Pi**, is Can Bölük's open-source terminal-first coding agent derived from [Pi](../pi/). OMP keeps Pi's session-oriented extensibility while expanding it into a more batteries-included development harness with integrated repository editing, shell execution, language-server and debugger tooling, browser/research capabilities, persistent language execution, and delegated subagents.

## Integration and execution surface

OMP exposes the same agent engine through an interactive TUI, one-shot CLI use, a Node/TypeScript SDK, RPC mode for cross-process control, and ACP interoperability with compatible clients. Plugins/extensions, skills, project instructions, MCP discovery, and configurable model providers extend the runtime further.

That broad tool surface is not sandboxing. Treat shell/debugger/browser access, repository writes, provider and OAuth credentials, network/data exposure, persistent Python or JavaScript state, plugins and skills, discovered MCP servers, subagents, remote/session-sharing surfaces, and generated diffs as explicit trust and review boundaries. Use external isolation when the repository or task is not fully trusted.

## Lineage

- [Pi](../pi/) — upstream coding-agent harness from which OMP is derived.
- [Can Bölük](../../../../../../../producers/sub/c/sub/can-boluk/) — producer and maintainer.

## Official resources

- [OMP](https://omp.sh/)
- [Oh My Pi repository](https://github.com/can1357/oh-my-pi)
- [SDK documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/sdk.md)
