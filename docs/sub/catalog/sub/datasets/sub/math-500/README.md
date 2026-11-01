# MATH-500

MATH-500 is the 500-problem held-out test subset selected by OpenAI from the original competition-mathematics MATH dataset for its [*Let's Verify Step by Step* research and PRM800K release](https://github.com/openai/prm800k#math-splits). It is a reproducible mathematical-problem evaluation set, not the full MATH corpus or the 800,000 step-level human correctness labels in PRM800K.

## Source and subset boundary

The [original MATH research repository](https://github.com/hendrycks/math) attributes the underlying dataset to Dan Hendrycks and collaborators. OpenAI's PRM800K README describes moving 4,500 original MATH test problems into an expanded training split, leaving 500 uniformly selected held-out test problems. OpenAI authored that selection and released the [original test split](https://github.com/openai/prm800k/blob/main/prm800k/math_splits/test.jsonl), stored through Git LFS.

[Hugging Face H4's MATH-500 distribution](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) describes itself as that selected subset, not as a second independently designed benchmark. The original and republished files were not independently compared byte-for-byte here; pin the exact upstream Git/LFS object and any downstream export before reproducing a result. The OpenAI PRM800K repository is archived, so active maintenance is not established.

## Evaluation limits

The question/solution data are distinct from answer checking, prompt protocol and a model's score. PRM800K's original [grading explanation](https://github.com/openai/prm800k#answer-grading) notes that symbolic or normalized answer matching can reject correct answers or admit incorrect ones. Report the exact split, grader, inference settings and scoring method when comparing evaluations.

The published test problems are susceptible to training contamination and do not establish general mathematical reasoning capability, model safety or real-world reliability. No model run or reproduced benchmark score is asserted here.

## License and provenance boundaries

The OpenAI [PRM800K repository LICENSE](https://github.com/openai/prm800k/blob/main/LICENSE) and upstream [Hendrycks MATH repository LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE) both use MIT language for repository software and associated documentation. The reviewed H4 MATH-500 card does not specify a dataset license. These facts **do not independently establish all rights to the original competition questions**; do not assume unrestricted redistribution of problem data or treat repository-code terms as a complete rights clearance.

OpenAI is attributed as selector/publisher of the 500-problem split, not author of all source MATH problems. H4 is the republisher. Ultimate beneficial ownership, indirect holdings and sanctions were not independently audited.

## Provenance

- Selected and published by: [OpenAI](../../../producers/sub/o/sub/openai/) — only the MATH-500 subset, not the original full MATH corpus.

## Original dataset relationship

- Selected test subset of: [MATH (Hendrycks et al.)](../math/). This documents selection lineage, not new ownership of the original competition questions.

## Primary resources

- [Original PRM800K split explanation](https://github.com/openai/prm800k#math-splits)
- [Original OpenAI LFS test split](https://github.com/openai/prm800k/blob/main/prm800k/math_splits/test.jsonl)
- [Hugging Face H4 subset distribution](https://huggingface.co/datasets/HuggingFaceH4/MATH-500)
- [Hendrycks et al. original MATH source](https://github.com/hendrycks/math)
- [OpenAI PRM800K repository MIT LICENSE](https://github.com/openai/prm800k/blob/main/LICENSE)
- [Hendrycks MATH repository MIT LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE)
