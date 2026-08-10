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

## Evidence minimum

Representative evaluation should include a bounded bug fix with a failing test, a multi-file feature, a behavior-preserving refactor, a review task with seeded defects, a framework-specific task, a tool-failure recovery case, and a final-diff audit for unrelated changes.

Record exact model/version/artifact identity and link its canonical facts from [Model Reference](../../../reference/). Workload-specific findings belong here; model identity and intrinsic technical facts do not.
