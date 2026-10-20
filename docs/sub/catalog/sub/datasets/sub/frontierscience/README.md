# FrontierScience

FrontierScience is OpenAI's benchmark of expert-level scientific reasoning in physics, chemistry, and biology. Its published full evaluation contains more than 700 questions; the public gold release contains 100 Olympiad and 60 Research questions. The remaining questions are held out for contamination tracking.

## Tracks and grading

| Track | Published evaluation approach |
| --- | --- |
| Olympiad | Constrained problems with short answers that can be checked against a reference. |
| Research | Self-contained research subtasks with a 10-point rubric; the published correctness threshold is at least 7/10. |

Experts author and review the tasks. The published method uses a model-based response grader, so task authorship and grading are separate roles. The two tracks and their gold subsets belong to this benchmark rather than constituting independent datasets here.

## Interpreting results

Record the track, full or public-gold scope, task revision, answer or rubric version, threshold, grader, and model configuration. Account for contamination and task-selection effects when comparing scores. Sample questions and reported model scores do not define the complete release.

The benchmark measures constrained scientific reasoning. It does not establish that a system can conduct a complete research program or independently produce validated discoveries.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Official resources

- [FrontierScience release, gold sets, and grading method](https://openai.com/index/frontierscience/)
