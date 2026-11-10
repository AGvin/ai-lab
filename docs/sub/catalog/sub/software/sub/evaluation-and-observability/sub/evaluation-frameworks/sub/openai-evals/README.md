# OpenAI Evals

OpenAI Evals is a self-managed, open-source Python framework for evaluating language models and applications that use them. Its `evals` package supplies evaluation runners, YAML-defined tasks and evaluation sets, score/report logging, and a protocol for integrating different model completion functions. The independently hosted evaluation experience in the OpenAI Dashboard is **not** a second copy of this software.

## Evaluation workflow

The package exposes `oaieval` to run one evaluation and `oaievalset` to run a configured evaluation set. Evaluation definitions live in the repository registry; scoring implementations and model adapters are separate pieces of a reproducible run. The `CompletionFn` interface supports configured model providers or custom implementations.

For a self-managed setup, review the selected evaluation and its data rights, provision the required model API access, then install `evals` (or `pip install -e .` from a trusted source checkout for custom development). The source README documents `OPENAI_API_KEY` for OpenAI-backed runs. Choose a compatible completion function and an authorized evaluation before running the CLI; package installation alone does not provide local inference.

The pinned source manifest at commit `8eac7a7de5215c907fbddc30efdaf316913eccdd` (2026-04-14) declares package version `3.0.1.post1` and Python 3.9 or newer. This records a reviewed source version, **not** a claim about the latest available release or executed compatibility.

## Results, rights, and reproducibility

The CLI can record results in local JSONL logs; optional Snowflake integration has its own account and credential requirements. Some registry data uses Git LFS. The repository's software code is MIT-licensed, but `LICENSE.md` explicitly identifies bundled datasets subject to different licenses. Neither those assets nor third-party/user-submitted evaluation data automatically inherit unrestricted reuse rights.

Pin the source/package version, test cases and dataset snapshot, task/scorer configuration, model and completion-function version, sampling parameters, and any model-judge rubric before comparing outcomes. Scores only support conclusions within the measured tasks. API calls may transmit prompts and outputs and incur charges; secure credentials, enforce provider budgets and rate limits, and govern local or external result retention.

## Relations

- Produced by: [OpenAI](../../../../../../../producers/sub/o/sub/openai/)

## Official resources

- [OpenAI Evals repository](https://github.com/openai/evals)
- [Pinned evaluation CLI instructions](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/docs/run-evals.md)
- [Pinned package manifest](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/pyproject.toml)
- [Software license and dataset exceptions](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/LICENSE.md)
