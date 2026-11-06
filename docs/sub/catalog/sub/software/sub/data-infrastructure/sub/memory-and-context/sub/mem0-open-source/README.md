# Mem0 Open Source

Mem0 Open Source is the self-managed/open-source Mem0 memory engine, distinct from the producer-operated Mem0 Platform service.

## Scope and boundaries

The library and self-hosted server are deployment forms of the same memory engine. Vector stores, graph services, rerankers, supported providers, and deployment dependencies vary with the selected release and configuration.

Current defaults in both forms use OpenAI for LLM and embedding operations. Memory storage and model processing are separate choices: self-managing the memory engine or its database does not make those model operations local, and providers must be configured independently.

## Relations

- Produced by: [`catalog/producers/m/mem0`](../../../../../../../producers/sub/m/sub/mem0/)

## Official resources

- <https://docs.mem0.ai/open-source/overview>
- <https://github.com/mem0ai/mem0>
