# Documentation Requirements

## Requirements

- Identify garak as NVIDIA's open-source LLM vulnerability scanner and Generative AI Red-teaming & Assessment Kit for probing and evaluating failure modes in language-model and dialog systems.
- Preserve its primary placement under `evaluation-and-observability/evaluation-frameworks`; vulnerability scanning and red teaming are evaluation/security-testing roles rather than a separate canonical product identity.
- Render the standard `entity-relations` block from validated current-entity relations and preserve NVIDIA as the producing organization.
- Preserve the distinction between the periodically released installable package and development code from the repository's main branch.
- Treat supported generators/providers, probes, detectors, mappings, attack techniques, runtime requirements, and release versions as mutable facts that require current first-party verification before expansion.
- Present adversarial testing as authorized security/evaluation work: readers should test only systems they own or have permission to assess and should isolate or constrain credentials, sensitive data, side-effecting tools, network access, and spend where attacks could trigger real actions.
- Include current official garak documentation and repository references.

## Validation

- garak is presented as a local evaluation/red-team framework/tool rather than a model, hosted-only service, or formal security standard.
- NVIDIA remains the producer and the `produces` / `produced-by` relation pair is materially consistent.
- Development-branch behavior is not silently presented as stable released behavior.
- Mutable plugin/support/version claims remain source- and release-sensitive.
- Safe-use guidance accompanies operational red-team usage.
