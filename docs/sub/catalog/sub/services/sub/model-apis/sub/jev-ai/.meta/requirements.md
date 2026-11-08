# Documentation Requirements

## Requirements

- Identify Jev AI at `thejevai.com` as a producer-operated SaaS/API/playground surface providing hosted Jev access, account/workspace features, credits, and developer documentation.
- Preserve the site's explicit disclosure that it is an app for Jev model playbooks and shared usage and **not the official TypeSafe product site**.
- Keep canonical Jev model ownership and TypeSafe AI producer provenance with their model/producer owners; do not infer that Jev AI produced Jev.
- Do not materialize a Jev AI organization/producer or an `operated-by` relation until a stable operator/legal identity is established from adequate first-party evidence.
- Treat pricing, credits, concurrency, endpoint paths, model aliases, plans, availability, and service limits as mutable service state.
- Keep TypeSafe's own API and documentation distinct from this third-party service even where request shapes or Jev identifiers overlap.

## Validation

- Jev AI remains a hosted model-API service rather than the canonical Jev model or TypeSafe AI producer.
- No unsupported ownership or operator relation is inferred from branding.
- Mutable commercial/API state is not treated as intrinsic Jev model fact.

## Scoped original-source qualification — 2026-11-08

- **Jev AI** is a distinct website-operated third-party playground, credit-billed hosted REST service and development surface at `thejevai.com`; its own site explicitly separates itself from the original TypeSafe producer. The original Jev model and producer identity do **not** transfer to this API operator, and no unsupported legal-company or `operated-by` relation should be invented.
- The website's publicly documented `POST https://thejevai.com/v1/systemone` endpoint accepts structured state and typed `choice`, `score`, `noul` questions; requests require a Bearer key and model ID, and responses return per-question answers and usage/credits. Supported model IDs, approximate probability/confidence fields and credits are supplier-defined, not validated accuracy, decision fairness or permissions to automate financially or medically material actions. Versioned model IDs should be preferred to moving latest aliases in reproducible trials.
- Original service source and terms/disclosure: https://thejevai.com/ ; https://thejevai.com/docs ; https://thejevai.com/terms-of-service ; https://thejevai.com/privacy-policy .
- Source acceptance confirms one existing independent hosted API/playground identity and currently public API shape, while operator legal identity, model-producer rights, service reliability, security, personal-data retention and high-risk business decision claims remain unresolved. No production calls/credentials, third-party rights/security/legal audit, whole-catalog schema/cache/CI/render, clean or final gate.
