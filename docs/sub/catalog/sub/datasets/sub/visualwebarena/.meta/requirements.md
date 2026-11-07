# Documentation Requirements

## Requirements

- Identify VisualWebArena as the separately published 2024 benchmark for multimodal autonomous web agents solving visually grounded website tasks, not a synonym for original text-oriented WebArena or general browser automation software.
- Record its independently maintained **910 visual tasks**, original 2024 release/research publication, reproducible self-hosted website/environment setup, evaluator configuration and visually meaningful success criteria, citing first-party benchmark documentation. Distinguish the 233 human-trajectories subset from the full 910-task evaluation corpus.
- Preserve vision-specific observation, image/media and website task semantics; do not assume WebArena's original 812 tasks, annotations v0.2.0, environment URLs, scoring comparability or browser baselines transfer unchanged to VisualWebArena.
- Treat 2024 released benchmark research and task corpus as a published evaluation artifact even though repository package versions, environments, and install instructions can change independently. A missing GitHub Release tag for the software package does not invalidate the public benchmark's original research release.
- Attribute benchmark maintenance to the original WebArena-x academic research project and named paper authors; keep VisualWebArena distinct from WebArena-Infinity, WebArena-Verified (ServiceNow), BrowserGym, OSWorld, and general multimodal agent model families.
- Keep benchmark scores, site/test subsets, evaluator model configurations, prompt/observation modes and infrastructure requirements version-sensitive and avoid direct cross-benchmark score comparisons without matched protocols.

## Validation

- Official repository and released research evidence establish this distinct 910-task multimodal benchmark.
- No duplicate WebArena family identity or inappropriate browser-runtime software classification is introduced.
- The producer `catalog/producers/w/webarena-x` has a reciprocal `produces` relation.

## Scoped original-source qualification — 2026-11-08

- **VisualWebArena** is the independently published **2024** multimodal web-agent task benchmark, with a first-party original release of **910 visually grounded website tasks**, distinct from WebArena's text-oriented 812-task setup. The publisher separately released **233 human trajectories** as an analysis subset; these are neither the total evaluation corpus nor a new independent benchmark.
- Its original repository explains reproducible self-hosted website resets and separate visually-grounded observation modes. Websites, screenshot/image observations, credentials, evaluator, generated task configuration and environment versions must match for comparable results; WebArena's scoring/version and BrowserGym are not interchangeable. Official task/runner availability and paper publication count as a research benchmark release even without a matching GitHub package-version tag.
- Original sources: https://github.com/web-arena-x/visualwebarena ; https://jykoh.com/vwa ; original study https://arxiv.org/abs/2401.13649
- Scope accepted: the existing original multimodal dataset identity, first-party published task inventory and distinct environment/evaluation contract. No self-hosted browser or multimodal model run, reproduction of success scores, complete third-party image/data rights assessment, whole-repository schema/cache/CI/render, clean or final credit.
