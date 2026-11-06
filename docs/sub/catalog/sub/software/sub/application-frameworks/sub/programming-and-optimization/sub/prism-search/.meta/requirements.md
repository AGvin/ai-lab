# Documentation Requirements

## Requirements

- Identify PRISM Search as a standalone Python optimization framework using pre-search fitness landscape diagnostics to choose permutation representations and mutation/search operators, not a model provider, benchmark score, or universal agent framework.
- Pin official README, pyproject.toml, code LICENSE and LICENSE-ARTIFACTS at source commit `07d36e0a9e137ada1bc53ae70b3c2eb099bc2055`.
- Describe `preflight` and `PRISM` entry points, correlation/fitness-distance diagnostics, selected operator, and the experimental conditions needed to reproduce behavior. The project describes empirical operating bands and explicitly does **not** claim universally superior search.
- Manifest identifies `prism-search` 0.1.0, Python >=3.10, NumPy as required runtime dependency and Inspect AI only as an optional evaluation extra. The optional Inspect task is not a second software identity and no run was conducted.
- Distinguish the **MIT software code license** from the **CC BY 4.0 research artifacts** in `experiments/`, `docs/`, selected deliverables and notebooks; any third-party datasets, source papers or hosted model terms must be reviewed independently.
- Discuss experiment reproducibility: seeds, fitness function, landscape representation, probe budgets, evaluator version, inference costs and data rights. Results depend on the target fitness landscape, not transferable proof of universal optimization.
- Do not claim package installation, running preflight, executing any optimization/evaluation, reproducibility audit, model-access confirmation or whole-catalog clean pass.

## Validation

- Pinned primary source, package manifest and two licensing files support the software/research-artifact boundary.
- One canonical entry under Programming and Optimization; no duplicate for optional Inspect AI evaluation.
