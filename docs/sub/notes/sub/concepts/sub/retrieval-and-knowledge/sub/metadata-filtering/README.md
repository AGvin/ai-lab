# Metadata Filtering

Legacy residual retained for metadata-operation, authorization-enforcement, and retrieval-quality guidance that are intentionally outside the canonical Retrieval Filtering concept owner.

> **Migration note:** Retrieval-filtering identity, eligibility-versus-relevance separation, pre/during/post-filter placement, metadata quality and version semantics, convenience-filter versus authorization boundaries, authoritative access-control requirements, and backend-dependent recall/performance effects are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/filtering/`. The remaining material below stays here until its exact learning, retrieval-engineering, security, evaluation, or operational-policy owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata-operation residual

Define metadata fields and values consistently enough that filtering remains predictable as documents are created, replaced, archived, localized, reclassified, or moved between collections. Normalize dates, categorical values, tenant/project identifiers, content types, versions, and other filter-bearing attributes according to the application contract rather than relying on ad-hoc free-form values.

Update or remove filter metadata together with source lifecycle changes so stale attributes do not silently expose obsolete content or exclude the current version.

## Authorization-enforcement residual

When tenant, repository, user, group, classification, or other security-sensitive attributes control access, derive allowed values from an authoritative identity/policy decision and enforce them before unauthorized content becomes visible to the caller or model.

Do not allow an unrestricted model-generated or user-supplied tenant, collection, or access identifier to become the authority for a security boundary. Retrieval filters can execute an already-authorized restriction, but they are not the policy source by themselves.

## Recall and performance residual

Evaluate missing, stale, or inconsistent metadata as a retrieval failure mode because strict predicates can suppress otherwise relevant evidence. Test representative filter combinations together with the concrete retrieval backend, especially when approximate vector search, candidate limits, distributed indexes, or post-filtering can change recall or latency.

Keep search-convenience filters distinguishable from mandatory access controls during evaluation so a recall-oriented tuning change does not accidentally weaken a security requirement.

These metadata-operation, authorization, recall, and performance practices remain migration source material until their exact learning, retrieval-engineering, security, evaluation, or operational-policy owners are verified.
