# Documentation Requirements

## Requirements

- Identify TIGER AI Lab as the current upstream steward of the represented released AI evaluation benchmark, using official project sources.
- Distinguish original paper contributors, data annotators, dataset authors and participating model submitters from current repository or project stewardship.
- Avoid turning auxiliary benchmark harness packages, leaderboards, version-specific subsets or submissions into duplicate producer identities.
- Keep revisions, methodology, licensing, dataset access and organizational ownership freshness-sensitive.
- Preserve this source-backed identity and provenance context: TIGER AI Lab is the Text and Image GEnerative Research lab whose official organization describes its University of Waterloo base. The lab publishes the represented MMLU-Pro benchmark through its first-party repository and the linked TIGER-Lab dataset distribution.
- Explain the following operating and decision boundary: Separate research authorship and benchmark maintenance from third-party model submissions and live leaderboard operation. Reproduction requires the chosen dataset revision, prompt and answer-extraction protocol; original MMLU and MMLU-Pro scores are not interchangeable. The official MMLU-Pro dataset card records its license, while other lab datasets and software require their own licensing checks.
- Support the producer context with these first-party sources: <https://github.com/TIGER-AI-Lab>, <https://github.com/TIGER-AI-Lab/MMLU-Pro>, <https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro>.

## Validation

- Every `produces` relation inverses a concrete benchmark's `produced-by` relation.
- Benchmark scores are not attributed to the project's producer as independent model quality results.
