# Documentation Requirements

## Requirements

- Identify PyRIT as Microsoft's open-source Python Risk Identification Tool for generative AI, used to red-team and evaluate risks in generative-AI systems.
- Preserve its primary placement under `evaluation-and-observability/evaluation-frameworks`; adversarial/security testing is an evaluation role rather than a separate canonical product identity.
- Treat `microsoft/PyRIT` as the current upstream project. The archived `Azure/PyRIT` repository is historical/moved provenance and must not be presented as the active canonical upstream.
- Render the standard `entity-relations` block from validated current-entity relations and preserve Microsoft as the producing organization.
- Treat release versions, attack/scanner techniques, targets, scorers, datasets, provider integrations, GUI/deployment surfaces, and Python/runtime support as mutable facts that require current first-party verification before expansion.
- Present adversarial testing as authorized security/evaluation work: readers should test only systems they own or have permission to assess and should protect production credentials, sensitive data, side-effecting tools, and spend limits when executing automated attacks.
- Include current official PyRIT documentation and repository references.

## Validation

- PyRIT is presented as an evaluation/red-team framework, not as a hosted-only service or generic governance standard.
- Microsoft remains the producer and the `produces` / `produced-by` relation pair is materially consistent.
- The obsolete Azure repository is not represented as the current upstream.
- Mutable feature/version claims are not frozen without current upstream evidence.
- Safe-use guidance accompanies operational red-team usage.
