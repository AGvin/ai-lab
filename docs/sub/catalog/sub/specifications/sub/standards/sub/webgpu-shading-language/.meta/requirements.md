# Documentation Requirements

## Requirements

- Define WGSL as the shader language used by the WebGPU API, including language syntax, typing and validation rather than a runtime or graphics API.
- Correctly cite the most recent W3C published Candidate Recommendation Draft on 6 November 2026; separate it from working editor revisions and past August drafts.
- Keep shader semantics, memory model, validation rules, capabilities and extension status attached to the cited revision.
- Do not infer portability, driver correctness, performance parity or security of arbitrary untrusted shader code from WGSL specification alone.

## Validation

- Canonical identity and first-party references match the current frozen cohort source lead.
- Version and source maturity are explicit and no implementation, availability or conformance is invented.

## Scoped original-source qualification — 2026-11-07

- WGSL specifies the typed shader programming language and validation/semantic contract used by WebGPU. It is distinct from the JavaScript WebGPU API, hardware drivers and the particular shader execution engine.
- The W3C latest **published Candidate Recommendation Draft is dated 6 November 2026**, superseding the 26 October published draft cited in prior catalog metadata. The working Editor's Draft remains separately mutable; neither document is a final W3C Recommendation or universal browser/driver support guarantee.
- Verified first-party source 1: https://www.w3.org/TR/2026/CRD-WGSL-20261106/
- Verified first-party source 2: https://www.w3.org/standards/history/WGSL/
- Existing WGSL identity and bounded first-party source qualified only; no shader compiled, validator, browser, GPU implementation, safety assessment or full-repository schema/cache/CI/render, clean/final gate or merge verification.
