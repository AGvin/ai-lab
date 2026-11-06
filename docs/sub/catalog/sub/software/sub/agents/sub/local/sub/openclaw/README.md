# OpenClaw

OpenClaw is a self-hosted personal AI assistant designed to run on user-controlled devices or infrastructure. Its Gateway is the always-on control plane that connects the assistant to messaging channels, Web/Control UI, tools, skills and plugins, sessions, memory, mobile/device nodes, and model providers.

## Execution and trust boundary

OpenClaw's current product boundary remains local/self-hosted even when it uses remote messaging channels or hosted model providers. Agent loops and tool orchestration are centered on the user-operated Gateway, while channel services, model providers, plugins, and companion/mobile clients extend that environment rather than turning OpenClaw into a hosted assistant service.

Treat channel credentials and DM policies, persistent Gateway operation, filesystem/workspace access, browser and tool execution, device-node permissions, third-party skills/plugins, scheduled work, model-provider credentials, and inbound untrusted messages as explicit trust boundaries. Use isolation and least privilege appropriate to the accounts, repositories, devices, and data connected to the assistant.

OpenClaw explicitly models **one trust boundary per Gateway**. That supports one operator or a mutually trusting team, but not adversarial multi-tenant use: isolate mutually untrusted users with separate Gateways and credentials, ideally also separate OS users/hosts. Since release 2026.9.2, omitted session-tool visibility and agent-to-agent settings permit broader cross-agent transcript access and messaging than older defaults. Operators should review `tools.sessions.visibility`, `tools.agentToAgent`, tool grants and `openclaw security audit` instead of assuming agent/session names or operator roles provide tenant isolation.

## Provenance and stewardship

- [Peter Steinberger](../../../../../../../producers/sub/p/sub/peter-steinberger/) — original creator and producer of OpenClaw together with the project's community.
- [OpenClaw Foundation](../../../../../../../producers/sub/o/sub/openclaw-foundation/) — current non-profit project steward.

## Official resources

- [OpenClaw](https://openclaw.ai/)
- [OpenClaw documentation](https://docs.openclaw.ai/)
- [OpenClaw repository](https://github.com/openclaw/openclaw)
- [Gateway security trust model](https://docs.openclaw.ai/gateway/security/trust-model)
- [OpenClaw 2026.9.2 security changes](https://docs.openclaw.ai/releases/2026.9.2)
