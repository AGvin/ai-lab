# Documentation Requirements

## Requirements

- Define evaluator/QC model selection by rubric, evidence, calibration, independence, and decision authority.
- Cover the selected evaluation families: language quality, agents, factuality/grounding, image/video/audio QC, multimodal consistency, and preference/aesthetic evaluation.
- Preserve the legacy judge requirements for pass/fail/inconclusive output, severity, calibration, disagreement, abstention, and escalation.
- Require deterministic validators first where they can prove a property.
- Use `QC agents` / `QC team` terminology for model-based content-quality checking.
- Require bias testing for position, order, verbosity, style, identity, and self-preference where relevant.
- Prevent workers or generators from being treated as independent sole approvers of their own material when independence matters.
- Preserve legacy perception/evaluation model names as audit inputs when they appeared in mixed perception/QC guidance, but do not promote a perception-capable or multimodal model into a QC/judge shortlist solely from modality support, provider positioning, or usefulness for content understanding.
- Materialize a concrete evaluator/QC candidate set only after calibration evidence exists for the target rubric and decision role, including relevant false-approval/false-rejection, agreement, abstention, bias, and human-overturn behavior.
- Keep content-understanding candidate eligibility under `../content-understanding/`; promote a model here only when evidence supports the distinct evaluator/QC assignment.
- Treat provider benchmark or self-evaluation claims as provider-documented evidence, not independent proof of judge reliability.
- Recheck mutable hosted model identities, aliases, tool/features, limits, and availability when they materially affect a future QC candidate evaluation.
- Link canonical model facts from `../../../reference/`.

## Validation

- A single model score is not presented as proof of quality.
- Calibration and evidence boundaries are explicit.
- Legacy perception candidate names are not silently discarded, but their absence from a QC shortlist is an explicit evidence decision rather than an accidental omission.
- A model is not listed as a QC/judge candidate merely because it can perceive the evaluated modality or generate the same artifact type.
- Any future concrete QC candidate has task-specific calibration evidence rather than provider positioning alone.
- QC task findings are kept separate from canonical model facts.
