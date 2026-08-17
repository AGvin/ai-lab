# Documentation Requirements

## Requirements

- Identify OpenClaw as a self-hosted personal AI assistant designed to run on the user's own devices or infrastructure.
- Preserve the product boundary that the Gateway is the user-operated control plane connecting the assistant to messaging/channel surfaces, Web/Control UI, tools, skills/plugins, sessions, memory, mobile/device nodes, and agent workflows.
- Preserve multi-channel and model-provider flexibility at a high level without freezing current channel/provider counts.
- Preserve current governance accurately: OpenClaw is developed and stewarded in the open by the non-profit OpenClaw Foundation.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve useful legacy trust boundaries around channel credentials and DM policies, persistent gateway/daemon operation, filesystem/workspace access, browser/tool execution, device-node permissions, third-party skills/plugins, scheduled tasks, external model providers, and inbound untrusted messages.
- Do not misclassify OpenClaw as a hosted assistant service merely because it integrates remote messaging or model services; current agent loops, tools, and inference orchestration remain centered on the user-operated Gateway even when external providers or channels are used.
- Keep foundation/governance details, platform inventories, runtime versions, provider/channel lists, plugin inventories, mobile-client capabilities, and other mutable state source-backed when expanded.
- Include the current official OpenClaw repository, site, and documentation.

## Validation

- The page distinguishes the OpenClaw assistant from its Gateway control-plane component.
- The profile preserves self-hosted/user-controlled execution as the primary ownership boundary.
- Remote channels and mobile clients are not misrepresented as hosted execution of the agent itself.
- Skills/plugins, channels, browser/tools, device nodes, scheduled work, and provider credentials are treated as explicit trust boundaries.
- Mutable integration counts are not treated as stable identity facts.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
