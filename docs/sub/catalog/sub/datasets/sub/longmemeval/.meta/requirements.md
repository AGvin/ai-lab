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
