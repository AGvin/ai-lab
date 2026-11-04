# VoxParity

**VoxParity** — voice-agent tool decisions influenced by acoustic cues.

## Data and evaluation boundary

The first-party release compares responses to paired original audio versus a transcript-only twin while matching tool name and typed arguments to gold actions without an LLM grader. The public development split, held-out item bank, resulting model runs and Inspect evaluator integration have distinct access and scoring boundaries.

The [pinned first-party source](https://github.com/bhavik-mangla/voxparity-bench/blob/b44deb05896f20824dbba29a386964b8ccaf3115/README.md) establishes the benchmark identity and version. Source data, trained models, scoring software, external service dependencies and leaderboard results are separate, version-dependent artifacts.

## Rights, limitations and safety

The pinned root LICENSE grants Apache-2.0 for covered code, while DATA_LICENSE grants CC BY 4.0 for covered audio/item data, runs and tables, with NOTICE listing third-party attribution. Voice examples can include sensitive emotional, child or caller-context signals; do not import private recordings or treat historical model rankings as fresh results.

This is a source-backed metadata profile only. No benchmark input, model run, generated program, audio recording, private data or unsafe code was executed or downloaded, and no repository-wide validation or complete rights audit was performed.

## Official source snapshot

- [Repository](https://github.com/bhavik-mangla/voxparity-bench)
- [Pinned README](https://github.com/bhavik-mangla/voxparity-bench/blob/b44deb05896f20824dbba29a386964b8ccaf3115/README.md)
- [Pinned LICENSE](https://github.com/bhavik-mangla/voxparity-bench/blob/b44deb05896f20824dbba29a386964b8ccaf3115/LICENSE)
- [Pinned DATA_LICENSE](https://github.com/bhavik-mangla/voxparity-bench/blob/b44deb05896f20824dbba29a386964b8ccaf3115/DATA_LICENSE)
