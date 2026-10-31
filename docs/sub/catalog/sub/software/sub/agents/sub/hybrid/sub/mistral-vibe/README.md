# Mistral Vibe

Mistral Vibe is Mistral AI's unified professional agent for productivity and coding. It brings web and mobile work, a terminal agent, VS Code integration, and managed remote coding into one product.

## Product and execution boundaries

Le Chat has become Vibe. Work and Code describe tasks and surfaces within that product: Work handles research, documents, connected applications, and scheduled workflows; Code works with repositories and development tools. The Chat/Work transition is progressive, and enterprise administrators have a migration window. Legacy names or screens may therefore remain visible.

Local CLI and editor sessions act in the user's checkout and can access files, shell commands, and configured tools. Remote Code agents run in Mistral-managed cloud sandboxes connected to repositories; web/mobile Work also uses managed execution. A local interface does not imply local model inference or prevent context from reaching configured services.

Repository access, shell execution, connectors, credentials, skills, browser content, scheduled work, and remote actions determine what an agent can affect. Review proposed changes and the approvals configured for each surface before accepting external side effects. Sandbox and permission controls do not guarantee correct output. Model access, plans, feature previews, and retention controls depend on the intended configuration.

Mistral Studio, Admin, Forge, Search Toolkit, and the underlying Mistral models retain their own product or model boundaries. An individual preview capability, such as a knowledge feature, does not change Vibe's released product identity.

## Related

- [Mistral AI](../../../../../../../producers/sub/m/sub/mistral-ai/) — producer.

## Official resources

- [Vibe documentation and product transition](https://docs.mistral.ai/vibe)
- [Vibe product announcement](https://mistral.ai/news/vibe-agent/)
- [Local and remote Code execution](https://docs.mistral.ai/vibe/code/overview)
- [Mistral release notes](https://docs.mistral.ai/resources/release-notes)
