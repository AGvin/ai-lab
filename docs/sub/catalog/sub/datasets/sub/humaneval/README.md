# HumanEval

HumanEval is OpenAI's hand-written programming evaluation dataset introduced with the Codex evaluation work.

## Dataset boundary

HumanEval is a concrete problem set for checking generated function completions for functional correctness. The `human-eval` harness, pass@k reporting procedure, model results, prompts, and generic code-evaluation concepts remain separate from the dataset identity; HumanEval results do not by themselves establish repository-scale software-engineering capability.

Dataset files, harness behavior, execution environment, pass@k settings, mirrors, preprocessing, and scores are protocol- or version-sensitive. Because practical evaluation executes model-generated code, the harness must be treated as untrusted-code execution and run with robust isolation rather than ordinary host execution. Long-public benchmark material also carries contamination or exposure risk.

## Relations

- Produced by [OpenAI](../../../producers/sub/o/sub/openai/).

## Official resources

- [HumanEval repository](https://github.com/openai/human-eval)
- [Codex evaluation paper](https://arxiv.org/abs/2107.03374)
