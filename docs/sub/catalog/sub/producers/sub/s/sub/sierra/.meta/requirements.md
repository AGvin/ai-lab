# Documentation Requirements

## Requirements

- Identify Sierra as the first-party organization maintaining the `sierra-research/tau2-bench` upstream that now publishes the current τ-bench family (including historical τ²/τ³ tracks and current 2.0 multilingual evaluation) for customer-service agents.
- Attribute the released benchmark and its reproducible evaluation harness to Sierra without treating simulated banking/airline/retail/telecom service domains, user simulators or voice vendor APIs as separately produced Sierra models or services.
- Preserve the benchmark's original publisher versus historical academic collaborators, cited papers, community forks and third-party leaderboard submissions.
- Treat task-corpus revisions, grading corrections, evaluation modalities, domain inventories, repository name and source URLs as independently mutable first-party facts.

- Render the identity, provenance and operational context recorded in canonical `entity.identity_note`; keep version-sensitive claims and official resources aligned with the cited first-party sources.

- Render the standard `entity-relations` block from validated current-entity relations, ordered by explicit numeric order, target canonical name and target ID; resolve every visible target to its reader.

## Validation

- Original upstream and official Sierra research evidence agree on publisher identity.
- The Sierra producer `produces` link reciprocates the canonical `tau-bench` dataset family `produced-by` link.
- Older tau and tau-two versions are not duplicated as independent current benchmarks solely because their historical papers were published under different names.
