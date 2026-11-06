# SimpleQA

SimpleQA is OpenAI's **October 30, 2024** released benchmark for short-form factual question answering. The original dataset contains **4,326** questions intended to have a single independently checkable answer. It is separate from the `simple-evals` evaluation software and from any model evaluated against it. [OpenAI release](https://openai.com/index/introducing-simpleqa/).

## Intended use and limits

The benchmark tests concise factual recall, not multi-claim long responses, browsing ability, or general AI safety. OpenAI selected questions on which two independent trainers agreed, then had a third trainer check 1,000 examples. The publisher estimated an **approximately 3% inherent question error rate** after inspecting disagreements; not every published reference answer is guaranteed correct.

The original evaluation labels answers **correct**, **incorrect** or **not attempted** with a prompted grader. Preserve the exact dataset revision, grader model, rubric, abstention handling, prompts, model snapshot and tool-access conditions before comparing results. Public questions and answers pose contamination risk. Scores from different evaluations or model-tool configurations cannot be equated without qualification.

## Distinct derivative and availability

**SimpleQA Verified** is a separately curated **1,000-question** derivative published by Google DeepMind and Google Research researchers in 2025, filtering and rebalancing the original and altering grading details. It is not a SimpleQA release alias, not an additional 4,326-question OpenAI dataset, and not equivalent in leaderboard scores. [Derivative paper](https://arxiv.org/abs/2509.07968).

The `simple-evals` repository announced in July 2025 that new model and benchmark result updates would stop; it continues to host the SimpleQA reference evaluator. That software maintenance announcement does not withdraw the source dataset. Its README associates SimpleQA with the repository's **MIT** license, which does not independently settle rights to every third-party factual source in the questions or mirrors. Review the applicable original source/data terms before redistribution; no independent model runs or rights audit are claimed here.

## Related datasets

- Derived and separately curated evaluation subset: [SimpleQA Verified](../simpleqa-verified/) by Google DeepMind and Google Research, 1,000 questions with a distinct grading protocol.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Original resources

- [Original OpenAI SimpleQA release](https://openai.com/index/introducing-simpleqa/)
- [Original SimpleQA research paper](https://arxiv.org/abs/2411.04368)
- [Original SimpleQA evaluator](https://github.com/openai/simple-evals/blob/main/simpleqa_eval.py)
- [Official Simple-Evals repository and maintenance notice](https://github.com/openai/simple-evals)
- [Official repository license](https://github.com/openai/simple-evals/blob/main/LICENSE)
- [Google-derived SimpleQA Verified paper](https://arxiv.org/abs/2509.07968)
