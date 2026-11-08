# Documentation Requirements

## Requirements

- Identify Blueprint-Bench 2 as Andon Labs' current agentic spatial-intelligence benchmark for reconstructing apartment floor plans from interior photographs across repeated tasks.
- Preserve the current benchmark boundary around spatial reconstruction, persistent notepad/cross-apartment learning, connectivity similarity scoring, random/human baselines, and sequential apartment evaluation only while first-party material supports them.
- Treat apartment inventory, scoring normalization, agent harness, feedback, leaderboard, model results, human baseline, and benchmark revisions as freshness-sensitive.
- Keep deprecated/earlier Blueprint-Bench results separate from Blueprint-Bench 2 rather than blending leaderboards.
- Keep spatial-reasoning concepts, image-generation models, robotics systems, and apartment data sources with their own owners.

## Validation

- The node remains the current Blueprint-Bench 2 benchmark identity.
- Model rankings are scoped to the exact benchmark revision and evaluation harness.

## Scoped original-source qualification — 2026-11-08

- **Blueprint-Bench 2** is Andon Labs' original **May 2026** successor to Blueprint-Bench for multimodal agent spatial reasoning. An agent processes **50 distinct apartments sequentially**, viewing roughly **20 interior photographs per apartment** and generating 2D room/connectivity plans, with a cross-apartment **persistent notepad**; the prior single-apartment experimental version, agents and public leaderboard are distinct evaluation contexts, not separate named products from each test run.
- The released scoring compares **room-connectivity graphs**, with a normalized random-baseline score of zero and perfect-plan score of one. Its six original components weight **connection Jaccard 50%, node degree 20%, graph density 10%, room count 10%, doorway count 5%, and orientation 5%**, under rotation/reflection-invariant matching. Publisher's human reference uses a restricted subset of apartments, so cross-cohort headline and model release comparisons must retain sample size, benchmark build and scoring policy.
- Source data are interior photographs and annotated floor plans; capture/privacy, property-image rights, public benchmark use and deployment safety are not proven by a scoreboard. Publisher model results are not independently reproduced or evidence of reliable real property-surveying, emergency route mapping or autonomy.
- First-party publisher source: https://andonlabs.com/evals/blueprint-bench-2 .
- Source acceptance verifies this existing versioned benchmark identity, 50-apartment protocol and evaluation weights only; no model runs, underlying apartment image redistribution rights/consent audit, whole-repo CI/render, missing reader repair, clean or final delivery gate.
