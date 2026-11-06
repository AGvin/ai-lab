# GSM8K

GSM8K (Grade School Math 8K) is OpenAI's published dataset of approximately 8,500 English grade-school mathematics word problems created by human problem writers. The [original research release](https://github.com/openai/grade-school-math) describes multistep elementary arithmetic questions with written explanations; most take two to eight steps to solve.

## Source data and versions

The original source has `grade_school_math/data/train.jsonl` and `test.jsonl` with `question` and `answer` fields. The README uses rounded sizes of 7.5K training and 1K test questions; the current [official OpenAI dataset card](https://huggingface.co/datasets/openai/gsm8k) reports 7,473 and 1,319 examples for its main train/test exports. Record the exact dataset configuration, revision and split.

Answers may contain calculator calculation annotations and a final numeric answer preceded by `####`. Socratic-subquestion data is an additional representation of this dataset, not a separately accepted dataset. The original publisher also provides historical model solution examples, which are evaluation material rather than extra source questions.

## Comparison and lifecycle limitations

The [original paper](https://arxiv.org/abs/2110.14168) studies learning and verification of grade-school arithmetic reasoning. GSM8K covers a different difficulty distribution from original competition-level [MATH](../math/) and its selected [MATH-500](../math-500/) evaluation subset; the scores are not interchangeable.

The original repository states that it is archived and maintained as-is. Its older sample-generation calculator had known defects, and public question exposure can contaminate held-out evaluation. Prompt formatting, answer extraction, calculator usage and data revision must match before comparing scores. No independent benchmark or model execution is asserted here.

## Licensing and provenance

The [official OpenAI Hub dataset card](https://huggingface.co/datasets/openai/gsm8k) declares MIT, while the [original repository LICENSE](https://github.com/openai/grade-school-math/blob/master/LICENSE) separately specifies MIT for software and associated documentation. Treat them as scoped declarations, not blanket proof of rights in unrelated repacks or all derived content.

GSM8K is an OpenAI-produced original source dataset. No complete beneficial-ownership/indirect-holdings or sanctions audit was performed.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/).

## Official resources

- [Original research repository](https://github.com/openai/grade-school-math)
- [Original OpenAI GSM8K Hub dataset](https://huggingface.co/datasets/openai/gsm8k)
- [Training Verifiers paper](https://arxiv.org/abs/2110.14168)
- [OpenAI research explanation](https://openai.com/index/solving-math-word-problems/)
- [Original repository LICENSE](https://github.com/openai/grade-school-math/blob/master/LICENSE)
