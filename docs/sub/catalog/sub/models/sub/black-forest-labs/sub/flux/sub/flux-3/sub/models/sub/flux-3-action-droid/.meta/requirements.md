# Documentation Requirements

## Identity and provenance

- Identify **FLUX 3 Action DROID** as a separate released **DROID embodiment fine-tuned policy**, with original BFL location [https://huggingface.co/black-forest-labs/flux-3-action-droid](https://huggingface.co/black-forest-labs/flux-3-action-droid); do not conflate this learned identity with the 7B adaptation base, a different embodiment, or precision-only FP8r artifacts.
- fine-tuned from the FLUX 3 Action 7B adaptation base for the DROID robot data/observation/action convention. The exact learned-weight variant and loading/LeRobot requirements must be verified against [BFL setup instructions](https://github.com/black-forest-labs/flux-action/blob/main/docs/setup.md) and the [official 2026-09-23 release](https://huggingface.co/blog/black-forest-labs/flux-3-action).
- DROID camera/state/action preprocessing and a matching action head are required; adapting this policy is not evidence of safe use on a different physical robot.

## Rights, deployment and safety

- The published action weights use the **FLUX Kommunity License**, not the Apache-2.0 license of the reference implementation. Check gated access, output/commercial clauses and the current exact weight license before use. [BFL model page](https://bfl.ai/models/flux-3-action).
- Physical control requires external robot-specific joint, velocity, force and workspace constraints, an independent emergency stop, verified action normalization, guarded testing and human supervision. Neither the learned checkpoint nor benchmark results guarantee safe physical motion.
- Use BFL's reported success/speed numbers only as source claims; no independent AI Lab robotics execution, GPU-fit, benchmark or deployment readiness is established.
- Current producer/beneficial ownership or potential minority interests must be checked on attributable evidence; do not infer verified Russia-linked origin/control from rumor or names. [AI Lab provenance policy](../../../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md).

## Validation

- Exactly one `member-of` relation to FLUX 3 and one reciprocal series `has-member`; model reader link resolves.
- Distinct student training stages, camera/action conventions, gated licenses and precision forms must not be merged.
- No full catalog freshness/CI/cache, proven security, robot control evaluation or final gate credited.
