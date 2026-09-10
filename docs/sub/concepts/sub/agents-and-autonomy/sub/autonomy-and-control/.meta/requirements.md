# Documentation Requirements

## Requirements

- Use the reader-facing title `Autonomy and Control`.
- Define agent autonomy as the degree and scope within which an AI-enabled system may select, sequence, revise, or execute actions without obtaining new human direction or approval at each decision point.
- Distinguish autonomy from capability, permissions/authority, and access. A system may be capable of an action but not authorized to perform it, or authorized to act only under approval, budget, time, data, tool, or policy constraints.
- Treat autonomy as configurable per capability, action class, environment, and risk boundary rather than one permanent label for an entire product or model. Read-only research, drafting, external communication, code changes, financial actions, and destructive operations can use different control levels in the same system.
- Preserve `autonomy levels` as a family of useful frameworks rather than one universally standardized scale. Advisory/operator, collaborator, approval-gated, bounded-autonomous, observer/supervisory, and other named levels differ across frameworks and must not be presented as one canonical numbering scheme.
- Explain control mechanisms such as explicit scope, allowed tools/actions, human approval/intervention, budgets, rate/step/time limits, stopping conditions, monitoring, revocation, rollback/recovery, and escalation as system controls that bound autonomy; no single mechanism is required by definition.
- Distinguish operational autonomy from model confidence or intelligence. Higher benchmark capability or apparent reasoning quality does not itself justify broader permissions or reduced oversight.
- Explain that increased autonomy can change the scale and speed of errors or side effects, but risk is determined jointly by capability, permissions, environment, reversibility, verification, observability, and consequence severity rather than autonomy alone.
- Keep detailed human-oversight semantics in `human-ai-interaction/oversight-and-intervention/`; this node owns the autonomy/control relationship and may link to oversight without duplicating its full canonical definition.
- Keep concrete permission matrices, product modes, approval UX, security policies, regulatory requirements, incident thresholds, and task-specific autonomy recommendations with their applicable catalog, security, governance, engineering, or project owners.
- Use the canonical entity references as research inputs for autonomy-level variation and human-control boundaries when reader-facing rendering is activated.

## Validation

- The page does not preserve the legacy example spectrum as one universally canonical autonomy-level scale.
- Autonomy is distinguished from model capability, credentials/permissions, and authorization.
- One global autonomy label is not assumed sufficient for every action or risk class in a system.
- Higher model capability is not treated as automatic evidence for higher operational autonomy.
- Human oversight is related but not duplicated as though this node owned the complete oversight concept.
- Legacy recommendations are preserved as control/risk principles rather than a universal deployment ladder.
