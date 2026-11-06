# NVIDIA Nemotron 3.5 Bolt

NVIDIA Nemotron 3.5 Bolt is a separately released **compressed and further-trained derivative** of [Nemotron 3.5 Super VL](../nemotron-3-5-super-vl/), published on **October 15, 2026**. NVIDIA identifies **74B total / 9B active parameters** and **OpenMDW-1.1** release terms.

## Model, artifacts and dependent drafter

Bolt is one trained model across BF16, quantized 24GB and GGUF serving artifacts. The advertised **24GB** configuration is specific to its released artifact, runtime and workload—not a guarantee that BF16 weights or arbitrary context sizes fit 24GB.

The separately trained **LiLiCorr speculative-decoding drafter** is a dependent component, not another Bolt alias or standalone replacement. NVIDIA sources report differently scoped parameter counts (673.5M in Hugging Face metadata; 1.113B in model-card review excluding shared target embeddings/head); these must not be conflated or promoted to one reconciled identity without further review.

Pin the exact weights and supported runtime; test multimodal quality, memory and latency.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-BF16)
