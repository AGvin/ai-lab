# HealthBench

HealthBench is OpenAI's rubric-based evaluation of AI response capability and safety in realistic health conversations. It asks models to respond to the final user message and grades responses against physician-written criteria, rather than treating medical exam accuracy as sufficient evidence.

## Benchmark family

| Evaluation | Published scope |
| --- | --- |
| HealthBench | 5,000 realistic conversations spanning layperson and clinician contexts. |
| HealthBench Hard | A 1,000-example subset selected for difficulty. |
| HealthBench Consensus | 3,671 examples with rubric criteria filtered through physician agreement; the original release reports error rates. |
| HealthBench Professional | 525 clinician tasks covering care consult, writing/documentation, and medical research. |

Professional complements the broader conversation benchmark. The variants remain part of the family here; their task inventories, rubric construction, and score conventions should remain explicit. Physician task authorship, rubric validation, model-based grading, and evaluated models are separate roles.

## Grading revisions and comparison

The GPT-5.5 system-card methodology reports an updated implementation and empirical adjustment for final-response length. Its reference point is 2,000 characters, with different coefficients for each variant. Consequently, an adjusted score cannot be compared directly with an earlier unadjusted score or with a different variant's error-rate convention.

Record the dataset/variant and implementation revision, rubric and theme/axis taxonomy, grader, model configuration, raw or adjusted score definition, and response-length method. Preserve both the reported result and enough run context to explain changes caused by grading rather than model behavior. Follow the release's precautions against publishing test examples where they can enter training corpora.

## Interpretation boundaries

HealthBench is distinct from [MentalHealthBench](../mentalhealthbench/), ChatGPT health products, and clinical information systems. Benchmark scores provide evidence about the evaluated responses; they are not approval to diagnose or treat patients, clinical validation, or grounds for replacing a medical professional.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Official resources

- [HealthBench paper](https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf)
- [HealthBench release, Hard, and Consensus](https://openai.com/index/healthbench/)
- [HealthBench Professional paper](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf)
- [Updated HealthBench implementation and length adjustment](https://deploymentsafety.openai.com/gpt-5-5/healthbench)
