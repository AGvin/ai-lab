# NV-Reason

## Relations

- Models: [NV-Reason-CT](sub/models/sub/nv-reason-ct/)
- Models: [NV-Reason-CXR-3B](sub/models/sub/nv-reason-cxr-3b/)
- Produced by: [NVIDIA](../../../../../producers/sub/n/sub/nvidia/)

## Series purpose

NV-Reason is NVIDIA's radiology reasoning model series. Its represented members address different medical-imaging inputs: NV-Reason-CXR-3B works with chest X-rays, while NV-Reason-CT processes native three-dimensional CT volumes. NVIDIA introduces these models within its wider Clara and Medical AI ecosystem; the ecosystem branding and the trained-model series are different scopes. [Radiology research overview](https://developer.nvidia.com/blog/advancing-explainable-ai-in-radiology-research-with-nvidia-clara-reason/); [CT model introduction](https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/).

## Member-specific boundaries

The member profiles own architecture, parameter structure, input preparation, training data, license, checkpoint, runtime, and evaluation details. CXR and CT are not interchangeable input modes of one checkpoint. Their model-use licenses differ and must be read at the concrete-model level.

NVIDIA positions the models for research and development. Generated reports, answers, and reasoning require appropriate expert review; neither the series identity nor a published benchmark establishes an autonomous diagnostic product or clinical clearance. Model-reported reasoning is generated output, not independent evidence that its explanation is correct.

Use each linked member's model card for the current release and supported inference path. Hardware guidance, model-card revisions, dataset scope, medical-use restrictions, and reported results must remain attached to that member and evaluation configuration.

## Official resources

- [Radiology research overview](https://developer.nvidia.com/blog/advancing-explainable-ai-in-radiology-research-with-nvidia-clara-reason/)
- [NV-Reason-CT introduction](https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/)
