# Documentation Requirements

## Requirements

- Identify bitsandbytes as an independently released PyTorch-focused k-bit quantization library, with 8-bit optimizers, LLM.int8 inference and QLoRA 4-bit quantization workflows.
- Place it under `software/model-and-data-platforms/model-optimization-and-compilation` for the primary low-bit model/optimizer transformation role. QLoRA's fine-tuning use is an application of this library, not a reason to duplicate the same software as a training framework.
- Keep specific kernel backends, integer/float precision formats, LLM.int8, QLoRA, 8-bit optimizer modules, Hugging Face integrations, and upstream Python wheels as one canonical software identity unless independent released product boundaries emerge.
- Treat CPU/NVIDIA/AMD/Intel/Apple silicon support, driver/toolchain versions, architecture coverage, install availability and quantization/operator feature matrices as version- and platform-specific. Experimental support in a development branch must not be stated as stable release support.
- Do not transfer the compatibility and measured efficiency of one quantization mode to all devices, architectures, or model families.
- Attribute benchmarks and quality results to exact model, dataset, precision/method, backend, hardware, software build, and runtime conditions.
- Preserve present bitsandbytes Foundation maintenance provenance and distinguish original publication authorship.

## Validation

- The independent library identity is distinct from PyTorch itself, TorchAO, GGUF or other quantization formats, and trained model checkpoints.
- Release support boundaries are sourced from the exact stable version rather than just the default development branch.
- `produced-by` and `produces` relations are reciprocal.
