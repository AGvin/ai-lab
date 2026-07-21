# Model Formats

Model formats define how weights, metadata, tokenizer files, computation graphs, and configuration are stored and exchanged.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Common format roles

- **Safetensors:** a safe tensor serialization format commonly used for model weights.
- **GGUF:** a self-contained format used by llama.cpp-compatible local runtimes, often including quantized weights and metadata.
- **ONNX:** a graph-exchange format intended for interoperable inference runtimes.
- **Framework checkpoints:** formats tied to libraries such as PyTorch or TensorFlow.

## Core idea

A model repository often contains more than one file: weights, tokenizer vocabulary, architecture configuration, chat template, generation defaults, and optional adapters. Compatibility depends on all of them, not only the weight file extension.

## Practical use

Choose the format supported by the target runtime and hardware. Verify architecture support, tokenizer compatibility, quantization type, context configuration, and license before downloading or converting.

## Trade-offs and limitations

Conversion can lose metadata, introduce quantization changes, or produce a format unsupported by older runtimes. Self-contained formats simplify deployment but may duplicate large weight files across quantizations.

## Common mistakes

- Loading weights with the wrong tokenizer or chat template.
- Assuming every runtime supports every architecture in the same format.
- Treating a file extension as sufficient compatibility information.
- Redistributing converted weights without checking the source license.

## Related concepts

- [Inference and Serving](../../)
- [Model Loading](../model-loading/)
- [Quantization](../quantization/)
- [Adapters](../../../training-and-adaptation/sub/adapters/)
