# Citations

Legacy residual retained for citation-generation workflow, source-location preservation, quality evaluation, readability, and access-control guidance that are intentionally outside the canonical Citations concept owner.

> **Migration note:** Citation identity, correctness/completeness/specificity/source-quality boundaries, trusted source metadata requirements, grounding/provenance/quotation distinctions, mutable-source versioning, multi-source and compound-claim support, citation resolvability, security boundaries, and evaluator limitations are already preserved in `docs/sub/concepts/sub/trustworthy-ai/sub/information-integrity/sub/citations/`. The remaining material below stays here until its exact learning, evidence-engineering, evaluation, UI/application, or security owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Citation-generation residual

Generate source identity and locations from retrieved or deterministic metadata rather than asking the model to reconstruct titles, URLs, page numbers, IDs, or timestamps from memory. Preserve stable source/version identity together with the most specific practical support location such as page, section, line range, record/field, timestamp, query result, or tool run.

When preprocessing, chunking, OCR, document moves, or re-indexing changes intermediate representations, maintain a resolver or mapping that keeps citations attached to the intended source evidence instead of allowing offsets to drift silently.

## Quality-evaluation residual

Evaluate at least the dimensions required by the task:

- whether the cited evidence actually supports the claim;
- whether material claims that require evidence are covered;
- whether the location is specific enough for verification;
- whether source identity/version remains resolvable;
- whether the source itself is current and appropriate authority.

Use automatic citation or entailment evaluators as assistance rather than ground truth when the risk warrants calibration or human review.

## Readability and access residual

Choose citation density according to verification risk and reader needs. Excessive markers can degrade readability, while document-level or sparse references can make claim-level checking impractical. Multi-source or compound claims may require several references rather than one convenient citation.

Do not expose protected source content, signed URLs, internal record identifiers, tenant data, or other restricted evidence merely to make a response appear traceable; citation rendering must preserve the caller's authorization boundary.

These citation-generation, quality, readability, and access practices remain migration source material until their exact learning, evidence-engineering, evaluation, UI/application, or security owners are verified.
