# AWS Agent Registry

AWS Agent Registry is Amazon Web Services' generally available private, governed organizational catalog and discovery service for agents, tools, skills, MCP servers, and custom resources. Its primary role is organization-wide discovery, approval, lifecycle metadata, access control, sharing, auto-detection, and resource reuse rather than agent execution.

## Service boundary

The service has its own console, `agent-registry` API and IAM namespace, managed IAM policy, resource ARN namespace, and lifecycle. Amazon Bedrock AgentCore remains a separate managed agent runtime/platform: Agent Registry can discover and integrate with AgentCore resources without becoming an AgentCore runtime capability.

Regions, record schemas, approval workflows, authorization, integrations, quotas, pricing, APIs, and migration timelines are freshness-sensitive service state.

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [AWS Agent Registry documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-get-started.html)
- [General availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-agent-registry-generally-available/)
- [AWS Agent Registry overview article](https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/)
