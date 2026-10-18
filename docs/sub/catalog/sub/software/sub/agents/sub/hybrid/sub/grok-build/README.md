# Grok Build

Grok Build is SpaceXSI's coding-agent product, produced by SpaceXAI LLC. It spans an installable terminal agent and hosted app-building experiences on the Grok web and mobile surfaces. The `grok-build-0.1` model is a separate model identity.

## Local and hosted work

The terminal agent reads and edits repositories, runs commands, reviews plans and diffs, and supports headless automation, subagents, worktrees, skills, plugins, hooks, MCP, and ACP. Its published source can be compiled and configured for local inference. The source repository is periodically synchronized from an internal monorepo; official binary releases have their own changelog.

The hosted surface builds applications from a conversation, supports publishing to a live address, and can export a project to GitHub. Publishing visibility, API access, connectors, and stored secrets belong to that hosted environment, rather than the local terminal's configuration.

## Permissions and sandbox

Tool approvals and operating-system sandboxing are separate controls. The terminal sandbox is off by default. Documented child-process network restrictions apply on Linux, not macOS, and do not block in-process model API or web-tool traffic. Credential paths need explicit policy where protection is required. Review repository access, extensions, shell actions, and external side effects for the selected runtime.

## Related

- [SpaceXAI LLC](../../../../../../../producers/sub/x/sub/xai/) — producer; SpaceXSI is the current public brand.

## Official resources

- [Grok Build](https://x.ai/build)
- [Open-source announcement](https://x.ai/news/grok-build-open-source)
- [Terminal source repository](https://github.com/xai-org/grok-build)
- [Web and mobile release](https://x.ai/news/grok-build-for-everyone)
- [Terminal sandbox](https://docs.x.ai/build/features/sandbox)
- [Binary release changelog](https://x.ai/build/changelog)
