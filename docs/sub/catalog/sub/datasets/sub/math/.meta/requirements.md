# Documentation Requirements

## Requirements

- Identify MATH as the original research dataset from Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song and Jacob Steinhardt, as documented by the authors' repository and original paper.
- The 2021 original paper describes 12,500 competition-mathematics problems, with step-by-step worked solutions and an original 7,500 training/5,000 test split. Preserve this original release scope and distinguish it from later repackaged/test-only splits and datasets.
- Distinguish the original MATH questions and solutions from AMPS auxiliary pretraining, OpenAI's later selected MATH-500 evaluation subset, PRM800K's 800,000 step correctness labels, benchmark protocols, graders and result tables.
- Source MATH-500 as an explicit derived subset of the original MATH test set using an exact reciprocal MATH `has-derivative` / MATH-500 `derived-from` pair. This denotes dataset subset lineage, **not** a claim about model training.
- Attribute the original research dataset to the named research authors without inventing a corporate producer or treating OpenAI's later subset selection as original-question authorship.
- The original repository contains loader/evaluation code and an MIT LICENSE describing software and documentation. Neither that file nor the linked third-party dataset distribution is independent evidence that all contest problems have the same unrestricted redistribution grant. Check source question rights and attribution before republishing data.
- Pin specific original data version, train/test partition, selected questions, prompt, answer normalization, scoring convention and model contamination controls when reporting results. Exposure to these publicly released evaluation items limits claims of clean held-out performance.
- Competing mathematical problem benchmarks test different domains and difficulties; do not infer broad mathematical competence, safety or robustness from MATH-only metrics.
- Preserve first-party research authorship, original repository/paper, repository code license and explicitly related MATH-500 subset. No exhaustive beneficial ownership, current indirect holdings or sanctions audit was conducted.

- Preserve OpenAI's PRM800K as a separate human-annotated process-supervision dataset **derived from MATH source problems**, with one original MATH `has-derivative` ↔ PRM800K `derived-from` reciprocal data-lineage pair. Its model-generated intermediate-step labels and phase-specific sampling are new annotations, **not** a second MATH problem source, a MATH-500 subset, or proof of any model being trained on it. Original contest-question rights must be evaluated separately.

## Validation

- One original MATH source-dataset identity separate from MATH-500, PRM800K labels, AMPS and evaluation harnesses; no duplicate catalog credit for subsets or mirrors.
- Exact reciprocal has-derivative/derived-from dataset relation and correct canonical links in both dataset readers and dataset index.
- Licensing notes never misrepresent a MIT software repo grant as unrestricted rights over all original competition questions. No full schema/cache/CI or final renderer credit for bounded content/link checks.

## Scoped original-source qualification — 2026-11-08

- **MATH** is the original **2021** mathematics competition question-and-solution corpus by **Hendrycks et al.**, with **12,500** released problems in the original paper (**7,500 training / 5,000 test**). It is distinct from auxiliary **AMPS** pretraining data, the later OpenAI-curated **MATH-500** test subset, and **PRM800K** step-level labeled model trajectories; dataset lineage does not equate their question rights or evaluation contracts.
- The researchers' repository provides original authorship/publication, loaders and evaluator, while linking a separate data download. Its MIT repository software/documentation license does **not** independently clear all original third-party competition math problems or test solutions. Reproductions must pin the data revision, answer-equivalence grader and split.
- Verified original sources: https://github.com/hendrycks/math ; https://arxiv.org/abs/2103.03874 ; source lineage: https://github.com/openai/prm800k
- Source qualification covers the original MATH identity, historic study/data splits and derivative boundaries only. No underlying problem-data redistribution, independent mathematical answer verification, model execution, rights/legal/privacy audit, whole-repository schema/cache/CI/render, clean or final acceptance.
