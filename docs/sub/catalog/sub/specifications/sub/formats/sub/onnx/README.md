# ONNX

ONNX is an open, versioned model and intermediate-representation specification for serialized computation graphs and associated model information.

## Format boundary

The ONNX IR defines graphs, nodes and operators, values and types, initializers, metadata, functions, external-data references, and related serialized model structure. IR versioning is distinct from operator-set versioning and other versioned ONNX surfaces; they must not be collapsed into one generic version number.

A valid ONNX artifact does not guarantee target-runtime operator support, semantic equivalence after conversion, hardware acceleration, model quality, licensing, or workload fit. Converter behavior, runtime/provider compatibility, optimizations, implementation bugs, benchmarks, and model-selection guidance remain separate concerns.

## Official resources

- [ONNX IR specification](https://onnx.ai/onnx/repo-docs/IR.html)
- [ONNX repository](https://github.com/onnx/onnx)
