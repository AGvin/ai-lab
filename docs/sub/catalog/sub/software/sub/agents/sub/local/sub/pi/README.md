# Pi

Pi is a minimal local terminal coding harness designed to keep its core small while letting users compose workflow-specific behavior through TypeScript extensions, Agent Skills, prompt templates, themes, and Pi packages.

## Runtime and extensibility boundary

Pi can be used interactively in the terminal or embedded/controlled through SDK, RPC, JSON event, and other non-interactive modes. Project instructions and context shape the session, while extensions and packages can add executable tools, commands, hooks, UI, subagents, and other behavior.

Those extension points are also trust boundaries. Project-local extensions, skills, prompts, themes, package-managed resources, shell/file access, provider credentials, and custom tools should be reviewed before use. Pi's current security documentation notes that non-interactive modes do not show the ordinary interactive project-trust prompt, so automated use requires explicit repository/environment trust controls. Third-party packages can execute code and influence agent behavior; their presence in the ecosystem is not a sandbox or trust guarantee.

Pi moved to the Earendil Works organization and `@earendil-works` package scope in May 2026 without becoming a new product identity.

## Related

- [OMP](../omp/) — separate Pi-derived coding agent with a more batteries-included tool surface.
- [Earendil Inc.](../../../../../../../producers/sub/e/sub/earendil-inc/) — current organizational home and maintainer.

## Official resources

- [Pi](https://pi.dev/)
- [Pi documentation](https://pi.dev/docs/latest)
- [Pi security](https://pi.dev/docs/latest/security)
- [Pi repository](https://github.com/earendil-works/pi)
- [Pi Has a New Home at Earendil](https://pi.dev/news/2026/5/7/pi-has-a-new-home)
