# NoveltyBench

**NoveltyBench** — response diversity and utility across repeated text generations.

## Data and evaluation boundary

The pinned first-party release has curated and WildChat prompt sources. v1.0 uses a DeBERTa-based similarity classifier reading the first 128 tokens of each response plus a reward model; v1.1 uses full-response LLM judging for partition and scoring. Versions differ in model, budget, judgement, and coverage and are not directly comparable.

The [original publisher source](https://novelty-bench.github.io/) and [pinned publisher README](https://github.com/novelty-bench/novelty-bench/blob/64a23be6b18ec1dacc298830aab276061b6e143c/README.md) establish this specific release. Source data, evaluation software, model weights, scoring outputs and historical leaderboards are independently attributable.

## Rights, limitations and safety

The MIT source license does not automatically cover third-party WildChat inputs, model-generated responses or external judge providers. Scoring outcomes depend on model/version, prompt, generation settings and paid model APIs; no rankings were independently reproduced.

This is an evidence-backed metadata profile only. No benchmark inputs, model inference, untrusted code, audio, private data or security experiment was executed or downloaded. No complete rights audit or whole-repository CI was performed.

## Official source snapshot

- [Publisher source](https://novelty-bench.github.io/)
- [Repository](https://github.com/novelty-bench/novelty-bench)
- [Pinned README](https://github.com/novelty-bench/novelty-bench/blob/64a23be6b18ec1dacc298830aab276061b6e143c/README.md)
- [Pinned LICENSE](https://github.com/novelty-bench/novelty-bench/blob/64a23be6b18ec1dacc298830aab276061b6e143c/LICENSE)
