# Documentation Requirements

## Requirements

- Identify Megatron Bridge, also called NeMo Megatron Bridge, as the independently packaged PyTorch-native training and Hugging Face/Megatron interoperability library installed as megatron-bridge and imported through megatron.bridge.
- Place it under Model Development: pretraining, supervised fine-tuning, LoRA/PEFT, custom training loops and recipes are its primary training-toolchain role, with bidirectional checkpoint conversion and verification.
- Keep Megatron Core, the Megatron-LM reference implementation, the NeMo umbrella, NeMo RL and deployment engines separate. Use of Bridge inside another project's reinforcement-learning workflow does not make all of that project's RL capabilities native Bridge features.
- Preserve NVIDIA producer provenance from package author/maintainer metadata. Retain the README's acknowledgement that the project continues MBridge by Yan Bai; this lineage does not imply exclusive NVIDIA authorship or require another standalone MBridge node.
- Distinguish architecture/configuration loading for random-initialized pretraining from conversion of pretrained weights. Import/export paths, tokenizer/configuration assets, precision and model-specific mappings require the relevant verification workflow.
- Treat supported model/variant lists and deprecation notices, Python/PyTorch/CUDA/Transformers versions, Megatron Core revision, optional dependencies, distributed configuration, checkpoint formats and container tags as release-sensitive.
- Preserve the package's Production/Stable classifier while keeping experimental main/dev features separate. Source installations pin compatible Core revisions; a development-branch example is not a promise of support in every tagged release.
- Scope performance results to exact model, hardware, topology, precision, batch/sequence settings and software stack. Do not promise universal conversion equivalence or universal model support.
- Render the standard entity-relations block from validated current-entity relations and include official project, package, documentation and migration references.

## Validation

- Megatron Bridge remains its own training/conversion library rather than a duplicate of Core, Megatron-LM, NeMo RL or a serving engine.
- Current producer attribution and predecessor acknowledgement are both preserved.
- The NVIDIA producer edge is reciprocal and every rendered destination resolves.
