# Augment Code

Augment Code is Augment Computing, Inc.'s software-engineering AI platform. Its product surfaces include IDE agents, the Auggie CLI, the Cosmos orchestration workspace, Context Engine, and managed Remote/Cloud Agents.

## Execution and review boundaries

Auggie can analyze repositories, edit files, and execute tools from a user-controlled terminal or automation environment. Managed Cloud Agents run in isolated vendor-operated virtual machines and can continue independently of the user's laptop. Cosmos coordinates agents and event-triggered workflows across the development lifecycle. These execution surfaces explain Augment Code's Hybrid placement.

The Auggie and Cosmos `toolPermissions` configuration governs shell, file, web, and MCP tool calls. The IDE extension does not enforce that configuration; its Agent and Agent Auto modes have their own approval behavior. Review the selected runtime, repository access, integration credentials, and automation permissions before delegating work. Cloud isolation does not itself approve a merge, deployment, or external action.

Choose the local IDE/CLI surface for interactive work in an existing development environment and the managed agent surface for delegated cloud work. Models, account eligibility, usage limits, and enterprise controls remain dependent on the current product configuration.

## Related

- [Augment Computing, Inc.](../../../../../../../producers/sub/a/sub/augment-computing-inc/) — producer.

## Official resources

- [Augment Code](https://www.augmentcode.com/)
- [Auggie CLI](https://www.augmentcode.com/product/cli)
- [Cloud Agents](https://www.augmentcode.com/product/cloud-agents)
- [Auggie and Cosmos tool permissions](https://docs.augmentcode.com/cli/permissions)
- [IDE Agent modes](https://docs.augmentcode.com/using-augment/agent)
