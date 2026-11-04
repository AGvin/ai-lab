# Documentation Requirements

## Requirements

- Identify `inspect-india-evals` as an independently packaged India-focused Inspect AI evaluation suite, not the core UK AISI Inspect framework, general model, or provider service.
- Pin the project's README and pyproject.toml at the referenced Git commit. Manifest `version=0.1.0`, `requires-python >=3.10`, `inspect-ai` and `pandas`; it declares Apache-2.0 via metadata, and the README also states Apache 2.0. A repository-root LICENSE file is **not present** in the pinned snapshot; do not invent a separate signed license file or assert dataset redistribution rights.
- Describe tasks covering Indic multilingual factual performance, BharatBBQ bias, safeguards/jailbreaks, Indian digital public infrastructure (DPI) and cultural knowledge, with an aggregate India Fairness Index. This index summarizes configured suite dimensions and is not a universal measurement of fairness.
- Explicitly carry the first-party README's known limitation: pilot safety/jailbreak scores in the referenced preprint predate the independent judge-model correction and are **invalid pending independent-judge reruns**.
- Note documented discrepancies between paper and current datasets (DPI evaluation English-only, cultural set currently smaller than projected, BharatBBQ categories differ). Use the repository files when dataset and preprint counts conflict.
- Keep evaluation data, LLM judges, regional coverage, provider credentials, run logs, sensitive prompts and source-ownership as separate boundaries. Scores need pinned dataset/config/judge/model versions.
- Do not claim rerunning the pilot, validating data rights, model or judge calls, independent reproduction, full CI or whole-catalog clean pass.

## Validation

- Match exact frozen candidate and keep this software identity distinct from benchmark data, operated services and parent frameworks.
- Verify official pinned upstream evidence and one matching category index entry; record unresolved rights or result-validity limits rather than assuming completeness.
