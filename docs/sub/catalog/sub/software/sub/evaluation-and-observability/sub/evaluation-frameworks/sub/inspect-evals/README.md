# Inspect Evals

Inspect Evals is an open-source, installable Python collection of model and agent evaluations built using the separate [Inspect AI](../inspect-ai/) evaluation framework. It supplies ready-to-run evaluation implementations and a distributed register of additional community evaluations. Inspect Evals is **not** a second copy of the Inspect AI runner or a single benchmark dataset.

## Installation and evaluation workflow

For an installed Python project, the source documents `pip install inspect-evals`; for a checkout of the upstream repository, use `uv sync`. After configuring a supported model/provider and securing any needed credentials, users can run selected tasks with the Inspect AI CLI:

```sh
uv run inspect eval inspect_evals/arc_easy --model openai/gpt-5-nano
uv run inspect eval-set inspect_evals/arc_easy inspect_evals/arc_challenge
uv run inspect view
```

These are documented examples, **not** commands executed for this catalog entry. The pinned source manifest at commit `7c31cf22830c4657a3894e095b452c7d50f6f3b8` (2026-11-03) declares Python `>=3.11`, dependency `inspect_ai >= 0.3.285`, and a dynamic package version. The README recommends Python 3.11 or 3.12 for broad task compatibility; some evaluations require additional optional packages, Docker, large datasets or hardware resources. Model-provider access and API charges are independent of package installation.

## Bundled evaluations versus distributed register

Inspect Evals began as a UK AI Security Institute-led evaluation collection in 2024, with contributions from other organizations. Its current maintainer is Generality Labs. Beginning 2026-05-08, new community contributions are submitted to the **Inspect Evals Register** as metadata referencing externally hosted implementations, rather than automatically being copied into the package's `src/` tree. A registered benchmark, its original dataset, the Inspect AI execution framework and this software collection each retain distinct identities and lifecycles.

## Safety, licensing and reproducibility

Pin the collection, individual evaluation/task version, dataset rights and snapshot, model/provider revision, grading configuration and run parameters before interpreting results. Results assess specified tasks and conditions, not general safety certification.

Runs may expose sensitive prompts, tool traces, model outputs and personally identifiable data in logs. Use authorized evaluation data, limit provider access and spend, isolate risky tool-execution workloads in appropriate sandboxes, secure API keys and control logs, caches and retention. The repository uses the MIT software license, but its `NOTICE` names third-party components with different terms; do not infer redistribution rights to every benchmark or downloaded dataset.

## Relations

- Originally developed by: [UK AI Security Institute](../../../../../../../producers/sub/u/sub/uk-ai-security-institute/) (with contributors)
- Maintained by: [Generality Labs](../../../../../../../producers/sub/g/sub/generality-labs/)
- Evaluation runner: [Inspect AI](../inspect-ai/)

## Official resources

- [Inspect Evals repository](https://github.com/UKGovernmentBEIS/inspect_evals)
- [Pinned upstream README and workflow](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/README.md)
- [Pinned package manifest](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/pyproject.toml)
- [Evaluation register migration](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/EVAL_REGISTER.md)
- [Pinned MIT software license](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/LICENSE)
- [Third-party attribution and license notice](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/NOTICE)
