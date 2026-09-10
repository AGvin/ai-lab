# Documentation Requirements

## Requirements

- Teach Hallucinations as an information-integrity failure to diagnose across the complete evidence and application path rather than automatically attributing every unsupported/incorrect result to one model cause.
- Check missing/ambiguous evidence, stale or contradictory retrieval, unavailable authoritative sources, exact-identifier requests without source access, context-selection failures, prompt pressure to answer, decoding settings, and application-side data handling before selecting a mitigation.
- Separate model-generation failure from retrieval failure, bad source data, deterministic computation bugs, and application corruption.
- Use authoritative data, retrieval, tools, or deterministic checks when the task requires externally verifiable claims; evidence references must be resolvable rather than citation-shaped text.
- Distinguish supplied evidence, inference, and uncertainty where material; validate calculations, URLs, identifiers, code/API claims, and structured values with appropriate authoritative/deterministic systems.
- Allow abstention, escalation, or requests for missing evidence when unsupported guessing would exceed the workflow's failure tolerance.
- Evaluate hallucination/faithfulness failures on representative tasks under the actual retrieval, prompting, tool, and model configuration rather than one example or generic benchmark.
- Evaluate mitigation trade-offs including answer coverage, retrieval/evidence quality, latency, operational cost, and new failure modes; no mitigation is presented as eliminating hallucinations universally.

## Validation

- Diagnosis distinguishes model, retrieval, source-data, deterministic, and application failure paths.
- Verifiable claims use evidence/checking mechanisms appropriate to their risk.
- Unsupported claims may remain unresolved instead of being plausibly completed.
- Mitigation quality, coverage, latency, and cost trade-offs remain visible.
