# Documentation Requirements

## Requirements

- Identify OpenBookQA as the original 2018 Ai2 multiple-choice science question evaluation dataset published by the Allen Institute for AI from research by Todor Mihaylov, Peter Clark, Tushar Khot and Ashish Sabharwal. Distinguish it from Ai2 Reasoning Challenge (ARC), ARC-AGI, source-model training scripts and leaderboards.
- Preserve exactly 5,957 question instances, with original 4,957 train, 500 validation/development and 500 test. Ai2's two Hub configurations, `main` and `additional`, contain the same question counts; `additional` includes fact and crowd-rating annotations, not a second independently developed question set.
- Preserve the open-book concept: fact retrieval and combining a relevant elementary science fact with broader common knowledge. The published EMNLP paper describes 1,326 core science facts; an earlier arXiv abstract has 1,329, so identify the source/edition rather than silently treating both values as identical immutable counts.
- Separate the main fact book from the separately described 5,167 crowd-sourced commonsense facts; neither is 5,957 new independent question identities.
- The original Ai2 Hub card marks the **data license as unknown**. The original Ai2 model/baseline repository carries an actual Apache-2.0 software-code LICENSE; do not silently apply that to all questions/facts or assume unrestricted reuse and redistribution. Source copyright and third-party fact licensing require verification.
- Attribute the original published dataset to the existing Ai2 organization and maintain reciprocal `produced-by` / `produces` relations. Do not create a new author-named corporation or new producer gate credit for this second publication.
- Model evaluation comparisons must fix dataset revision, main/additional context, retrieval or oracle-fact availability, prompts, answer ordering, scoring and model setup. Oracle fact input is a distinct evaluation condition, not a separate trained model or dataset.
- Document common benchmark-data exposure, retrieval and knowledge-source limits; old accuracy is not a general reasoning, truthfulness or safety guarantee. No independent model score, inference, full data rights, sanctions or ownership audit was conducted.
- Use official Ai2 publisher Hub card, final original paper, upstream Ai2 baseline software repo, exact source-code LICENSE, and published TensorFlow Datasets reference. Render validated current-entity relations and official resource links.

## Validation

- One concrete canonical OpenBookQA source dataset; do not double-count `main`/`additional` or separate task/harness identities.
- Exact one reciprocal Ai2 producer dataset relation, canonical ID and index destination.
- Reader includes source rights uncertainty and disambiguation from original Ai2 ARC.
- Scoped link/YAML/readback checks are distinct from whole-repository schema/cache/CI and final reader rendering.
