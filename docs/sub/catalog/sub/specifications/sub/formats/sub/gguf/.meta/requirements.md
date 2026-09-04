# Documentation Requirements

## Requirements

- Present GGUF as the upstream GGML model file format for storing models for inference with GGML and GGML-based executors, and identify it as the successor to the earlier GGML/GGMF/GGJT file-format line according to the upstream specification.
- Treat the upstream `ggml-org/ggml/docs/gguf.md` document as the normative research source. Re-check the live upstream specification before changing exact versioned fields/rules; do not infer current normative behavior from legacy AI Lab prose or runtime implementation behavior alone.
- Explain the format's upstream design goals at the specification level: single-file deployment, extensibility, memory-mapping friendliness, ease of implementation/reading, and carrying the information needed to load the model without relying on an external untyped hyperparameter list.
- Explain that GGUF uses typed key-value metadata to describe model/general information and extensible attributes, separating that metadata structure from tensor payloads and tensor metadata.
- Describe the file at a specification-oriented structural level: GGUF magic and structural version in the header, tensor and metadata entry counts, typed metadata key-value entries, tensor descriptors, required padding/alignment before tensor data, and the tensor data region.
- Record structural-version claims only from the current upstream specification. At the migration snapshot the upstream document describes structural version `3`; make clear that structural version changes are a specification concern and that non-structural evolution may occur through metadata without requiring a new file-structure version.
- Preserve the upstream alignment contract: tensor data alignment is governed by `general.alignment`; writers/readers must follow the specification's padding rules, and the current upstream document defines a default alignment when the metadata key is absent. Exact numeric defaults/constraints must remain source-backed and be re-checked when the upstream spec changes.
- Preserve the upstream endianness boundary: byte order is part of the file-format contract and must be interpreted according to the active specification/version rather than host assumptions. Do not turn runtime-specific byte-swapping behavior into GGUF normative truth.
- Distinguish tensor data type/encoding from the separate GGUF quantization-version metadata contract. When documenting quantized tensors, source required metadata and supported type identifiers from the current upstream specification rather than copying a point-in-time enum as timeless prose.
- Treat GGUF metadata keys as versioned/extensible specification vocabulary. Separate required/general keys, architecture-specific keys, tokenizer/model metadata, and optional/recommended metadata according to the upstream contract; do not assume arbitrary runtime metadata is normative GGUF vocabulary.
- Cover the upstream GGUF naming convention only as the specification describes it: a human-oriented convention for conveying important model/file attributes, not a guarantee that every historical/community filename is perfectly machine-parseable.
- Keep formal GGUF identity and normative file/metadata rules here; keep model-format selection/conversion pedagogy under `learning/areas/models/inference-and-generation/execution/model-formats-and-conversion/`.
- Keep concrete llama.cpp/other runtime feature support, implementation limitations, version-specific compatibility, converter bugs, device support, benchmarks, and performance/quality findings with their applicable software/evidence/decision owners.
- Do not infer model license, redistribution rights, model quality, architecture support, tokenizer compatibility, or practical workload fit merely from the fact that an artifact is encoded as GGUF.

## Validation

- Every exact normative field, default, type identifier, alignment rule, or structural-version statement is traceable to the current upstream GGUF specification.
- The page does not become a llama.cpp compatibility matrix or model-selection guide.
- Format validity is not presented as proof that a particular model/runtime combination is supported or performs acceptably.
- GGUF serialization is not presented as changing or granting the source model/artifact license.
- The learning node owns how to choose/convert/validate formats; this specification node owns what GGUF formally is.
