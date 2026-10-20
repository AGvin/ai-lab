# Stable Diffusion 3.5 Medium

Stable Diffusion 3.5 Medium is the 2.5-billion-parameter Medium model in Stability AI’s 3.5 series. Its model card describes the MMDiT-X architecture and a smaller-capacity deployment option than Large. Medium remains a separate trained model.

## Hardware and workload

Stability positions Medium for a wider range of hardware, but suitability depends on the full inference setup. Include text encoders, precision, runtime overhead, resolution and batch size when measuring memory. Provider memory examples that exclude encoders must not be presented as complete application requirements. Use the exact model card and artifact revision, and evaluate image quality for the intended prompts instead of inheriting Large’s results.

## Access and license

The official distribution uses Stability AI’s Community license with access-condition acceptance. Check revenue-dependent commercial eligibility and any Enterprise agreement requirement. Quantized or optimized packages retain this model’s lineage and can introduce artifact-specific conditions; they do not create a new original model or guarantee compatibility with every consumer GPU.

## Relations

- Member of: [Stable Diffusion 3.5](../../../../)

## Official resources

- [Series release](https://stability.ai/news/introducing-stable-diffusion-3-5)
- [Official documentation](https://stability.ai/core-models)
- [Official Medium model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
- [License program](https://stability.ai/license)
