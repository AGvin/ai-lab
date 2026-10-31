# NVIDIA NemoClaw

NVIDIA NemoClaw is an installable, self-managed agent environment that combines agent onboarding, NVIDIA OpenShell sandboxing, inference routing, network policy, and lifecycle tooling. NVIDIA currently labels it an alpha / early preview project.

## Runtime and support boundaries

OpenClaw is the default integrated agent. The current support matrix also lists Hermes and LangChain Deep Agents Code, with agent-specific qualifications. Hermes is suitable for its documented evaluation and onboarding paths; NVIDIA does not assert production parity with OpenClaw. Use the matrix to distinguish tested features, limitations, experimental opt-ins, and deferred work.

The operator runs the host tooling and agent sandbox locally or on a self-managed server. NVIDIA does not currently offer managed NemoClaw SaaS. Hosted inference providers can receive model requests independently of where the sandbox runs.

OpenShell supplies the isolation layer; each integrated agent, model, and serving endpoint retains its own identity. Sandbox enforcement and network policy depend on the selected host, runtime, permissions, and credentials. Memory-driven workflows and onboarding examples apply only to the documented agent and release.

The NemoClaw repository is Apache-2.0 licensed. That license does not assign the same terms to every integrated agent, model, or service.

## Related

- [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/) — produced by.

## Official resources

- [NemoClaw documentation](https://docs.nvidia.com/nemoclaw/)
- [Support matrix](https://docs.nvidia.com/nemoclaw/user-guide/hermes/reference/platform-support)
- [Architecture](https://docs.nvidia.com/nemoclaw/user-guide/hermes/reference/architecture)
- [NemoClaw repository](https://github.com/NVIDIA/NemoClaw)
