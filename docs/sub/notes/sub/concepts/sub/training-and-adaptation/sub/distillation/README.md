# Distillation

Legacy residual retained for teacher-signal provenance, independent student evaluation, deployment-cost verification, and licensing/governance guidance that are intentionally outside the canonical Knowledge Distillation concept owner.

> **Migration note:** Distillation identity, teacher-to-student transfer, non-smaller-student boundary, response/feature/relation/generated-target families, SFT/synthetic-data/pruning/quantization distinctions, teacher-error propagation, capacity/architecture/loss dependencies, capability-preservation limits, and nominal-versus-realized deployment-cost boundaries are already preserved in `docs/sub/concepts/sub/models/sub/optimization-and-compression/sub/distillation/`. The remaining material below stays here until its exact learning, training-engineering, evaluation, governance, artifact-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Teacher-signal residual

Record the exact teacher model/version or ensemble, prompts/tasks, source/seed data, temperature or generation configuration, logits/features/labels/outputs retained, filtering, and any human or automated validation used to create the transfer signal. A distilled dataset or feature dump should remain traceable to the teacher behavior it encodes.

When provider-hosted teachers are used, verify whether terms, licenses, API policy, privacy constraints, or redistribution rules permit the intended generation, training, storage, and distribution workflow rather than assuming generated outputs are unrestricted training data.

## Independent-evaluation residual

Evaluate the student on independently sourced or held-out task evidence, not only on teacher-generated examples or the exact distillation objective. Compare both task performance and regressions in robustness, calibration, safety behavior, long-tail capabilities, and domains outside the transfer distribution.

Treat teacher agreement as one metric rather than ground truth. A student can match a teacher's preferred outputs while inheriting its errors or losing capabilities the transfer data did not exercise.

## Deployment-cost residual

Measure student memory, artifact size, latency, throughput, energy/power, runtime compatibility, and total serving cost on the actual target system. A lower parameter count or smaller architecture does not guarantee better end-to-end deployment when kernels, batching, quantization, context behavior, or hardware utilization differ.

Compare the distilled student against an existing smaller model or simpler adaptation route when the operational goal is cost reduction; training a student can be more expensive than selecting an already adequate compact model.

## Governance residual

Version teacher/student identities, transfer data, training configuration, evaluation evidence, and resulting artifact together. Preserve enough lineage to update or retire the student when the teacher, source data, policy constraints, or discovered defects change materially.

These provenance, evaluation, deployment, and governance practices remain migration source material until their exact learning, training-engineering, evaluation, governance, artifact-management, or decision-support owners are verified.
