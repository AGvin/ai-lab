# Choosing Models for Coding

Use this guide to select models for code completion, implementation, debugging, review, refactoring, testing, architecture, and repository-scale agentic work.

## Translations

- English

## Status

Initial guidance verified on 2026-07-24. Model availability, pricing, tool support, and benchmark results can change; validate the exact model and coding environment before adoption.

## Start with the coding task

Do not choose a coding model from one aggregate score. Define the work first:

- inline completion or short code generation;
- bounded edits in one or several files;
- debugging from logs, tests, or runtime behavior;
- repository-scale implementation and refactoring;
- code review and defect detection;
- test generation and test repair;
- architecture and migration planning;
- long-running agentic coding with shell, browser, issue tracker, and repository tools.

The strongest model for architecture may not be the best low-latency completion model. A model that writes plausible code quickly may still be unsuitable for autonomous repository changes if it omits requirements, mishandles tools, or reports completion before verification.

## Required evaluation dimensions

### Correctness and acceptance

Measure:

- functional correctness against explicit acceptance criteria;
- compilation, type checking, linting, and test results;
- regression rate in unchanged behavior;
- correctness across edge cases and failure paths;
- security and data-handling implications;
- maintainability and consistency with repository conventions;
- cost per accepted result, including retries and review.

A generated patch is not complete until the relevant checks pass or unresolved limitations are reported explicitly.

### Repository understanding

Evaluate whether the model can:

- locate the correct implementation and related tests;
- follow existing architecture rather than inventing parallel abstractions;
- preserve naming, formatting, and dependency conventions;
- distinguish generated files, vendored code, migrations, and source files;
- reason across call sites, configuration, schemas, documentation, and localization;
- keep unrelated files out of the final diff.

Large context windows help only when retrieval, prioritization, and instruction retention remain reliable across the complete task.

### Tool and agent reliability

For agentic coding, test:

- shell-command selection and argument accuracy;
- patch application and file-edit reliability;
- structured-output and function-call validity;
- response to failing tests and tool errors;
- bounded retry behavior;
- ability to inspect the final diff;
- ability to verify remote repository state after writes;
- respect for approval boundaries and destructive-action controls.

Evaluate the complete agent scaffold, not the base model in isolation. Tool schemas, prompts, repository instructions, permissions, and environment feedback materially affect results.

### Framework and language fit

Use representative work from the actual stack. Include:

- dominant languages and framework versions;
- build tools and package managers;
- generated code and metaprogramming;
- legacy patterns and migration constraints;
- domain-specific APIs;
- repository size and monorepo structure;
- documentation and localization requirements.

A model can be strong on common benchmark languages and still perform poorly on a specialized framework or older codebase.

## Coding quality tiers

### Exploration

Use for feasibility checks, examples, API discovery, and rough alternatives. Manual review is mandatory.

### Concept draft

Use for implementation plans, prototype patches, test ideas, and migration sketches that are not yet ready to merge.

### Working result

Require the change to build or execute, satisfy primary acceptance criteria, and pass the relevant focused tests. Known limitations may remain documented.

### Production quality

Require repository-convention compliance, regression checks, security review where relevant, complete tests, documentation updates, and a clean final diff.

### Exceptional quality

Use stronger models or additional review passes when architecture, security, performance, maintainability, or user experience materially benefits from deeper analysis and polish.

## Initial model candidates

These are starting candidates, not universal rankings.

### GPT-5.6 Sol

**Recommendation:** Preferred frontier candidate for difficult repository-scale work, complex debugging, architecture, and long-running coding agents where maximum accepted-result quality matters more than minimum token cost.

OpenAI positions GPT-5.6 Sol for complex reasoning and coding and provides it through the API and Codex. The API supports tool use and configurable reasoning effort.

**Use when:**

- the task spans many files, tools, or repositories;
- architecture and implementation must be handled together;
- failures are expensive enough to justify frontier-model cost;
- the workflow can use Codex or a Responses API agent scaffold.

**Limitations:**

- hosted, paid, and provider-moderated;
- higher output cost than balanced or high-volume tiers;
- production behavior must be verified with the exact reasoning level and tool configuration;
- a large context window does not remove the need for scoped retrieval and diff review.

Sources: [GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model) and [OpenAI model catalog](https://developers.openai.com/api/docs/models).

### GPT-5.6 Terra

**Recommendation:** Preferred balanced candidate for routine professional coding and agent workflows when Sol-level capability is not economically justified.

OpenAI describes Terra as the balance point between intelligence and cost in the GPT-5.6 family.

**Use when:**

- most work is implementation, debugging, tests, and review rather than frontier-level architecture;
- the same hosted tool stack as Sol is useful;
- workload volume makes cost materially important;
- escalation to Sol can be reserved for difficult or failed tasks.

**Limitations:**

- still requires task-specific evaluation against Sol and lower-cost alternatives;
- hosted access, provider policy, and regional availability apply;
- a cheaper first pass can become more expensive if retries and escalation are frequent.

Sources: [GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model) and [GPT-5.6 availability](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/).

### Claude Sonnet 5

**Recommendation:** Preferred balanced candidate for coding-heavy and tool-heavy agents, especially in Claude Code or Anthropic-compatible workflows.

Anthropic describes Sonnet 5 as its most agentic Sonnet model, emphasizing planning, terminal and browser tools, coding, and long-running work.

**Use when:**

- repository and terminal workflows dominate;
- tool use and autonomous execution are central;
- Claude Code is already part of the development environment;
- a balance between frontier capability and operating cost is required.

**Limitations:**

- hosted and provider-moderated;
- vendor benchmark claims require validation on the target repository;
- prompt-injection defenses do not replace least privilege and human approval boundaries;
- pricing and rate limits can change after introductory periods.

Source: [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5).

### Qwen3-Coder

**Recommendation:** Preferred open-model family candidate for self-hosted or provider-hosted agentic coding experiments where deployment control, inspectability, or offline operation matters.

Qwen introduced Qwen3-Coder as an agentic coding model family with tool-use support and long-context variants. The flagship 480B-A35B model is not a practical single-GPU local model, so deployment decisions must name the exact smaller artifact, quantization, runtime, and hardware profile.

**Use when:**

- open weights or self-hosting are required;
- the team can benchmark an exact artifact on its own repositories;
- Qwen Code or an OpenAI-compatible coding scaffold is acceptable;
- privacy or offline operation outweighs hosted-model simplicity.

**Limitations:**

- family-level claims do not establish the quality of every smaller or quantized artifact;
- large variants require substantial infrastructure;
- tool-call behavior depends on templates, runtime, quantization, and scaffold integration;
- community fine-tunes and abliterated variants must be evaluated as separate artifacts.

Sources: [Qwen3-Coder announcement](https://qwenlm.github.io/blog/qwen3-coder/) and [Qwen Code documentation](https://qwenlm.github.io/qwen-code-docs/).

## Selection by workload

### Inline completion and high-volume edits

Prioritize latency, low interruption cost, predictable formatting, and editor integration. A smaller hosted tier or compact local model may be preferable to a frontier model.

### Debugging and defect isolation

Prioritize evidence use, hypothesis revision, log interpretation, test execution, and resistance to inventing causes. Require the model to distinguish observed facts from hypotheses.

### Repository-scale implementation

Prioritize instruction retention, dependency awareness, tool reliability, test iteration, and final-diff inspection. Use bounded subtasks and explicit acceptance criteria even with frontier models.

### Code review

Use a reviewer that is independent from the implementation pass when defect cost is material. Measure true-positive value, false-positive burden, severity calibration, and whether suggested changes preserve intended behavior.

### Refactoring and migration

Require behavior-preservation tests, staged changes, compatibility constraints, rollback strategy, and inspection for accidental scope expansion. Architecture strength alone is insufficient without disciplined verification.

### Agentic coding

Prefer a model and scaffold that can plan, edit, run checks, recover from failures, and stop only after verifying completion. Restrict destructive commands, credential access, deployment, and merge operations behind explicit approval policies.

## Local deployment and quantization

For local coding models, record:

- exact base model and artifact;
- parameter count and active parameter count for mixture-of-experts models;
- weight format and quantization;
- runtime and prompt or tool-call template;
- context length used in practice;
- model memory, KV-cache, and peak RAM or VRAM;
- tokens per second for prompt processing and generation;
- cold-start and reload time;
- acceptance rate on representative repository tasks.

Do not describe a quantized artifact as equivalent to the full model without task-specific evidence. The operational default may be a smaller quantization, while the best-quality option may require more memory or a hosted endpoint.

## Recommended evaluation set

Build a small repository-specific suite containing:

1. one bounded bug fix with a failing test;
2. one multi-file feature with explicit acceptance criteria;
3. one refactor that must preserve behavior;
4. one code-review task with seeded defects;
5. one framework-specific task;
6. one documentation or localization change;
7. one tool-failure recovery scenario;
8. one final-diff audit for unrelated changes.

Run each candidate with recorded model version, scaffold, prompts, tools, permissions, reasoning settings, runtime, hardware, and date.

## Decision rule

Choose the least expensive model and scaffold that consistently reaches the required quality tier within bounded retries.

Escalate when:

- the task exceeds the model's demonstrated repository or reasoning capability;
- repeated attempts fail the same acceptance criterion;
- review finds material omissions or regressions;
- security, architecture, or migration risk justifies an independent stronger model.

Do not keep retrying the same unsuitable model indefinitely. Retry cost, engineer review time, and failed tool actions belong in total cost.

## Related pages

- [AI Model Selection and Team Design](../../)
- [Choosing Models for AI Agents](../agents/)
- [Choosing Models for Orchestration](../orchestration/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../benchmarks/)
- [Disclaimer](../../../../../disclaimer/)
