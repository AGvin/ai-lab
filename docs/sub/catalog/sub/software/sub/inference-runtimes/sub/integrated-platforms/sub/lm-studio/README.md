# LM Studio

LM Studio is Element Labs, Inc.'s integrated local inference platform for downloading, managing, running, and serving models. It combines a desktop application with headless `llmster`/daemon operation, the `lms` CLI, local chat and model management, SDKs, and API serving.

## Local and cloud boundary

Downloaded-model inference, local chats/documents, and LM Studio's local API server can operate entirely on the user's machine and offline. The server can also be bound for local-network access, which creates a network exposure boundary that should be protected with appropriate binding and authentication controls.

LM Studio also offers optional cloud-processing features such as cloud models or web search. Current official privacy documentation distinguishes these from local processing: local prompts and documents stay on-device, while explicitly selected cloud features use a separate transient cloud data path. Treat model sources and licenses, server exposure, API tokens, MCP/tool integrations, and downloaded models as independent trust boundaries.

## Developer surfaces

LM Studio supports its native REST API, OpenAI-compatible and Anthropic-compatible endpoints, Python and TypeScript SDKs, CLI/headless workflows, and MCP/tool integration.

## Related

- [Element Labs, Inc.](../../../../../../../producers/sub/e/sub/element-labs-inc/) — canonical producer organization.

## Official resources

- [LM Studio](https://lmstudio.ai/)
- [LM Studio app documentation](https://lmstudio.ai/docs/app)
- [LM Studio developer documentation](https://lmstudio.ai/docs/developer)
- [LM Studio app privacy](https://lmstudio.ai/app-privacy)
