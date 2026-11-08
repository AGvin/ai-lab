# Amazon Quick

Amazon Quick is Amazon Web Services' hosted agentic-AI assistant and workspace for enterprise questions, research, connected-data analysis, document and application creation, and automated workflows. Users interact through chat and configurable agents grounded in the knowledge, datasets, and applications they are authorized to access. [Amazon Quick overview](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html).

## Product and execution boundary

The product combines conversational assistance, Quick Research, Quick Sight analytics, Quick Index, Quick Flows, Quick Automate, and interactive app creation. These are capabilities inside the same managed workspace, not automatically independent AI Lab service identities. Amazon Bedrock AgentCore, AWS Agent Registry, and the separate Strands or Kiro software products retain their own canonical product boundaries.

Chat agents may use connected resources and configured actions; authorization depends on the active account, data-source permissions, agent configuration, and administrators. Autonomous runs and cross-system actions require appropriate scopes, monitoring and approvals. [Agent configuration and operation](https://docs.aws.amazon.com/quick/latest/userguide/working-with-agents.html).

## Access and currentness

Consumer-style signup and organization-managed AWS provisioning have different identity, governance, and billing boundaries. Check current plan, region, subscription, connector catalog, agent allowances, available clients, approval policy, data handling and retention before adopting Quick for sensitive workflows. Agent features, skill catalogs and execution limits may change without creating a separate service identity.

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [Amazon Quick product](https://aws.amazon.com/quick/)
- [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)
- [Working with Quick chat agents](https://docs.aws.amazon.com/quick/latest/userguide/working-with-agents.html)
