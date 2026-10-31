# Documentation Requirements

## Requirements

- Identify Pydantic Evals as the independently distributed `pydantic-evals` Python library for evaluating stochastic functions, model calls and agent/application behavior. It is developed within the Pydantic AI monorepo and works with task functions from other frameworks; its distribution identity must remain distinct from Pydantic AI, Pydantic AI Harness and Pydantic Logfire.
- Preserve Pydantic as the first-party producer, with an inverse `produces` relation. Do not create another producer for the monorepo, package registry publisher or named contributors.
- Explain the code-first boundary: datasets contain cases and evaluators; a task function is run against them and produces an evaluation report. Local Python execution, report serialization and optional telemetry/report destinations are distinct from a managed evaluation or observability service.
- Record the reviewed published package `pydantic-evals==2.57.0` dated 2026-10-16, tied to monorepo release `v2.57.0` and commit `54a31abfb7bb2a4354528ba4693ec2618afabf6e`. Treat this as a dated release observation, not a permanently latest-version claim. PyPI's production/stable classifier is publisher metadata, not a general guarantee.
- Preserve the released manifest's Python >=3.11 requirement and required matching-version `pydantic-ai-slim` dependency. The full `pydantic-ai` distribution is not required; this does not mean the library has no Pydantic AI code dependency. The `logfire` extra adds the Logfire SDK, while `logfire-api` is a core dependency.
- Provide a bounded setup path with a pinned Python package, typed cases, evaluators and a task function. Model-based judges or generators require their own configured provider, credentials, access and budget; deterministic/custom evaluators do not imply a hosted model service.
- Before comparing results, pin the package/runtime, task and dataset snapshot, expected outputs, evaluator/rubric configuration and any judge/model/provider settings. Report scores, assertions and execution outcomes separately; dataset results or judge opinions do not establish general model quality or production safety.
- Preserve the MIT license boundary for the library code. External models, datasets, provider services and the separately operated Logfire service retain their own licenses, access and commercial terms.
- Explain that optional traces/reports can contain inputs, outputs and tool activity. Configure the destination, credentials, sampling, redaction and retention before exporting sensitive evaluation data. Do not assume a Logfire account is required for local reports or that optional integration creates another software identity.
- Do not expand this identity into separate catalog items for individual evaluators, datasets, report objects, online evaluation modes, telemetry exporters or package extras.

## Validation

- The [published 2.57.0 distribution](https://pypi.org/project/pydantic-evals/2.57.0/) supplies separate wheel/sdist release records; its displayed publishing provenance and the [release tag](https://github.com/pydantic/pydantic-ai/releases/tag/v2.57.0) identify the same source commit.
- The tagged [package manifest](https://github.com/pydantic/pydantic-ai/blob/54a31abfb7bb2a4354528ba4693ec2618afabf6e/pydantic_evals/pyproject.toml), [package README](https://github.com/pydantic/pydantic-ai/blob/54a31abfb7bb2a4354528ba4693ec2618afabf6e/pydantic_evals/README.md) and [license](https://github.com/pydantic/pydantic-ai/blob/54a31abfb7bb2a4354528ba4693ec2618afabf6e/LICENSE) support the package identity, cross-framework boundary, dependencies and MIT licensing.
- The reader distinguishes the evaluation library, agent framework/harness and observability destination; it exposes setup and result limitations without implying executed runtime validation.
- The producer relation and inverse agree, all reader destinations resolve to canonical identities, and the category lists this child once.
