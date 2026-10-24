# Documentation Requirements

## Requirements

- Use the PyTorch Project as the direct project-level producer identity for PyTorch, ExecuTorch and TorchAO while preserving their distinct model-development, inference-runtime, and optimization/library identities.
- Do not infer a corporate producer solely from contributor, foundation, or historical stewardship relationships unless a separate current provenance relation is required and authoritatively sourced.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The PyTorch, ExecuTorch and TorchAO `produced-by` relations are reciprocated by this project's `produces` links.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

PyTorch Project is the open-source project identity behind the represented PyTorch, ExecuTorch and TorchAO software. PyTorch provides tensor and model-development infrastructure, ExecuTorch targets edge inference, and TorchAO provides model optimization and quantization tools. The PyTorch Foundation supplies a vendor-neutral home hosted by the Linux Foundation; foundation stewardship is distinct from project and contributor authorship. [PyTorch](https://github.com/pytorch/pytorch) · [ExecuTorch](https://github.com/pytorch/executorch) · [TorchAO](https://github.com/pytorch/ao) · [Foundation](https://pytorch.org/foundation/).

Select the framework, optimization path and device runtime together with the target model. A framework's software license does not license downloaded model weights, guarantee that a quantization method supports every architecture or establish compatibility with every accelerator. Pin the relevant software and backend versions and validate the intended execution path. [PyTorch](https://github.com/pytorch/pytorch) · [ExecuTorch](https://github.com/pytorch/executorch) · [TorchAO](https://github.com/pytorch/ao).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
