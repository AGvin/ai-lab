# Stanford HELM Framework

**HELM (Holistic Evaluation of Language Models)** is the open-source Python framework developed by Stanford's **Center for Research on Foundation Models (CRFM)** for transparent, repeatable evaluation across model capabilities, efficiency, fairness, safety and other metrics.

**Maintenance status:** HELM entered [maintenance mode on June 1, 2026](https://crfm-helm.readthedocs.io/en/latest/maintenance_mode/). This is important for dependency planning: the repository and published leaderboards remain useful, but future feature development and support should not be presumed. Check the project's latest maintenance policy and releases before choosing it for a new long-lived deployment.

## Framework and evaluation workflow

The repository documents `pip install crfm-helm` followed by `helm-run` to execute configured benchmark scenarios, `helm-summarize` for metrics and `helm-server` to inspect results locally. It offers multiple benchmark and model-provider interfaces plus a frontend and published research leaderboards. The software itself is **not** the same identity as each tested model, benchmark dataset or the leaderboard result sets.

For reproducibility, fix the HELM source/package version, scenario, split, prompt, scorer/judge, model version, service API, sampling controls, run limit and evaluation input rights. Provider requests may incur charges and expose sensitive prompts or responses; budget and limit credentials, downloads and retention. Do not turn one published ranking into a universal quality guarantee.

The [source license](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/LICENSE) is Apache-2.0 for covered code, not third-party model/data licenses or hosted providers. No HELM evaluation or dependency audit was run for this profile.

## Official resources

- [HELM repository](https://github.com/stanford-crfm/helm)
- [Pinned first-party README](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/README.md)
- [Maintenance mode policy](https://crfm-helm.readthedocs.io/en/latest/maintenance_mode/)
- [Package metadata](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/pyproject.toml)
