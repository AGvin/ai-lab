# Documentation Requirements

## Scenario Fit

- Present this scenario for organizations or environments where **network isolation, disconnected or air-gapped operation, classified/highly sensitive data, controlled artifact ingress/egress, local administration, model/runtime supply-chain assurance, and zero hidden cloud dependency** dominate AI model selection.
- Keep the scenario organization-scale. General regulatory governance belongs in `regulated-organization/`; ordinary enterprise privacy/security controls belong in the applicable domain or `internal-ai-platform/`; a single professional with sensitive data belongs in `professionals/sensitive-data-professional/`.
- Distinguish `disconnected`, `air-gapped`, `restricted-egress`, `sovereign/on-prem`, and `offline edge` deployments. They are not interchangeable security states.
- Do not turn this page into a classified-network implementation manual. It owns the model/runtime route and the evidence required to select models for a high-security boundary.

## Security Boundary Before Model Choice

- Define the exact boundary first: connected enterprise network, restricted-egress enclave, disconnected enclave, physically air-gapped network, field/edge system, classified domain, or another organization-defined zone.
- Record which networks, systems, administrators, removable-media paths, maintenance stations, registries, package repositories, telemetry collectors, and update channels can cross the boundary.
- Define authorized data classes, model artifacts, software packages, logs, outputs, and user populations for each zone.
- Do not call a deployment `air-gapped` when it relies on ordinary outbound package/model downloads, cloud licensing callbacks, remote telemetry, or hidden external APIs.
- Treat transfer between zones as a governed security workflow rather than ordinary file copy.

## Local/Disconnected Inference as the Default Route

- Prefer local/self-hosted inference when the security boundary prohibits hosted model processing or external network access.
- Current NVIDIA NIM LLM/VLM documentation explicitly supports air-gapped deployment by pre-staging model assets/cache on a connected system and serving them locally with no internet/remote registry connection in the isolated phase.
- Current Foundry Local on Azure Local supports on-premises inference and disconnected operation with local Kubernetes-managed model serving; treat current preview/feature status as mutable.
- Use these products only as evidence that modern supported disconnected routes exist. Exact model/runtime/security fit still requires organization-specific validation.
- Do not preserve one vendor/runtime as a permanent default. Route choice depends on approved model artifacts, target hardware, operating environment, supply-chain controls, and operations.

## Eliminate Hidden External Dependencies

- Inventory every component that may initiate outbound communication: model runtime, model hub client, container runtime, package manager, license service, observability SDK, telemetry, crash reporting, DNS/NTP, update checker, browser/web UI, plugin, tokenizer/resource downloader, certificate validation, and agent tool.
- Verify startup and steady-state behavior with outbound network denied.
- Current NVIDIA air-gap guidance explicitly supports local model paths/caches and documents no-key/no-outbound operation in the isolated phase; use equivalent evidence for any runtime before approval.
- Do not rely on vendor claims alone. Capture network telemetry/firewall evidence during validation.
- Disable optional usage statistics/telemetry where required and verify they do not become startup dependencies.

## Two-Phase Artifact Workflow

- Model disconnected deployment as at least two phases:
  - connected acquisition/staging;
  - isolated verification/deployment.
- Acquire models, container images, packages, runtime dependencies, licenses where required, SBOM/signature metadata, documentation, and evaluation assets in an approved staging environment.
- Verify identities/hashes/signatures and malware/supply-chain controls before transfer.
- Transfer only approved immutable artifacts through the organization's authorized channel.
- Re-verify hashes/signatures after transfer before promotion into local registries/model stores.
- Preserve artifact manifest, source, version, hash, approval owner, transfer date, and target environment.

## Model Artifact Provenance

- Require exact model identity: producer, model family/version, revision/commit/tag, artifact format, quantization/precision, license, tokenizer, adapters/LoRAs, auxiliary encoders, safety/guard models, and runtime compatibility.
- Do not import an artifact from an unofficial mirror merely because its file name matches an approved model.
- Preserve checksums and trusted source references for every artifact entering the enclave.
- Treat converted/quantized/optimized artifacts as new deployment artifacts with their own provenance and validation.
- If the organization builds an optimized TensorRT/ONNX/GGUF/other artifact internally, record the source model, conversion tool/version, parameters, and validation evidence.

## Container and Package Supply Chain

- Use approved container/image registries, OS/package mirrors, Python/Node/system package repositories, and vulnerability/signature scanning paths that can operate within the boundary.
- Mirror only the dependencies required for approved workloads where practical.
- Pin versions/digests for production deployment and preserve dependency manifests/SBOMs.
- Do not allow runtime startup to download Python wheels, tokenizer files, model components, browser binaries, CUDA/runtime packages, or plugins dynamically.
- Treat custom nodes/plugins/extensions as executable software requiring the same review as normal application dependencies.

## Local Registry and Model Store

- Maintain local container registry/model repository/package mirror where repeated deployments or multiple nodes require it.
- Separate staging/quarantine from approved production artifacts.
- Use immutable digests/hashes and access controls rather than mutable `latest` aliases for sensitive production paths.
- Define retention, rollback, deprecation, and revocation for compromised or superseded artifacts.
- Verify that model-serving systems use only the approved local repository in disconnected mode.

## Licensing and Entitlement

- Verify that the model/runtime/license permits the intended offline, internal, classified, commercial, or government use as applicable.
- Determine whether software requires online activation, periodic license renewal, telemetry, or vendor callback and whether an approved offline mechanism exists.
- Do not select a technically suitable runtime that cannot legally or operationally remain licensed inside the boundary.
- Preserve license version/effective date and entitlement evidence with the deployment record.

## Runtime and Hardware Fit

- Bind every model recommendation to exact target hardware, runtime/backend, model artifact, quantization/precision, context/KV cache, concurrency, modalities, and sustained workload.
- Measure usable memory after OS/platform/security agents and other resident services, not nominal RAM/VRAM alone.
- Test startup time, prompt processing, generation throughput, p50/p95 latency, memory pressure, accelerator utilization, thermals/power where relevant, and concurrent-user behavior.
- Do not infer practical fit from parameter count, quantized file size, GPU name, TOPS, or successful loading.
- Keep unsupported or unmeasured model/runtime/hardware combinations `Unknown`.

## CPU, GPU, and Accelerator Separation

- Distinguish CPU-only, GPU, NPU/accelerator, shared-memory, and multi-device execution paths.
- Verify exact operator/kernel/runtime support rather than assuming a model can use every accelerator present.
- Measure fallback to CPU and its latency/memory effects.
- For multi-GPU/multi-node inference, verify tensor/pipeline/data-parallel support, interconnect requirements, failure behavior, and usable memory/context scaling rather than summing VRAM blindly.
- Hardware buying remains outside this scenario; selection is for owned/fixed approved infrastructure.

## Local API and Service Security

- Treat local inference endpoints as network services requiring authentication, authorization, TLS where applicable, rate/size limits, request isolation, and audit.
- Do not expose an unauthenticated OpenAI-compatible endpoint to an entire secure network merely because the model is on-premises.
- Bind service identities and user/application access to least privilege.
- Separate administrative model deployment privileges from inference-consumer privileges.
- Validate cross-tenant/project separation when multiple security domains or teams share infrastructure.

## Network Segmentation and Egress

- Use deterministic firewall/network policy to enforce allowed flows between clients, model servers, registries, observability, and storage.
- For strict disconnected environments, validate that no default route/outbound DNS/HTTP path exists from inference workloads.
- For restricted-egress environments, allow only named approved destinations and verify agents/tools cannot select arbitrary hosts.
- Do not rely on model instructions such as `do not access the internet` when network policy can enforce it.
- Treat web search, remote MCP, cloud object storage, external embeddings, remote OCR, and third-party moderation as explicit boundary expansions requiring approval.

## Time, Certificates, and Infrastructure Dependencies

- Define trusted local time/NTP, DNS, PKI/certificate issuance/rotation, secrets, identity, and package-signing infrastructure for disconnected operation.
- Verify certificates/licensing/runtime behavior during prolonged disconnection and clock drift scenarios.
- Avoid dependencies on public OCSP/CRL or cloud identity endpoints unless the security architecture explicitly supports them.
- Test restart/recovery after extended offline periods.

## Identity and Privileged Administration

- Use named/administered identities for platform operators, model publishers, application owners, and inference clients.
- Apply MFA/privileged access workflows where the environment permits and policy requires them.
- Use separate service/workload identities for applications and agents.
- Record privileged model/runtime/configuration changes.
- Do not share static administrator/API credentials across workloads for convenience.

## Secrets and Key Material

- Keep API keys, signing keys, certificates, private keys, recovery material, credentials, and encryption keys out of model prompts/context/logs.
- Use enclave-approved secret storage and workload identity/credential injection.
- Do not import connected-environment tokens such as model-hub/API credentials into a strict air-gapped runtime when local artifacts make them unnecessary.
- Rotate/revoke secrets according to local policy and preserve offline recovery procedures.

## Retrieval and Local Knowledge

- Keep RAG sources, embeddings, indexes, OCR artifacts, caches, and generated summaries within the approved zone when source data cannot leave it.
- Preserve deterministic source permissions and project/compartment separation.
- Do not assume `local RAG` prevents cross-document leakage or prompt injection.
- Treat imported documents as untrusted instructions even when they entered through approved media.
- Verify source provenance/currentness and keep citations/record IDs for material answers.

## Agent and Tool Restrictions

- Treat agents as a higher-risk tier because local inference can still execute destructive actions inside the secure boundary.
- Explicitly inventory tools: shell, files, databases, ticket systems, code repositories, deployment systems, device/industrial controls, email/message gateways, removable media, and cross-domain transfer tools.
- Use least privilege, allowlists, sandboxing, approval gates, bounded retries, deterministic validation, and audit.
- Do not grant an agent access to cross-domain transfer or release channels merely because it can generate useful summaries.
- Prevent retrieved documents/code/logs from expanding agent authority through prompt injection.

## Cross-Domain Transfer and Output Release

- Treat export of model outputs, summaries, code, embeddings, logs, images, or derived data from the enclave as a separate release workflow.
- Define what content may cross, who approves it, required review/redaction/sanitization, malware/content inspection, and destination.
- Do not assume a generated summary is safe to release because it contains no verbatim secret; models can transform/classify sensitive information into derived sensitive content.
- Preserve release decision/evidence where policy requires it.

## Updates and Patch Management

- Maintain an explicit cadence/process for model, runtime, OS, driver, container, package, vulnerability signature, and security-policy updates.
- Acquire updates through the approved connected staging path and re-run supply-chain and compatibility checks before transfer.
- Do not auto-update models/runtime behind mutable tags inside the enclave.
- Preserve rollback to the last approved version.
- Track security advisories/vulnerabilities for deployed runtime/model dependencies despite disconnection.

## Model Change and Revalidation

- Treat model revision, quantization, tokenizer, adapter, runtime, driver, CUDA/ROCm/accelerator stack, prompt/system policy, context length, or inference-engine change as potentially behavior-changing.
- Re-run applicable evaluation before production promotion.
- Use canary/shadow/bounded rollout where the environment supports it.
- Do not combine many changes in one promotion when isolation of regressions is required.

## Evaluation Suite

- Build a versioned offline evaluation pack that can be transferred and run entirely inside the secure environment.
- Cover representative task quality, long context, structured output, local RAG, tool/agent tasks where applicable, refusal/escalation, prompt injection, sensitive-data leakage, concurrency, and exact device/runtime performance.
- Include negative network tests proving that the workload remains functional with outbound connectivity denied and fails safely when an unapproved external dependency is requested.
- Include artifact-integrity tests and deployment restart/recovery tests.
- Preserve evaluation data provenance and prevent test datasets from importing data classes not approved for the enclave.

## Prompt Injection and Imported Content

- Treat all imported files, code, documents, packages, model cards, issue text, logs, emails, and data as potentially adversarial content.
- Disconnection reduces remote attack surface but does not make local content trustworthy.
- Keep system instructions/tool policy outside imported content.
- Test direct/indirect prompt injection against agents that can access privileged local systems.
- Do not reveal secrets/system configuration because an imported document requests them.

## Model and Runtime Supply-Chain Threats

- Treat model weights, tokenizer/config files, custom code, pickle-like formats, plugins, container images, installation scripts, adapters, and custom operators as software/supply-chain inputs.
- Prefer formats/runtime paths that minimize arbitrary-code execution where feasible and supported.
- Scan/review executable components and disable `trust remote code`-style behaviors unless explicitly reviewed/required.
- Verify model package contents before importing to sensitive zones.
- Maintain revocation/incident procedures for compromised upstream artifacts.

## Observability Without External Telemetry

- Use local logs, metrics, traces, audit stores, SIEM integration, and performance monitoring inside the permitted zone.
- Ensure observability components themselves do not export telemetry externally.
- Record model/runtime/artifact version, request/consumer identity as permitted, latency/errors/resource use, tool actions, and security events.
- Minimize sensitive prompt/output logging according to need-to-know and retention policy.
- Preserve enough evidence for incident and performance investigation without creating an unnecessary sensitive-data copy.

## Backup, Recovery, and Continuity

- Define backups for model artifacts, registries, configuration, evaluation packs, indexes, audit records, and required application state according to zone policy.
- Test restore without internet access.
- Keep spare/recovery artifacts for critical runtimes whose upstream source may be unavailable during an incident.
- Define degraded/manual workflow if the AI service or accelerator fails.
- Do not make safety/security/mission-critical operation dependent on an AI service without an accepted fallback.

## Vendor Support Boundary

- Define how vendor support/debug bundles/logs can be provided from a high-security environment.
- Minimize exported diagnostics and apply release review/redaction.
- Do not enable remote support tunnels or cloud diagnostics that violate the boundary.
- Preserve internal ability to diagnose common failures because vendor direct access may be impossible.

## Sovereign and Connected-On-Prem Variants

- A connected sovereign/on-prem deployment can use vendor control planes, Arc-like management, or cloud-linked updates while keeping inference local; treat that as distinct from strict disconnection.
- Current Foundry Local on Azure Local is a current example of on-prem local inference that can also operate disconnected; verify which management/control-plane dependencies apply to the selected mode.
- Do not label connected on-prem as air-gapped merely because inference data stays local.
- Record which operations require reconnect/staging and which remain fully local.

## Cost per Accepted Secure Outcome

- Compare **total cost per accepted secure outcome**: model/runtime licenses, hardware, local registries/storage, transfer/staging, security review, scanning/signing, platform operations, patching, evaluation, admin, electricity/cooling, human review, downtime, and incident risk.
- A managed cloud route can be cheaper operationally but is irrelevant if it violates the boundary.
- A smaller local model can be economically superior when it meets acceptance and materially reduces hardware/operations burden.
- A larger model is wasted cost if runtime/hardware limits cause unacceptable latency or if its capabilities require forbidden external tools.

## Escalation Triggers

- Move to this scenario when disconnected/air-gapped/sovereign/threat-sensitive isolation materially determines AI architecture.
- Move to `regulated-organization/` when formal compliance/audit obligations dominate but normal enterprise connectivity remains acceptable.
- Move to `internal-ai-platform/` when centralized model gateway/runtime/portfolio operation within the secure environment becomes the main problem.
- Move to domain scenarios such as SOC/manufacturing/legal when their task-specific acceptance rules dominate inside the same security boundary.
- Do not recommend AI deployment when no available artifact/runtime/hardware route can meet both security-boundary and task-quality requirements.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` whenever the secure environment uses fixed local hardware and exact runtime/model fit is a first-order constraint.
- Use `../../../hardware/sub/servers/`, `../../../hardware/sub/computers/`, or `../../../hardware/sub/embedded/` according to the actual deployment target.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link regulatory governance to `catalog/models/selection/user-scenarios/organizations/regulated-organization`.
- Link shared local platform/gateway operation to `catalog/models/selection/user-scenarios/organizations/internal-ai-platform`.
- Link SOC, manufacturing, legal, and other domain acceptance to their scenario owners.
- Link exact runtimes/models/software to canonical catalog owners only when current evidence justifies them.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party NVIDIA NIM LLM/VLM air-gap deployment documentation and current Microsoft Foundry Local on Azure Local disconnected-inference documentation.
- Current NVIDIA evidence establishes a two-phase air-gap workflow with model assets prepared on a connected system and served from local cache/model paths without remote registry access or API credentials in the isolated phase; current Foundry Local on Azure Local evidence establishes local on-prem inference and disconnected operation with local model serving and CPU/GPU options.
- Air-gap/runtime procedures, supported models, model profiles, container versions, licensing, telemetry behavior, local management/control planes, driver/runtime support, and hardware compatibility are mutable; recheck them before rendering current guidance.
- Organization security architecture, exact artifact provenance, offline network tests, exact runtime/hardware measurements, and enclave-specific evaluation remain the acceptance authority.

## Validation

- `disconnected`, `air-gapped`, `restricted-egress`, and connected on-prem routes remain explicitly distinct.
- Runtime startup and steady-state external dependencies are inventoried and verified under network denial.
- Model/container/package artifacts use an approved connected-stage → transfer → local verification workflow with identity/hash/signature provenance.
- No remote registry, package download, telemetry, license callback, or cloud tool is assumed available inside a strict air gap.
- Local inference endpoints still use authentication, least privilege, segmentation, and audit.
- Imported documents/models/plugins remain untrusted supply-chain/prompt-injection inputs.
- Model/runtime/hardware fit is measured on exact fixed infrastructure rather than nominal RAM/VRAM/TOPS/load-success shortcuts.
- Agent/tool actions and cross-domain release remain separate controlled boundaries.
- Offline update, rollback, observability, backup, restore, and evaluation procedures are included.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
