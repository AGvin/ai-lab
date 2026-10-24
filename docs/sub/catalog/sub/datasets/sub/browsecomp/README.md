# BrowseComp

BrowseComp is OpenAI's released benchmark for browsing agents that must locate difficult, interconnected information on the web. The April 2025 release contains 1,266 problems and is distributed through the simple-evals repository.

## What it measures

Questions are designed to require persistent information finding while allowing short-answer verification. That structure tests a narrower capability than open-ended research conversations or general factuality. The benchmark is separate from the browsing product, model, or agent used to solve it, and from the simple-evals software that distributes it.

## Interpreting a run

Record the dataset and evaluator revision, agent harness, browsing/search tools, model configuration, sampling or answer-aggregation policy, execution budget, and web-access conditions. Treat reported accuracy, rankings, and test-time-compute effects as properties of that complete setup. Public availability also creates contamination risks; preserve the evaluation's test-data handling precautions.

Choose BrowseComp when hard-to-find web information and verifiable answers match the intended capability. A score alone does not establish the quality of long reports, reliability over ordinary user questions, or the current quality of a browsing service.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Official resources

- [BrowseComp release and methodology](https://openai.com/index/browsecomp/)
- [OpenAI simple-evals distribution repository](https://github.com/openai/simple-evals)
