# Evaluation and Quality Control Model Selection

Choose models for independent evaluation and QC by the rubric, evidence, calibration, and authority required for the acceptance decision.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers language-quality evaluation, agent evaluation, factuality and grounding, image/video/audio QC, multimodal consistency evaluation, and preference or aesthetic evaluation.

A model that can perceive or generate an artifact is not automatically a reliable evaluator of that artifact. A worker or generator should not be the sole authority on whether its own result is accepted when independence matters.

## Evaluation contract

Define before testing:

- explicit acceptance criteria or rubric;
- allowed evidence and required citations or provenance;
- structured outcomes such as pass, fail, or inconclusive;
- severity and blocking rules;
- calibration examples with known outcomes;
- independence requirements;
- tie, disagreement, abstention, and escalation policy.

Use deterministic metrics and validators first when they can prove a property. Use QC agents to interpret ambiguous evidence, compare candidates, or apply rubrics after calibration; use qualified human review where consequence or accountability requires it.

## Judge reliability

Test position, order, verbosity, style, identity, and self-preference bias. Randomize or normalize irrelevant presentation features where appropriate and measure agreement, calibration, false approval, false rejection, abstention, and human-overturn rates.

Do not treat one model score as proof of quality. Link intrinsic evaluator-model facts from [Model Reference](../../../reference/) and keep calibration and task evidence here.
