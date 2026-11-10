# Documentation Requirements

## Requirements

- Describe WebGPU as a web API for GPU computation and rendering; distinguish WGSL language, native driver APIs and inference frameworks.
- Preserve the published 15 September 2026 Candidate Recommendation Draft and separately identify the 30 October 2026 Editor's Draft; neither is a final W3C Recommendation.
- Tie adapter/device lifecycle, limits, feature negotiation, queue/resources and security considerations to the cited revision.
- Do not infer broad browser, hardware, training/inference workload or performance compatibility from specification membership.

## Validation

- Canonical identity and first-party references match the current frozen cohort source lead.
- Version and source maturity are explicit and no implementation, availability or conformance is invented.

## Scoped original-source qualification — 2026-11-07

- WebGPU is W3C GPU for the Web Working Group's web API for GPU graphics and computation, distinct from WGSL shader syntax and from any native drivers or model-inference engine. The W3C published Candidate Recommendation Draft remains dated **15 September 2026** as of 7 November 2026; its editor draft advances independently.
- Adapter/device limits, resource access, feature flags, shader support and browser/driver implementation vary. Candidate Recommendation Draft publication is not W3C Recommendation, hardware compatibility certification, performance evidence or assurance that arbitrary ML workloads are secure.
- Verified first-party source 1: https://www.w3.org/TR/2026/CRD-webgpu-20260915/
- Verified first-party source 2: https://www.w3.org/standards/history/webgpu/
- Verified first-party source 3: https://www.w3.org/TR/webgpu/
- Existing W3C WebGPU specification/source qualified only; no browser, accelerator, shader, model runtime, cross-device performance or security validation, root-wide schema/cache/CI/render, clean pass or final gate.
