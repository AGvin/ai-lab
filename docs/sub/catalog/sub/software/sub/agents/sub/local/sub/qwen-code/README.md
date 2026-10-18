# Qwen Code

Qwen Code is Qwen Team's released, open-source agentic coding tool for terminal-based software development. It runs on the user's machine to inspect and edit repositories, execute development tools, and carry out coding tasks. The repository is Apache-2.0 licensed and publishes stable releases separately from preview and nightly builds.

## Execution boundary

Local execution, including configured sandbox or container modes, is separate from model inference. Alibaba Cloud Model Studio or other configured providers can receive task context and require their own credentials and terms. A local CLI does not imply that all data remains local.

Review shell and file permissions, sandbox configuration, provider credentials, MCP servers, extensions, external context, and autonomous changes for the intended repository. Runtime and operating-system requirements, model providers, SDKs, editor or desktop surfaces, and plan rules should be checked in current documentation.

Qwen Code is distinct from trained Qwen models, Qwen Studio, Alibaba Cloud Model Studio, and its SDK or integration packages. Component release tags are not interchangeable with the CLI's release version.

## Related

- [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) — produced by.

## Official resources

- [Qwen Code repository](https://github.com/QwenLM/qwen-code)
- [Qwen Code overview](https://github.com/QwenLM/qwen-code/blob/main/docs/users/overview.md)
- [Qwen Code releases](https://github.com/QwenLM/qwen-code/releases)
