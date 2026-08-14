# Ollama

Ollama is Ollama Inc.'s open-source integrated inference runtime for running and serving models on user-controlled machines. It exposes a CLI and local HTTP API, supports model management and customization, and has official Python and JavaScript libraries for application integration.

## Local and cloud boundary

Local Ollama requests are handled by the local runtime. Current Ollama privacy documentation states that prompts, responses, and model interactions processed locally stay on the user's machine and are not available to Ollama.

Ollama also provides optional cloud-hosted models and a hosted API. Those requests use a separate cloud processing path and require account/API authentication. Invoking a cloud model through the local Ollama client does not make that inference local. Treat local API/network exposure, cloud credentials, model provenance/licenses, model storage, and connected tool integrations as separate trust boundaries.

## Related

- [Ollama Inc.](../../../../../../../producers/sub/o/sub/ollama-inc/) — canonical producer organization.

## Official resources

- [Ollama](https://ollama.com/)
- [Ollama documentation](https://docs.ollama.com/)
- [Ollama API](https://docs.ollama.com/api/introduction)
- [Ollama repository](https://github.com/ollama/ollama)
- [Ollama privacy](https://ollama.com/privacy)
