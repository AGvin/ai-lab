# ComfyUI

ComfyUI is Comfy Organization Inc.'s open-source modular node-based generative-AI engine and application. Its graph workflow model supports controllable pipelines for images, video, 3D, audio, and other supported generative media.

## Workflow views

Node Graph mode exposes the workflow graph for direct editing. APP mode provides a simplified interface for a workflow's selected inputs and outputs, and a workflow can choose either view as its default. These are interaction views available independently of whether execution is local or hosted.

Menu layout is a separate setting. The current `Use new menu` documentation lists Top and Bottom positions; version-specific legacy layouts do not add another workflow interaction mode.

## Local and hosted boundary

ComfyUI can run locally or on user-controlled infrastructure, including offline core workflows. Current product surfaces also include optional Comfy Cloud and online/API nodes. Those hosted/API paths have separate network, credential, billing, and data-processing boundaries. Partner nodes can send the selected workflow inputs and model parameters to external providers.

Saved JSON workflows, templates, local API/backend operation, APP mode, and custom nodes make workflows reusable and embeddable. Custom nodes execute code with their own dependencies and access to the runtime environment. Workflow and template sources, model licenses, filesystem access, local API exposure, external credentials, and generated outputs therefore have distinct trust and data boundaries.

## Related

- [Comfy Organization Inc.](../../../../../../../producers/sub/c/sub/comfy-organization-inc/) — canonical producer organization.

## Official resources

- [ComfyUI documentation](https://docs.comfy.org/)
- [ComfyUI repository](https://github.com/Comfy-Org/ComfyUI)
- [Workflow templates](https://docs.comfy.org/interface/features/template)
- [ComfyUI](https://www.comfy.org/)
- [APP mode and default workflow view](https://docs.comfy.org/interface/app-mode)
- [Menu and interface settings](https://docs.comfy.org/interface/settings/comfy)
- [Comfy terms and partner-node processing](https://comfy.org/terms-of-service)
