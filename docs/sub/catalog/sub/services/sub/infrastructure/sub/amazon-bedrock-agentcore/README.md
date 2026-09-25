# Amazon Bedrock AgentCore

Amazon Bedrock AgentCore is AWS's managed agentic platform for building, deploying, operating, and observing AI agents across multiple frameworks, models, and protocols.

## Service boundary

AgentCore remains one hosted runtime and platform identity. Runtime, Memory, Gateway, Identity, Observability, Policy, Evaluations, managed harness, payments, browser and code execution, and knowledge or retrieval capabilities remain platform surfaces unless independently durable identities are materialized. AWS Agent Registry is separate: it moved from preview inside AgentCore to its own generally available service identity and namespace, while AgentCore integrates with it. Open-source SDKs and frameworks such as Strands Agents remain separate from the managed service.

Capability lifecycle, regions, quotas, pricing, integrations, and availability are freshness-sensitive; general availability of one capability does not imply GA for every AgentCore surface.

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AgentCore release notes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html)
