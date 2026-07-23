# Content Moderation

Content moderation detects, labels, restricts, or routes content according to safety, legal, platform, or community policies.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Moderation may apply before model processing, after generation, or both. Systems combine rules, classifiers, model judgments, user reports, and human review. Policies must define categories and actions explicitly because “unsafe” is context-dependent.

## Practical use

- Filter prohibited user input.
- Review generated public content.
- Protect minors or workplace environments.
- Route uncertain cases to human moderators.
- Enforce product-specific policy boundaries.

## Trade-offs and limitations

Moderation systems produce false positives and false negatives. Language, culture, sarcasm, quoted material, and educational context complicate classification. Overly broad filtering can suppress legitimate content.

## Common mistakes

- Using one global threshold for every category.
- Hiding moderation decisions without an appeal path.
- Treating quoted harmful content the same as endorsement.
- Applying text moderation to tool actions without separate controls.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Guardrails](../guardrails/)
- [Human in the Loop](../../../agents-and-automation/sub/human-in-the-loop/)
- [Model Alignment](../model-alignment/)
