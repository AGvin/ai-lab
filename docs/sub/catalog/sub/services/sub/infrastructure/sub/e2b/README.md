# E2B

E2B is a producer-operated cloud sandbox service that gives AI agents isolated Linux execution environments for files, commands, code, and application workloads.

## Service boundary

The hosted sandbox infrastructure and control-plane APIs define the service identity even though public SDKs and repository code are available. Explicitly beta lifecycle, persistence, MCP, regional, or SDK surfaces remain beta and are not generalized into the stable service contract.

Sandbox isolation reduces risk but does not remove caller responsibility for credentials, secrets, sensitive data, network access, side effects, resource limits, and authorization when executing untrusted or agent-generated code. Sandbox limits, regions, lifecycle controls, templates, SDK versions, pricing, network behavior, persistence, and integration support are freshness-sensitive.

## Relations

- Produced by [E2B](../../../../../producers/sub/e/sub/e2b/).

## Official resources

- [E2B](https://e2b.dev/)
- [E2B documentation](https://e2b.dev/docs)
- [E2B repository](https://github.com/e2b-dev/E2B)
