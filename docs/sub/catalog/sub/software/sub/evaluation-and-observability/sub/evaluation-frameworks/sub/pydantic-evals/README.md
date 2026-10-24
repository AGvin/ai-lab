# Pydantic Evals

Pydantic Evals is a Python library for evaluating stochastic functions, model calls and agent applications with datasets, test cases and evaluators. It is published as `pydantic-evals` within the Pydantic AI monorepo and can evaluate task functions written with other frameworks.

## Evaluation workflow

Define cases and expected outputs, choose built-in or custom evaluators, then run a task function against the dataset. The result is a report with scores, assertions and execution details that can be inspected locally or serialized. Optional Logfire integration supplies trace and report views.

Keep the dataset, task implementation, evaluator rubric and any judge/model settings fixed when comparing runs. A score describes those cases and evaluators; it does not establish general model quality. Model-based judges need their own provider access, credentials and budget.

## Release and operating boundary

The reviewed release is `pydantic-evals==2.57.0`, published on 2026-10-16 under the MIT license. That release requires Python 3.11 or newer and depends on the matching version of `pydantic-ai-slim` and on `logfire-api`; installing the full `pydantic-ai` distribution is unnecessary.

Install a pinned package with `python -m pip install "pydantic-evals==2.57.0"`, then define typed cases, evaluators and a matching task function. Add `pydantic-evals[logfire]==2.57.0` when the optional Logfire SDK integration is needed. Local report inspection does not require a Logfire account. Model, dataset and hosted-service terms remain separate from the library's MIT license.

Configure credentials, data destinations, sampling, redaction and retention before exporting traces or reports containing sensitive inputs, outputs or tool activity.

## Related entities

- [Pydantic](../../../../../../../producers/sub/p/sub/pydantic/) — producer.
- [Pydantic AI](../../../../../agent-frameworks/sub/pydantic-ai/) — agent framework in the same monorepo.
- [Pydantic AI Harness](../../../../../agent-frameworks/sub/pydantic-ai-harness/) — separate agent execution harness.
- [Pydantic Logfire](../../../observability-platforms/sub/pydantic-logfire/) — optional observability and evaluation-report destination.

## Official resources

- [Documentation](https://pydantic.dev/docs/ai/evals/evals/)
- [Package source](https://github.com/pydantic/pydantic-ai/tree/main/pydantic_evals)
- [Published 2.57.0 package](https://pypi.org/project/pydantic-evals/2.57.0/)
- [Release v2.57.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.57.0)
