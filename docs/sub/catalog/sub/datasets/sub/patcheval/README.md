# PatchEval

**PatchEval** — LLM-generated security patch correctness on isolated CVE cases.

## Data and evaluation boundary

The publisher differentiates the original 2025 benchmark from the 2026 PatchEval-Verified evaluation environments, with 230 CVE cases and Docker-based regression tests. Dataset case metadata, generated patches, built container images and evaluation adapters are distinct assets.

The [pinned first-party README](https://github.com/bytedance/PatchEval/blob/b43285cdde80cc04608d5f1178a330b740c91c2d/README.md) is the identity and version source. Data, benchmark tasks, evaluator software, trained models and published leaderboards must be attributed separately.

## Rights, limitations and safety

Root Apache-2.0 does not override the third-party licenses for underlying vulnerable projects, patches or container contents. Evaluate solely in authorized isolated systems with network isolation and explicit resource limits. Benchmark repair success is not production security assurance.

No exploit, vulnerable image, PoC, generated patch or container execution was performed. No complete rights audit or repository-wide validation was run.

## Official source snapshot

- [Repository](https://github.com/bytedance/PatchEval)
- [Pinned README](https://github.com/bytedance/PatchEval/blob/b43285cdde80cc04608d5f1178a330b740c91c2d/README.md)
- [Pinned LICENSE](https://github.com/bytedance/PatchEval/blob/b43285cdde80cc04608d5f1178a330b740c91c2d/LICENSE)
