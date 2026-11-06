# LongMemEval

**LongMemEval** is the original 2024 [long-term conversational memory benchmark](https://github.com/xiaowu0162/LongMemEval) by Di Wu and collaborators, later published at ICLR 2025. It tests whether chat assistants can retain and retrieve facts over many previous sessions with **500 curated questions**. Its five core abilities are information extraction, multi-session reasoning, knowledge updates, temporal reasoning and abstention.

## Dataset revisions and evaluation settings

The project provides **LongMemEval_S** (roughly 40 sessions, about 115k concatenated tokens), **LongMemEval_M** (roughly 500 sessions), and an **oracle** history variant containing only relevant evidence. These variants reuse the benchmark's 500 evaluation instances under different history lengths or retrieval assumptions; do not report them as 1,500 separately authored questions.

The authors [published cleaned history files in September 2025](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) to remove sessions that interfered with answer correctness. The publisher describes this as replacing the original data, **not a new independent benchmark**. Pin clean/original release, reader model, memory access mode and scoring protocol before comparing results.

This is also distinct from [LongMemEval-V2](../longmemeval-v2/), which was separately released in 2026 for web/enterprise agent-trajectory memory with 451 questions, rather than simulated conversational history.

## Licensing, data safety and limitations

The [original code repository](https://github.com/xiaowu0162/LongMemEval/blob/main/LICENSE) is MIT licensed, and the [publisher-managed cleaned dataset card](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) declares MIT. Underlying conversation fillers or examples can be derived from ShareGPT, UltraChat and other sources; those origin rights, privacy and redistribution restrictions are not independently cleared by the repository code license. Verify actual dataset files and downstream data permissions, especially for commercial use.

AI Lab has not independently downloaded or executed the evaluator, reproduced model rankings, inspected all individual dialogue rows or audited third-party corpus rights.

## Original resources

- [LongMemEval original repository](https://github.com/xiaowu0162/LongMemEval)
- [Project homepage](https://xiaowu0162.github.io/long-mem-eval/)
- [Original 2024 paper](https://arxiv.org/abs/2410.10813)
- [Publisher cleaned dataset revision (2025)](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned)
- [Original repository MIT license](https://github.com/xiaowu0162/LongMemEval/blob/main/LICENSE)
- [LongMemEval-V2 source (separate 2026 benchmark)](https://github.com/xiaowu0162/LongMemEval-V2)
