# LongMemEval-V2

**LongMemEval-V2 (LME-V2)** is a released 2026 benchmark for whether AI-agent memory can recover useful knowledge about customized environments after many prior trajectories. The [original paper](https://arxiv.org/abs/2605.12493) and [project](https://xiaowu0162.github.io/longmemeval-v2/) introduce it as a benchmark of memory for experienced web agents, not as an agent model, production memory server or live browser test.

## Dataset and task boundary

The [publisher's dataset card](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2/blob/main/DATA_CARD.md) identifies **451 manually curated questions** and **1,870 trajectories** in custom web and synthetic enterprise environments. Questions test five capabilities: **static-state recall, dynamic-state tracking, workflow knowledge, environment gotchas, and premise awareness**. Each evaluation haystack can include up to **500 trajectories** and, in the largest cases, about **115 million tokens**. Small and medium tiers, screenshot bundles, dataset versions and model/reader setup change the cost and evaluation setting.

This is **not** the [original LongMemEval (2024)](https://github.com/xiaowu0162/LongMemEval), which tests long-term conversational memory over **500 questions** from user/assistant sessions. V2 has a separately released 2026 paper, repository and trajectory/question corpus; it is also distinct from evaluation harness code, AgentRunbook baselines, and Hindsight/Graphiti/Mem0 agent-memory software or services.

## Interpretation, rights and operational limits

The [publisher data card](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2/blob/main/DATA_CARD.md) declares **Apache-2.0** for the released dataset and describes benchmark-generated, not real-account, user and enterprise records. The [source repository](https://github.com/xiaowu0162/LongMemEval-V2) includes an Apache-2.0 license for distributed code. This is not independent rights clearance for any third-party screenshots or assets, or unrestricted permission for external models and commercial datasets.

Results are sensitive to the reader model, retrieved context budget, embedding configuration, candidate memory backend, task mix and latency. Publisher performance experiments have **not** been independently reproduced by AI Lab. The benchmark does not prove production tenant isolation, retention/deletion behavior, safe prompt handling or generalization beyond its custom environments.

## Original resources

- [LongMemEval-V2 project and data overview](https://xiaowu0162.github.io/longmemeval-v2/)
- [Original LongMemEval-V2 paper](https://arxiv.org/abs/2605.12493)
- [First-party source and evaluation harness](https://github.com/xiaowu0162/LongMemEval-V2)
- [Original dataset distribution](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2)
- [Publisher data card, licensing and limitations](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2/blob/main/DATA_CARD.md)
- [Original LongMemEval conversational benchmark (different dataset)](https://github.com/xiaowu0162/LongMemEval)
