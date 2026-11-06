# Documentation Requirements

## Requirements

- Identify ArxivRoll as a dynamic benchmark **pipeline** for creating private tasks from newer arXiv papers, assessing score contamination and publishing retired benchmark rounds, not the same identity as an ArxivRollBench dataset or the separately maintained harness fork.
- Use pinned repository README and pyproject.toml. The pinned manifest calls the project `arxivbench`, sets Python >=3.13 and lists dependencies; do not infer tested installability.
- Describe task construction as sequencing, cloze and next-fragment prediction; the release process includes crawling, parsing, constructing, evaluating and reporting round-specific outputs.
- Explicitly warn that the pinned README identifies hardcoded 2025a paths and a separate [harness-4-arxivrollbench](https://github.com/liangzid/harness-4-arxivrollbench) requirement. Running the scripts unchanged does not imply a current 2026a benchmark.
- **Rights block:** no repository-root LICENSE or LICENSE.md was present at the pinned snapshot. Treat code redistribution, modification and commercial reuse permissions as **not established**; public visibility is not a license. Check arXiv article-level terms before reproducing or redistributing source papers, HTML extracts or task text.
- Do not infer that private evaluation sets are shareable, contaminate held-out tasks by publishing them early, bypass arXiv rate limits or claim model contamination was measured from the software listing.
- Do not claim an end-to-end run, source-code legal clearance, corpus audit, model evaluations or a whole-catalog clean pass.

## Validation

- Preserve one canonical entry for this frozen candidate, indexed in Evaluation Frameworks.
- Only source-backed identity/materialization/acceptance evidence counts; no runtime, rights/redistribution clearance, CI or whole-catalog clean pass is implied.
