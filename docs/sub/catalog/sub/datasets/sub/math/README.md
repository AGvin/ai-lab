# MATH

MATH is the original dataset of 12,500 mathematics-competition problems introduced by Dan Hendrycks and collaborators in the [2021 research paper](https://arxiv.org/abs/2103.03874). It includes worked, step-by-step solutions and an original split of 7,500 training and 5,000 test problems. The [research-author repository](https://github.com/hendrycks/math) owns the original dataset research, loaders and evaluation code.

## Dataset boundary

The source problems cover challenging competition mathematics rather than only elementary arithmetic. MATH is not the auxiliary AMPS pretraining dataset, an evaluation grader, a scoring protocol or a model performance table.

OpenAI later selected a 500-problem held-out subset from the original MATH test collection. That separately published [MATH-500 subset](../math-500/) is a *derived dataset selection*, not an alternative creator of the original competition problems. PRM800K's human-labeled steps are yet another data corpus and are not included as a second MATH identity.

## Evaluation and rights

Question choice, exact source file, prompt, grading and answer normalization matter when comparing results. Public evaluation data can leak into training, and an old score cannot establish broad mathematical reasoning or safety. No model run or benchmark reproduction was performed here.

The author repository's [MIT LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE) is written for software and associated documentation. It does not alone verify permission to redistribute *all original contest questions* or establish the terms of every third-party mirror. Review the applicable source and attribution requirements before republishing data.

This profile identifies its research authors but does not claim a separate corporate producer or a complete beneficial-ownership/sanctions audit.

## Related datasets

- Derived held-out subset: [MATH-500](../math-500/).
- Separately annotated process-supervision corpus using original problem prompts: [PRM800K](../prm800k/) (OpenAI, 2023); not a new original MATH contest-question set.

## Primary research

- [Original research repository](https://github.com/hendrycks/math)
- [Original paper](https://arxiv.org/abs/2103.03874)
- [Original code/documentation LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE)
- [Later OpenAI MATH-500 split selection](https://github.com/openai/prm800k#math-splits)
