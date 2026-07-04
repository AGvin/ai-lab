# Pi

Pi is a terminal coding harness for AI-assisted software work.

## Metadata

```text
Resource type: AI coding harness
Primary use case: Terminal-based coding agent workflow
Access model: Open-source package and hosted/subscription or API-key model providers depending on configuration
License: MIT
Source model: Open source
Operational requirement: Node.js package installation and provider authentication or API keys
Integration modes: Terminal UI, SDK, RPC mode, JSON event stream mode, TypeScript extensions, skills, prompt templates, themes, and Pi packages
Source: pi.dev documentation
Risk notes: Coding harnesses can read files, run shell tools, use networked providers, and modify repositories depending on configuration. Review security settings, provider credentials, extensions, skills, and packages before use.
```

## What it is

Pi is a minimal terminal coding harness. It is designed to stay small at the core and be extended through TypeScript extensions, skills, prompt templates, themes, and Pi packages.

It is not the `pi.ai` conversational assistant product. This page tracks the software documented at `pi.dev`.

## Why it belongs here

Pi belongs under `agents/` because its primary documented role is a terminal-based coding agent harness, not a general code editor or editor extension.

## Capabilities

Pi documentation describes these relevant areas:

- terminal coding-agent workflow;
- provider authentication through subscription providers or API keys;
- SDK usage for embedding agent capabilities in Node.js applications;
- RPC and JSON event stream modes for programmatic integrations;
- TypeScript extensions for tools, commands, events, and custom UI;
- skills for reusable on-demand capabilities;
- Pi packages for bundling and sharing extensions, skills, prompt templates, and themes.

## When it may be worth evaluating

Pi is worth documenting and evaluating when the goal is to compare terminal coding agents, build custom agent tooling, embed a coding agent in another workflow, or study extension and skill packaging for agent workflows.

## Open questions

Before deeper practical notes are added, verify:

- supported operating systems and runtime requirements;
- current package name and installation flow;
- model/provider support;
- sandbox and project trust behavior;
- extension, skill, and package permission boundaries;
- how it compares with other terminal coding agents in real repository tasks.

## References

- https://pi.dev/docs/latest
- https://pi.dev/docs/latest/sdk
- https://pi.dev/docs/latest/extensions
- https://pi.dev/docs/latest/skills
- https://pi.dev/docs/latest/packages
