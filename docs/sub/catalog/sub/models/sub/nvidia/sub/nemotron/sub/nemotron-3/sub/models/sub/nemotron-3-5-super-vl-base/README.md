# NVIDIA Nemotron 3.5 Super VL Base

NVIDIA Nemotron 3.5 Super VL Base is a separately released **pretrained vision-language checkpoint** for additional training, dated **October 15, 2026**. NVIDIA describes **120B total / 12B active parameters** and **OpenMDW-1.1** terms.

## Lineage and task boundaries

The released base checkpoint has source-explicit initialization from [Nemotron 3 Super Base](../nemotron-3-super-base/). NVIDIA also describes **Ultra Base teacher distillation**, which is different from backbone initialization; it must not be rewritten as derivation from post-trained Ultra. This base model remains distinct from the post-trained [Nemotron 3.5 Super VL](../nemotron-3-5-super-vl/) and does not inherit its behavior or benchmark results.

Pin checkpoint, processor and training/runtime configuration. Precision formats and serving packages do not define additional trained-model identities.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-Base-BF16)
