# Documentation Requirements

## Requirements

- Define translation/localization model selection by exact language pair, direction, domain, content type, terminology, format, privacy boundary, and quality tier.
- Evaluate opposite translation directions separately and prevent unsupported transfer across language, domain, version, artifact, quantization, or deployment boundaries.
- Preserve useful legacy acceptance metrics: semantics, critical errors, omissions/additions, terminology, structural validation, consistency, correction/reviewer effort, latency, retries, and accepted-result cost.
- Preserve deterministic software-localization validation requirements without treating structural checks as proof of linguistic quality.
- Require independent qualified bilingual review for production-quality linguistic claims.
- Preserve useful concrete model-candidate hypotheses from the legacy mixed model/service guide only after current first-party identity/capability verification; present them as language/content-specific evaluation candidates, not as universal pair rankings or copied quick picks.
- Keep compact local/private draft hypotheses distinguishable from context-heavy hosted-model hypotheses, and state the evidence boundary or limitation that must be tested for every candidate.
- Treat multilingual or modality support as eligibility evidence only; it does not establish translation quality for a particular language direction, document type, terminology set, or quality tier.
- Treat tool/function-calling and other hosted/runtime features as surface-dependent when applicable and recheck mutable hosted availability, aliases, limits, prices, and provider features at decision time.
- Keep dedicated translation services, software platforms, parsers, renderers, and broader workflow selection outside this model-only subtree.
- Link canonical model facts from `../../../../../reference/`.
- Materialize `general-translation`, `technical-translation`, or `software-localization` child nodes only when their candidate sets or evaluation contracts materially diverge.

## Validation

- No service comparison table is copied from the legacy mixed model/service guide.
- No dated quick-pick order or universal language-pair ranking is asserted.
- Useful legacy model-candidate hypotheses are not discarded merely because they were embedded in a mixed model/service page or a model-reference page.
- Every retained candidate is framed as an evaluation starting point with explicit language/content scope and evidence limitations.
- Linguistic quality and structural validity remain separate acceptance dimensions.
