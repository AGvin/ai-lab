# Documentation Requirements

## Requirements

- Identify original Mind2Web as the NeurIPS 2023 web-agent dataset for offline action prediction: more than 2,000 recorded tasks from 137 real websites across 31 domains, not a live browser task-success benchmark.
- Preserve distinct cross-task, cross-website and cross-domain generalization splits, action trajectories, candidate-generation method and evaluation revision; do not compare different splits as equivalent.
- The 2023-10-30 official evaluation correction distinguishes the paper's macro-averaged accuracy from earlier micro-averaged reporting. Record the aggregation method whenever reporting benchmark scores.
- Respect the official test-data contamination and redistribution precautions, including the request not to republish extracted test files or place benchmark test examples in training corpora.
- Treat 2024 Multimodal-Mind2Web screenshot/HTML pairing as an extension to the original annotations absent a separate benchmark protocol; keep Online-Mind2Web live-site execution and Mind2Web 2 agentic-search evaluation as separate benchmark identities.
- Preserve Ohio State NLP Group stewardship while distinguishing collaborating research authors and trained/evaluated model providers.

## Validation

- The first-party repo substantiates benchmark size, splits, scoring change and access restrictions.
- The Ohio State NLP Group `produces` endpoint exactly reciprocates the Mind2Web `produced-by` relation.
