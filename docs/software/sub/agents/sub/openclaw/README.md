# OpenClaw

OpenClaw is a personal AI assistant that runs on user-controlled devices and connects to messaging channels.

## Metadata

```text
Resource type: AI agent system
Primary use case: Personal always-on assistant across messaging channels
Access model: Open-source package
License: MIT
Source model: Open source
Operational requirement: Node.js runtime, local or self-hosted gateway, model/provider authentication, channel credentials, and optional daemon setup
Integration modes: Gateway daemon, CLI onboarding, messaging channels, macOS/iOS/Android voice interfaces, live Canvas, Docker, Nix, and companion apps
Source: https://github.com/openclaw/openclaw
Risk notes: OpenClaw can become a high-trust personal agent connected to local devices, messaging channels, filesystem access, model providers, and external services. Review credentials, channel permissions, daemon behavior, skill/tool permissions, and data exposure before using it with private accounts or sensitive repositories.
```

## Purpose

Use this page to track OpenClaw as a personal AI agent system for future setup notes, comparisons, and risk analysis.

## What it is

OpenClaw describes itself as a personal AI assistant that runs on the user's own devices. The project positions the Gateway as the control plane and the assistant as the product.

The assistant is designed to interact through channels the user already uses, including messaging platforms and companion interfaces.

## AI relevance

OpenClaw is relevant to AI Lab because it represents a local-first or self-hosted personal agent workflow with broad channel integrations and persistent agent behavior.

## Deployment notes

The upstream README recommends `openclaw onboard` as the setup path. It also documents Node.js runtime requirements and daemon installation for keeping the Gateway running.

## Security notes

Treat OpenClaw as high-trust infrastructure. A personal assistant connected to messaging channels, model providers, local services, files, and external accounts can create a large attack surface.

Before use, evaluate:

- what channels and accounts are connected;
- where credentials are stored;
- which skills, tools, and integrations are enabled;
- whether the Gateway runs as a persistent daemon;
- what filesystem and shell access the agent receives;
- what data is sent to hosted model providers;
- whether a test instance can be isolated before production use.

## References

- https://github.com/openclaw/openclaw
- https://openclaw.ai
- https://docs.openclaw.ai
