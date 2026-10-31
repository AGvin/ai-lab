# IREE

IREE is an MLIR-based end-to-end compiler and runtime centered on model and program import, compilation, lowering, target-specific code generation, and deployable compiled modules.

## Software boundary

IREE is compiler and optimization-first despite including a runtime. The runtime executes compiled IREE artifacts and does not move the project into serving-first inference-runtime ownership.

Supported ML frontends, deployment targets, accelerators and APIs, compiler and runtime packages, experimental targets, and platform support are freshness-sensitive.

## Artifact and runtime compatibility

Pin the compiler and runtime together and check release compatibility before reusing compiled modules. IREE allows breaking changes in minor releases. For example, 3.12.0 requires recompiling VMFB modules produced by 3.11 or earlier: the HAL module changed to 0.7 even though the VMFB bytecode version remained unchanged.

## Relations

- Produced by [IREE Project](../../../../../../../producers/sub/i/sub/iree-project/).

## Official resources

- [IREE documentation](https://iree.dev/)
- [IREE repository](https://github.com/iree-org/iree)
- [Versioning scheme](https://iree.dev/developers/general/versioning-scheme/)
- [IREE 3.12.0 compatibility changes](https://github.com/iree-org/iree/releases/tag/v3.12.0)
