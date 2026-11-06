# Mastra

Mastra is a TypeScript framework for building AI agents and applications with primitives for tools, workflows, memory, model access, and production-oriented integrations.

## Framework and operational boundaries

Mastra builds open-ended, tool-using TypeScript agents and structured workflows with explicit steps, branching and resumable execution. Its memory, workspace, observability and deployment integrations are optional components; Mastra Cloud is not required to run self-managed agents.

**Code execution needs deliberate isolation.** A default `LocalSandbox` runs shell commands on the application host and is not secure isolation. For untrusted tasks, enable native Seatbelt/Bubblewrap isolation where supported, or use a restricted remote/container sandbox. Configure tool approvals, filesystem mounts, network access and secrets. A static sandbox can be shared between requests; use a resource/thread-scoped resolver and clean up resolver-owned sandboxes to prevent tenant state leakage.

**License boundary:** Most core framework code is Apache-2.0, but directories named `ee/` use a separate Mastra Enterprise License and may require production licensing.

## Official resources

- [Official website](https://mastra.ai/)
- [Documentation](https://mastra.ai/docs)
- [Official repository](https://github.com/mastra-ai/mastra)
- [Sandbox and filesystem security](https://mastra.ai/docs/sandbox/overview)
- [License mapping](https://github.com/mastra-ai/mastra/blob/main/LICENSE.md)
