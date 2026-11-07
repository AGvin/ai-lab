# Documentation Requirements

## Requirements

- Present GroundedPlanBench as the released benchmark for spatially grounded long-horizon task planning in robot manipulation scenarios.
- Preserve its distinguishing scope of 1,009 tasks derived from 308 DROID scenes, explicit/implicit instruction variants, and action-location grounding for grasp/place/open/close planning.
- Keep V2GP training methodology, DROID source data, robot hardware, evaluated VLMs, and real-world validation experiments separate from the benchmark identity.
- Treat task inventory, annotations, evaluation protocol, and reported model results as freshness-sensitive.

## Validation

- GroundedPlanBench remains a benchmark/dataset identity rather than the V2GP method or a robot-planning product.

## Scoped original-source qualification — 2026-11-08

- **GroundedPlanBench** is the **2026-03-26** Microsoft Research/coauthor release for spatially grounded long-horizon robot action planning. Its **1,009 benchmark tasks** derive from **308 selected DROID robot-manipulation scenes**; explicit and implicit instructions are distinct forms of task wording, with short/medium/long action horizons of **345/381/283** tasks.
- The benchmark evaluates an ordered plan and spatial target boxes/points for **grasp, place, open and close** primitives; correctness includes both sequence and location. The separately trained **V2GP** procedure, its 43K generated training plans, upstream DROID recordings, trained VLMs and authors' physical robot experiments do not constitute additional GroundedPlanBench tasks or independent AI Lab runtime validation. Underlying videos, image/annotation rights and robotic safety require separate assessment.
- Original first-party source: https://www.microsoft.com/en-us/research/blog/groundedplanbench-spatially-grounded-long-horizon-task-planning-for-robot-manipulation/ ; https://groundedplanning.github.io/
- The scoped acceptance concerns the existing original 2026 benchmark identity and source-backed task/protocol boundaries. No robot deployment, simulator or model run, full dataset rights/privacy/security review, schema/cache/CI/render, clean or final credit.
