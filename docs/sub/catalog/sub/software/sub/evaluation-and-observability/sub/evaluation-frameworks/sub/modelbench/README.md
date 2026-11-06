# ModelBench

ModelBench is MLCommons' open-source Python evaluation framework and command-line tool for running AI-model safety benchmarks and reporting outcomes against specified hazard categories. This is independently installable software, not a second AILuminate benchmark suite or a hosted model API.

## Safety-evaluation workflow

The source repository includes two cooperating components: **ModelGauge** runs tests against a configured system under test (SUT) and annotates responses, while **ModelBench** aggregates those measurements by hazard and benchmark and generates reports. Both console entry points are distributed by one Python package and repository; they do not establish two separate catalog products.

For a local source checkout, the documented setup uses `uv` (including `uv python install 3.12` and `uv sync`). Configure a permitted SUT/model provider and place credentials in a private, excluded `config/secrets.toml` rather than in source control. The first-party example runs a reduced `modelbench benchmark general` with `-m 1` against a Together AI-backed SUT; other supported SUT adapters may use different authorized remote or self-hosted model endpoints.

**Official safety-benchmark evaluation also requires credentials for the MLCommons `cheval` evaluator service**, obtained through MLCommons administration. Installing ModelBench does not supply those credentials, paid model-provider access, or unrestricted access to protected official prompts. Smaller `--max-instances` runs give quicker but lower-fidelity reports; they are not comparable substitutes for full published benchmarking.

The pinned [source manifest](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/pyproject.toml) at commit `a4c8d6c928de6465db29d13561ad0ac26e667a43` (2026-10-30) declares version `1.0.0`, Python `>=3.12,!=3.12.5,<4`, the `modelbench` and `modelgauge` CLI scripts, and Apache-2.0 software licensing. These are source observations rather than a claim that this is the latest distribution or that any runtime evaluation was executed.

## Reporting, rights and safe operation

Runs generate JSON score/annotation records and compressed journal files, and the framework can cache model and annotator responses. Record the benchmark version, SUT/model version, provider, evaluator, hazard configuration and run parameters before comparing results. Hazard-level scores describe the configured tested system and tasks; they are not general safety certification for a model or service.

Prompts and outputs may include sensitive or distressing material. Restrict data disclosure, source/score log access, local caches, and retention; protect credentials and control model/evaluator API costs. The upstream CLI only includes prompts marked shareable when requested and excludes annotations for official prompt sets. Apache-2.0 applies to the software source, **not automatically** to protected official benchmark data, third-party model APIs, or evaluator-service entitlements.

## Relations

- Produced by: [MLCommons](../../../../../../../producers/sub/m/sub/mlcommons/)
- Related benchmark family: [AILuminate](../../../../../../../datasets/sub/ailuminate/)

## Official resources

- [ModelBench source repository](https://github.com/mlcommons/modelbench)
- [Pinned first-party README and setup](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/README.md)
- [Pinned source manifest](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/pyproject.toml)
- [Pinned system-under-test integration guide](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/docs/suts-how-to.md)
- [Pinned Apache-2.0 license](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/LICENSE.md)
