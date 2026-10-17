# Pi

Pi is a minimal local terminal coding harness designed to keep its core small while letting users compose workflow-specific behavior through TypeScript extensions, Agent Skills, prompt templates, themes, and Pi packages.

## Runtime and extensibility boundary

Pi can be used interactively in the terminal or embedded/controlled through SDK, RPC, JSON event, and other non-interactive modes. Project instructions and context shape the session, while extensions and packages can add executable tools, commands, hooks, UI, subagents, and other behavior.

Those extension points are also trust boundaries. Project-local extensions, skills, prompts, themes, package-managed resources, shell/file access, provider credentials, and custom tools should be reviewed before use. Pi's current security documentation notes that non-interactive modes do not show the ordinary interactive project-trust prompt, so automated use requires explicit repository/environment trust controls. Third-party packages can execute code and influence agent behavior; their presence in the ecosystem is not a sandbox or trust guarantee.

Pi moved to the Earendil Works organization and `@earendil-works` package scope in May 2026 without becoming a new product identity.

On October 1, 2026, Earendil released Pi 1.0, adding native Codemode/MCP, virtual-model extension support, deferred tool loading and other incremental core capabilities without replacing the terminal agent's minimal identity. At the same time, Earendil released **Pi Durable**, a distinct experimental framework for long-running, crash-resumable, concurrent agentic applications with pluggable storage and execution environments. Pi Durable is not an automatic Pi CLI upgrade or evidence of an Earendil-operated cloud-agent service.

## Provenance and lineage

- [Mario Zechner](../../../../../../../producers/sub/m/sub/mario-zechner/) — original/current author and producer of Pi.
- [Earendil Inc.](../../../../../../../producers/sub/e/sub/earendil-inc/) — current organizational home and maintainer.
- [OMP](../omp/) — separate Pi-derived coding agent with a more batteries-included tool surface.
- [Pi Durable](../../../../../agent-frameworks/sub/pi-durable/) — separate experimental durable-agent framework by Earendil.

## Official resources

- [Pi](https://pi.dev/)
- [Pi documentation](https://pi.dev/docs/latest)
- [Pi security](https://pi.dev/docs/latest/security)
- [Pi repository](https://github.com/earendil-works/pi)
- [Pi Has a New Home at Earendil](https://pi.dev/news/2026/5/7/pi-has-a-new-home)
- [Pi 1.0 release announcement](https://earendil.com/posts/pi-1-0/)
- [Pi Durable framework announcement](https://earendil.com/posts/pi-durable/)
