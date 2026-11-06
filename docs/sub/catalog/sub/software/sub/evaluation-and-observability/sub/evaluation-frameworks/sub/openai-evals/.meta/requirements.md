# Documentation Requirements

## Requirements

- Identify OpenAI Evals as OpenAI's independently installable open-source Python evaluation framework, distributed as the `evals` package, rather than a hosted OpenAI Dashboard evaluation feature or a separate model/dataset identity.
- Keep exactly one software identity for the source repository `openai/evals`; the independent Inspect intake candidate `openai-evals-oss` maps to this entity. Evaluation templates and third-party registry datasets are not automatically separate canonical software entities.
- Preserve first-party provenance: OpenAI is the producer, with reciprocal `produced-by` / `produces` relationships using the existing canonical OpenAI producer node.
- Describe the supported entry points `oaieval` for a single eval and `oaievalset` for an eval set, the local registry of YAML configurations and implementations, and the `CompletionFn` abstraction. Do not imply this is a managed service or that installing the package alone supplies model inference.
- Record the source snapshot at commit `8eac7a7de5215c907fbddc30efdaf316913eccdd` (2026-04-14), whose `pyproject.toml` declares package version `3.0.1.post1` and Python >=3.9. This is a *source-manifest observation*, not proof that the version remains the latest published distribution.
- Explain the self-managed setup path: obtain approved provider/API access, secure `OPENAI_API_KEY` when using OpenAI-backed completion functions, install `evals` or install editable source for custom evaluation development, select an evaluation and completion function, then run the appropriate CLI. No real API or shell execution is claimed by the authored page.
- Separate locally written JSONL evaluation logs from optional Snowflake result storage; source-provided evaluation assets may use Git LFS and require fetching only the datasets a user is entitled to use.
- Preserve reproducibility requirements: record the exact code/package commit, evaluation/task configuration and dataset snapshot, completion function, model/provider identity and revision, generation parameters, scorer/judge rubric and run settings. A score only describes the evaluated scenario; do not infer production safety or general model quality from it.
- Preserve the repository MIT code license and the explicit LICENSE.md carve-out for bundled datasets; individual benchmark datasets and user submissions may have different licenses and permissions. Do not assert blanket redistribution rights to registry contents or user-provided examples.
- Warn that evaluation calls can incur third-party API charges, share prompts/results with configured providers, and write sensitive data to local logs or optional Snowflake storage. Use budget/rate limits, least-privilege keys, data minimization, and storage/retention controls.
- Include official, pinned references for project identity, source manifest, runtime instructions, and license, and keep hosted OpenAI Evals in the Dashboard conceptually separate from this OSS repository.

## Validation

- The pinned [source README](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/README.md), [package manifest](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/pyproject.toml), [CLI instructions](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/docs/run-evals.md) and [license with dataset exceptions](https://github.com/openai/evals/blob/8eac7a7de5215c907fbddc30efdaf316913eccdd/LICENSE.md) support the documented claims.
- Reader output distinguishes the original OSS framework, bundled evaluation registry, any third-party datasets, and separately hosted OpenAI evaluation tooling.
- OpenAI producer relation resolves in both directions, and the category lists the newly materialized child exactly once.
- No claim of executed evaluation, current release freshness audit, catalog-wide clean pass, or license rights beyond the cited software terms.
