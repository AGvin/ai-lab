# Documentation Requirements

## Requirements

- Identify HELM as the executable `crfm-helm` Python framework by Stanford's Center for Research on Foundation Models (CRFM), not the Stanford NLP Group/DSPy project, a hosted model API, or any one leaderboard/benchmark dataset.
- Pin source `63754d05db6f874e41a395880fb573890a13e791` (June 5, 2026) and its official [README](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/README.md), [Python package](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/pyproject.toml), and Apache-2.0 LICENSE. Current PyPI version or live benchmark status is not inferred from that commit.
- Give **maintenance mode since June 1, 2026** prominent decision-relevant placement, linked to the project's [maintenance policy](https://crfm-helm.readthedocs.io/en/latest/maintenance_mode/). A limited-maintenance lifecycle changes suitability for new long-lived integrations, and does not imply permanent abandonment or missing published leaderboards.
- The source documents `pip install crfm-helm` and `helm-run`, `helm-summarize`, `helm-server`; each run depends on pinned scenario/data, metric, model, API provider, judge settings and package version. Public leaderboard values cannot be generalized to different versions or reproduced without their exact configs.
- Distinguish CRFM research provenance from a separately minted Stanford CRFM producer entity: no matching, independently accepted frozen producer node is created in this package. Avoid inventing `produced-by` references to Stanford NLP Group just because both are Stanford-affiliated.
- Running evaluations may upload private prompts and model outputs to remote providers, incur costs, retrieve external datasets, and process protected data. Require authorized sources, credential controls, appropriate data processing and cost budgets.
- Respect Apache-2.0 only for covered software. Third-party model weights, evaluation datasets, external leaderboards, hosted APIs, bundled dependencies and outputs have separate terms.
- No installation, model benchmark reproduction, live model call, source-wide security or legal audit, CI suite or whole-catalog clean pass is claimed.

## Validation

- First-party source and maintenance policy support identity, lifecycle, CLI and licensing.
- Exactly one Evaluation Frameworks reader is indexed and no separate Stanford CRFM producer or duplicated benchmark entity is counted.
