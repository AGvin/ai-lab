# Model Formats

Legacy residual retained for concrete formal format definitions and mutable format/runtime/catalog evidence whose exact canonical owners are not yet materialized.

> **Migration note:** Practical format-selection/conversion pedagogy is preserved in `docs/sub/learning/sub/areas/sub/models/sub/inference-and-generation/sub/execution/sub/model-formats-and-conversion/.meta/requirements.md`. The selected specification hierarchy `docs/sub/catalog/sub/specifications/sub/formats/` is now materialized, and GGUF formal identity/specification requirements are preserved in `.../formats/sub/gguf/.meta/`. The remaining formal subjects below still lack exact materialized concrete-format owners. Do not create a generic specification item named `model-formats` merely to empty this residual.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Formal format residual

The remaining legacy source distinguishes these concrete format roles:

- **Safetensors:** tensor serialization commonly used for model weights.
- **ONNX:** a graph-exchange format intended for interoperable inference runtimes.
- **Framework checkpoints:** framework-specific checkpoint representations such as PyTorch or TensorFlow artifacts.

These descriptions remain migration source material only. Exact file structure, required metadata, supported data types/operators, versioned behavior, conformance, and other normative details must move to explicitly selected concrete format specification owners and be verified against their authoritative specifications.

GGUF is no longer part of this formal residual: its canonical specification owner is `catalog/specifications/formats/gguf/`, sourced from the upstream `ggml-org/ggml` GGUF specification.

## Mutable catalog and evidence residual

Exact model/runtime/provider/hardware compatibility for any format, conversion-tool behavior and bugs, supported quantization variants, model-specific companion-file requirements, current software-version support, and dated performance/quality findings are mutable evidence/catalog facts rather than formal format identity or reusable learning truth.

License and redistribution obligations can also depend on the source model/artifact rather than the serialization format itself. Preserve those facts with the applicable model/artifact/source owner instead of inferring redistribution rights from the output format.

This residual remains until the remaining concrete format specification and applicable mutable catalog/evidence owners are materialized and reconciled.
