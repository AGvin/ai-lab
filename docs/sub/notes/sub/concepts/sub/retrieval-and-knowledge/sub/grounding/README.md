# Grounding

Legacy residual retained for evidence-acquisition workflow, provenance handling, critical-value validation, source-conflict handling, and abstention guidance that are intentionally outside the canonical Grounding concept owner.

> **Migration note:** Grounding identity, claim-level support, distinction from factuality/citations/retrieval/source authority/provenance, evidence-form diversity, direct versus derived support, conflict/insufficient-evidence handling, temporal/security boundaries, and non-guarantees from RAG/tool/database access are already preserved in `docs/sub/concepts/sub/trustworthy-ai/sub/information-integrity/sub/grounding/`. The remaining material below stays here until its exact learning, evidence-engineering, evaluation, trustworthy-AI, or application-workflow owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Evidence-acquisition residual

Acquire evidence from the mechanism appropriate to the claim: internal documentation, structured records, authoritative APIs, deterministic calculations, code execution, tests, logs, sensors, or other verifiable sources. Retrieve narrowly enough that irrelevant material does not obscure the support relation, while preserving enough context to interpret qualifiers, scope, version, and exceptions correctly.

Keep untrusted evidence content separate from instruction authority. A retrieved page or document can contribute factual evidence without gaining permission to alter system behavior, tool permissions, or access policy.

## Provenance and validation residual

Preserve source identity, version/time, and the evidence location or tool/run result needed to reconstruct material claims. Distinguish direct source statements from deterministic calculations, inference, and synthesis when that distinction matters for verification.

Validate critical values outside generative interpretation where feasible, especially identifiers, financial totals, permissions, transactions, legal/policy constraints, safety-relevant values, and exact computations. A plausible explanation or citation-shaped output is not a substitute for checking the actual source/result.

## Conflict and abstention residual

When sources disagree, surface the disagreement or apply an explicit authority/version policy instead of silently selecting the evidence that matches the generated conclusion. When available evidence cannot support a material claim, allow qualification, a request for more data, or abstention rather than filling the gap with plausible detail.

Evaluate grounding at the claim/evidence level and separately assess source quality, freshness, authority, and downstream task correctness.

These evidence-acquisition, provenance, validation, conflict, and abstention practices remain migration source material until their exact learning, evidence-engineering, evaluation, trustworthy-AI, or application-workflow owners are verified.
