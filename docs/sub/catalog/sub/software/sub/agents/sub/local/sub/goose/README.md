# goose

goose is an open-source, local-first general-purpose AI agent that runs on the user's machine through desktop, CLI, and API surfaces. It is intended for more than coding: current upstream materials also position it for research, writing, automation, data analysis, and other tool-driven work.

## Runtime and extension boundary

goose supports multiple model providers and local-model options, including optional built-in llama.cpp inference using GGUF models. Provider choice still determines credential and data-flow boundaries, so local execution of the agent does not make every workflow offline or private by default.

ACP provides an interoperability path between goose and compatible agent clients or agent providers, while MCP remains a primary mechanism for connecting extensions and tools. Treat filesystem and shell access, provider credentials, extension/tool permissions, prompt-injection exposure, desktop/API surfaces, and unattended workflows as explicit trust boundaries; use approval and sandboxing controls appropriate to the data and repository sensitivity.

The desktop client can connect to an operator-run `goose serve` backend. Protect network exposure with the shared secret and TLS; this remote deployment remains self-managed rather than a goose-operated hosted service.

## Provenance

- [Block](../../../../../../../producers/sub/b/sub/block/) — original producer and founder of goose.
- [Agentic AI Foundation](../../../../../../../producers/sub/a/sub/agentic-ai-foundation/) — current steward at the Linux Foundation.

## Official resources

- [goose documentation](https://goose-docs.ai/)
- [goose repository](https://github.com/aaif-goose/goose)
- [Remote goose server](https://goose-docs.ai/docs/guides/remote-goose-server/)
- [Built-in local inference](https://goose-docs.ai/blog/2026/04/24/use-goose-with-built-in-local-inference/)
