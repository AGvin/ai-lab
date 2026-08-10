# Agents and Automation Model Selection

Choose models for tool-using, multi-step, and agentic execution by evaluating the complete loop rather than chat quality alone.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers tool use and function calling, general agents, browser/desktop/mobile computer use, voice agents, planning and execution, and long-running task execution.

Small or inexpensive models may be useful as bounded workers, routers, extractors, or formatters without being reliable primary agents. Open weights, long context, low token price, or an `agentic` product label do not establish long-horizon reliability.

## What to evaluate

Evaluate the complete execution loop with the same tools, permissions, environment snapshot, initial context, and stopping rules:

- planning and task decomposition;
- tool selection and argument accuracy;
- structured-output reliability;
- recovery after tool or environment failures;
- context and state retention across long workflows;
- unnecessary loops, duplicate actions, and token use;
- compliance with permissions and human-approval boundaries;
- terminal acceptance, retries, corrections, wall-clock time, and total cost per accepted result.

Include adversarial and degraded cases such as missing files, timeouts, conflicting instructions, stale documentation, prompt injection, and failed verification.

Use application-level trust boundaries, least privilege, explicit stopping rules, and independent verification where risk requires it. Model safeguards are not a substitute for those controls.

Link intrinsic model facts from [Model Reference](../../../reference/) and keep agent-workload evidence here.
