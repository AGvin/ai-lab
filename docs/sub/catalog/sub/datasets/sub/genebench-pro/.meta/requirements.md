# Documentation Requirements

## Requirements

- Identify GeneBench-Pro as OpenAI's research-level computational-biology benchmark/dataset for evaluating judgment-heavy agent analyses across genomics, quantitative biology, translational medicine, and related domains.
- Preserve its construction as 129 synthetic problems with controlled data-generating processes only while supported by current first-party evidence.
- Preserve the access boundary: the complete benchmark identity exists independently of public distribution, while OpenAI publicly releases 10 representative questions/case studies and has announced a separate 50-question subset for independent benchmarking.
- Keep the benchmark dataset identity distinct from evaluation results, model rankings, the isolated execution workspace/tool stack, and generic benchmark methodology.
- Treat question counts, public subsets, third-party access, scoring setup, and reported model results as mutable/version-sensitive facts.

## Validation

- Partial public release is not misrepresented as full open-source distribution of all 129 problems.
- GeneBench-Pro is not collapsed into the earlier GeneBench benchmark merely because it expands that work.
- Scores are not generalized across different model versions, reasoning settings, harnesses, or future benchmark revisions.

## Scoped original-source qualification — 2026-11-08

- **GeneBench-Pro** is OpenAI's original **June 30, 2026** research-level computational-genomics benchmark, a successor to GeneBench with **129 multi-stage synthetic-data evaluations** across **ten primary domains and 21 subdomains**. Each evaluation involves statistical/causal analysis, diagnostics and downstream research decisions; these are not single-question medical exams or a license to make clinical patient-care decisions.
- The publisher releases **ten representative problems publicly**, with **50 distinct held-out problems** furnished to an independent third-party evaluation and the remaining **69 retained internally**; the public Hub/case-study materials are not the full 129-problem corpus. Official synthetic data and deterministic targets aid reproducibility within a pinned isolated workspace, but published frontier-model results are not independently replicated here.
- The companion bioRxiv research preprint has a separate display license from the released task-data package. Do not infer commercial, redistribution or health-system clearance for withheld tasks, third-party assets, case reports or evaluation toolchains from the publication text. Full setup, model/harness revision, reasoning effort and scoring policy are required for score comparison.
- Original publisher sources: https://openai.com/index/introducing-genebench-pro/ ; https://openai.com/index/genebench-pro/case-studies/ ; https://huggingface.co/datasets/ajh-oai/genebench-pro-public-package .
- Source acceptance verifies the existing original benchmark family, date, task counts and restricted/public split only; no private tasks, experimental model run, clinical certification, independent rights/privacy/security/legal review, whole-catalog CI/renderer, clean or final gate.
