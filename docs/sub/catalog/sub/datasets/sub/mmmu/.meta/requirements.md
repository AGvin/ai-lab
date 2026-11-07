# Documentation Requirements

## Requirements

- Identify MMMU as the concrete multi-discipline multimodal benchmark/dataset for college-level expert knowledge and reasoning tasks.
- Keep MMMU distinct from MMMU-Pro, evaluation harnesses, leaderboards, hosted evaluation services, and generic multimodal-evaluation concepts.
- Preserve subject, subfield, modality, image-type, split, and question-count facts only at the dataset/version scope supported by current upstream sources.
- Treat the 2026 release of test answers, evaluation integrations, dataset revisions, and leaderboard state as mutable/version-sensitive facts.
- Do not compare MMMU and MMMU-Pro results as though they were scores on the same test set.

## Validation

- The page profiles MMMU rather than silently merging it with MMMU-Pro.
- Test-set availability and evaluation workflow claims remain current-source backed.
- Results are not compared across differing dataset variants or evaluation conditions without qualification.

## Scoped original-source qualification — 2026-11-08

- **MMMU** is the original expert-level multimodal knowledge/reasoning benchmark by the `MMMU-Benchmark` researchers. The public source reports **approximately 11.5K questions**, six disciplines, 30 subjects, 183 subfields and heterogeneous charts, diagrams, images, tables and maps. These are release-scope facts, not invariant row counts for all data versions.
- **MMMU-Pro** is a separate benchmark/data selection with distinct multimodal evaluation conditions, not an equivalent MMMU score. Maintainers announced public **MMMU test answers on 2026-02-12**, changing the local evaluation access and contamination boundary; evaluator integrations, leaderboards and scoring runners are not independent MMMU dataset identities.
- Original sources: https://github.com/MMMU-Benchmark/MMMU ; https://huggingface.co/datasets/MMMU/MMMU ; https://arxiv.org/abs/2311.16502
- Source acceptance covers original dataset identity, original public research and publisher maintenance/availability notices. No multimodal benchmark run, test-answer verification, original source-image rights audit, score assurance, full repository schema/cache/CI/render, clean or final credit.
