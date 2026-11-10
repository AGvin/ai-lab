# NVIDIA Personal AI Router (PAIR)

NVIDIA Personal AI Router (PAIR) is self-managed software for routing independent AI inference requests among compatible computers on the same trusted local network.

## Role and product boundaries

PAIR exposes compatible Ollama and OpenAI-style proxy endpoints and selects an eligible inference node per request using engine/model availability and load. It is a request router, not a distributed execution engine: it does not pool VRAM, combine GPUs into one device, shard a single model, or split one in-flight request across hosts. Ollama and LM Studio remain independent inference engines.

## Release and safe operation

The first-party project is Apache-2.0-licensed. Validate the release's supported OSes, engine versions, local discovery and pairing controls, proxy compatibility and network assumptions. Restrict trusted local network access and credentials. Treat performance data in NVIDIA demonstrations as vendor measurements tied to their test configuration.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source](https://github.com/NVIDIA/Personal-AI-Router)
- [Getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx)
- [NVIDIA announcement](https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/)
