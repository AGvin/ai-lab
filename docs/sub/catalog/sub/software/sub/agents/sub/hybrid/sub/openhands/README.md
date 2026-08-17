# OpenHands

OpenHands is an open-source AI-driven software-development platform whose supported product surface spans a Software Agent SDK, CLI, Local GUI, hosted OpenHands Cloud, and enterprise self-hosting. Because agent workflows can run under user-controlled local execution or in first-party hosted Cloud environments, OpenHands is classified as a Hybrid Agent.

## Execution and licensing boundaries

Local use can run through the CLI, SDK, or Local GUI with application-selected model providers and runtime isolation. OpenHands Cloud provides hosted execution, while Enterprise supports organization-controlled deployment and additional enterprise capabilities.

Operational use should treat filesystem and shell access, repository permissions, backend isolation, integration scopes, automation triggers, credentials, and human approval gates as explicit security boundaries. The core OpenHands project and core container images are MIT-licensed; the repository's `enterprise/` directory uses separate enterprise licensing, so those licensing surfaces should not be conflated.

## Official resources

- [OpenHands documentation](https://docs.openhands.dev/overview/introduction)
- [OpenHands repository](https://github.com/OpenHands/OpenHands)
- [All Hands AI, Inc.](../../../../../../../producers/sub/a/sub/all-hands-ai-inc/)
