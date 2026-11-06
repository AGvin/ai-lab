# Documentation Requirements

## Requirements

- Identify the installable `hangman-bench` package as a game-based LLM evaluation using UK AISI Inspect AI, distinct from the Inspect framework itself or independent model APIs.
- Pin README, pyproject.toml and MIT LICENSE. Pinned manifest specifies Python >=3.10 and `inspect-ai>=0.3.132`, with an Inspect task entry point; no actual installation is claimed.
- Describe `inspect eval hangman_bench/hangman` with configurable model, difficulty, guesses, word guessing and language.
- Explain `game_scorer` (win rate by difficulty) and `oracle_scorer` (measure of provably wrong or suboptimal letter choices against remaining candidate words); distinguish from universal logical reasoning.
- Note that externally connected model providers may incur charges and that language word lists, sampling and task configuration materially change outcomes.
- Do not claim a benchmark run, validated scores, runtime compatibility or complete CI, dataset licensing audit or whole-catalog clean pass.

## Validation

- Preserve one canonical entry for this frozen candidate, indexed in Evaluation Frameworks.
- Only source-backed identity/materialization/acceptance evidence counts; no runtime, rights/redistribution clearance, CI or whole-catalog clean pass is implied.
