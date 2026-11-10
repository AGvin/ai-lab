# Qwen3-Nemotron-235B-A22B-GenRM

Qwen3-Nemotron-235B-A22B-GenRM is NVIDIA's separately released **generative reward model**, published on **December 15, 2025**. NVIDIA describes it as fine-tuned from **Qwen3-235B-A22B-Thinking-2507** to evaluate and rank candidate assistant responses, including use in Nemotron Nano RLHF.

## Training and evaluation boundaries

This is a **reward evaluator**, not a general Nemotron chat checkpoint or evidence that Nano uses its weights as the language-model backbone. The Qwen foundation is identified textually; do not infer additional canonical derivative edges. The published checkpoint uses **Apache-2.0**. Scoring behavior, evaluations and training recipes are source-scoped.

Hardware support, quantization, provider endpoints and serving performance require runtime-specific testing; this catalog does not validate hosted or local execution.

## Family and official source

- [Nemotron family](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/Qwen3-Nemotron-235B-A22B-GenRM)
