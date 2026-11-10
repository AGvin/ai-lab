# Documentation Requirements

## Requirements

- Identify Butter-Bench as Andon Labs' released evaluation of LLM-controlled robot systems on practical household/office delivery tasks.
- Preserve the high-level orchestrator versus low-level executor boundary; benchmark performance reflects the evaluated combined robot/agent system and must not automatically be attributed to the language model alone.
- Treat robot platform, task inventory, executor/controller, prompts/tools, trials, scoring, human baseline, leaderboard, physical environment, and model results as freshness-sensitive.
- Keep Butter-Bench distinct from Drone-Bench, robotics model families, robot simulators, and general physical-AI concepts.
- Attribute observed capability/failure modes to the exact benchmark configuration and model/robot stack.

## Validation

- The node remains a robotics benchmark rather than a robot product or trained robotics model.
- Combined-system results are not generalized to the underlying LLM alone.

## Scoped original-source qualification — 2026-11-08

- **Butter-Bench** is Andon Labs' original 2025 evaluation of a **physical low-cost robot controlled by an LLM** on a household/office butter-delivery scenario. The publisher splits the work into **six tasks**, including search, recognition of the refrigerated package, noticing the user has moved, awaiting a confirmed pickup, segmented spatial planning, and the end-to-end delivery-and-return within 15 minutes.
- The LLM serves as a higher-level orchestrator over a separately implemented low-level robot controller. Camera/environment sensing, movement delays, actuation and timeout/collision rules influence observed outcomes; benchmark results measure a **complete model–controller–physical-system configuration**, not a transferable score for the LLM alone or operational robot safety. Task scores, hardware/software stack, leaderboard and human baseline must be pinned to original experimental settings.
- Original publisher source: https://andonlabs.com/evals/butter-bench .
- Scope: one existing original robotics benchmark source and six-task/orchestration/reliability boundary only. No robot operation, human or physical safety certification, asset licensing/privacy/security/legal assessment, existing reader repair (reader is absent), global schema/cache/CI/render, clean or final gate.
