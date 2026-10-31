# SWE-Serve

SWE-Serve is NVIDIA's released benchmark of inference-serving engineering by coding agents, developed with input from the SGLang team. Its first release turns 83 merged SGLang pull requests into 53 executable tasks; 19 tasks include live-serving checks.

## What a successful patch means

An agent receives an instruction and a containerized SGLang checkout from before the target change. Success requires the complete hidden verifier on the declared hardware, rather than similarity to a reference patch. Live-serving tasks load models and test behavior through serving interfaces, so local tests alone do not establish success.

The first release uses CPU or a single H100 and does not evaluate other serving engines, multi-GPU execution, or multi-node serving. Some tasks combine several pull requests. Keep task counts distinct from upstream change counts.

## Evaluation conditions

Pin the task and checkout revision, verifier, hardware, agent harness, model configuration, and time/step budgets. Preserve the published closed-book restrictions on retrieving upstream solutions and report whether the complete live-serving checks ran. Pass rates and harness comparisons apply to those conditions, not to general coding quality.

## Provenance

- Produced by: [NVIDIA](../../../producers/sub/n/sub/nvidia/)

SGLang is both the target runtime and a research collaborator. The producer relation does not assign ownership of SGLang or its contributors' work to NVIDIA.

## Official resources

- [SWE-Serve release, live-serving protocol, and collaboration](https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/)
