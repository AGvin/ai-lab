# AgentIF

**AgentIF** is a research dataset for evaluating how well language models follow lengthy, constraint-rich instructions inside agentic workflows. The original **THU-KEG** release comprises **707 human-annotated instructions from 50 agentic applications**, with an average of **11.9 constraints per instruction**. These are published dataset-level averages, not guarantees for every example. The work appeared in the NeurIPS 2025 Datasets and Benchmarks track.

## Dataset, harness and scores

Examples include system/user instructions and annotated constraints on tool use, formatting, conditions and semantics. **Constraint Success Rate (CSR)** measures the fraction of constraints satisfied; **Instruction Success Rate (ISR)** measures complete instruction success. The prompt/constraint dataset is separate from the code/LLM evaluator, model provider endpoints, leaderboard and model results. It is also distinct from [IFEval](../ifeval/) and [AgentBench](../agentbench/), which have different task designs and scoring semantics.

**Evaluation versions must be pinned.** AgentIF's October 2026 update evaluates reasoning and non-reasoning modes, uses recommended decoding configurations, three independent runs and an `gpt-5.6-luna` judge. Earlier results used one greedy run and `gpt-4o-2024-11-20`. The project states that **scores across these methods are not comparable**; recorded model rankings do not establish general safety, accuracy or tool competence.

## Licensing and safe evaluation

**Rights are distribution-specific and currently contradictory.** The original GitHub project's [`data/LICENSE`](https://github.com/THU-KEG/AgentIF/blob/main/data/LICENSE) explicitly gives the dataset under **CC BY 4.0**, and its root [`LICENSE`](https://github.com/THU-KEG/AgentIF/blob/main/LICENSE) grants **Apache-2.0 to code**. The publisher's [Hugging Face dataset mirror](https://huggingface.co/datasets/THU-KEG/AgentIF) currently declares **CC BY-NC 4.0**. Do not assume that either grant universally resolves the other distribution; confirm the rights for the exact artifact and intended commercial use before redistributing or operationalizing it.

Evaluation cases contain machine-checked instructions and may include executable checker snippets. Run checkers in isolated environments, inspect scripts, protect API keys and externally sent prompts, and treat untrusted prompts and judge outputs as data. We have **not run** the benchmark or audited all source examples, model scores, third-party content rights or beneficial ownership.

## Producer

- Produced by [THU-KEG (Knowledge Engineering Group, Tsinghua University)](../../../producers/sub/t/sub/thu-keg/).

## Official resources

- [Original dataset and evaluation repository](https://github.com/THU-KEG/AgentIF)
- [Original dataset licensing](https://github.com/THU-KEG/AgentIF/blob/main/data/LICENSE)
- [Code licensing](https://github.com/THU-KEG/AgentIF/blob/main/LICENSE)
- [Hugging Face data distribution](https://huggingface.co/datasets/THU-KEG/AgentIF)
- [2026-10 evaluation protocol and leaderboard](https://agentif.github.io/)
- [Original research paper](https://arxiv.org/abs/2505.16944)
