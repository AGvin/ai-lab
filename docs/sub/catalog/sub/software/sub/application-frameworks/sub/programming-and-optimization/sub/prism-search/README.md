# PRISM Search

**PRISM Search** is an MIT-licensed Python framework for selecting and executing permutation search strategies after measuring properties of a fitness landscape. Its name expands to **Predictive Protocol for Permutation Optimization via Landscape Diagnostics**.

## What it does

The pinned [first-party README](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/README.md) describes estimating one-step move autocorrelation, fitness–distance correlation and related characteristics *before* choosing a mutation operator or deciding whether structured search improves upon simpler sampling. Its `preflight` interface returns diagnostic recommendations, and `PRISM` exposes search machinery. The guidelines are empirically derived, not a guarantee that any operator wins on all landscapes.

The [source manifest](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/pyproject.toml) identifies `prism-search` 0.1.0 for Python >=3.10, using NumPy as its required dependency. Optional extras add plotting or Inspect AI-based evaluation scripts, including LLM instruction-order experiments. Those experiments and their results are research artifacts rather than a second copy of the PRISM software.

## Reproducibility and licensing

Before interpreting an optimization result, record the fitness function, representation, seed, probe budget, evaluator/model revision, prompt/data rights and any external inference costs. The repository separates licensing: its [software code is MIT](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/LICENSE), while identified experiment records, docs and deliverables have a distinct [CC BY 4.0 artifact license](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/LICENSE-ARTIFACTS). These terms do not automatically grant access to third-party papers, datasets, models or providers.

This is documentation supported by pinned repository evidence. No package installation, optimization run, model API call, full artifact reproducibility audit or whole-catalog clean pass was executed.

## Official source snapshot

- [Repository](https://github.com/bleymambwe/PRISM)
- [Pinned README](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/README.md)
- [Pinned Python manifest](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/pyproject.toml)
- [Pinned MIT LICENSE](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/LICENSE)
- [Pinned CC BY 4.0 artifact license](https://github.com/bleymambwe/PRISM/blob/07d36e0a9e137ada1bc53ae70b3c2eb099bc2055/LICENSE-ARTIFACTS)
