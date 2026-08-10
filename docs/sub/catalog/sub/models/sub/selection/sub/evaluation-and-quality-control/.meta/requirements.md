# Documentation Requirements

## Requirements

- Define evaluator/QC model selection by rubric, evidence, calibration, independence, and decision authority.
- Cover the selected evaluation families: language quality, agents, factuality/grounding, image/video/audio QC, multimodal consistency, and preference/aesthetic evaluation.
- Preserve the legacy judge requirements for pass/fail/inconclusive output, severity, calibration, disagreement, abstention, and escalation.
- Require deterministic validators first where they can prove a property.
- Use `QC agents` / `QC team` terminology for model-based content-quality checking.
- Require bias testing for position, order, verbosity, style, identity, and self-preference where relevant.
- Prevent workers or generators from being treated as independent sole approvers of their own material when independence matters.
- Link canonical model facts from `../../../reference/`.

## Validation

- A single model score is not presented as proof of quality.
- Calibration and evidence boundaries are explicit.
- QC task findings are kept separate from canonical model facts.
