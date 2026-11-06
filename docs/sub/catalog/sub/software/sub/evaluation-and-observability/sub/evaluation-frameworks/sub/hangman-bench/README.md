# Hangman Benchmark

**Hangman Benchmark** (`hangman-bench`) is Matt Fisher's MIT-licensed game evaluation distributed as an [Inspect AI](https://inspect.ai-safety-institute.org.uk/) task package. It evaluates how an LLM plays Hangman through game tools; it is not a separate LLM provider or a standalone Inspect runtime.

## Evaluation

The [pinned README](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/README.md) documents `inspect eval hangman_bench/hangman` with options for language, difficulty, allowed mistakes and whether whole-word guesses are permitted. The `game_scorer` records wins by difficulty; the `oracle_scorer` replays decisions against the candidate-word posterior to identify moves that are provably wrong or fall below the available best choice. This more granular measure is not an exhaustive test of reasoning.

The pinned [package manifest](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/pyproject.toml) requires Python >=3.10 and `inspect-ai>=0.3.132`; model-provider access, prompts, game word lists and task parameters determine real run costs and reproducibility. The [MIT LICENSE](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/LICENSE) applies to code, not automatically to model APIs, user data or any third-party task assets.

No game evaluation, scorer regression, integration tests or whole-catalog clean pass were executed.

## Official source snapshot

- [First-party repository](https://github.com/MattFisher/hangman-bench)
- [README.md](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/README.md)
- [pyproject.toml](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/pyproject.toml)
- [LICENSE](https://github.com/MattFisher/hangman-bench/blob/7a797dccb75e65bb44de596c4306c346817d0523/LICENSE)
