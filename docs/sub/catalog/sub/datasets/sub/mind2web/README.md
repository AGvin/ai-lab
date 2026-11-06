# Mind2Web

Mind2Web is the NeurIPS 2023 dataset for offline web-agent action prediction. Its original release records more than 2,000 tasks from 137 real websites across 31 domains, with annotated action trajectories and page information.

## Evaluation scope

The cross-task, cross-website, and cross-domain splits test different generalization boundaries. Record the split, task and trajectory revision, candidate-generation method, and action-prediction configuration with each result. These offline measurements do not establish live browser task success.

The official evaluation update of 2023-10-30 added the paper's macro-averaged accuracy alongside the repository's earlier micro-average. Always identify the aggregation method; longer trajectories affect a micro-average differently, so the two are not interchangeable.

## Data and related benchmarks

Follow the repository's contamination precautions: keep benchmark test examples out of training corpora and do not republish extracted test files online. Dataset access, model artifacts, and evaluation code are separate resources.

The 2024 Multimodal-Mind2Web extension pairs the original HTML annotations with screenshots. [Online-Mind2Web](../online-mind2web/) measures execution on live websites, while [Mind2Web 2](../mind2web-2/) evaluates agentic search and citation-backed answers. Use the protocol matching the capability being tested.

## Provenance

- Produced by: [Ohio State NLP Group](../../../producers/sub/o/sub/osu-nlp-group/)

The group publishes the research project. Collaborating authors and providers of trained or evaluated models retain their separate roles.

## Official resources

- [Mind2Web repository and evaluation guidance](https://github.com/OSU-NLP-Group/Mind2Web)
- [Mind2Web project site](https://osu-nlp-group.github.io/Mind2Web/)
