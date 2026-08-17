# Documentation Requirements

## Requirements

- Identify mini-SWE-agent as the current v2 minimal software-engineering agent designed for simple, inspectable, scriptable task execution.
- Preserve its command-line/software-engineering focus: repository inspection/editing, shell commands, tests, debugging, and patch-producing workflows.
- Preserve support for multiple local or isolated execution environments at a high level, including ordinary local execution and container/sandbox backends, without freezing a complete backend list.
- Preserve the upstream design boundary: mini-SWE-agent intentionally uses a small agent scaffold and shell-oriented interaction rather than a large specialized-tool surface.
- Preserve useful legacy operational boundaries around repository write access, shell/test execution, sandbox isolation, generated patch review, model-provider credentials, source/log/secret exposure, and benchmark-versus-production assumptions.
- Preserve that mini-SWE-agent has superseded SWE-agent for the upstream project's general recommendation, without turning historical SWE-agent details into mini-SWE-agent identity.
- Do not freeze line-count claims, benchmark scores, adoption lists, or performance comparisons in the canonical profile.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official mini-SWE-agent documentation and repository references.

## Validation

- The profile does not turn benchmark positioning into intrinsic product identity.
- The page distinguishes current v2 identity from historical-version details.
- Research/benchmark usefulness is not presented as a production-security guarantee.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
