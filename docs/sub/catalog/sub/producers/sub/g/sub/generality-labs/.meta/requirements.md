# Documentation Requirements

## Requirements

- Identify Generality Labs as an independently identifiable London-based AI safety research/engineering organization founded in 2026 as an Arcadia Impact spin-off, not a new name for the UK AI Security Institute or for the original Inspect AI framework.
- Attribute current Inspect Evals maintenance, its registry work, and AI evaluation research to Generality Labs on the basis of the organization's official website, founder update and the first-party Inspect Evals repository. Do not infer ownership of every benchmark or upstream dataset in the registry.
- Preserve the historical provenance boundary: the UK AI Security Institute introduced Inspect Evals in 2024 (alongside community collaborators), whereas Generality Labs now maintains the collection. Reflect only current maintenance as `maintains` and its software inverse `maintained-by`; do not fabricate exclusive original `produces` authorship for Generality Labs.
- Keep Generality Labs a separate organization identity even though the maintained Inspect Evals repository continues to use `UKGovernmentBEIS` in its GitHub URL.
- Treat externally maintained third-party evaluations, model provider access, and protected datasets as independent; the organization's research and maintenance do not convey third-party redistribution or execution rights.
- Include official, stable organization/provenance URLs and a reciprocal canonical link to Inspect Evals. Do not assert that Generality Labs owns or operates Inspect AI's core framework.

## Validation

- [Official site](https://generality.org/) lists Inspect Evals maintenance; [organization update](https://generality.org/blog/posts/an-update-on-generality-labs/) identifies the 2026 spin-off; the [Inspect Evals first-party README](https://github.com/UKGovernmentBEIS/inspect_evals/blob/7c31cf22830c4657a3894e095b452c7d50f6f3b8/README.md) identifies the current maintainer.
- `maintains` / `maintained-by` links resolve both ways and the Producers G index lists this node exactly once.
- No unsupported original ownership claim, source-dataset license grant, runtime evaluation result, or whole-catalog audit.
