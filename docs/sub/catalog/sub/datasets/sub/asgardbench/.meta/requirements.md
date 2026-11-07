# Documentation Requirements

## Requirements

- Present AsgardBench as Microsoft Research's benchmark for visually grounded interactive planning under minimal feedback in controlled embodied-task simulations.
- Preserve its distinguishing scope of 108 task instances across 12 task types, conditional scene variations, image-based observations, lightweight success/failure signals, and repeated plan adaptation.
- Keep navigation, low-level manipulation, simulator implementation, evaluated VLMs, and planning methods separate from the benchmark identity.
- Treat task variants, environment versions, evaluation protocols, and model results as freshness-sensitive.

## Validation

- AsgardBench remains a benchmark/dataset identity rather than a robotics planner or simulator product.
- Claims about visual-grounding effects remain experiment-scoped.

## Scoped original-source qualification — 2026-11-08

- **AsgardBench** is Microsoft Research's **March 2026** released AI2-THOR-based visually grounded interactive-planning benchmark: **108 task instances across 12 task types** and three home-scene types. It tests whether a vision-language agent revises a plan after visual observations with simple action success/failure feedback; navigation and low-level manipulation are deliberately abstracted away.
- The original public `microsoft/AsgardBench` repository distinguishes **108 full tasks** (`magt_benchmark`) from a separate **two-task installation sanity check** (`magt_benchmark_sanity`). It uses images, history and limited feedback, with only the first action of each proposed plan executed per step. Published visual-vs-text results depend on the tested model/API, controlled variants and source revision, not on demonstrated general-purpose robotics capability.
- First-party sources: https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning/ ; https://github.com/microsoft/AsgardBench ; https://microsoft.github.io/AsgardBench/
- Source qualification credits one existing dataset/benchmark identity with publisher-controlled 2026 methodology and task limits; it does not imply installed simulator testing, safe model API execution, all third-party asset rights, whole-repo CI/renderer, clean or final acceptance.
