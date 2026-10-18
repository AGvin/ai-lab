# Google Antigravity

Google Antigravity is Google's standalone agent application, introduced as Antigravity 2.0, with a CLI for the same agent runtime. It coordinates development tasks in user-selected folders, repositories, projects, and worktrees. The separately shipped Antigravity IDE has its own product surface; IDE-specific behavior should not be assumed for this application.

## Execution and release boundaries

The released application and CLI support asynchronous work, dynamic subagents, scheduled tasks, skills, MCP servers, and hooks. Remote control can reach an operator-selected machine or cloud VM. These remain user-operated execution environments; hosted model inference and Google Cloud commercial access do not by themselves move the agent workspace into a Google-managed agent service.

Google's launch roadmap for cloud-deployed agents is distinct from these available local and operator-managed surfaces. The Antigravity SDK is a preview developer surface. Check current documentation for its status, supported operating systems, model access, quotas, and organization requirements.

Repository instructions, tools, hooks, browser access, credentials, filesystem access, and unattended tasks determine what an agent can affect. Configure permissions and review generated changes for the chosen environment.

## Related

- [Google](../../../../../../../producers/sub/g/sub/google/) — produced by.

## Official resources

- [Antigravity application](https://antigravity.google/product/antigravity-2)
- [Antigravity CLI](https://antigravity.google/product/antigravity-cli)
- [Remote control](https://antigravity.google/blog/remote-control-for-antigravity)
- [Antigravity 2.0 launch and product boundaries](https://antigravity.google/blog/introducing-google-antigravity-2)
- [Release notes](https://antigravity.google/changelog)
