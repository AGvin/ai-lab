# Apache TVM

Apache TVM is a machine-learning compilation framework for importing pretrained models, optimizing them, generating target-specific code and modules, and customizing compiler and optimization pipelines.

## Software boundary

TVM is compiler and optimization-first. Runtime execution belongs to the compiled deployment workflow and does not make TVM an inference-serving engine.

Supported frontends, targets, code generators, optimization APIs, package versions, and hardware support are freshness-sensitive.

## Trust boundary

TVM assumes trusted users, URLs and serialized artifacts. Its RPC server permits arbitrary file writes and remote code execution by clients that can reach it. Native tracker, server and client traffic is plaintext; keep RPC within trusted networks or encrypted channels.

## Relations

- Produced by [Apache Software Foundation](../../../../../../../producers/sub/a/sub/apache-software-foundation/).

## Official resources

- [Apache TVM overview](https://tvm.apache.org/docs/get_started/overview.html)
- [Apache TVM repository](https://github.com/apache/tvm)
- [Security guide](https://tvm.apache.org/docs/reference/security.html)
