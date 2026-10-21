# Documentation Requirements

## Requirements

- Identify Tencent Hy Team as the producing team named by the official Hy4 preview upstream repository.
- Keep team identity distinct from Tencent corporation, Tencent Cloud access routes, Hunyuan product surfaces, and individual model identities.
- Render the standard `entity-relations` block from validated relation state.
- Preserve this source-backed identity and provenance context: Tencent Hy Team is the producing team explicitly credited by the official Hy4 preview repository. The represented Tencent Hy family remains distinct from Tencent's corporate identity, Tencent Cloud access and applications that integrate the models.
- Explain the following operating and decision boundary: Release status and deployment conditions belong to each model. The official Hy4 preview repository describes an early version with known limitations and provides released weights under Apache 2.0; that combination does not make it a generally available production service or establish the same license for every Hy release. Assess the exact checkpoint, serving runtime and intended workload before deployment.
- Support the producer context with these first-party sources: <https://github.com/Tencent-Hunyuan/Hy4-preview>.

## Validation

- The Hy family `produced-by` relation has the matching `produces` inverse here.
- No unsupported corporate parent relation is inferred merely from branding or repository ownership.
