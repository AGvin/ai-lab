# Documentation Requirements

## Requirements

- Present ONNX as the open, versioned model/intermediate-representation specification for serialized computation graphs and associated model information.
- Treat the current upstream ONNX IR specification and schema sources as normative research sources for IR semantics and serialization structure. Re-check live sources before changing exact versioned rules.
- Distinguish IR version from operator-set versioning and other versioned specification surfaces; do not collapse them into one generic ONNX version number.
- Describe graphs, nodes/operators, values/types, initializers, metadata, functions, external-data references, and other structural concepts only to the level supported by the current upstream specification.
- Distinguish standard ONNX operator/schema semantics from implementation-specific or vendor extension behavior.
- Keep converter support, runtime/provider/operator compatibility, optimization behavior, hardware acceleration, implementation bugs, benchmarks, and dated performance/quality findings with their software/evidence/decision owners.
- Keep model-format selection/conversion pedagogy under `learning/areas/models/inference-and-generation/execution/model-formats-and-conversion/`.
- Do not infer semantic equivalence after conversion, runtime support, model quality, licensing, or workload fit merely because an artifact is valid ONNX.

## Validation

- Exact IR/operator/version claims are traceable to current upstream ONNX specification sources.
- The page does not become an ONNX Runtime compatibility guide or converter matrix.
- Successful serialization or validation is not presented as proof of execution support or semantic equivalence for a target runtime.
- ONNX serialization is not presented as changing or granting source-model licensing rights.
