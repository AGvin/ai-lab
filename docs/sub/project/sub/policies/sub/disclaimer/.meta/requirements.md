# Documentation Requirements

## Requirements

- Explain the limits on relying on AI Lab documentation, examples, comparisons, evaluations, recommendations, experimental material, commands, configurations, and workflows.
- State that AI Lab is an informational and experimental documentation repository and that its content is intended for research, learning, engineering evaluation, and practical experimentation rather than as professional advice.
- State that repository material is not a substitute for qualified legal, financial, medical, compliance, security, or other professional review when a decision requires that expertise.
- Describe evaluations, rankings, comparisons, conclusions, and recommendations as scoped evidence and judgment rather than universal properties of a model, tool, service, or workflow.
- Make the evaluation boundary explicit: results can materially depend on the exact model/version/artifact or hosted snapshot, provider/runtime, hardware and deployment configuration, numerical precision or quantization, prompts and system instructions, context and tool access, datasets and representative inputs, evaluation method, acceptance criteria, and evaluation date.
- Keep provider or vendor claims distinguishable from AI Lab testing, independent evidence, community reports, and inference; do not present one evidence class as another.
- Explain that mutable facts such as pricing, availability, rate limits, aliases, API behavior, provider terms, data-handling practices, licenses, and supported features may change and must be rechecked against current authoritative sources when they affect a decision.
- State that the repository can contain mistakes, incomplete conclusions, stale assumptions, broken external links, or information that is correct only for a narrower historical or technical scope.
- Require readers to verify material claims against current primary or otherwise authoritative sources and to reproduce or test operational claims under the intended environment when the decision is material.
- Explain that repository-level disclaimers do not replace page-specific safe-use guidance. Material risks must still be documented near the affected resource or procedure.
- For commands, code, models, tools, infrastructure changes, and operational workflows, recommend controls proportionate to the actual risk, such as backups, isolated test environments, least privilege, access and secret controls, security/privacy review, rollback planning, and verification of destructive or billable state changes.
- State that high-impact or regulated decisions should not rely solely on repository material, model output, automated evaluation, or an AI-generated recommendation when qualified independent review is required.
- Distinguish repository-owned material from third-party resources. Models, datasets, software, code samples, assets, services, downloads, and linked resources may have their own licenses, terms, acceptable-use rules, privacy policies, or other constraints that must be checked separately.
- Link the repository-root `LICENSE` as the authoritative repository license text. Do not imply that the repository's MIT License overrides or relicenses third-party material or external services.
- Explain that the disclaimer adds repository-specific context for informational, evaluative, experimental, and practical material and does not replace, amend, or broaden the repository license.
- Avoid singular-author framing such as "the author's interpretation"; describe repository assessments by their actual evidence boundary instead.
- Avoid absolute guarantees of safety, correctness, reproducibility, suitability, compliance, or currency.

## Validation

- The page is reproducible from these canonical requirements without relying on the legacy `docs/sub/disclaimer/README.md` wording.
- The page reflects the current evidence-boundary and safe-use rules used by AI Lab rather than preserving obsolete generic disclaimer prose mechanically.
- The repository MIT License is linked correctly, and third-party licensing/terms are clearly separated from repository licensing.
- No mutable provider-specific fact is presented as permanently current.
- The page does not use a repository-level disclaimer as a substitute for material page-specific warnings or controls.
- No broken localization link is emitted merely because localization may be generated later.
