# NASA-IBM Lunar Foundation Model

NASA-IBM Lunar Foundation Model is a jointly released multimodal, multi-resolution foundation model for lunar remote sensing. Its current model card describes a ViT-B encoder-decoder pretrained from scratch on SomBench, with nearly two million co-registered lunar tile bundles spanning 11 modalities at two spatial scales: LROC NAC imagery at about 1 m/pixel and WAC-scale imagery at about 100 m/pixel. [NASA release](https://science.nasa.gov/science-research/artificial-intelligence-lunar-foundation-model/) [Model card](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model) [Technical paper](https://arxiv.org/abs/2609.13283)

## Identity and provenance

NASA and IBM jointly released the model in September 2026. The public checkpoint and the companion fine-tuning repository are released under Apache 2.0. The model adapts the TerraMind masked-token approach with explicit acquisition-geometry context, joint mixed-resolution pretraining, FlexiViT patch embeddings, and modality-wise tokenization. [IBM release](https://newsroom.ibm.com/2026-09-10-ibm-and-nasa-release-open-source-ai-model-to-support-lunar-exploration) [Model card](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model) [Fine-tuning repository](https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model)

## Decision and operating boundaries

- The released checkpoint is a reusable lunar representation intended for downstream adaptation such as crater detection, irregular-mare-patch segmentation, and ice-prospectivity regression. The separately published downstream task models are adaptations, not aliases of this pretrained identity. [Model card](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model)
- The model card supports qualitative any-to-any multimodal generation as a probe of learned cross-modal structure, but explicitly says generated fields are not calibrated scientific predictions. It also states that the model has no absolute geodetic reference frame and is not validated for operational decisions such as landing-site certification or hazard clearance. Evaluation does not cover other celestial bodies or products outside SomBench. [Model card](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model)
- NASA reports training on roughly two million tiles and multiple lunar missions, while the technical paper evaluates crater detection, irregular mare patch segmentation, and polar ice prospectivity. Source-reported gains are benchmark results, not locally reproduced measurements. [NASA release](https://science.nasa.gov/science-research/artificial-intelligence-lunar-foundation-model/) [Technical paper](https://arxiv.org/abs/2609.13283)
- Fine-tuning uses the companion TerraTorch integration. Match the checkpoint, configuration, modalities, preprocessing, and task data to the selected workflow; this catalog audit does not establish runtime compatibility, throughput, memory use, or downstream scientific validity. [Fine-tuning repository](https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model)

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [NASA](../../../../../producers/sub/n/sub/nasa/) — producer.

## Official resources

- <https://science.nasa.gov/science-research/artificial-intelligence-lunar-foundation-model/>
- <https://newsroom.ibm.com/2026-09-10-ibm-and-nasa-release-open-source-ai-model-to-support-lunar-exploration>
- <https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model>
- <https://arxiv.org/abs/2609.13283>
- <https://github.com/NASA-IMPACT/NASA-IBM-Lunar-Foundation-Model>
