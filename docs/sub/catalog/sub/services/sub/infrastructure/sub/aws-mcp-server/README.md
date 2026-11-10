# AWS MCP Server

AWS MCP Server is Amazon Web Services' hosted Model Context Protocol server providing AI agents with managed access to AWS documentation and service information, and, after appropriate authorization, AWS API operations, curated skills and sandboxed script execution. [AWS MCP Server documentation](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html).

## Managed service and authorization boundary

AWS MCP Server is a remotely operated tool-access endpoint. **Agent Toolkit for AWS** is a broader installation and configuration distribution; individual AWS services, agent skill packages, CLI commands and older local MCP servers remain distinct. Each tool exposed through the server does not constitute a new service.

AWS describes unauthenticated documentation discovery but requires existing IAM credentials for API execution, script runs and privileged curated actions. Permissions, IAM policy context, AWS account/region scope, observability, CloudTrail and CloudWatch controls still govern requests. A tool endpoint does not grant an AI agent independent authority to perform actions without appropriate policy. [AWS managed MCP access](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html).

## Operational boundaries

Validate supported regions, endpoint/access method, OAuth or SigV4 setup, network reachability, IAM permissions, tool inventory, usage quotas, pricing, audit logging and data handling for the current account. Treat agent-issued commands and tool outputs as untrusted until reviewed. Do not store API tokens or sensitive session artifacts in documentation or logs.

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [AWS MCP Server guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html)
- [2026 serverless service update](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/)
