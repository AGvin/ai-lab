# Documentation Requirements

## Scenario Fit

- Present this scenario for one software engineer whose normal development machine is capable enough for professional coding but has **no useful local accelerator for the model workloads they actually want to run**.
- Keep the constraint outcome-oriented rather than device-label-oriented. An integrated GPU/NPU or weak discrete GPU does not move the user out of this scenario unless the exact runtime/model/context produces useful measured coding performance.
- Distinguish this scenario from `software-engineer-with-local-gpu/`: that route starts from a verified useful local accelerator and asks how far local coding/model workflows can go; this route assumes heavy local inference is not an attractive default.
- Distinguish it from `general-knowledge-worker/`: source-code understanding, repository edits, terminal/tool use, test execution, patch review, long-running agent loops, and software-delivery verification materially change the model route.
- Keep generic coding-model ranking in `decision-guides/software-development/` and complete-loop agent evaluation in `decision-guides/agents-and-automation/`. This scenario owns the **no-local-GPU deployment and workflow trade-off**.

## Separate the Engineering Workloads

- Classify recurring work before choosing one model or product:
  - inline completion and small edits;
  - code explanation and unfamiliar-repository navigation;
  - multi-file implementation/refactoring;
  - debugging and failure diagnosis;
  - test generation and test repair;
  - code review and security review;
  - architecture/design assistance;
  - terminal/tool-driven agentic engineering;
  - long-running issue-to-PR work;
  - multimodal UI/screenshot/document work;
  - repetitive repository maintenance or scheduled automation.
- Do not force every workload through the same execution surface. A local editor assistant, cloud coding agent, direct API harness, deterministic static-analysis/test tool, CPU-local helper, and temporary GPU worker can each own different parts of the workflow.
- Preserve the repository, build/test system, compiler/typechecker, linter, package manager, version control, CI, and application runtime as authoritative verification systems. Model output is proposed work, not completion evidence.

## Default Hosted Coding-Agent Route

- Use a current organization-approved hosted or provider-backed coding assistant/agent as the default capability-first route when source-code data handling and provider access are acceptable. Without a useful local GPU, this normally provides stronger models and better agent-loop latency without operating inference infrastructure.
- Current examples include Codex, Claude Code, and Cursor Agent/Cloud Agents. Treat product names as **execution surfaces**, not proof that one underlying model is universally best for coding.
- Current Codex product evidence supports repository-scale engineering work, cloud environments/worktrees, multi-agent execution, and background/scheduled engineering workflows. Evaluate exact plan access, model availability, rate/credit limits, repository integration, and organization controls at decision time.
- Current Claude Code is a local development agent backed by hosted model inference. Its permission/sandbox controls and model/provider path remain separate from the fact that the CLI executes on the developer machine.
- Current Cursor foreground agents and Cloud Agents have materially different execution/data boundaries. Cursor documents that model requests can send prompts and code context to model providers, while Cloud Agents require cloud storage of code/environment state for the run and can execute terminal commands autonomously in their isolated cloud environment.
- Do not describe a locally installed IDE/CLI as `local AI` merely because the client binary runs locally. Trace where prompts, code context, indexes/embeddings, agent environments, logs, and model inference actually go.

## Source-Code Data Boundary

- Classify the repository before enabling hosted inference: public/open source, ordinary private company code, client code, confidential product code, security-sensitive repository, regulated data/code, or another organization-defined class.
- Verify the complete path: editor/CLI → intermediary service if any → model provider → cloud agent/runtime → connected tools → telemetry/logging/storage. A provider privacy toggle covers only the boundary it actually documents.
- Current Cursor Privacy Mode states that code is not used for training by Cursor or model providers, while Cursor still sends prompts/code context through its service/provider path; current Cloud Agent documentation separately requires temporary cloud code/environment storage. Treat these as distinct properties.
- For organization-managed coding tools, verify admin-enforced privacy/model access, subprocessors, data retention, regional/residency constraints, repository allow/block lists, and whether personal API keys/BYOK change the contractual boundary.
- Do not send secrets, private keys, production credentials, signing material, recovery codes, customer datasets, or unrelated environment files merely because they exist in the repository/workspace. Use ignore rules, secret stores, narrow checkout/context, and redaction where appropriate.
- When policy forbids hosted source-code processing, move to a permitted local/self-hosted route or limit hosted use to public/sanitized material instead of silently weakening the data boundary.

## Agent Permissions and Repository Safety

- Treat an agent that can edit files, run shell commands, access the network, use MCP/tools, create branches/PRs, or operate cloud infrastructure as a side-effecting system rather than a chat model.
- Keep version control active so file edits are recoverable. Review the exact diff and run repository verification before accepting completion.
- Prefer sandboxing, allowlists, bounded network access, and explicit approval for higher-risk actions. Current Cursor guidance recommends guarded run modes and documents that local agents can modify workspace files while shell/MCP/network behavior is separately controlled; current Codex and Claude Code guidance likewise treats permissions/sandbox boundaries as first-class safety controls.
- Do not disable permission checks merely to reduce friction on an untrusted repository or workflow. Source files, issue text, documentation, web content, and tool output can carry prompt-injection instructions.
- Keep credentials out of model-visible context where they are not required. Grant the narrowest repository, filesystem, network, cloud, package-registry, and deployment permissions that let the bounded task succeed.
- Require explicit human approval for destructive Git/ref changes, publishing/releases, production/deployment changes, broad external communication, access-control changes, and other high-impact operations unless a separately governed automation policy authorizes them.

## Evaluate the Complete Engineering Loop

- Compare routes on **task completion**, not one-shot code generation. A representative evaluation should include understanding the request, locating the right code, editing the correct files, running tests/checks, diagnosing failures, correcting the patch, and producing a reviewable final diff.
- Use repository-native acceptance commands. At minimum include the tests directly affected by the change plus applicable typechecking/lint/build steps; for larger changes include the repository's full required verification.
- Measure correctness, unnecessary changes, missed requirements, regression rate, tool-call reliability, recovery from failed commands/tests, number of retries/corrections, human review time, elapsed time, and total cost per accepted change.
- Evaluate on the target language/framework/repository shape. A coding benchmark or provider case study is eligibility evidence, not proof of performance on the user's monorepo, legacy stack, generated code, unusual build system, or proprietary conventions.
- Test degraded cases: failing dependency install, stale task text, ambiguous requirement, conflicting instructions, missing tool, large test output, flaky test, and a tempting but unsafe shortcut.
- Require the agent to stop or escalate when verification cannot be completed rather than converting `I could not run tests` into a completion claim.

## Hosted Model and Product Selection

- Let `decision-guides/software-development/` own the concrete model shortlist for coding tasks. This scenario should select the **route class first** and consume current coding candidates from that guide.
- Prefer the least expensive hosted route that repeatedly passes the user's acceptance suite. Escalate to a stronger/more expensive model only when failures, retries, review cost, long-context/repository reasoning, or agent-loop reliability justify it.
- Do not infer superiority from a product's default model alias. Hosted products can route, replace, or expose multiple models, and model access can vary by plan/organization configuration.
- Long context is not a substitute for repository navigation. Evaluate whether the agent retrieves the right files, follows project instructions, and keeps relevant state without repeatedly re-reading the entire repository.
- If the developer needs several providers/models, compare the additional data paths, model-switching behavior, caches/indexes, pricing, and operational complexity against the measured benefit rather than collecting model access for its own sake.

## Direct API or Custom Harness Route

- Use a direct model API or organization-approved routing layer when the developer needs a custom coding harness, deterministic prompt/tool contract, batch workflow, internal evaluation system, or integration not provided by a managed coding product.
- Include the harness itself in the evaluation: repository retrieval, context construction, tool schema, permissions, loop control, retries, state persistence, error handling, observability, model switching, and verification logic can dominate real reliability.
- An API model with strong coding capability is not automatically a strong coding agent. Compare complete-loop behavior on the same scaffold and tool permissions.
- Apply the full provider-chain/data-boundary rule to routing services and hosted sandboxes. A gateway can change logging, retention, regional processing, pricing, rate limits, and failure modes.
- Protect API credentials with normal secret-management controls and explicit spend/rate limits. Do not store keys in prompts, checked-in config, issue text, or assistant memory.

## CPU-Local Bounded Route

- Keep CPU-local inference as a **bounded fallback or privacy/offline tool**, not the capability default for repository-scale agentic work when there is no useful local accelerator.
- `Qwen2.5-Coder 3B Instruct` and `Qwen2.5-Coder 7B Instruct` remain reproducible compact coding candidates for small generation/edit/explanation/test-drafting experiments; `Qwen3 8B` can remain a broader reasoning/text candidate. Their continued availability and canonical identities do not establish current superiority.
- Use CPU-local models for tasks whose latency and context needs are genuinely small enough: private snippets, bounded transformations, explanation, local classification/routing, commit-message/test skeleton assistance, or offline fallback.
- Do not preserve the old blanket `16–32 GB RAM` statement as a recommendation. Determine usable memory after the OS/IDE/build tools, exact artifact/quantization, runtime buffers, context/KV cache, and concurrent developer workload.
- Measure time to first token, sustained generation, prompt-processing speed on realistic code context, context limit/headroom, CPU utilization, heat/noise/power, and accepted-result correction cost. `The model loads` is not evidence that it is useful interactively.
- A modern developer laptop can outperform a cheap generic CPU VPS; a VPS can also win under another CPU/memory configuration. Benchmark the exact systems rather than comparing vCPU/RAM labels.
- If local privacy is mandatory and CPU performance is inadequate, the correct escalation can be an approved self-hosted/rented accelerator or a smaller/narrower workflow—not pretending the slow route is productive.

## Temporary or Rented Accelerator Route

- Use temporary GPU/accelerator capacity when the user needs open-weight/self-hosted model control or stronger local-like inference only intermittently and does not own suitable hardware.
- Treat the route as an **ephemeral infrastructure workflow**: provision, attach/persist required model/cache data, verify runtime/driver compatibility, run the workload, preserve outputs, and stop/terminate resources according to the provider's actual billing/storage semantics.
- Include startup/model-download time, persistent volume/storage charges, idle capacity, egress, retries after unavailable hardware, image/runtime maintenance, and forgotten-running-resource risk in total cost.
- Do not treat an `RTX 3090/4090-class 24 GB` label from legacy notes as a guaranteed model fit. Verify exact GPU/VRAM, model artifact, precision/quantization, context/KV headroom, runtime, concurrency, and accepted performance.
- Use `Qwen3 14B` or current coding-specific open models only as evaluation candidates when their canonical model evidence and exact artifact/runtime fit are available; do not retain a legacy model merely because it once matched a rented GPU example.
- For long-running daily coding, compare recurring rental/operations cost with a managed coding service or organization-owned inference. Ephemeral GPU economics can be poor when repeated startup, storage, maintenance, and idle overhead dominate.

## Remote Development and Self-Hosted Alternatives

- A developer can keep a lightweight local editor while running model inference or the whole coding environment on an approved remote workstation/server. Treat this as a separate route from third-party cloud coding agents because ownership, network, storage, identity, and maintenance differ.
- Verify repository location, network latency, VPN/zero-trust access, secret storage, build/test data, model endpoint exposure, backups, and concurrent-user isolation.
- Do not expose an unauthenticated local-model or agent endpoint merely to make remote development convenient.
- If server operation, monitoring, updates, scheduling, multi-user access, or GPU capacity planning becomes the main problem, route to infrastructure/hardware owners rather than expanding this scenario into platform engineering.

## Multimodal Development Work

- Use multimodal capability only when screenshots, design references, diagrams, PDFs, browser state, logs rendered as images, or visual regression evidence are recurring engineering inputs.
- A local CPU multimodal model can be technically runnable yet operationally poor because image/audio preprocessing and long multimodal context increase latency and memory pressure.
- Prefer the managed coding/assistant route when visual input materially improves accepted work and the data boundary permits it; use compact local multimodal candidates only after exact runtime/device validation.
- Verify visual conclusions against the actual UI/application/test result. A model description of a screenshot is not a regression test.

## Cost per Accepted Engineering Change

- Compare the complete route by **cost per accepted engineering change**, including subscription/API/compute spend, retries, developer review/correction time, CI usage, cloud-agent runtime, temporary-GPU startup/idle/storage cost, local power/thermal cost, and environment administration.
- Cheap tokens or a free local model can be expensive when the engineer spends substantially more time correcting repository misunderstandings or waiting on CPU inference.
- A premium hosted coding agent can be economical when it consistently completes larger changes with fewer retries and less review effort; require measured evidence on the user's workload rather than assuming this from marketing.
- Keep provider/product switching cost visible: separate indexes, project instructions, permissions, billing, data boundaries, and learned workflow conventions can erase small model-price advantages.

## Escalation Triggers

- Move from CPU-local to hosted when latency, context, tool use, or quality repeatedly fails the acceptance suite and hosted processing is permitted.
- Move from managed coding product to direct API/custom harness when the required tools, deterministic controls, evaluation instrumentation, or integration cannot be expressed safely in the managed surface.
- Move to a temporary/self-hosted accelerator when open-weight/private control is required and CPU-local performance is inadequate.
- Move to `software-engineer-with-local-gpu/` when the developer obtains or gains reliable access to a useful local accelerator and local inference becomes a first-order route rather than a fallback.
- Move to `mac-developer-or-creator/` when Apple-Silicon unified-memory/MLX constraints materially determine local inference fit.
- Move toward `sensitive-data-professional/` or an organization/high-security route when source-code classification, client contracts, regulated data, or isolation requirements dominate the decision.
- Move to team/organization software-development or internal-platform scenarios when shared agent policy, repository-wide permissions, budgets, observability, multi-user infrastructure, or standardized tooling become the real problem.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when evaluating CPU-local inference or another exact owned/fixed hardware route.
- Use `../../../hardware/sub/computers/` for the developer laptop/workstation and its CPU/vendor specialization where material.
- Use `../../../hardware/sub/servers/` only when an owned/approved remote inference server is actually part of the route.
- Do not turn the absence of a local GPU into hardware purchasing advice. Hosted, API, remote, rented, CPU-local, and hybrid routes must remain valid alternatives.

## Canonical Links

- Link compact local candidates to `catalog/models/alibaba/qwen/qwen2-5-coder/models/qwen2-5-coder-3b-instruct`, `catalog/models/alibaba/qwen/qwen2-5-coder/models/qwen2-5-coder-7b-instruct`, and `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link heavier local/rented candidates only through their exact canonical Model Reference identities after the current coding decision guide retains them for the intended role.
- Link generic coding-model evaluation to `decision-support/selection/models/decision-guides/software-development` and complete-loop agent evaluation to `decision-support/selection/models/decision-guides/agents-and-automation` instead of duplicating their candidate rankings.
- Product-specific coding-agent documentation remains owned by the applicable software/service catalog entities where materialized; this scenario records only the route implications needed for model selection.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI Codex product/security material, Anthropic Claude Code permission/sandbox material, Cursor privacy/agent/cloud-agent security documentation, current official Qwen model artifacts, and canonical AI Lab model-selection owners.
- Current evidence confirms that coding-agent execution surfaces differ materially in code/data routing, local-versus-cloud environment placement, permission/sandbox behavior, autonomous command execution, network access, and organization controls. These execution properties must not be inferred from the underlying model name.
- Qwen2.5-Coder 3B/7B and Qwen3 8B remain available canonical local candidates, but their model-card/provider status is eligibility evidence only; CPU practical fit and accepted repository-level quality remain workload/device measurements.
- Hosted model aliases, coding-agent capabilities, cloud-environment behavior, prices/credits/rate limits, privacy/retention guarantees, provider/subprocessor chains, and rented-accelerator availability/pricing are mutable; recheck them before rendering current advice.
- Provider coding benchmarks and end-to-end product claims are not independent AI Lab proof of correctness, maintainability, security, or lower accepted-result cost on the target repository.

## Validation

- The route is specifically for a developer without a **useful** local accelerator; nominal hardware labels do not determine scenario membership.
- Hosted coding agent, direct API/custom harness, CPU-local helper, temporary accelerator, and remote/self-hosted routes remain distinct choices with distinct data and operational boundaries.
- A local editor/CLI is not mislabeled as local inference when prompts/code/model execution leave the machine.
- Source-code privacy checks cover the complete client/intermediary/provider/cloud-agent/tool path.
- Agent permissions, sandboxing, network/tool access, prompt injection, secrets, and recoverability are part of route evaluation.
- Completion is measured by repository-native tests/checks and final diff review rather than generated-code plausibility.
- Compact local models remain bounded candidates and no RAM, parameter-count, quantized-size, or load-success shortcut is used as practical-fit proof.
- Temporary accelerator cost includes startup, persistence, idle/storage, teardown, and availability risk rather than hourly GPU price alone.
- Hardware buying remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
