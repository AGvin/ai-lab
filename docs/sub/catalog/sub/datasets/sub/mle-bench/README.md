# MLE-bench

MLE-bench is OpenAI's released benchmark of machine-learning engineering across 75 Kaggle competitions. Tasks involve preparing data, training models, running experiments, and producing competition submissions; code generation alone is insufficient.

## Running and comparing evaluations

The repository provides data-preparation and grading code. It constructs train/test splits from public competition training data and grades competition-specific CSV submissions. Kaggle credentials and competition rules remain separate access dependencies.

Distinguish the 75-competition full evaluation from the 22-competition Low/Lite split. Record the competition inventory, preparation and grading revision, agent scaffold, model, compute, runtime, and contamination controls. Follow the repository's split-specific Any Medal reporting guidance, including repeated seeds and uncertainty; changing resources or mixing splits changes the comparison.

## Lifecycle and limitations

The repository notice dated 2026-04-24 pauses new leaderboard submissions while the maintainers improve comparability. Its known-issues section documents preparation defects and label leakage, and describes planned v2 fixes. Check the issues affecting the selected revision; do not assume those fixes are already included.

The submission pause does not withdraw the released benchmark. Kaggle, underlying competition datasets, preparation/grading software, and evaluated AutoML or agent frameworks remain distinct. Results apply to the tested model/scaffold/resource setup and do not establish unrestricted ML-engineering competence.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Official resources

- [MLE-bench publication](https://openai.com/index/mle-bench/)
- [MLE-bench repository, preparation, grading, and known issues](https://github.com/openai/mle-bench)
