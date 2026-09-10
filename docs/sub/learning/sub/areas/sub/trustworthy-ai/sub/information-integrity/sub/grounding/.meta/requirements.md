# Documentation Requirements

## Requirements

- Teach Grounding as supporting material claims with evidence appropriate to the claim: authoritative documents/APIs, structured records, deterministic calculations, code/tests/logs, sensors, or other verifiable sources.
- Retrieve narrowly enough to preserve the support relation while retaining qualifiers, scope, version, and exceptions needed to interpret the evidence correctly.
- Preserve source identity, version/time, and the evidence location or tool/run result needed to reconstruct material claims; distinguish direct source statements from deterministic calculation, inference, and synthesis when material.
- Validate critical exact values outside generative interpretation where feasible, including identifiers, totals, transactions, policy constraints, and exact computations.
- When sources conflict, surface the conflict or apply an explicit authority/version rule rather than silently selecting whichever source supports the generated conclusion.
- When available evidence cannot support a material claim, allow qualification, request for more data, or abstention rather than plausible completion.
- Evaluate grounding at claim/evidence level separately from source quality, freshness, authority, and downstream task correctness.
- Keep evidence content separate from application instruction authority.

## Validation

- A plausible explanation or citation-shaped output is not accepted as evidence without checking the actual source/result.
- Conflicting evidence is not silently collapsed.
- Unsupported material claims can remain qualified or unanswered.
- Claim support and source quality are evaluated as distinct dimensions.
