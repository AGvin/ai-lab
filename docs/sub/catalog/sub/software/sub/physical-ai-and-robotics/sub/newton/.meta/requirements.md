# Documentation Requirements

## Requirements

- Present Newton as an independently released, open-source physics simulation engine and Python SDK whose first-class purpose is robot learning, robotics simulation, and extensible multiphysics. Keep Physical AI and Robotics as its canonical owner.
- Distinguish Newton from the Warp kernel framework, its predecessor warp.sim, integrated solver backends, robot assets, and training frameworks such as Isaac Lab; keep its model/state/control APIs, asset import, solvers, sensors, and viewers within the Newton identity.
- Ground released lifecycle in v1.7.0, published 2026-10-14. Keep release status separate from component maturity: solver capabilities, differentiation, coupled simulation, and Isaac Lab integration have specific support or experimental limits.
- Explain the decision between direct engine integration and higher-level environment/training frameworks, including MuJoCo Playground, robosuite, and Isaac Lab. Select solvers by coordinate representation, supported bodies/joints/contacts, differentiation, and component maturity; do not describe every backend as differentiable.
- Explain that Newton runs in the caller's Python process and does not sandbox assets, extensions, credentials, network access, or mutually untrusted tenants. Scene references may load further files or network resources.
- Preserve the v1.7.0 serialized-policy boundary: USD-referenced Torch checkpoints are rejected unless the caller explicitly enables allow_unsafe_torch_checkpoints for trusted inputs; direct neural-drive construction has a separate loading path. Treat serialized policies/checkpoints as trusted executable inputs.
- Preserve the documented ViewerViser boundary: its underlying unauthenticated HTTP/WebSocket listener binds all interfaces even when share is false and a localhost URL is printed; intentional remote use requires access controls around the viewer.
- Explain installed-Warp-dependent GPU/driver compatibility, macOS CPU-only support, optional dependency groups, and the difference between release lockfiles and downstream dependency resolution.
- State that minor releases may contain breaking changes and only the most recent minor release line is actively maintained; keep installation constraints and migration guidance release-scoped.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- First-class robot-learning evidence satisfies the category boundary; generic physics use alone is not the inclusion rationale.
- Provenance resolves to Newton Project, with Linux Foundation hosting and Disney Research, Google DeepMind, and NVIDIA initiation distinguished from sole-company ownership.
- The producer edge has an exact inverse and all reader links resolve.
- Release, feature maturity, compatibility, performance, and physical-transfer claims stay within their cited source scope; documentation review conveys no runtime or physical safety assurance.
