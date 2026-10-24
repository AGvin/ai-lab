# Documentation Requirements

## Identity and provenance

- North Mini Code 1.0 is Cohere’s sparse agentic-coding model with 30B total parameters and 3B active per token.
- The card explicitly credits Cohere and Cohere Labs and identifies North-Mini-Code-1.0; the Cohere API uses north-mini-code-1-0. Its post-training combines cascaded supervised fine-tuning with reinforcement learning using verifiable rewards. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0) [North Mini Code release](https://docs.cohere.com/changelog/north-mini-code-1-0).

## Operational decision boundaries

- The documentation advertises a 256K input context and a 64K output limit. The 128-expert architecture activates eight experts per token; 3B active parameters is not the total storage or runtime-memory requirement. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0) [North Mini Code release](https://docs.cohere.com/changelog/north-mini-code-1-0).
- The weights state Apache 2.0. BF16 and quantized distributions are model artifacts; choose supported serving and precision settings rather than treating each filename as a new learned model. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).
- The model generates code and tool requests. Repository access, terminal execution, permissions and test execution belong to its harness. Benchmark results depend on the producer’s specified harness and were not reproduced here. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
