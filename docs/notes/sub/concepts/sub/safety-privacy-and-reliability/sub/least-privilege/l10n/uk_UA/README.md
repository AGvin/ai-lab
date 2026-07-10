<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5dac9198999e69689aa9e8d80150b4a346b4cec9
  mode: copy-through
-->

# Least Privilege

Granting an AI system only the permissions required for its current task.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Granting an AI system only the permissions required for its current task. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Least privilege grants only the permissions needed for a task and only for the required duration and scope.
- Read and write capabilities are separated, and credentials are limited to specific repositories, paths, APIs, or actions.
- Privilege escalation requires an explicit policy or approval.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Least Privilege affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Reduce impact when an agent is manipulated or makes a mistake.
- Create safer tokens, service accounts, and tool allowlists.

## Example

A documentation agent receives read access to the repository and write access only to its feature branch, not production deployment credentials.

## Trade-offs and limitations

- Very narrow permissions can make workflows brittle and increase operational overhead.
- Permissions must be reviewed as task scope changes.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Least Privilege expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../../../l10n/uk_UA/)
- [Trust Boundaries](../../../trust-boundaries/l10n/uk_UA/)
- [Sandboxing](../../../sandboxing/l10n/uk_UA/)
