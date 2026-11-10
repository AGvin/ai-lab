# Documentation Requirements

## Requirements

- Treat **LongMemEval** as the original **2024** independently published 500-question benchmark for long-term conversational assistant memory, later ICLR 2025. Distinguish from **LongMemEval-V2** (2026, 451 different agent-trajectory questions), generic memory products, retriever/evaluator code and model leaderboard results.
- Identify five core abilities: information extraction, multi-session reasoning, knowledge updates, temporal reasoning and abstention; per-item task labels and evidence sessions vary.
- Preserve three source context settings: **LongMemEval_S** roughly 40 history sessions/115k tokens, **LongMemEval_M** roughly 500 history sessions, and an **oracle** variant containing only selected evidence sessions. Their 500 instances refer to task/configuration variants, not 1,500 independent questions.
- The upstream **September 2025 cleaned dataset** replaces noisy conversation-history sessions. It is a publisher revision of the original benchmark, not an independent new dataset identity or silently equivalent payload.
- Official original MIT repository license and the publisher-maintained Hugging Face cleaned card's MIT metadata are version/asset scoped, not an automatic grant for underlying ShareGPT/UltraChat filler text, third-party histories or commercial use of all possible source materials. Verify actual file/rights chain.
- Benchmark scores require pinned memory/retrieval pipeline, input context length, source revision, reader model and evaluation. Auto-evaluator implementations and publisher model claims are not independent AI Lab runtime verification.
- Original first-party paper names Di Wu and collaborators; do not invent a single legal organization producer from the GitHub username or affiliation. Preserve original provenance through source references without speculative canonical producer relation.

## Validation

- One original dataset node with reader, entity and requirements plus direct parent index link; no duplicate for 2025 cleaned edition.
- Link to independently materialized LongMemEval-V2 by reader without conflating the two source identities.
- Scoped branch file/diff verification does not count as full eight-root clean cycle, global schema/cache/CI/render or independent model evaluation.

## Scoped original-source qualification — 2026-11-08

- **LongMemEval** is the original **2024** memory benchmark with **500 questions** probing information extraction, multi-session reasoning, updates, temporal reasoning and abstention. Its short, medium and oracle histories are *context configurations*, not 1,500 distinct authored questions.
- The publisher's **2025 cleaned** conversation-history files supersede noisy original examples without creating another canonical benchmark. Keep original versus cleaned data revision, context length, evaluator and memory-model configuration pinned. The publisher's repository/cleaned card indicate MIT while background ShareGPT/UltraChat and other third-party conversation materials retain separate privacy and reuse rights.
- First-party sources: https://github.com/xiaowu0162/LongMemEval ; https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned ; https://xiaowu0162.github.io/long-mem-eval/ .
- Accepted only the already existing 2024 benchmark source and its 2025 correction; it is not LongMemEval-V2. No evaluator/model run, data redistribution or user-content rights guarantee, global schema/cache/CI/render, clean or final gate.
