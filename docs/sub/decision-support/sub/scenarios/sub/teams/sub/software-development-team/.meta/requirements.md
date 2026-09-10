# Documentation Requirements

## Scenario Fit

- Present this scenario for a bounded software-development team—several to tens of developers—sharing repositories, coding assistants/agents, engineering standards, reviews, budgets, and acceptance responsibility.
- Keep the scenario team-scoped. One engineer choosing a personal route belongs in the relevant professional software-engineer scenario; cross-team centralized model gateways, organization-wide identity/policy, enterprise contracts, shared inference infrastructure, and platform ownership belong in `organizations/internal-ai-platform/` when they dominate.
- Keep coding-task model evidence in `decision-guides/software-development/` and complete-loop agent safeguards in `decision-guides/agents-and-automation/`. This scenario owns **team adoption, routing, governance, review, and cost economics**.
- Do not select a team route from benchmark rank or seat price alone. The route must work across representative repositories, users, task types, security boundaries, and review practices.

## Define the Team Engineering Loop

- Identify the team workflows that AI may assist:
  - inline completion and small edits;
  - repository Q&A/navigation;
  - issue-to-code implementation;
  - debugging and test repair;
  - refactoring/migration;
  - code review and security review;
  - documentation and release notes;
  - dependency/maintenance work;
  - CI/test failure diagnosis;
  - cloud coding-agent issue/PR work;
  - scheduled/repetitive engineering automation.
- Preserve repository-native issue/PR/review, test, typecheck, lint, build, security, and CI systems as the acceptance layer.
- A generated patch is not complete because the agent says it is complete; it must satisfy the team's required checks and review contract.

## Default Managed Coding-Tool Pilot

- Start with a managed coding assistant/agent pilot when source-code processing is approved and the team does not yet need to operate shared inference infrastructure.
- Current team-capable examples include GitHub Copilot Business/Enterprise, Cursor Teams/Enterprise, Codex, and Claude/Claude Code integrations. Treat products as execution surfaces with different policies, data paths, agent environments, models, and cost controls—not as interchangeable labels for one coding model.
- Pilot on representative users and repositories rather than only enthusiasts or toy projects. Include at least one ordinary service/library, one larger/legacy repository if the team has one, and one workflow where tests fail initially.
- Evaluate acceptance rate, correction/review time, total elapsed time, regression rate, unsafe/unnecessary changes, developer satisfaction, usage distribution, and total cost per accepted change.
- Keep the pilot bounded enough that the team can disable or replace the route without losing source-of-truth engineering state.

## Team Policy and Model Availability

- Define who may use which coding surfaces, models, cloud agents, CLI tools, MCP servers, browser/network access, and preview features.
- Current GitHub Copilot Business/Enterprise policies can control available features/models and whether partner coding agents such as Claude or Codex are enabled for repositories. Treat exact policy surfaces as mutable.
- Current Cursor enterprise controls include model/provider restrictions, agent/sandbox/network controls, repository blocklists, usage/spend controls, and group/team-level policy. Treat Team versus Enterprise capability differences explicitly.
- Do not rely on each developer to remember a verbal model policy when the chosen platform can enforce it centrally.
- Re-review policy after new models/providers/agent surfaces are introduced; `allowed provider` does not imply every future model/configuration from that provider is acceptable.

## Repository and Source-Code Boundary

- Classify repositories and paths: public, ordinary internal, confidential/proprietary, customer data/code, security-sensitive, regulated, production configuration, or another organization-defined class.
- Verify the complete client/agent path for each coding product: IDE/CLI/web → provider/intermediary → model → cloud agent/sandbox → repository integration → tools/network → telemetry/storage.
- A locally installed IDE/CLI does not prove local inference or local-only code handling.
- Use repository allow/block lists or equivalent controls where a product supports them and the team has repositories that must not be processed.
- Keep secrets, production credentials, signing keys, customer exports, private keys, and unrelated environment files out of model/agent context through secret stores, ignore rules, scoped checkouts, and tool policy.

## Cloud Coding Agents

- Treat cloud coding agents as remote execution environments with repository access, not as chat assistants.
- Verify how code is cloned/stored, how long the environment persists, which repositories/branches are accessible, what network access is available, which secrets can be injected, and how artifacts/commits/PRs return to the team.
- Current GitHub enterprise controls can govern cloud/partner agents and expose agent activity/audit surfaces; current Cursor Cloud Agents run in isolated virtual machines and can store encrypted repository copies temporarily while a run executes. Treat product-specific behavior as current evidence only.
- Do not enable cloud agents on repositories whose code-storage/execution boundary is not approved.
- Require branch/worktree/PR isolation appropriate to the team's Git workflow so autonomous edits are reviewable and recoverable.

## Agent Permissions and Sandboxing

- Treat shell, filesystem write, network, browser, MCP/tool, package-manager, cloud, GitHub, deployment, and secret access as separate capabilities.
- Use least privilege and the strongest practical sandbox/allowlist defaults for untrusted or broad tasks.
- Current Codex safety guidance explicitly treats access boundaries, approval gates, telemetry, and higher-risk actions as first-class deployment controls; current Cursor enterprise controls can enforce sandbox/network/auto-run constraints. Apply the same conceptual requirement regardless of product.
- Do not disable approval/sandboxing globally merely to improve benchmark speed or reduce friction.
- Prompt injection from repository files, issues, dependency docs, web pages, tool output, test artifacts, and code comments remains a team security risk.

## Shared Engineering Instructions and Standards

- Keep canonical coding standards, architecture rules, test commands, repository workflows, and protected operations in version-controlled project/repository instructions rather than relying on individual chat memory.
- Use team rules/memory features only as derived assistance; keep durable standards in the repository or another authoritative engineering owner.
- Current GitHub Copilot Memory can store repository facts/user preferences under organization/enterprise billing ownership and is administratively controllable; treat it as mutable derived context, not the canonical source of standards.
- Current Cursor Team Rules can enforce shared agent instructions. Verify precedence with repository-level instructions so conflicting rule layers do not silently produce different behavior across developers.
- Review stored agent memories/rules when repositories or standards change materially.

## Model Routing by Task

- Consume the current coding-model shortlist from `decision-guides/software-development/`.
- Do not force every task onto the strongest/most expensive model. Use lower-cost/fast models for bounded edits, explanation, boilerplate, classification, or review preprocessing when they pass acceptance; escalate difficult repository reasoning, debugging, planning, or long agent loops when evidence justifies it.
- Preserve a stable fallback when a preferred model is rate-limited, unavailable, changes behavior, or exceeds team budget.
- Evaluate model changes using the same representative task suite; do not change the whole team route from release-note claims alone.
- Keep provider/model switching explicit because data policy, tool support, context behavior, price, and output quality can change together.

## Human Review and Ownership

- Every agent-generated change must have a clear human/team owner for review and integration unless the team has explicitly approved a bounded autonomous maintenance workflow with deterministic checks.
- Preserve normal code-review standards. Do not lower review because a change was generated by a preferred model or because tests pass.
- Require reviewers to inspect scope, architecture, security, tests, dependencies, generated files, config, migrations, and external behavior as applicable.
- Separate agent author from final approval when practical for higher-risk changes.
- Track recurring agent failure patterns and feed durable fixes into repository instructions/tests/tooling rather than repeatedly correcting them in chat.

## Verification Contract

- Define task-class verification before rollout. Examples: unit/integration tests, typecheck, lint, build, migration validation, security scanning, dependency checks, UI/regression tests, performance tests, and manual acceptance.
- Agents must surface which checks actually ran, which failed, and which could not run.
- Treat skipped/unavailable verification as an explicit incomplete state, not success.
- Require bounded retries. An agent that repeatedly edits until tests happen to pass can introduce unrelated regressions or excessive compute cost.
- For flaky tests or nondeterministic systems, distinguish pre-existing instability from agent-caused failure with evidence.

## Team Evaluation Set

- Maintain a versioned evaluation set sampled from real team work rather than synthetic coding puzzles alone.
- Include multiple task sizes and failure modes: small bug, multi-file feature, refactor, test failure, unfamiliar subsystem, ambiguous issue, dependency problem, and a task the agent should decline/escalate.
- Score complete-loop success: requirement coverage, correct files, code quality, test outcomes, regression/incident risk, review comments, retries, elapsed time, and human correction effort.
- Compare agent/model configurations under similar repository state and tool permissions where possible.
- Provider benchmarks can select candidates for evaluation; they do not replace team-specific evidence.

## Usage, Spend, and Capacity

- Measure per-user and per-surface usage distribution rather than average seat cost only. A few heavy agent users can dominate usage-based spend while many seats use little capability.
- Current Cursor enterprise tooling exposes model access, spend controls/alerts, and usage breakdown by product surfaces; current GitHub plans expose centralized policy/licensing/usage controls. Treat exact meters and billing units as mutable.
- Include premium-model multipliers, cloud-agent runtime/request costs, API overages, CI usage, and duplicated subscriptions where material.
- Track cost per accepted engineering change or saved engineer-hour, not prompts/tokens alone.
- Use soft/hard limits carefully so budget controls do not cause silent fallback to unapproved personal tools.

## Local and Self-Hosted Team Workers

- Use shared local/self-hosted inference only when repeated utilization, source-code boundary, offline/provider-independence needs, or measured economics justify operating a team service.
- Keep `Qwen2.5-Coder 7B Instruct` as a bounded lower-resource coding-worker candidate and `Qwen3-Coder-Next` as a larger specialist evaluation candidate only when current model/runtime/infrastructure evidence supports the intended task. Candidate ranking remains in the coding guide.
- A shared local endpoint does not prove the IDE/agent/client path is local; verify any hosted embeddings, telemetry, search, or fallback model.
- Measure concurrency, queue time, context/KV memory, model loading, GPU/host utilization, reliability, updates, monitoring, access control, and accepted-result quality under simultaneous developers.
- If operation requires centralized gateway, multi-team quotas, provider abstraction, shared observability, policy, or infrastructure ownership, escalate to `organizations/internal-ai-platform/`.

## Hybrid Team Routing

- A practical team route can use managed coding products for difficult/agentic work while a private local worker handles bounded sensitive/repetitive tasks.
- Define explicit routing criteria from repository/data class, task type, model capability, latency, and cost.
- Do not let clients silently fail over from private/local to hosted inference when the repository requires local-only processing.
- Keep final verification consistent across routes so local and hosted work are judged against the same engineering standards.

## Third-Party/Partner Agents

- Treat partner agents enabled through a shared platform as separate providers with their own model/data/agent behavior even when repository policy is centrally managed.
- Current GitHub Copilot organization policies can enable partner agents such as Claude and Codex for repositories; the central enablement does not erase provider-specific data terms or behavior.
- Review what repository access, issue/PR permissions, secrets, network tools, and audit events apply to each agent.
- Do not enable multiple agents simply for choice; add a provider when a measured task advantage justifies extra policy/review complexity.

## Direct API and Internal Coding Harnesses

- Use direct APIs/custom harnesses when the team needs deterministic tool contracts, custom repository retrieval, internal evaluation, specialized automation, or model/provider routing beyond managed coding products.
- Include the harness in reliability/security review: context selection, tools, sandbox, retries, state, observability, secret handling, and stopping logic can dominate outcome quality.
- Apply project budgets/rate limits and separate credentials by environment/team where useful.
- Do not turn a team harness into an organization-wide model platform without moving ownership to the internal-platform scenario.

## Data Retention and Offboarding

- Review how each tool handles source context, cloud-agent repository copies, histories, memories, indexes, telemetry, and user offboarding.
- Current Cursor team documentation describes deletion of user-associated Memories/Cloud Agent data on removal and team-level privacy controls; treat exact behavior as product-specific and recheck before relying on it.
- Ensure reusable engineering knowledge remains in company-owned repositories/docs rather than disappearing with an employee account.
- Revoke licenses/tokens/connections promptly when developers leave or change roles.

## Cost per Accepted Team Change

- Compare **total cost per accepted engineering change** across seats, usage/API charges, cloud-agent runtime, self-hosted infrastructure, CI, failed attempts, review/correction time, admin/security work, and incident risk.
- A managed coding product can be cheaper than self-hosting when it reduces operational burden and improves agent quality; self-hosting can win for repeated private workloads when utilization and quality justify it.
- Do not assume included quotas are equal value across developers; model the team's actual heavy/light usage distribution.
- Account for duplicated tools when developers keep a second assistant because the official route fails specific workloads.

## Escalation Triggers

- Move from individual coding tools to this scenario when repository policy, shared review, budgets, or team agents become shared concerns.
- Move from managed pilot to a local/hybrid/API route only when measured task/data/cost evidence justifies added operations.
- Move to `organizations/internal-ai-platform/` when centralized gateway, provider contracts, organization-wide identity, cross-team model policy, budgets, shared inference, observability, or platform SLOs dominate.
- Move toward high-security/regulated routes when repository/data classification requires materially stronger isolation/compliance controls.
- Stop or narrow autonomous agent use when complete-loop verification and incident/review burden do not meet team acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when the team already operates a fixed shared local inference machine and exact hardware constrains candidate selection.
- Use `../../../hardware/sub/servers/` for a dedicated shared inference host and the relevant accelerator specialization.
- Hardware purchasing remains outside this scenario; managed/API/hybrid routes remain valid alternatives.

## Canonical Links

- Link coding-model candidates to `decision-support/selection/models/decision-guides/software-development`.
- Link agent complete-loop safeguards to `decision-support/selection/models/decision-guides/agents-and-automation`.
- Link exact local models to canonical Model Reference owners when named.
- Link managed coding products to their canonical software/service owners where materialized.
- Link centralized platform concerns to `decision-support/scenarios/organizations/internal-ai-platform` instead of duplicating them here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current GitHub Copilot Business/Enterprise policy/agent/memory documentation, current Cursor enterprise privacy/model/spend/agent-control documentation, current OpenAI Codex safety/workspace-agent documentation, and canonical AI Lab coding/agent decision guides.
- Current evidence establishes that team coding products now expose materially different admin controls for models, agents, repositories, sandbox/network access, memories, usage/spend, and partner agents. These product controls do not prove task quality or complete source-code suitability.
- Coding-agent/model availability, policy surfaces, retention, cloud-agent storage, memory behavior, partner-agent integration, usage/billing, and provider terms are mutable; recheck them before rendering current guidance.
- Provider benchmarks and productivity claims remain eligibility evidence only; team acceptance requires representative repository-level complete-loop measurement.

## Validation

- The scenario remains a bounded software-development team route, not organization-wide AI platform architecture.
- Coding model ranking stays in `software-development`; agent loop/security fundamentals stay in `agents-and-automation`.
- Repository/source-code data path, cloud-agent storage, sandbox/network/tool permissions, secrets, and prompt injection are first-class evaluation dimensions.
- Team rules/memory supplement rather than replace canonical repository engineering standards.
- Completion requires repository-native verification and human review appropriate to the change.
- Usage/spend is measured by real team distribution and accepted changes, not seat price alone.
- Shared self-hosted workers include concurrency/operations and do not imply complete client locality.
- Central gateway/identity/budget/contract/platform concerns escalate to `internal-ai-platform`.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
