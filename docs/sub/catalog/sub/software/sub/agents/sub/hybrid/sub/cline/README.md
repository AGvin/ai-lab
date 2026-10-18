# Cline

Cline is an open-source coding agent spanning editor integrations, a desktop app, CLI, SDK, Kanban and automation workflows, and Cline-managed Cloud Agents. It can inspect repositories, edit files, execute commands, and use browser or external tools. These are surfaces of one product.

## Local and managed execution

Local clients run in user-controlled environments. Remote hubs and SSH connections can place execution on infrastructure selected by the operator; those deployments remain self-managed.

Cloud Agents provide a distinct Cline-operated execution surface. Each session receives an isolated sandbox and a repository workspace, can continue after the browser tab closes, and can commit and push changes to its own branch for pull-request review. Repository access is scoped to the repository selected for the session. This supported local-plus-managed product envelope places Cline under Hybrid Agents.

Client features differ. Current Cloud Agents documentation says local rules, skills, MCP servers, and connectors are not loaded in cloud sessions. Do not assume local configuration follows a task into the cloud.

Repository instructions, shell and browser access, credentials, network tools, filesystem permissions, automation, and auto-approval settings determine what an agent can affect. Review generated changes and external side effects. Approval controls and sandboxing do not guarantee correct or safe results. The open-source repository license is Apache-2.0; hosted access and model services have separate terms and availability.

## Related

- [Cline Bot Inc.](../../../../../../../producers/sub/c/sub/cline-bot-inc/) — producer.

## Official resources

- [Cline](https://cline.bot/)
- [Cline overview](https://docs.cline.bot/cline-overview)
- [Cloud Agents](https://docs.cline.bot/usage/cloud-agents)
- [Desktop SSH execution](https://docs.cline.bot/usage/cline-desktop-ssh)
- [Cline repository](https://github.com/cline/cline)
