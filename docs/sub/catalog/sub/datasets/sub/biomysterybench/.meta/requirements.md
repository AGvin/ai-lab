# Documentation Requirements

## Requirements

- Identify BioMysteryBench as Anthropic's released bioinformatics research benchmark built from real-world biological datasets and expert-authored questions with verifiable ground truth.
- Preserve the current benchmark boundary around open-ended bioinformatics analysis with canonical tools/database access rather than reducing it to static multiple-choice scientific QA.
- Treat question/dataset inventory, container/tool access, external database availability, evaluation criteria, human-expert comparison, model roster, scores, and benchmark revisions as freshness-sensitive.
- Keep BioMysteryBench distinct from LifeSciBench, FrontierScience, GeneBench-Pro, generic bioinformatics datasets, and downstream scientific-agent systems.
- Do not generalize benchmark performance into independent scientific discovery capability, clinical validity, or biological truth outside the verified tasks.
- Preserve Anthropic provenance.

## Validation

- The node remains a concrete benchmark rather than a generic bioinformatics-research concept.
- Results remain scoped to the exact tool/container/data/evaluation setup.

## Scoped original-source qualification — 2026-11-08

- **BioMysteryBench** is Anthropic's original **2026** research benchmark of expert-authored, open-ended computational biology and bioinformatics investigations grounded in real biological datasets; it tests data analysis and tool use rather than multiple-choice recall or authorized clinical practice. The first-party **full 90-problem corpus is gated for evaluation**, whereas the publisher's public Hugging Face preview contains **five problems**, not the full benchmark.
- The official preview was **refreshed in July 2026 (v11)**, replacing two example problem IDs. Its source files include questions, per-task answer rubrics, permitted online databases and separately packaged input data. The evaluation prohibits discovering the answer via original dataset/paper accession lookup, while allowing normal reference-genome, gene/sequence and protein identification tools; change of corpus or allowed resources affects score comparability.
- First-party original sources: https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench ; https://huggingface.co/datasets/Anthropic/BioMysteryBench-preview ; https://huggingface.co/datasets/Anthropic/BioMysteryBench-full .
- Scoped source acceptance verifies one pre-existing benchmark identity, 90-gated versus five-public release boundaries, first-party science/rights limitations only; no biological data downloaded or executed, scientific discovery replicated, clinical/biological safety claim, complete license/security/privacy review, missing reader repair, global schema/cache/CI/render, clean or final gate.
