# scBench

**scBench** — reproducible single-cell RNA-seq analysis tasks for AI agents.

## Data and evaluation boundary

The publisher reports 195 tasks over six platform labels and six analysis categories. Six example task specifications are released; the full test corpus is withheld to reduce contamination. Each task combines an AnnData snapshot, prompt and deterministic output grading, separate from the agent harness and benchmark leaderboard.

The [pinned first-party source](https://github.com/latchbio/scbench/blob/370a68ca042133fb463748295f955b1b8b58f4a0/README.md) establishes the identity and release scope. Related model outputs, scoring programs, downloaded task materials and historical leaderboard measurements remain separate artifacts.

## Rights, limitations and safety

The Apache-2.0 repository license does not establish rights or patient-data consent for every underlying biological AnnData source. Data provenance, de-identification and independent clinical/scientific validation are required before reuse. The publisher's benchmark results are not independently reproduced.

No benchmark datasets were downloaded and no evaluator, model, untrusted code, harmful safety prompt or physical experiment was executed. No full rights audit or repository-wide CI was run.

## Official source snapshot

- [Repository](https://github.com/latchbio/scbench)
- [Pinned README](https://github.com/latchbio/scbench/blob/370a68ca042133fb463748295f955b1b8b58f4a0/README.md)
- [Pinned LICENSE](https://github.com/latchbio/scbench/blob/370a68ca042133fb463748295f955b1b8b58f4a0/LICENSE)
