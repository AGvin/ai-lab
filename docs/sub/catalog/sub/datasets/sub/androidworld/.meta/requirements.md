# Documentation Requirements

## Requirements

- Identify AndroidWorld as the independently released **2024 Google DeepMind and Google Research dynamic Android-agent benchmarking environment**, with **116 reproducible task definitions across 20 Android applications**, a live Android emulator and parameterized task instantiation producing many distinct concrete task instances.
- Distinguish the **116 benchmark task templates** from dynamically generated combinations and the broader Android emulator/application ecosystem; do not report the potentially millions of task instances as millions of separately authored benchmark tasks.
- Preserve actual app state, emulator reset, task parameter seed, execution/action step budget and programmatic success/reward evaluator semantics for reproducibility. Upstream **2024-11-18 task step-limit updates** mean result comparisons must pin task/environment code revision and budget policy.
- Retain explicit Android SDK/emulator/ADB, app permissions, emulator images, OS architecture, network, optional experimental Docker execution and model agent wrapper prerequisites. Do not imply native Apple Silicon emulator/container compatibility without the documented AMD64 emulation limitations.
- Separate AndroidWorld from OSWorld desktop evaluations, BrowserGym/WebArena web-only evaluations, visual web tasks and mobile agent models; it is an evaluation artifact and executable environment, not a standalone hosted Android automation service.
- Attribute first-party benchmark research to the cross-affiliated Google DeepMind and Google Research team, with Google DeepMind as the selected canonical research producer and Google paper coauthors credited without inventing a separate service owner.
- Preserve its original released research identity, but keep ranking data, setup commands, Android version, task budgets, agent wrapper APIs, licences and current maintenance activity mutable and primary-source verified.

## Validation

- The 116 tasks / 20 app count applies to original published benchmark task definitions, not all generated task instances.
- Versioned task-step limits and emulator prerequisites are explicit for reproducible results.
- The `catalog/producers/g/google-deepmind` `produces` relation inverses AndroidWorld's `produced-by` link.

## Scoped original-source qualification — 2026-11-08

- **AndroidWorld** is Google DeepMind / Google Research's original **2024 Android emulator benchmark** for device-control agents, with **116 hand-crafted task definitions across 20 real applications** and many parameterized instances. These generated instances are not separate authored source benchmarks or evidence of millions of independently verified tasks.
- First-party docs require Android SDK/emulator images, app setup, agent model API, task/reset seeds, defined action budgets, and working accessibility/grpc interaction; **experimental Docker support** should not be described as production-ready or natively compatible with Apple Silicon. The environment evaluates live task completion, unlike Mind2Web's offline trajectories or OSWorld's desktop environments.
- First-party sources: https://github.com/google-research/android_world ; https://google-research.github.io/android_world/ ; original paper https://arxiv.org/abs/2405.14573
- Accepted bounded identity, original dataset/task definition and publisher-described execution/version requirements only. No emulator, model/API key use, task completion, independent safety/security/privacy/licensing audit, full repo schema/cache/CI/render, clean or final credit.
