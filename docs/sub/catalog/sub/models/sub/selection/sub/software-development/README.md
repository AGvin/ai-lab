# Software Development Model Selection

Choose models for software-development tasks by the exact work to be performed, the required acceptance tier, repository context, tool surface, and consequence of failure.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers model selection for code generation and editing, code understanding, debugging and repair, testing, code review, security engineering, software architecture, autonomous software engineering, and development/reliability analysis.

Use more specific child pages when a shortlist, evaluation suite, or acceptance criteria differ materially by task. Do not treat one broad coding ranking as valid for every software-development workload.

## Decision criteria

Evaluate the complete assignment rather than chat quality or benchmark rank alone:

- correctness against explicit acceptance criteria;
- omission and regression rate;
- repository and dependency understanding;
- tool selection, argument accuracy, and recovery after tool failure;
- instruction retention across multi-file work;
- verification discipline and final-diff quality;
- retries, engineer review, wall-clock time, and total cost per accepted result.

Start with the least expensive credible route for the required quality tier. Escalate when repeated failures indicate a capability ceiling, when review cost erases the apparent saving, or when architecture, security, or other high-consequence work requires stronger independent reasoning or review.

## Candidate evaluation set

These candidates preserve useful hypotheses from the legacy coding guides after current first-party identity/capability revalidation. They are **evaluation starting points, not a rank order or AI Lab proof of superiority**.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [Qwen2.5-Coder 3B Instruct](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-3b-instruct/) | Reproducible compact local baseline for bounded code generation/explanation, test drafts, small edits, and repetitive transforms | Provider-documented coding model; legacy AI Lab candidate hypothesis | Older compact baseline; repository-scale reasoning, long tool loops, and high-consequence changes require separate evidence or escalation |
| [Qwen2.5-Coder 7B Instruct](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-7b-instruct/) | Stronger compact local coding baseline for debugging, repair, tests, and bounded multi-file work | Provider-documented coding model; legacy AI Lab candidate hypothesis | More capable than the 3B baseline is a hypothesis to measure on the target suite, not a transferable ranking |
| [Phi-4 Mini Instruct](../../../reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/) | Compact multilingual mixed coding/reasoning assistant where a coding specialist is not the only workload | Provider-documented text/coding and multilingual capability; legacy AI Lab candidate hypothesis | Tool/function-calling support is surface/runtime-dependent; do not assume it from model identity alone |
| [Gemma 4 E4B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) | Compact multimodal coding experiments that need image, UI, document, or short-audio context in addition to text | Provider-documented multimodal, coding, and function-calling capability; legacy AI Lab candidate hypothesis | Not coding-specialized; exact runtime modality/tool support and coding quality must beat simpler specialists on the target workload |
| [GPT-5.6 Terra](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) | Hosted professional implementation, debugging, tests, review, and tool-assisted work where intelligence/cost balance matters | Current provider positioning; AI Lab task quality unverified here | Mutable hosted surface and accepted-result economics must be rechecked; escalate when the task exceeds measured capability |
| [GPT-5.6 Sol](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/) | Difficult architecture, repository-scale implementation, complex debugging, or other capability-first coding work | Current provider positioning for complex reasoning/coding; AI Lab task quality unverified here | Higher-capability positioning does not remove the need for independent verification or prove best cost per accepted result |
| [Claude Sonnet 5](../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) | Coding-heavy and tool-heavy agent workflows, including repository, terminal, and browser work | Current provider-documented coding/agentic strengths; AI Lab task quality unverified here | Provider benchmark claims are not independent evidence; exact scaffold, tokenizer/cost behavior, and tool loop must be measured |
| [Qwen3-Coder-Next](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-next/) | Self-hosted long-horizon coding-agent experiments, complex tool use, and recovery from execution failures | Provider-documented coding-agent model for local development; AI Lab task quality unverified here | Large total-weight footprint and runtime requirements can dominate deployment; active parameters are not a residency estimate |

Candidate membership does not imply current recommendation state. Pin the exact model/version/artifact or hosted ID, record the evaluation date and scaffold, and recheck mutable availability, features, limits, and prices before a material decision.

## Evidence minimum

Representative evaluation should include a bounded bug fix with a failing test, a multi-file feature, a behavior-preserving refactor, a review task with seeded defects, a framework-specific task, a tool-failure recovery case, and a final-diff audit for unrelated changes.

Record exact model/version/artifact identity and link its canonical facts from [Model Reference](../../../reference/). Workload-specific findings belong here; model identity and intrinsic technical facts do not.
