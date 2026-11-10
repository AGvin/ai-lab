# Documentation Requirements

## Requirements

- Present Apache TVM as a machine-learning compilation framework for importing pretrained models, optimizing them, generating target-specific code/modules, and customizing compiler/optimization pipelines.
- Keep runtime execution as part of TVM's compiled deployment workflow rather than reclassifying TVM as an inference-serving engine.
- Treat supported frontends, targets, code generators, optimization APIs, package versions, and hardware support as freshness-sensitive.
- State that TVM APIs and serialized artifacts assume trusted users and inputs. Its RPC server permits arbitrary file writes and remote code execution; native RPC traffic is plaintext and requires a trusted network or encrypted channels.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- TVM remains compiler/optimization-first rather than training- or serving-first.
- Producer provenance resolves to the Apache Software Foundation.
