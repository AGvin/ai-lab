# NV-Reason-CT

## Relations

- Series: [NV-Reason](../../../../)

## Model identity

NV-Reason-CT is NVIDIA's research vision-language model for native three-dimensional CT analysis, structured reports, question answering, and multi-step reasoning across chest and abdominal volumes. Its model card describes supervised fine-tuning followed by Group Relative Policy Optimization (GRPO). [Model card](https://huggingface.co/nvidia/NV-Reason-CT).

## Technical scope

| Aspect | Documented boundary |
| --- | --- |
| Architecture | Primus 3D vision transformer initialized from COLIPRI, coupled to a Qwen3.5-4B language-model component with 3D positional encoding. |
| Input | CT volumes in NIfTI form; the supplied processing path uses compressed `.nii.gz` inputs and anatomy-specific chest or abdomen preparation. |
| Training data | Structured question/answer data derived from CT-RATE, CancerVerse, and an internal NIH dataset, as described by NVIDIA. |
| Evaluation | CT-RATE and internal NIH evaluation splits; dataset corrections and anatomy-specific crop counts must follow the current card. |
| Inference | PyTorch and Transformers with model-specific processing code; NVIDIA lists H100 and L40S test hardware. |
| Model terms | OpenMDW-1.1 License. |

## Interpretation and use

NVIDIA restricts the intended use to research and education and excludes clinical diagnosis or treatment decisions. Outputs require qualified medical review. Users must have rights to the input scans and handle their identifying information appropriately.

The language-model component's nominal size is not the full multimodal parameter count or a memory estimate. CT-RATE classification and clinical-plausibility comparisons describe NVIDIA's stated data, thresholds, and test setup; they do not establish independent clinical validation or performance on another population. CXR-specific checkpoints, licenses, preprocessing, and results do not transfer to this model.

## Official resources

- [Official model card and files](https://huggingface.co/nvidia/NV-Reason-CT)
- [NVIDIA CT research introduction](https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/)
