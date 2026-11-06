# MBPP

**MBPP** — entry-level Python program synthesis with unit tests.

## Data and evaluation boundary

The original Google Research source stores mbpp.jsonl alongside sanitized-mbpp.json. It documents the evaluation split by task IDs: 11–510 test, 1–10 prompting, 511–600 validation and 601–974 training. Code solutions and automated tests are dataset artifacts that must be kept out of model-visible evaluation prompts where relevant.

The [pinned first-party source](https://github.com/google-research/google-research/blob/83f1e7b59e762648c953de751d31f75720683622/mbpp/README.md) establishes the benchmark identity and version. Source data, trained models, scoring software, external service dependencies and leaderboard results are separate, version-dependent artifacts.

## Rights, limitations and safety

The root Google Research repository LICENSE is Apache-2.0 for covered material; any third-party dependency and code execution environment requires its own review. Generated Python is untrusted: isolate execution, limit resources/network, and prevent reference-solution or test leakage into prompts.

This is a source-backed metadata profile only. No benchmark input, model run, generated program, audio recording, private data or unsafe code was executed or downloaded, and no repository-wide validation or complete rights audit was performed.

## Official source snapshot

- [Repository](https://github.com/google-research/google-research)
- [Pinned README](https://github.com/google-research/google-research/blob/83f1e7b59e762648c953de751d31f75720683622/mbpp/README.md)
- [Pinned LICENSE](https://github.com/google-research/google-research/blob/83f1e7b59e762648c953de751d31f75720683622/LICENSE)
