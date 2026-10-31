# Runpod

Runpod is a hosted GPU and CPU infrastructure service for AI, machine-learning, and other compute-intensive workloads.

## Service boundary

Runpod is managed infrastructure rather than self-managed inference software or a model provider. Pods provide dedicated containerized compute, while Serverless provides autoscaling execution for variable workloads. Other managed model-access surfaces remain capabilities of the same service unless they develop an independently durable identity.

Runpod may expose Secure Cloud and Community Cloud capacity with different operational characteristics. `runpodctl`, REST APIs, templates, network volumes, registry integration, SSH, Jupyter, IDE connectivity, and similar mechanisms are interfaces or supporting capabilities rather than separate canonical products. Workloads may run vLLM, Ollama, ComfyUI, custom containers, and other software without transferring ownership of those runtimes to Runpod.

GPU inventory, regions, pricing, queue or startup behavior, storage and network costs, limits, compliance claims, and availability are mutable and source-sensitive.

## Relations

- Produced by [Runpod, Inc.](../../../../../producers/sub/r/sub/runpod-inc/).

## Official resources

- [Runpod](https://www.runpod.io/)
- [Runpod documentation](https://docs.runpod.io/overview)
- [Runpod terms of service](https://www.runpod.io/legal/terms-of-service)
