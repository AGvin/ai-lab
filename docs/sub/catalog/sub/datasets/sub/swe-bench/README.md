# SWE-bench

SWE-bench is a dataset family built from real-world software-repository issues and repository states for evaluating systems that generate patches intended to resolve those issues.

## Dataset boundary

Dataset tasks remain distinct from the SWE-bench evaluation harness, Docker execution environment, leaderboard surfaces, scoring procedures, and generic software-engineering benchmark concepts. Source-backed variants such as full SWE-bench, Lite, Verified, Multimodal, and Multilingual are separate evaluation sets and must not be compared as if they were the same test set. `Verified` is a curated subset whose instances were reviewed by software engineers for solvability, not a quality label for the whole family.

Task repositories, issue and commit snapshots, container images, harness versions, dataset revisions, supported architectures, execution resources, and leaderboard policies are mutable or version-sensitive. Public repository-derived tasks also carry contamination and patch-leakage risk. SWE-bench evaluates repository-level software-engineering work rather than function-completion tasks such as HumanEval.

## Official resources

- [SWE-bench repository](https://github.com/SWE-bench/SWE-bench)
- [SWE-bench documentation](https://swebench.com/SWE-bench/)
- [SWE-bench on Hugging Face](https://huggingface.co/datasets/SWE-bench/SWE-bench)
