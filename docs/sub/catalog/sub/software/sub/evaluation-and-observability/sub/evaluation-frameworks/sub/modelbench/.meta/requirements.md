# Documentation Requirements

## Requirements

- Identify ModelBench as MLCommons' independently installable open-source Python/CLI safety-evaluation framework and report generator, not the AILuminate published benchmark family, a dataset, a hosted model API, or a second identity for the bundled ModelGauge components.
- Preserve first-party MLCommons provenance with reciprocal `produced-by` / `produces` relations to the existing MLCommons organization entity.
- Explain the source-backed responsibility split: ModelGauge runs tests against configured systems under test (SUTs) and annotates model responses; ModelBench aggregates measurements by hazard/benchmark and generates reports. The two CLI entry points are distributed by the same source package.
- Record the source snapshot at commit `a4c8d6c928de6465db29d13561ad0ac26e667a43` (2026-10-30): `pyproject.toml` declares `modelbench` package version `1.0.0`, `>=3.12,!=3.12.5,<4` Python, `modelbench` and `modelgauge` scripts, and Apache-2.0 software licensing. This is a pinned manifest observation, not an assertion about the latest published release or runtime compatibility.
- Describe local source-checkout installation using `uv`, SUT/provider configuration and the `modelbench benchmark` CLI; the package does not provide free model inference, full official benchmark entitlements, or a universal scoring service.
- Disclose that the described official safety evaluation workflow requires approved credentials for the MLCommons `cheval` evaluator service. The documented Together AI example requires a separate provider account; other authorized SUTs can use supported hosted or self-managed backends.
- Distinguish quick reduced-instance trials from full official benchmark fidelity. Record benchmark/test snapshot, model/SUT revision, provider, evaluator, scoring parameters and hazard categories before comparing outcomes. Hazard scores do not establish blanket safety certification.
- Warn that prompts, completions, annotations, run journals and caches can contain sensitive or distressing material. Keep API keys and `config/secrets.toml` out of version control, restrict logs/results and retention, do not expose protected official prompt sets and avoid unnecessary raw-harmful-content review.
- Distinguish Apache-2.0 source-code terms from third-party model API terms, protected benchmark prompts, evaluator-service access and third-party data rights. Do not grant implied redistribution rights or claim paid/external access is included.
- Include pinned first-party sources for software identity, source manifest, setup and license. Do not imply that a benchmark, evaluator, API integration, local tests or complete catalog verification was executed.

## Validation

- Pinned first-party [README](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/README.md), [package manifest](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/pyproject.toml), [SUT guide](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/docs/suts-how-to.md) and [license](https://github.com/mlcommons/modelbench/blob/a4c8d6c928de6465db29d13561ad0ac26e667a43/LICENSE.md) support documented facts.
- The evaluation-framework category lists ModelBench once and the existing MLCommons producer has the reciprocal relation.
- The reader distinguishes ModelBench software, its bundled ModelGauge runtime, separately published AILuminate benchmarks, managed evaluator access, and independent model providers.
- No claim of executed evaluation, complete CI, current-release audit, full-catalog clean pass or implied rights to nonpublic test data.
