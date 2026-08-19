# ComfyUI

ComfyUI is Comfy Organization Inc.'s open-source modular node-based generative-AI engine and application. Its visual workflow model supports controllable pipelines for images, video, 3D, audio, and other supported generative media.

## Workflow interface

ComfyUI's primary workflow views are **Node Graph mode** and **APP mode**. Node Graph mode exposes the graph directly for building and editing workflows. APP mode lets a workflow define a simpler input/output interface so it can be run or shared without requiring users to edit nodes; a workflow can also choose APP mode or Node Graph mode as its default view.

The frontend's **new menu** and **old menu** setting is a separate interface-compatibility choice, not another workflow mode. The new interface is the current default, while the old menu remains available as a compatibility option.

Saved JSON workflows, built-in templates, local API/backend operation, custom nodes, model paths, and production/API integration make workflows reusable beyond interactive graph editing.

## Local and hosted boundary

ComfyUI can run locally or on user-controlled infrastructure, including offline core workflows. Comfy Cloud is the official hosted version and is a separate operating surface; online/API nodes likewise introduce their own network, credential, billing, and data-processing boundaries even when invoked from the same workflow environment.

Custom nodes are executable extensions with their own dependencies and provenance, so review them independently. Also review workflow/template sources, model licenses, local API exposure, filesystem/model access, external API credentials, cloud data paths, and generated outputs.

## Related

- [Comfy Organization Inc.](../../../../../../../producers/sub/c/sub/comfy-organization-inc/) — canonical producer organization.

## Official resources

- [ComfyUI documentation](https://docs.comfy.org/)
- [APP mode guide](https://docs.comfy.org/interface/app-mode)
- [ComfyUI repository](https://github.com/Comfy-Org/ComfyUI)
- [Workflow templates](https://docs.comfy.org/interface/features/template)
