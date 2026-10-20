# NV-Reason-CXR-3B

## Relations

- Series: [NV-Reason](../../../../)

## Model identity

NV-Reason-CXR-3B is NVIDIA's chest-X-ray vision-language model for report generation, structured reasoning, and conversational analysis. The published model card describes a Qwen2.5-VL-3B-derived model trained with supervised fine-tuning and Group Relative Policy Optimization (GRPO). [Model card](https://huggingface.co/nvidia/NV-Reason-CXR-3B).

## Technical scope

| Aspect | Documented boundary |
| --- | --- |
| Input | Two-dimensional chest X-ray images, including frontal views, with text prompts; the card describes JPEG and PNG inputs. |
| Output | Generated reports, answers, and structured explanatory text. |
| Architecture | Qwen2.5-VL-derived vision-language model; the nominal 3B family/name is not a measured total runtime-memory requirement. |
| Data | The card identifies MIMIC-CXR, ChestXRay14, and CheXpert in its training/testing/evaluation overview. |
| Inference | PyTorch and Transformers on Linux; the card identifies A100, H100, and L40S test hardware. |
| Model terms | NVIDIA OneWay Non-Commercial License for academic research purposes. |

## Interpretation and use

The release is for research and education, with qualified medical review of outputs. NVIDIA explicitly excludes clinical diagnosis and treatment decisions. The license, input-data permissions, checkpoint, and supported software stack each need review for the actual use.

Published study and benchmark findings belong to the cited research and evaluation setup. They do not establish clinical clearance, independent medical validation, or transfer to other images and populations. NV-Reason-CT is a separate member with three-dimensional inputs and different terms.

## Official resources

- [Official model card and files](https://huggingface.co/nvidia/NV-Reason-CXR-3B)
- [NVIDIA radiology research introduction](https://developer.nvidia.com/blog/advancing-explainable-ai-in-radiology-research-with-nvidia-clara-reason/)
