# Documentation Requirements

## Requirements

- Identify Shannon as Keygraph's open-source autonomous white-box AI pentester for source-available web applications and APIs, run by the user from a local/self-managed CLI workflow.
- Preserve the current distinction between Shannon Open Source and the separate commercial Keygraph platform: Shannon is the standalone pentesting agent/core, while the commercial platform adds broader continuous AppSec, management, and enterprise capabilities.
- Preserve proof-by-exploitation behavior at a high level: Shannon combines source-code analysis with live application testing and reports findings it can validate through working exploit evidence.
- Preserve useful legacy execution boundaries around Docker/ephemeral worker execution, read-only mounting of the target repository in the recommended workflow, live target mutation through exploit attempts, external model-provider credentials, resumable workspaces, and local result storage.
- Preserve the white-box scope boundary without freezing obsolete edition details: source access materially informs Shannon's testing and the open-source project should not be represented as proof of complete external-attacker or black-box coverage unless current upstream documentation explicitly provides that capability.
- Treat Shannon as active offensive-security tooling: require ownership or explicit written authorization for the target, prefer isolated non-production targets, scoped test credentials, recovery/backup readiness, and human review of findings and proof-of-concept evidence.
- Preserve prompt-injection/source-content, network access, target-state mutation, provider-safeguard interruption, credential exposure, and false-negative/false-positive risks as material evaluation boundaries.
- Keep provider lists, vulnerability counts, benchmark results, edition feature matrices, model recommendations, runtime versions, installation commands, pricing, and other mutable details source-backed and time-scoped when expanded.
- Preserve Keygraph as the canonical producer through the physically materialized `produced-by` relation when the reciprocal Keygraph `produces` relation resolves successfully.
- Include the current official Shannon repository/open-source references.

## Validation

- Shannon remains a Local Agent/software identity rather than being collapsed into the hosted/commercial Keygraph platform.
- The page makes clear that Shannon actively executes exploits and is not a passive scanner.
- Authorization and non-production/isolation guidance is explicit.
- Read-only repository mounting is not misrepresented as preventing mutation of the running target application.
- Open-source white-box coverage is not presented as automatically equivalent to comprehensive pentesting coverage.
- The Keygraph/Shannon `produces` / `produced-by` relation pair is physically present at both endpoints, semantically consistent, and resolves to canonical profiles.
