# GLM-5.3-Flash

**GLM-5.3-Flash** is the natively multimodal GLM-5 model released by Z.AI on **August 27, 2026**. It has a newly trained base, distinct from the post-trained GLM-5.3 checkpoint that shares GLM-5.2's base.

## Canonical profile

- **Architecture:** hybrid sparse-plus-linear attention with Manifold-Constrained Hyper-Connections, in a Mixture-of-Experts design.
- **Scale:** **320B total / 18B active** parameters, as reported by Z.AI.
- **Modalities:** trained on text and visual information, including image and video inputs. Supported formats and output limits depend on the implementation.
- **Context:** Z.AI describes a maximum of **1M tokens**; this is not an independently verified deployment result.
- **Published weights:** the official checkpoint is **MIT licensed**. FP8 and BF16 weight formats are deployment artifacts rather than separate learned models.

## Evidence and use

Claims about speed, memory efficiency, capability rankings and benchmark improvements come from the producer; AI Lab has not reproduced them. Specific inference frameworks, hardware, serving capacity and context settings need runtime validation. Hosted API pricing, quotas, products and availability are separate service properties.

## Translations

- English

## Relations

- Member of: [GLM family](../../../../)

## Official resources

- [Model and license](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [Official Z.AI launch](https://autoclaw.z.ai/blog/model/glm-5.3-flash/)
- [GLM-5 series model repository](https://github.com/zai-org/GLM-5)
