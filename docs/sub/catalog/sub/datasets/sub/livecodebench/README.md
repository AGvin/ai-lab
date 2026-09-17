# LiveCodeBench

LiveCodeBench (LCB) is a continuously updated coding benchmark/dataset family with explicit versioned releases.

## Dataset boundary

Code generation, code execution, test-output prediction, self-repair, and other upstream scenarios are distinct evaluation slices when their datasets or results differ. Dataset releases remain separate from the LiveCodeBench runner, evaluation implementation, leaderboards, model adapters, and generic code-evaluation concepts. Recency is a contamination-mitigation strategy, not proof that every evaluated model is contamination-free.

Release membership, task counts, default-release aliases, evaluation timeouts, supported model adapters, and leaderboard results are mutable or version-sensitive.

## Official resources

- [LiveCodeBench](https://livecodebench.github.io/)
- [LiveCodeBench repository](https://github.com/LiveCodeBench/LiveCodeBench)
- [LiveCodeBench on Hugging Face](https://huggingface.co/livecodebench/)
