# Documentation Requirements

## Requirements

- Attribute the first-party AgentBench research benchmark and maintained `THUDM/AgentBench` repository to THUDM's Tsinghua University research contributors, without equating the project with all academic departments or all models built by the university.
- Keep original AgentBench (ICLR 2024) and later AgentBench FC (2025 function-calling/task packaging) details in the benchmark's dataset requirements rather than duplicating release-scoped methodology under the producer.
- Do not imply THUDM produces the independent AgentRL, Docker, Redis, benchmark participants or evaluated third-party models solely because those tools appear in benchmark setup instructions.
- Keep collaborators, citation authors and evolving upstream maintainers attributable to the relevant first-party source.
- Preserve this source-backed identity and provenance context: THUDM is the Tsinghua University research publishing identity represented here for AgentBench. Its first-party organization and benchmark sources distinguish academic contributors and project stewardship from the models and tools evaluated by the benchmark.
- Explain the following operating and decision boundary: Pin the benchmark and harness revision when reproducing results. The original AgentBench and later AgentBench FC use different task packaging; the current FC repository depends on AgentRL and containerized environments. Isolate those execution environments and treat evaluated models, Docker, Redis and other dependencies as separate identities. A benchmark score is evidence for its versioned protocol, not a universal model-quality guarantee.
- Support the producer context with these first-party sources: <https://github.com/THUDM>, <https://github.com/THUDM/AgentBench>, <https://huggingface.co/THUDM>.

## Validation

- The `produces` relation directly reciprocates the current `catalog/datasets/agentbench` `produced-by` relation.
- Producer scope does not conflate one research benchmark with implementation dependencies or evaluated models.
