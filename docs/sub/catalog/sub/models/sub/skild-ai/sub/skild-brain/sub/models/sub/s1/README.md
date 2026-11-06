# S1

**S1** is Skild AI's separately released robotics foundation model in the Skild Brain family. The publisher describes S1 as an **in-context learner**: a single video demonstration specifies a task, and the model can execute previously unseen manipulation tasks without *task-specific weight updates* in the reported experiments.

## In-context learning contract

Skild's August 2026 research demonstrates single-video prompting and long-horizon manipulation tasks of up to approximately **10 minutes**. This is a producer-reported experimental scope, not a guarantee of performance on arbitrary hardware or environments. The video's context and the actual robot observation/action interfaces are part of the operating conditions.

The publisher reports error recovery, perturbation robustness, and comparison with task-specific post-training demonstrations. These are not independently reproduced AI Lab benchmarks or a universal robotics safety certification. More recent self-play research describes a separate post-training direction; it does not retroactively change the original S1 in-context experiments.

## Deployment boundary

Skild AI remains the model producer. NVIDIA infrastructure, robots from other manufacturers, customer integration, control software, and physical safety assessments are separate. Neither the research article nor an observed deployment establishes public weights, general hardware compatibility or reproducible success rates. Validate the actual robot, task, controls, operating envelope and current access terms.

## Translations

- English

## Relations

- Member of: [Skild Brain](../../../../)

## Official resources

- [Skild AI S1 research](https://www.skild.ai/blogs/s1)
- [Skild AI deployment context](https://www.skild.ai/blogs/skild-crosses-100m-arr)
- [Physical self-play follow-on research (September 2026)](https://www.skild.ai/blogs/physical-self-play)
