# Documentation Requirements

## Requirements

- Identify EleutherAI's Language Model Evaluation Harness as the independently installable MIT-licensed `lm-eval` benchmark execution and evaluation framework, not a trained model, benchmark dataset, or Hugging Face Open LLM Leaderboard service.
- Preserve its multiple standardized language-model task definitions, few-shot prompt/configuration controls, scoring/aggregation and plugin backends for local Hugging Face models, vLLM, API-served models and third-party extensions. Supported tasks and backend interfaces are release-sensitive, not guarantees of exact model/metric equivalence.
- Preserve release-specific compatibility: v0.4.13 was published 2026-08-31 and upstream 2026-09 notes registerable plugin entry points; CLI restructuring (`run`, `ls`, `validate`) and optional backend extras were documented in 2025-12. Do not present old pre-refactor commands as universally valid.
- Pin harness commit/package version, registered plugins, task YAML/revision, dataset split/licensing, prompt template, tokenization and chat-template settings, backend/model/quantization, few-shot samples, scoring aggregation, random seed and model runtime to reproduce results.
- Distinguish the framework's task definitions and leaderboard integrations from independently authored datasets and MLPerf, LLM-as-a-judge/agent interactive suites, and full multimodal `lmms-eval` as a separate project. The upstream expressly labels selected multimodal backends experimental/prototype.
- Account for model API cost, evaluation-set contamination, remote data sharing, stochastic variation and differences in quantized or GGUF runtime handling; benchmark outcomes are not portable across incompatible backend/tokenizer/settings revisions.
- Attribute the maintained first-party repository to the EleutherAI research collective and preserve the reciprocal producer relation.

## Validation

- The official EleutherAI upstream confirms released 0.4.x harness, package/backend use, 2025/26 CLI and plugin changes.
- The `produced-by` link has the exact EleutherAI producer inverse.
