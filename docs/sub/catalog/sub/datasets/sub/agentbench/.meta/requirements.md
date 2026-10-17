# Documentation Requirements

## Requirements

- Present AgentBench as a published, independently maintained broad agent-evaluation benchmark for language models acting across diverse interactive environments, rather than an agent model, general RL framework or a particular LLM serving API.
- Preserve the **ICLR 2024 original AgentBench** scope and versioned eight-environment evaluation methodology, distinguishing operating system, database, knowledge-graph, simulated game and shopping/browsing tasks where supported by the first-party paper/repository.
- Explain that the maintained first-party repository announced **AgentBench FC** (function-calling based on AgentRL) on **2025-10-10** with five containerized interactive task types. The original v0.1/v0.2 benchmark task and score setups must not be treated as directly comparable to the newer FC packaging/harness.
- Keep the benchmark's task dataset identity distinct from its supporting AgentRL controller, Docker-compose execution infrastructure, Redis/Freebase dependencies, leaderboard service, model submissions and separately released VisualAgentBench research work.
- Attribute first-party benchmark maintenance and research to the THUDM (Tsinghua University research) organization, while keeping versioned authorship/research affiliations source-backed.
- Treat environment inventory, benchmark scores, task splits, package/run dependencies, prompt/token budgets, dates and reported model performance as version-sensitive.

## Validation

- Original AgentBench and AgentBench FC evaluations are clearly version-separated.
- A running benchmark evaluator, AgentRL framework or leaderboard is not duplicated as a new dataset family.
- The THUDM producer relation reciprocates this canonical benchmark identity.
