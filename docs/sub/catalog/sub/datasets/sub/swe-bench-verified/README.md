# SWE-bench Verified

SWE-bench Verified is the human-reviewed **500-task subset** of [SWE-bench](../swe-bench/) for issue-to-patch software engineering evaluation. The [2024 release](https://openai.com/index/introducing-swe-bench-verified/) was curated jointly by OpenAI and the original SWE-bench researchers. It involved 93 professional developers screening 1,699 candidates, with three independent reviews per task.

## Historical availability versus current suitability

**Do not treat Verified as a reliable frontier coding-progress benchmark.** In [February 2026](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), OpenAI stopped reporting Verified scores due to public-data contamination and tests that reject correct patches. It found material defects in 59.4% of a **nonrandom group of 138 tasks** that o3 had not consistently solved across 64 independent runs. That result is not an estimated failure rate for all 500 tasks.

In February OpenAI recommended SWE-bench Pro instead, but in [July 2026](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) it **retracted that recommendation** after reviewing the earlier **731-task Pro V1 public split**. The July findings do not automatically validate or invalidate the later [September Pro V2 release](../swe-bench-pro/). These historical recommendations are not current endorsements.

Verified remains useful for reproducing earlier studies and investigating benchmark quality, with explicit contamination and test limitations.

## Dataset boundary and evaluation

The [SWE-bench-maintained Verified distribution](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified) packages selected tasks from public GitHub issue/PR histories. The subset is distinct from the original family, its Lite/Multimodal variants, runner/harness, Docker images, and Scale AI's separate Pro dataset.

For reproducibility, pin the exact dataset revision, issue/base commit, test setup, environment, model, agent/scaffold, prompts and verifier. Public issue and patch availability may contaminate training; narrow or mismatched tests may reject correct submissions. This profile contains no independently reproduced model scores.

## Licensing and provenance

The original [SWE-bench repository LICENSE](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE) is MIT for source software/documentation, not proven universal clearance for original third-party issues, source repositories, patches and tests. The reviewed Verified Hub card did not state an explicit standalone data license. OpenAI jointly curated this subset; it is not the sole producer of original SWE-bench tasks. Indirect ownership and sanctions status were not audited.

## Relations

- Derived from: [SWE-bench](../swe-bench/).
- Jointly curated by: [OpenAI](../../../producers/sub/o/sub/openai/).

## Primary sources

- [2024 Verified creation](https://openai.com/index/introducing-swe-bench-verified/)
- [Official Verified dataset](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)
- [Original SWE-bench repository](https://github.com/SWE-bench/SWE-bench)
- [February 2026 Verified audit](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [July 2026 Pro audit and retraction](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)
- [Original repository license](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE)
