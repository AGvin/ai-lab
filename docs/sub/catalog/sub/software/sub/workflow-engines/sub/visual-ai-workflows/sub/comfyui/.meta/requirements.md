# Documentation Requirements

## Requirements

- Identify ComfyUI as Comfy Organization Inc.'s open-source modular node-based generative-AI engine/application and visual workflow environment.
- Preserve the current broader creation boundary: workflows can compose models and operations for images, video, 3D, audio, and other supported generative media rather than only image generation.
- Preserve local/self-managed execution as the software identity while distinguishing optional first-party Comfy Cloud and online/API-node services as separate hosted processing surfaces.
- Explain the two current workflow interaction views supported by official documentation: Node Graph mode for direct graph editing and APP mode for a simplified workflow-specific input/output interface.
- Explain that a workflow can choose APP mode or Node Graph mode as its default view while current upstream support retains that behavior.
- Treat the new-versus-old menu setting as an interface-version/compatibility option rather than a third workflow mode; do not conflate it with Node Graph versus APP mode.
- Distinguish workflow interaction views from distribution/operating surfaces such as local self-hosted installs and Comfy Cloud.
- Preserve durable workflow surfaces: node graph, saved JSON workflows, templates, local API/backend operation, APP mode, custom nodes, model paths, and production/API integration at a stable level.
- Preserve useful legacy trust boundaries around custom-node provenance and executable dependencies, workflow/template provenance, model sources/licenses, local API/network exposure, filesystem/model access, external API-node credentials, cloud data paths, and generated outputs.
- Make clear that core/local execution can run offline while explicitly selected online/API/cloud nodes have separate network/data boundaries.
- Keep exact supported model lists, hardware backends, installation packages, platform availability, cloud pricing/limits, interface-version details, and other mutable details source-backed when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official documentation and repository.

## Validation

- ComfyUI remains a Visual AI Workflow Engine software identity despite optional Comfy Cloud availability.
- The profile is not restricted to Stable Diffusion or image-only workflows.
- Node Graph mode and APP mode are presented as workflow interaction views, while the new-versus-old menu setting is presented separately as a compatibility/interface option.
- APP mode is not conflated with Comfy Cloud or another hosted execution surface.
- Custom nodes are treated as independently trusted executable extensions.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
