# Choosing Models for Coding

Choose the least expensive model and scaffold that reliably reaches the required coding quality tier within bounded retries.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Pilot table layout verified on 2026-07-26. Model availability, pricing, artifacts, benchmarks, ecosystem maturity, and task quality can change; validate the exact model and deployment before adoption.

## Quick picks

| Need | First route | Model type | Why start here | Escalate when |
| --- | --- | --- | --- | --- |
| Lowest-footprint local coding assistant | [Qwen2.5-Coder 3B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/3b-instruct/) | Coding-specialized instruct model | Compact open-weight baseline for bounded generation, explanations, tests, and small edits | Repeated omissions, weak repository understanding, or multi-step tool work increase review cost |
| Stronger compact local coding route | [Qwen2.5-Coder 7B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/7b-instruct/) | Coding-specialized instruct model | More capacity than the 3B route while remaining in the SLM comparison group | Architecture, high-risk changes, or autonomous repository work exceed measured reliability |
| Compact multilingual mixed assistant | [Phi-4 Mini Instruct](../../../../../../../software/sub/models/sub/microsoft/sub/phi/sub/phi-4/sub/mini-instruct/) | General-purpose instruct model with reasoning and coding capability | Useful when coding is combined with multilingual instructions, reasoning, and general assistant work | A coding specialist wins representative tests or the compact route needs repeated correction |
| Balanced hosted professional coding | [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/) | General-purpose reasoning, coding, and tool-use model | Hosted balance for implementation, debugging, tests, review, and tool-assisted workflows | Difficult architecture, repeated failure, or high consequence justifies a stronger route |
| Difficult repository-scale or architecture work | [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) | Flagship general-purpose reasoning and coding model | Capability-first route for complex multi-file, multi-tool, and high-risk work | Use a specialist or independent reviewer when domain or defect risk requires it |
| Anthropic-centered coding agents | [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose agentic coding and reasoning model | Natural candidate for Claude Code and Anthropic-compatible tool workflows | Cost, availability, scaffold behavior, or task evidence favors another route |
| Self-hosted long-horizon coding agent | [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) | Coding-agent specialist | Open-weight agentic route with long context and explicit tool-work orientation | Infrastructure, memory residency, runtime support, or quality does not justify the 80B MoE model |

## Economical SLM candidates

This table contains only [Small Language Models](../../../../../concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab coding context. SLM is an economy-oriented filter, not proof of lower total cost: measure hardware, hosted price when applicable, throughput, quality, retries, engineer review, and accepted-result cost.

| Model | Model type | Parameters | [Architecture](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) | Access and license | Best fit | Main limitation | Sources |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| [Qwen2.5-Coder 3B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/3b-instruct/) | Coding-specialized instruct | 3.09B | Dense | Open-weight; Qwen Research License | Small local assistant, bounded edits, code explanation, test drafts, repetitive transformations | Lowest capability ceiling of this shortlist; verify instruction retention and repository context | [Official release](https://qwenlm.github.io/blog/qwen2.5-coder-family/) · [Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct) |
| [Phi-4 Mini Instruct](../../../../../../../software/sub/models/sub/microsoft/sub/phi/sub/phi-4/sub/mini-instruct/) | General-purpose instruct with reasoning and coding capability | 3.8B | Dense | Open-weight; MIT | Multilingual mixed workloads, compact reasoning, function-calling experiments, coding plus general assistance | Not coding-specialized; a code model may deliver better accepted-result quality | [Official report](https://www.microsoft.com/en-us/research/publication/phi-4-mini-technical-report-compact-yet-powerful-multimodal-language-models-via-mixture-of-loras/) · [Hugging Face](https://huggingface.co/microsoft/Phi-4-mini-instruct) |
| [Qwen2.5-Coder 7B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/7b-instruct/) | Coding-specialized instruct | 7.61B | Dense | Open-weight; Apache-2.0 | Stronger compact coding assistant, debugging, bounded multi-file changes, tests, and repair | Higher memory and latency than 3B-class routes; still requires human review for repository-scale work | [Official release](https://qwenlm.github.io/blog/qwen2.5-coder-family/) · [Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) |

Do not mix an LLM into this table because it has a small active-parameter count, a compact quantization, or a low hosted price. For example, Qwen3-Coder-Next remains an LLM with 80B total and 3B active parameters; active parameters do not represent storage or memory residency.

## Broader coding candidates

| Model | Model type | [Scale](../../../../../concepts/sub/model-classification/sub/language-model-scale/) | Architecture | Access | Best fit | Main trade-off |
| --- | --- | --- | --- | --- | --- | --- |
| [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/) | General-purpose reasoning, coding, multimodal, and tool-use model | Unclear; provider does not publish a parameter-based classification | Undisclosed | Hosted proprietary API | Routine professional implementation, debugging, tests, review, and tool workflows | Usage cost and data exposure; weaker accepted-result quality than a stronger route can erase token savings |
| [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose agentic coding and reasoning model | Unclear; provider does not publish a parameter-based classification | Undisclosed | Hosted proprietary API and products | Tool-heavy coding agents, Claude Code, long-context implementation and review | Hosted-only operation, mutable pricing and limits, scaffold-specific behavior |
| [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) | Flagship general-purpose reasoning and coding model | Unclear; provider does not publish a parameter-based classification | Undisclosed | Hosted proprietary API | Difficult architecture, complex debugging, repository-scale implementation, and high-consequence work | Highest request price among the listed hosted routes; capability must justify the premium |
| [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) | Coding-agent specialist | LLM | Sparse — MoE; 80B total, 3B active | Open-weight; self-hosted | Long-horizon coding agents, complex tool use, private deployment, and runtime control | Large memory residency and infrastructure burden despite low active-parameter count; [official artifact](https://huggingface.co/Qwen/Qwen3-Coder-Next) |

## Workload view

| Workload | Start with | Required evidence before adoption |
| --- | --- | --- |
| Bounded generation, explanation, or test draft | Economical SLM table | Correctness, formatting, latency, review time, and failure rate on representative prompts |
| Debugging from logs and tests | Qwen2.5-Coder 7B, Phi-4 Mini, or a balanced hosted route | Hypothesis revision, evidence use, resistance to invented causes, and test-backed repair |
| Multi-file implementation | Balanced hosted model or validated stronger local model | Instruction retention, dependency handling, conventions, tests, and clean final diff |
| Repository-scale refactoring or migration | GPT-5.6 Terra, Claude Sonnet 5, or GPT-5.6 Sol according to risk | Behavior-preservation tests, staging, rollback, architecture consistency, and accepted-result cost |
| High-risk architecture, security, or repeated failure | GPT-5.6 Sol plus independent review where justified | Explicit threat or failure analysis, verification, regression coverage, and approval boundaries |
| Self-hosted agentic coding | Qwen3-Coder-Next or another validated agent specialist | Runtime support, tool-call accuracy, memory residency, recovery, stopping behavior, and final-diff verification |

## Classification and table rules

- **Model type** describes task specialization, such as coding-specialized, general-purpose, reasoning, multimodal, embedding, or reranking. It is independent from scale and architecture.
- **[SLM or LLM](../../../../../concepts/sub/model-classification/sub/language-model-scale/)** describes relative language-model scale in the stated comparison context, not local versus hosted deployment.
- **[Dense, sparse, or MoE](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)** describes parameter activation architecture, not quality or hardware fit.
- For [Mixture of Experts](../../../../../concepts/sub/model-architectures/sub/mixture-of-experts/) models, record total and active parameters separately.
- [Frontier status](../../../../../concepts/sub/model-classification/sub/frontier-models/) requires current task-scoped evidence and a verification date.
- [Ecosystem status](../../../../../glossary/#model-ecosystem-status) describes adoption and tooling maturity, not coding quality.

## Decision and escalation rule

Start with the smallest credible route for the required quality tier. Include model or API cost, infrastructure, prompt processing, retries, failed tool actions, engineer review, and regression risk in total cost.

Escalate when the task exceeds demonstrated capability, repeated attempts fail the same criterion, review finds material omissions or regressions, or architecture and security risk justify a stronger independent route. Do not retry an unsuitable economical model indefinitely.

## Evaluation minimum

Test at least:

1. a bounded bug fix with a failing test;
2. a multi-file feature with explicit criteria;
3. a behavior-preserving refactor;
4. a review task with seeded defects;
5. a framework-specific task;
6. a tool-failure recovery scenario;
7. a final-diff audit for unrelated changes.

Record the exact model and artifact, model type, scale, architecture, scaffold, prompts, tools, permissions, runtime, hardware, context, date, acceptance rate, and total accepted-result cost.

## Related pages

- [AI Model Selection and Team Design](../../)
- [Practical AI User Scenarios](../practical-user-scenarios/)
- [Model Selection Methodology](../methodology/)
- [Small and Large Language Models](../../../../../concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../../../concepts/sub/model-architectures/sub/mixture-of-experts/)
- [Frontier Models](../../../../../concepts/sub/model-classification/sub/frontier-models/)
- [Choosing Models for AI Agents](../agents/)
- [Choosing Models for Orchestration](../orchestration/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [General repository disclaimer](../../../../../../../disclaimer/)
