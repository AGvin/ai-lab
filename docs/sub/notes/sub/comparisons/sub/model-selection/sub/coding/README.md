# Choosing Models for Coding

Select models for completion, implementation, debugging, review, refactoring, testing, architecture, and repository-scale agentic work.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Initial guidance verified on 2026-07-24. Model availability, pricing, tools, benchmark results, frontier status, and ecosystem maturity can change; validate the exact model, scaffold, and repository before adoption.

## Classification vocabulary

Use independent classification fields only when they improve a coding decision:

- [SLM or LLM](../../../../../concepts/sub/model-classification/sub/language-model-scale/) describes relative language-model scale in the stated comparison context, not local or hosted deployment.
- [Dense, sparse, or MoE](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) describes parameter activation architecture, not capability tier or hardware fit.
- [Frontier status](../../../../../concepts/sub/model-classification/sub/frontier-models/) requires current, task-scoped evidence and a verification date.
- [Ecosystem status](../../../../../glossary/#model-ecosystem-status) describes adoption and tooling maturity, not coding quality.

For MoE models, record total and active parameters separately. Active parameters are not a storage or VRAM estimate and do not determine whether the model is an SLM or LLM.

## Start with the coding task

Distinguish:

- inline completion or short generation;
- bounded edits in one or several files;
- debugging from logs, tests, or runtime behavior;
- repository-scale implementation and refactoring;
- code review and defect detection;
- test generation and repair;
- architecture and migration planning;
- long-running agentic coding with shell, browser, issue tracker, and repository tools.

The best architecture model may not be the best low-latency completion model. A fast model may still be unsuitable for autonomous changes when it omits requirements, mishandles tools, or reports completion before verification.

## Required evaluation dimensions

### Correctness and acceptance

Measure functional correctness, compilation, type checking, linting, tests, regressions, edge cases, security, maintainability, repository conventions, and cost per accepted result.

A patch is not complete until relevant checks pass or unresolved limitations are reported explicitly.

### Repository understanding

Evaluate whether the model can locate the right implementation and tests, preserve architecture and conventions, distinguish generated or vendored files, reason across call sites and configuration, update documentation or localization when required, and keep unrelated files out of the diff.

Large context helps only when retrieval, prioritization, and instruction retention remain reliable.

### Tool and agent reliability

Test shell and patch accuracy, function calls, structured output, recovery from failed checks, bounded retries, final-diff inspection, remote-state verification, and respect for approval boundaries.

Evaluate the complete scaffold: tool schemas, prompts, repository instructions, permissions, runtime, and environment feedback materially affect results.

### Framework and language fit

Use representative work from the actual languages, framework versions, build tools, generated code, legacy patterns, domain APIs, and repository structure. Common-language benchmark strength does not prove quality on a specialized or older stack.

## Coding quality tiers

- **Exploration** — feasibility, examples, and rough alternatives; manual review required.
- **Concept draft** — plans, prototypes, test ideas, and migration sketches not ready to merge.
- **Working result** — builds or executes, satisfies primary criteria, and passes focused tests.
- **Production quality** — conventions, regression checks, security where relevant, tests, documentation, and clean diff.
- **Exceptional quality** — additional architecture, performance, maintainability, security, or UX polish justified by value.

## Candidate routes

These are starting candidates, not universal rankings.

### GPT-5.6 Sol

**Recommendation:** Preferred frontier candidate for difficult repository-scale work, architecture, complex debugging, and long-running agents when accepted-result quality matters more than minimum request price.

Use when work spans many files, tools, or repositories; architecture and implementation must be handled together; or failure cost justifies a flagship route.

Limitations: hosted, paid, provider-moderated, and sensitive to the exact reasoning level, tools, retrieval, and approval scaffold.

Canonical page: [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/).

### GPT-5.6 Terra

**Recommendation:** Preferred balanced candidate for routine professional implementation, debugging, tests, and review when Sol-level capability is not economically justified.

Use a measured escalation policy to Sol for architecture, repeated failure, or high-risk work. Lower token price is not lower accepted-result cost when retries and review increase.

Canonical page: [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/).

### Claude Sonnet 5

**Recommendation:** Preferred balanced candidate for coding-heavy and tool-heavy agents, especially in Claude Code or Anthropic-compatible workflows.

Validate on the actual repository, permissions, terminal and browser tools, prompt-injection boundaries, rate limits, and price snapshot.

Canonical page: [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/).

### Qwen3-Coder

**Recommendation:** Preferred open-model family candidate when self-hosting, inspectability, offline operation, or deployment control matters.

Name the exact version, format, quantization, runtime, context, hardware, and tool template. Family-level claims do not establish the quality of a smaller or quantized artifact.

The current [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) page records it as an LLM with sparse MoE architecture, 80B total parameters, and 3B active parameters. Its frontier and ecosystem status remain unassessed rather than inferred from architecture or release position.

Canonical pages: [Qwen3-Coder](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/) and [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/).

## Selection by workload

| Workload | Prioritize |
| --- | --- |
| Inline completion | latency, interruption cost, formatting, editor integration |
| Debugging | evidence use, hypothesis revision, logs, tests, resistance to invented causes |
| Repository implementation | instruction retention, dependencies, tools, test iteration, final diff |
| Code review | true-positive value, false-positive burden, severity, independence |
| Refactoring and migration | behavior-preservation tests, compatibility, staging, rollback |
| Agentic coding | planning, safe editing, verification, failure recovery, correct stopping |

Use a reviewer independent from the implementation pass when defect cost is material. Reusing the same model with another prompt offers weaker independence and must be labeled accordingly.

## Local deployment and quantization

Record:

- exact base model, artifact, format, and quantization;
- [scale class](../../../../../concepts/sub/model-classification/sub/language-model-scale/) and comparison context;
- [architecture](../../../../../concepts/sub/model-architectures/sub/dense-and-sparse-architectures/);
- total and active parameters for [Mixture of Experts](../../../../../concepts/sub/model-architectures/sub/mixture-of-experts/) models;
- runtime and prompt or tool template;
- practical context length;
- model memory, KV cache, peak RAM and VRAM;
- prompt-processing and generation throughput;
- cold-start and reload time;
- acceptance rate on representative tasks.

Do not treat a quantized artifact as equivalent to the full model without task-specific evidence. Quantization does not change the underlying SLM or LLM label or dense versus MoE architecture.

## Recommended evaluation set

Include:

1. a bounded bug fix with a failing test;
2. a multi-file feature with explicit criteria;
3. a behavior-preserving refactor;
4. a review task with seeded defects;
5. a framework-specific task;
6. a documentation or localization change;
7. a tool-failure recovery scenario;
8. a final-diff audit for unrelated changes.

Record model version, scaffold, prompts, tools, permissions, reasoning settings, runtime, hardware, and date.

## Decision rule

Choose the least expensive model and scaffold that consistently reaches the required quality tier within bounded retries.

Escalate when the task exceeds demonstrated capability, repeated attempts fail the same criterion, review finds material omissions or regressions, or architecture and security risk justify a stronger independent route.

Do not retry the same unsuitable model indefinitely. Retry cost, engineer review time, and failed tool actions belong in total cost.

## Related pages

- [AI Model Selection and Team Design](../../)
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