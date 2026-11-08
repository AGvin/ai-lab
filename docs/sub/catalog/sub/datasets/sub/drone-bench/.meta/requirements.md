# Documentation Requirements

## Requirements

- Identify Drone-Bench as Andon Labs' released benchmark for measuring AI agents' ability to write code for autonomous surveillance-style tasks on low-cost drone hardware, developed in the broader Project Pilot collaboration with Anthropic.
- Preserve the five-task boundary—reconstruction, localization, navigation, detection, and following—and the distinction between best-run capability, average reliability, and end-to-end success only while supported by current benchmark material.
- Treat office environment, held-out data, agent harness, iteration/feedback budget, cheating detection, baselines, hardware, scoring, model roster, and live results as freshness-sensitive.
- Keep Drone-Bench distinct from real-world drone products, model families, military capability claims, Project Pilot narrative, and generic robotics/autonomy concepts.
- Do not generalize benchmark performance into operational surveillance capability outside the benchmark's constrained environment and hardware.

## Validation

- The node remains the benchmark identity, not an autonomous-drone product.
- Capability statements remain scoped to the benchmark setup and reliability metric used.

## Scoped original-source qualification — 2026-11-08

- **Drone-Bench** is Andon Labs' 2026 research benchmark developed alongside the Anthropic **Project Pilot** study, testing a coding agent on **five separate steps** of a deliberately constrained indoor office drone scenario: reconstruction, localization, navigation, visual detection and following. Original benchmarks provide baseline outputs from upstream steps when testing the downstream task, so passing separate tasks does not establish reliable end-to-end autonomous surveillance.
- Each step is scored against the publisher's human-assisted baseline under a fixed iteration/feedback protocol (**ten submissions per run and ten runs per model**); best-run scores, average reliability and the compounded probability of completing all steps are distinct. The original project reports **no model surpassing the reconstruction baseline at its July 2026 review**; that historical statement is not a verified present-day capability ceiling. Human/privacy rights and physical flight safety remain critical and are not certified by the task.
- Publisher sources: https://andonlabs.com/evals/drone-bench ; https://www.anthropic.com/research/project-pilot .
- Scope: one pre-existing constrained research benchmark original source and task/iteration/reliability split only. No surveillance implementation or flight, personal-image reuse authority, independent physical safety/security/legal review, missing reader repair, whole-repo CI/render, clean or final acceptance.
