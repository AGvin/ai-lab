# Kilo Code

Kilo Code is an open-source AI coding product spanning editor integrations, a local CLI runtime, model/provider and MCP integrations, and a hosted Cloud Agent surface.

## Local, remote-control, and hosted execution

Local editor and CLI work executes on the developer's machine, including `kilo serve` and CI runs with `kilo run --auto`. **Cloud Agent** is different: it clones repositories into Kilo-hosted Linux containers, applies environment setup and credentials, and runs agent work remotely. The `kilo cloud` CLI commands start and manage those hosted tasks; Cloud Agent webhook/schedule triggers also execute there. **Remote Connections** are different again: the cloud UI can control an active local CLI session, but that user-owned machine retains the compute and file permissions.

That distinction matters for trust. Review provider or gateway credentials, repository and filesystem access, custom rules/agents/skills, MCP servers, terminal/browser execution, account security for remote control, hosted-agent environment access, generated diffs, and human approval before commit, push, or merge. Cloud Agent containers can receive repository integration permissions, injected secrets, project skills and startup commands. In remote-control mode, anyone with access to the Kilo account may send prompts to the connected local computer; autonomous tool approvals and hosted trigger execution require their own least-privilege controls. The old `kilo console` browser interface is deprecated.

## Official resources

- [Kilo](https://kilo.ai/)
- [Kilo CLI](https://kilo.ai/docs/code-with-ai/platforms/cli)
- [Kilo Cloud Agent](https://kilo.ai/docs/code-with-ai/platforms/cloud-agent)
- [Kilo Code repository](https://github.com/Kilo-Org/kilocode)
- [Local CLI runtime architecture](https://kilo.ai/docs/contributing/architecture/cli-runtime)
- [Kilo CLI/cloud command reference](https://kilo.ai/docs/code-with-ai/platforms/cli-reference)
- [Kilo Code Inc.](../../../../../../../producers/sub/k/sub/kilo-code-inc/)
