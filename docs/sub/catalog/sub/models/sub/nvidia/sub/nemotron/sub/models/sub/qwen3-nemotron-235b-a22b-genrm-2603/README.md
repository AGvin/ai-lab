# Qwen3-Nemotron-235B-A22B-GenRM-2603

Qwen3-Nemotron-235B-A22B-GenRM-2603 is NVIDIA's separately released **generative reward checkpoint**, published on **March 11, 2026**. NVIDIA identifies **Qwen3-235B-A22B-Thinking-2507** as its fine-tuning foundation and describes its role in Super RLHF.

## Checkpoint boundaries

The **2603** release is a distinct trained model, not a mere service alias of the earlier [Qwen3-Nemotron GenRM](../qwen3-nemotron-235b-a22b-genrm/). Use as a reward evaluator does not prove backbone derivation of the Nemotron Super model, and membership does not establish a derivative edge between the two GenRM checkpoints. Its published weights use **Apache-2.0**.

Consult the exact model card for scoring interface and evaluate the intended training/evaluation workflow. Quantization, endpoint availability and hardware requirements are deployment concerns.

## Family and official source

- [Nemotron family](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/Qwen3-Nemotron-235B-A22B-GenRM-2603)
