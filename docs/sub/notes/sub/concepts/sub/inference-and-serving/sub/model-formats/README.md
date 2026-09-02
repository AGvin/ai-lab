# Model Formats

Legacy residual retained for concrete formal format definitions and mutable format/runtime/catalog evidence whose exact canonical owners are not yet materialized.

> **Migration note:** Practical format-selection/conversion pedagogy is now preserved in `docs/sub/learning/sub/areas/sub/models/sub/inference-and-generation/sub/execution/sub/model-formats-and-conversion/.meta/requirements.md`. Generic inference/runtime boundaries are preserved by canonical model-inference owners. The selected specification architecture assigns concrete formats to `docs/sub/catalog/sub/specifications/sub/formats/<concrete-format>/`, but that specification subtree is not yet materialized on the active AI Lab ref. Keep only the formal/mutable residual below until those exact owners exist; do not create a generic specification item named `model-formats`.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Formal format residual

The legacy source distinguished these concrete format roles:

- **Safetensors:** tensor serialization commonly used for model weights.
- **GGUF:** a self-contained model artifact format used by llama.cpp-compatible local runtimes and commonly carrying weights plus model/runtime metadata, including quantized representations.
- **ONNX:** a graph-exchange format intended for interoperable inference runtimes.
- **Framework checkpoints:** framework-specific checkpoint representations such as PyTorch or TensorFlow artifacts.

These descriptions remain migration source material only. Exact file structure, required metadata, supported data types/operators, versioned behavior, conformance, and other normative details must move to the applicable concrete format specification owner and be verified against its authoritative specification.

## Mutable catalog and evidence residual

Exact model/runtime/provider/hardware compatibility for a format, conversion-tool behavior and bugs, supported quantization variants, model-specific companion-file requirements, current software-version support, and dated performance/quality findings are mutable evidence/catalog facts rather than formal format identity or reusable learning truth.

License and redistribution obligations can also depend on the source model/artifact rather than the serialization format itself. Preserve those facts with the applicable model/artifact/source owner instead of inferring redistribution rights from the output format.

This residual remains until concrete format specification and applicable mutable catalog/evidence owners are materialized and reconciled.
