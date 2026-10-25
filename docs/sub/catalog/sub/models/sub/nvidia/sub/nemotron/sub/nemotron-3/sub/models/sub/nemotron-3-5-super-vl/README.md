# NVIDIA Nemotron 3.5 Super VL

NVIDIA Nemotron 3.5 Super VL is a released **post-trained vision-language model**, published on **October 15, 2026**, with **120B total / 12B active parameters**. The official weights use **OpenMDW-1.1** terms.

## Architecture and lineage

The model's source-explicit backbone initialization is from [Nemotron 3 Super Base](../nemotron-3-super-base/). NVIDIA separately describes distillation from **Ultra Base**; this teacher role is not equivalent to initializing from post-trained Ultra. The post-trained checkpoint is distinct from [Super VL Base](../nemotron-3-5-super-vl-base/), and the compressed [Nemotron 3.5 Bolt](../nemotron-3-5-bolt/) is a derivative of this checkpoint.

BF16 and NVFP4 are weight/deployment formats, not additional trained-model identities. Verify processor and runtime support, quality, memory and latency under the target workload; published benchmarks remain producer claims.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
