# Documentation Requirements

## Requirements

- Identify PRM800K as OpenAI's **2023 released process-supervision dataset** with approximately **800,000 human correctness labels for intermediate steps** of model-generated solutions to original MATH contest problems; distinguish the name from exact raw/filtered row counts and distinct numbers of problems or solutions.
- Separate original MATH problem/solution data, the selected MATH-500 held-out test set, the model-generated solution trajectories, human step ratings, process-reward-model weights and model performance results. PRM800K is a separate annotation/training-data corpus, not another original question set or a trained model.
- Original GitHub repository includes phase-1 and phase-2 train/test JSONL files stored using **Git LFS**, and phase-specific human-labeling instructions. Preserve exact repository commit, split, preprocessing and ratings policy for reproducibility.
- Human step ratings include **negative (-1)**, **neutral (0)** and **positive (+1)** semantics; a neutral rating does not necessarily indicate correctness. Phase-2 data and active-selection policies differ from phase-1; do not compare unqualified filtered/unfiltered samples.
- Source page belongs to OpenAI's May 31, 2023 original release. GitHub's original repository is **archived/read-only as of May 29, 2026**; archival of the reference implementation is not withdrawal of the historical released research data or evidence of active support.
- OpenAI source repository's MIT `LICENSE` explicitly covers software and associated documentation. It is **not** proof that every underlying MATH contest question, source solution, generated trajectory, annotation or downstream distribution has unrestricted reuse rights; pin and audit exact data before commercial reuse or redistribution.
- The dataset uses derived MATH questions, but the new annotated model-generated trajectories are not the source MATH test-set subset. Model `trained-on` provenance is not implied by the dataset `derived-from` lineage.
- The original raw JSONL example contains labeler pseudonyms and timestamps; apply appropriate privacy and data handling controls if downloading or republishing raw records. No private data were fetched for catalog authoring.
- Cite OpenAI publication, original research paper, original archived GitHub repository, official data directory and LICENSE, and original MATH repository. Avoid unverified current performance metrics, ongoing maintenance claims and independent model-score claims.
- Reconcile exactly one `produced-by` / `produces` original OpenAI producer pair and one `derived-from` / `has-derivative` MATH data-lineage pair. Preserve all existing MATH-500 relation edges and original researcher provenance.

## Validation

- One stable `catalog/datasets/prm800k` source identity, not MATH, MATH-500, an open-source evaluator or a trained PRM model.
- Dataset index, original MATH reader/metadata, and existing OpenAI producer metadata/reader must resolve with unique exact inverse relation pairs.
- Report a bounded nine-path authored change-set and actual SHA readbacks separately from full eight-root clean-cycle, repository-wide schema/cache/CI and final render acceptance.
