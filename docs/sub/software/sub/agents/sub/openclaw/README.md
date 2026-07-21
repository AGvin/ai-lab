# OpenClaw

OpenClaw is a personal AI assistant that runs on user-controlled devices and connects to messaging channels.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: AI agent system
Primary use case: Personal always-on assistant across messaging channels and local or self-managed devices
Access model: Open-source package with local-first gateway and companion/node surfaces
License: MIT
Source model: Open source
Use rights signal: Permissive core; model providers, hosted services, channels, mobile app stores, and third-party skills must be reviewed separately
Cost model signal: BYO cost; the core may be open-source, but useful operation depends on selected model/provider, runtime, channel credentials, and optional companion surfaces
Deployment model: Hybrid; local-first gateway with optional Docker/Nix/source setup, companion apps, device nodes, messaging channels, and external model providers
Adoption signal: Mainstream; GitHub-visible adoption is very high, but security posture and operational fit still require separate review
Operational requirement: Node.js runtime, local or self-hosted gateway, model/provider authentication, channel credentials, workspace, skills, and optional daemon or companion app setup
Integration modes: Gateway daemon, CLI onboarding, messaging channels, macOS/iOS/Android voice interfaces, live Canvas, Docker, Nix, companion apps, device nodes, browser/canvas/nodes/cron/session tools, and workspace skills
Source: https://github.com/openclaw/openclaw
Risk notes: High-trust personal agent. OpenClaw can connect to messaging channels, local devices, filesystem/workspace state, skills, model providers, browser-like tools, nodes, cron, and external services. Review credentials, DM policies, channel permissions, daemon behavior, third-party skills, device node permissions, and data exposure before using it with private accounts or sensitive repositories.
Last verified: 2026-07-06
```

## Purpose

Use this page to track OpenClaw as a personal AI agent system for future setup notes, comparisons, and risk analysis.

## What it is

OpenClaw describes itself as a personal AI assistant that runs on the user's own devices. The project positions the Gateway as the control plane and the assistant as the product.

The assistant is designed to interact through channels the user already uses, including messaging platforms and companion interfaces.

## AI relevance

OpenClaw is relevant to AI Lab because it represents a local-first or self-hosted personal agent workflow with broad channel integrations and persistent agent behavior.

## Verification snapshot

As of 2026-07-06, the upstream repository presents OpenClaw as an MIT-licensed personal AI assistant that users run on their own devices. The README describes the Gateway as the control plane and lists broad messaging-channel support.

The upstream README also documents local onboarding, Docker/Nix/source-oriented setup paths, workspace skills, device nodes, companion apps, and security defaults for direct-message access. These features make OpenClaw a strong personal-agent candidate, but they also create a broad trust boundary around channels, local workspace state, skills, device nodes, model providers, and inbound untrusted messages.

## Deployment notes

The upstream README recommends `openclaw onboard` as the setup path. It also documents Node.js runtime requirements, gateway operation, workspace setup, development channels, Docker/Nix/source paths, and optional companion/device-node surfaces.

## Security notes

Treat OpenClaw as high-trust infrastructure. A personal assistant connected to messaging channels, model providers, local services, files, skills, devices, and external accounts can create a large attack surface.

Before use, evaluate:

- what channels and accounts are connected;
- whether direct-message access is paired, allowlisted, or publicly exposed;
- where credentials are stored;
- which skills, tools, nodes, and integrations are enabled;
- whether the Gateway runs as a persistent daemon;
- what filesystem, workspace, browser, node, and shell access the agent receives;
- what data is sent to hosted model providers;
- whether third-party skills are trusted, reviewed, and pinned;
- whether a test instance can be isolated before production use.

## References

- OpenClaw GitHub: https://github.com/openclaw/openclaw
- OpenClaw website: https://openclaw.ai
- OpenClaw documentation: https://docs.openclaw.ai
