# NVIDIA Nemotron 3 Nano Omni

**NVIDIA Nemotron 3 Nano Omni** is a separately released **multimodal** hybrid Mamba-2/Transformer Mixture-of-Experts model with approximately **31 billion total / 3 billion active parameters**, published **April 28, 2026** under the **NVIDIA Open Model Agreement**. It supports **video, audio, image and text inputs**, produces **text output**, and advertises up to **256K tokens of context**. It is not a quantized or renamed text-only Nano checkpoint.

## Architecture, provenance and use

Omni uses the **post-trained Nemotron 3 Nano 30B-A3B** as its language backbone, connected through projectors to the **C-RADIOv4-H** vision encoder and **Parakeet-TDT** audio encoder. These encoder components and other models used to improve training data are not interchangeable with Omni's language-backbone parent or independent Omni releases. The separately published **Nano Base** pretrained checkpoint is *not* the Omni backbone.

NVIDIA documents video and speech understanding, transcription, document intelligence, OCR and GUI/agent scenarios. Published BF16, FP8 and NVFP4 weight variants are alternate deployment formats of the same trained Omni identity; GPU fit, multimodal preprocessing, video/audio limits, model context and throughput depend on exact serving software and hardware. Published performance results and suitability claims are from NVIDIA, not reproduced AI Lab benchmarks. The model's repository uses custom model code; review and pin that code before executing it in a trusted deployment.

## Translations

- English

## Relations

- [Nemotron 3 model series](../../../../)
- [Nemotron 3 Nano language-backbone parent](../nemotron-3-nano/)
- [Nano Base pretrained checkpoint — different training stage](../nemotron-3-nano-base/)

## Official resources

- [NVIDIA Nano Omni BF16 checkpoint and model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)
- [NVIDIA Nano Omni NVFP4 format](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4)
- [NVIDIA Nemotron model overview](https://developer.nvidia.com/topics/ai/nemotron)
- [NVIDIA Nano Omni technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf)
