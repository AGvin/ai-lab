# Terminal-Bench 2.0

Terminal-Bench 2.0 is a released, independently versioned benchmark of agents performing end-to-end tasks in containerized terminal environments. It is distinct from the original Terminal-Bench task corpus, later benchmark revisions, and Harbor, the software framework used to run evaluations.

## Evaluation scope

Tasks combine instructions, a reproducible environment, reference solutions, and automated validators. Keep the exact dataset revision, environment, agent harness, model, tool access, execution budget, and scoring configuration with every result. Resolution rates describe the tested agent setup; they are not model-quality measurements independent of that setup.

Use the Terminal-Bench 2.0 repository as the release-specific source and record an explicit dataset revision when running Harbor. The current generic run page may target a later benchmark release; a URL query parameter does not pin the evaluation. Do not combine task counts or scores from different Terminal-Bench versions. Benchmark material must be kept out of training corpora to avoid contamination.

## Provenance

- Produced by: [Laude Institute](../../../producers/sub/l/sub/laude-institute/)

Terminal-Bench is a collaboration involving Laude Institute and Stanford researchers, with Harbor providing the evaluation infrastructure. This provenance does not assign ownership of submitted models or every external contribution to the benchmark steward.

## Official resources

- [Terminal-Bench 2.0 repository](https://github.com/harbor-framework/terminal-bench-2)
- [Terminal-Bench 2.0 and Harbor announcement](https://www.tbench.ai/news/announcement-2-0)
