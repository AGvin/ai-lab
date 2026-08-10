# Documentation Requirements

## Requirements

- Define translation/localization model selection by exact language pair, direction, domain, content type, terminology, format, privacy boundary, and quality tier.
- Evaluate opposite translation directions separately and prevent unsupported transfer across language, domain, version, artifact, quantization, or deployment boundaries.
- Preserve useful legacy acceptance metrics: semantics, critical errors, omissions/additions, terminology, structural validation, consistency, correction/reviewer effort, latency, retries, and accepted-result cost.
- Preserve deterministic software-localization validation requirements without treating structural checks as proof of linguistic quality.
- Require independent qualified bilingual review for production-quality linguistic claims.
- Keep dedicated translation services, software platforms, parsers, renderers, and broader workflow selection outside this model-only subtree.
- Link canonical model facts from `../../../../../reference/`.
- Materialize `general-translation`, `technical-translation`, or `software-localization` child nodes only when their candidate sets or evaluation contracts materially diverge.

## Validation

- No service comparison table is copied from the legacy mixed model/service guide.
- No universal language-pair ranking is asserted.
- Linguistic quality and structural validity remain separate acceptance dimensions.
