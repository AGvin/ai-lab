# PRM800K

**PRM800K** is an OpenAI research dataset released on **May 31, 2023**, containing approximately **800,000 human step-level correctness labels** for generated mathematical solutions to problems from the original [MATH](../math/) corpus. It was published alongside the [*Let's Verify Step by Step* research](https://arxiv.org/abs/2305.20050) on training process reward models.

## Source and usage

PRM800K is **annotation/training data**, not a trained process reward model, another set of competition questions, or the separately curated [MATH-500](../math-500/) evaluation subset. The original OpenAI release includes human ratings on intermediate steps in model-generated reasoning trajectories. A positive label indicates a reasonable correct step, a negative label indicates an incorrect or unreasonable step, and a neutral label captures ambiguity or no clear progress. These ratings are not a guarantee of a mathematically correct final answer.

The [original repository](https://github.com/openai/prm800k) contains phase-1 and phase-2 train/test JSONL files tracked with **Git LFS**, plus the labelers' instructions. Pin the repository commit and data split, account for different phase sampling and any filtering of raw quality-control or uncertain labels. Its examples include pseudonymous labeler identifiers and timestamps; review data-handling needs before redistribution.

## Lifecycle and rights

The original OpenAI repository was **archived on May 29, 2026**, so it is read-only and not an actively maintained evaluation package. That does not erase its historical dataset release. Do not imply that results from a 2023 process reward model remain current or comparable to modern systems without rerunning the actual model/evaluation.

The repository's [MIT LICENSE](https://github.com/openai/prm800k/blob/main/LICENSE) grants rights to software and related documentation; it does not by itself prove complete redistribution rights for all underlying third-party MATH contest problems, human-labeled trajectories or external mirrors. Confirm source licenses, attribution and permitted use for the exact files before training, redistribution or commercial use. No independent dataset-rights audit, privacy certification or model execution was performed here.

## Relations

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)
- Derived from source problems: [MATH](../math/); separate original question authorship and OpenAI annotations

## Original resources

- [OpenAI May 2023 process-supervision release](https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/)
- [Original research paper](https://arxiv.org/abs/2305.20050)
- [Original OpenAI repository (archived)](https://github.com/openai/prm800k)
- [Original Git LFS data directory](https://github.com/openai/prm800k/tree/main/prm800k/data)
- [Original MIT code/documentation license](https://github.com/openai/prm800k/blob/main/LICENSE)
- [Original MATH research dataset](https://github.com/hendrycks/math)
