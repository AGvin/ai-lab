<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:aca5677a8cb64725c094dd86034afb952699ac37
  mode: copy-through
-->

# Jailbreaking

Attempts to bypass a model's configured safety or policy constraints.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Attempts to bypass a model's configured safety or policy constraints. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Jailbreaking uses adversarial wording, role play, encoding, or multi-turn pressure to bypass configured model restrictions.
- It targets model behavior rather than necessarily exploiting software code.
- Mitigations include layered policy enforcement, model updates, monitoring, and restricting consequential tools.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Jailbreaking affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Evaluate whether public-facing assistants resist policy bypass attempts.
- Test how model safety changes across versions and prompts.

## Example

A user wraps a prohibited request in a fictional scenario and asks the model to ignore normal rules.

## Trade-offs and limitations

- Passing a known jailbreak set does not prove general safety.
- Overly broad blocking can harm legitimate use.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Jailbreaking expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../../../l10n/uk_UA/)
- [Content Moderation](../../../content-moderation/l10n/uk_UA/)
- [Model Alignment](../../../model-alignment/l10n/uk_UA/)
