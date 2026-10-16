# OpenHands Software Agent SDK

OpenHands Software Agent SDK is an independently installable **MIT-licensed** SDK/runtime for software-development agents, distinct from the [OpenHands end-user application](../../../agents/sub/hybrid/sub/openhands/) and OpenHands Cloud.

## SDK, server and execution

The first-party project provides a Python agent SDK, browser-compatible TypeScript API client and an Agent Server using REST/WebSocket interfaces. These are related interfaces, not three different agent runtimes.

The operator configures local or isolated workspaces such as Docker/Kubernetes. File, shell, network, repository and credential permissions follow the actual chosen backend, not the SDK name.

## Operational considerations

Protect Agent Server authentication and endpoint access; scope tools and secrets; review isolated workspace setup and human approval gates. Local workspace operation does not make model inference local or guarantee data residency. SDK/API, supported languages, runtime backends and provider compatibility are release-sensitive. Keep the platform's automation and Cloud service ownership separate.

## Relations

- Produced by: [All Hands AI, Inc.](../../../../../producers/sub/a/sub/all-hands-ai-inc/)

## Official resources

- [SDK documentation](https://docs.openhands.dev/sdk)
- [Repository](https://github.com/OpenHands/software-agent-sdk)
