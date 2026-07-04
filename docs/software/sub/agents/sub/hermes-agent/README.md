# Hermes Agent

Hermes Agent is a self-improving AI agent system built by Nous Research.

## Metadata

```text
Resource type: AI agent system
Primary use case: Persistent personal or workflow agent with memory, skills, scheduled automations, multi-channel access, and terminal tooling
Access model: Open-source package with bring-your-own or hosted model/provider access
License: MIT
Source model: Open source
Operational requirement: Local, VPS, container, or serverless runtime plus model/provider credentials and optional messaging gateway credentials
Integration modes: CLI, terminal UI, gateway process, Telegram, Discord, Slack, WhatsApp, Signal, local/Docker/SSH/Singularity/Modal/Daytona terminal backends, model providers, skills, scheduled automations, subagents, and RPC-style tool use
Source: https://github.com/NousResearch/hermes-agent
Risk notes: Hermes Agent can run commands, connect to messaging channels, use external model providers, retain memory, create or improve skills, and run scheduled automations. Review tool permissions, credentials, memory behavior, enabled channels, terminal backend isolation, and automation scope before using it with sensitive accounts or repositories.
```

## Purpose

Track Hermes Agent as an AI agent system for future setup notes, comparisons, and risk analysis.

## What it is

Hermes Agent describes itself as a self-improving AI agent with a built-in learning loop. Its upstream documentation emphasizes agent-curated memory, skill creation from experience, skill improvement during use, scheduled automations, subagents, and multi-channel access.

The project is designed to run beyond a single laptop, including local machines, VPS deployments, containers, SSH environments, and serverless-style backends.

## AI relevance

Hermes Agent is relevant to AI Lab as an example of a persistent agent system that combines terminal work, messaging access, memory, skills, automation, model-provider flexibility, and delegated subagents.

## Deployment notes

The upstream README documents Linux, macOS, WSL2, Termux, and native Windows install paths. It also supports model/provider selection through commands such as `hermes model` and a gateway process for messaging channels.

## Security notes

Treat Hermes Agent as high-trust infrastructure. Its value comes from combining memory, skills, tool use, terminal access, messaging channels, and scheduled automations; those same features increase operational risk.

Before use, evaluate:

- which model providers and tool gateways are configured;
- where API keys and messaging credentials are stored;
- what terminal backend is used and how it is isolated;
- which tools and skills are enabled;
- what memory is retained across sessions;
- what scheduled automations are allowed to do;
- whether subagents can access sensitive files or services.

## References

- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/
- https://hermes-agent.nousresearch.com/docs/
