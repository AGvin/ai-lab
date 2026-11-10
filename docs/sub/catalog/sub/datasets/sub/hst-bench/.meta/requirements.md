# Documentation Requirements

## Requirements

- Present HST-Bench as the released Facebook Research benchmark dataset associated with the ICML 2026 work on scaling small agents through strategy auctions.
- Preserve the benchmark's 753 agentic-task metadata coverage across coding and deep-search tasks, including human completion-time metadata, without claiming that the repository redistributes all host-dataset question/answer content.
- Keep host datasets, enrichment scripts, evaluated agents, strategy-auction methods, and model results separate from the benchmark identity.
- Treat task inventory, host-dataset access requirements, enrichment behavior, licenses, and reported results as freshness-sensitive.

## Validation

- HST-Bench remains a benchmark/dataset identity rather than an agent framework or strategy-auction algorithm.
- Claims about task contents respect the repository's host-dataset reconstruction model.

## Scoped original-source qualification — 2026-11-08

- **HST-Bench** is Meta/Facebook Research's original evaluation dataset accompanying the **2026 ICML strategy-auction** research: **753 task-metadata records** spanning coding and deep-search tasks, with originating dataset IDs and average human completion-time fields. These records do not reproduce all source questions, correct answers or evaluation tests.
- Its official `hst-bench` repository publishes metadata-only coding/search CSVs plus enrichment scripts; reconstruction requires the original host datasets and their separate rights, including gated **GAIA** and **Humanity's Last Exam**. The HST-Bench release states **CC BY-NC 4.0**, which does not override those host licenses or access requirements. Benchmark strategy-auction paper results are separate from this corpus and are not independently rerun.
- First-party sources: https://github.com/facebookresearch/hst-bench ; https://arxiv.org/abs/2602.02751
- Source qualification covers this existing original 753-record metadata benchmark identity, original publication, task/host separation and noncommercial/gated-access conditions. No host corpus fetched, benchmark run, redistribution permission, full legal/security/freshness, repository CI/render, clean or final pass.
