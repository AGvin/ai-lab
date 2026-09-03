# Documentation Requirements

## Scenario Fit

- Present this scenario for one professional using AI across ordinary knowledge-work activities such as writing, summarization, planning, document review, research, meetings, spreadsheets, presentations, email, and internal information retrieval where **workplace data handling and approved-tool policy** materially distinguish the route from personal use.
- Keep the scenario individual-professional in scope. The reader is choosing a workable route for their own daily work inside an organization's rules, not designing the organization's AI platform, procurement program, identity architecture, governance model, or enterprise-wide knowledge system.
- Distinguish this scenario from `personal/everyday-home-user/`: the same writing or research task becomes a different route when employer/client confidentiality, managed identity, retention, approved applications, connected internal sources, or audit expectations apply.
- Distinguish it from `sensitive-data-professional/`: routine internal/confidential work can remain here when standard organization controls are sufficient; that scenario becomes the owner when legal/health/financial/client secrecy or similarly high-sensitivity professional obligations dominate the route.
- Distinguish it from role-specific professional scenarios when software engineering, research, structured data analysis, creative production, or another specialized workload materially changes the model/evaluation contract.

## Start With the Organization Boundary

- Before selecting a model, determine what the organization actually permits: approved products/accounts, data classifications, prohibited data, connected sources, browser/desktop/mobile restrictions, retention, region/residency requirements, logging/audit expectations, and whether external tools or local inference are allowed.
- Do not infer workplace approval from consumer availability, a personal subscription, an opt-out switch, or a provider's general privacy marketing. The employer/client policy and applicable agreement determine whether a route is allowed.
- Prefer an organization-approved managed workspace when it satisfies the workload because it can combine current hosted models with managed identity, administrator controls, business data terms, controlled connectors, and provider-managed updates without requiring the individual to operate inference infrastructure.
- Keep personal and managed work identities separate. Current managed ChatGPT account guidance makes clear that organization administrators can control and may access/audit/retain/delete data associated with the managed account; do not present a managed work account as a private personal space.
- If the organization has no approved AI route, treat that as a real blocker for protected work data. Use only public/sanitized material or an explicitly permitted local/offline route rather than silently moving confidential content into a consumer assistant.

## Separate the Knowledge-Work Workloads

- Classify recurring tasks before deciding whether one assistant is sufficient:
  - drafting, rewriting, editing, and tone adaptation;
  - summarizing documents, threads, meeting notes, or supplied source material;
  - current web/source research and evidence synthesis;
  - internal knowledge search over approved workplace repositories;
  - spreadsheet/data inspection and code-backed analysis;
  - presentation/report preparation;
  - email/calendar/task assistance;
  - translation and multilingual communication;
  - meeting preparation/follow-up;
  - repetitive workflow automation or agentic actions.
- Do not force all tasks into one model merely for convenience. A managed assistant, enterprise search surface, spreadsheet-native assistant, deterministic calculator/code runtime, specialist tool, or local model can each own different workloads.
- Evaluate the route by accepted-result quality, correction/review burden, latency, source traceability, workflow friction, policy fit, data exposure, and total cost rather than model benchmark rank alone.

## Default Managed Workspace Route

- Use an organization-approved Business/Enterprise/workspace assistant as the default low-administration route when hosted processing is permitted and its controls satisfy the data boundary.
- Current canonical assistant-workspace examples include ChatGPT, Claude, and Gemini. Select among them using the organization's approved services and real workloads rather than assuming consumer-product familiarity translates into workplace suitability.
- Current OpenAI business-product commitments state that business data from ChatGPT Business/Enterprise/Edu and the API is not used to train models by default, with additional controls varying by product such as access management, retention, residency, audit, and connected-source controls. Treat exact product coverage and options as mutable.
- Current Google Workspace with Gemini documentation states that enterprise-grade data protections apply to Workspace AI interactions and that submitted Workspace data is not human-reviewed or used to train generative models outside the domain under the documented enterprise protections. Recheck the exact account/product boundary before relying on that commitment.
- Current Claude Team/Enterprise surfaces provide organization-managed connectors and enterprise controls; the organization's account owner determines available services and access. Treat exact plan features, retention controls, connector availability, and pricing as mutable.
- Do not collapse provider privacy claims into a universal compliance statement. The complete organization/provider/subprocessor/connector path still has to satisfy the user's actual policy and legal obligations.

## Managed Account and Administrator Visibility

- Explain that a managed work account is organization-controlled. Depending on product/configuration, administrators or designated owners may be able to manage access, features, retention, audit/compliance data, exports, or other workspace data.
- Keep personal conversations, personal files, and unrelated private activity out of managed work accounts unless the user intentionally accepts the organization's management boundary.
- Do not assume that teammate privacy and administrator privacy are the same thing. For example, current ChatGPT Business documentation says other members do not automatically see each user's chat history, while organization/managed-account controls remain a separate administrator boundary.
- Treat account switching as a trust-boundary operation. Verify which account/workspace is active before uploading work material or using a connector.

## Internal Sources, Connectors, and Permission Inheritance

- Use connected workplace sources when they materially reduce copy/paste, improve freshness, or enable grounded answers, but treat each connector as an extension of the data-access boundary.
- Verify which systems are connected, what scopes/tools are enabled, which identity authenticates, whether access is read-only or write-capable, whether content is indexed/cached or fetched on demand, and how access is revoked.
- Preserve source-system permissions. A model/search layer should not become a shortcut around document, mailbox, channel, or repository authorization.
- Current Google Workspace guidance states that administrator and content-owner controls can restrict which Workspace data Gemini can access.
- Current Claude enterprise-search/connectors documentation describes permission-aware access with user-level authentication, and current Microsoft 365 connector guidance states that Claude mirrors existing M365 permissions. Treat those as product-specific evidence, not a generic guarantee for all connectors.
- When a connected source is used for an important answer, preserve links/citations or enough source identity to verify the result in the authoritative system.
- Do not connect broad mail/drive/chat sources when a narrower project folder, selected file, or sanitized upload is sufficient.

## Writing and Document Work

- Use the assistant for drafting, restructuring, summarization, translation, comparison, and review, but preserve the authoritative source document and distinguish source facts from generated wording.
- For contracts, policy, HR, finance, legal, medical, regulated, or other high-consequence documents, use the assistant as support rather than sole authority and escalate to the appropriate specialist/source owner.
- When summarizing a long document, ask for source references/section anchors where the product can provide them, and verify material claims against the original.
- Do not let a fluent summary erase exceptions, conditions, dates, defined terms, footnotes, table qualifiers, or uncertainty that changes the professional meaning.
- For externally sent work, final human review must cover factual claims, names, dates, amounts, commitments, confidential information, and organization-specific tone/policy.

## Current Research and Evidence

- Treat current external facts—market conditions, laws, product capabilities, competitor information, pricing, schedules, standards, news, and organization/public announcements—as retrieval/search tasks rather than training-memory facts.
- Prefer primary/authoritative sources for material professional claims and record publication/effective dates when freshness matters.
- Separate `source says X` from the model's interpretation or recommendation.
- Deep-research or web-enabled assistant modes can be useful for multi-source synthesis, but citation presence is not proof of support; inspect whether cited sources actually substantiate each important claim.
- When the organization requires specific approved information sources, restrict research to those sources rather than letting a general web search silently widen the evidence boundary.

## Internal Knowledge Search

- If the recurring need is `find what our organization already knows`, prefer a permission-aware enterprise knowledge/search route over repeatedly uploading files into isolated chats.
- Require freshness/provenance: identify the underlying source, owner, last-updated time when relevant, and whether conflicting documents exist.
- Do not treat retrieved internal text as automatically correct or current merely because access was authorized.
- If organization-wide knowledge architecture, indexing, access policy, source governance, or shared RAG becomes the main design problem, route to organization-scale knowledge/platform scenarios rather than expanding this individual page.

## Spreadsheet and Data Work

- For calculations, aggregations, transformations, or statistical analysis, prefer code/formula-backed execution that can be inspected and rerun rather than prose-only arithmetic.
- Preserve source data, formulas/code, assumptions, filters, units, and important intermediate results.
- Use spreadsheet-native assistants when the workbook itself is the authoritative artifact and organization policy allows the integration.
- If structured-data analysis becomes the professional's dominant workload, continue into the role-specific data-analyst/data-scientist scenario rather than duplicating the full analysis contract here.

## Email, Calendar, Meetings, and Tasks

- Treat communication and scheduling integrations as side-effecting workflow surfaces when they can draft/send email, create/update files, or modify calendar/task state.
- Read-only retrieval and write actions have different risk. Do not infer authorization to send, delete, schedule, invite, publish, or change shared state from authorization to read context.
- Require user confirmation for consequential external messages, commitments, meeting changes, broad file edits, or actions involving sensitive recipients/data unless the organization has explicitly approved a narrower automation policy.
- Verify recipients, dates/timezones, attachments, confidentiality, and generated commitments before external communication.
- Keep deterministic calendar/task systems as the source of truth for deadlines and commitments rather than assistant memory.

## Consumer Account Boundary

- A consumer assistant may be useful for public-domain research, generic skill development, or sanitized drafting when organization policy permits it.
- Do not upload internal/confidential/client/regulated information to a personal consumer account merely because the user has disabled model training or the provider offers similar models in its business product.
- Consumer privacy controls, managed business terms, retention controls, administrator governance, and connector approvals are distinct dimensions.
- If the organization explicitly approves a consumer account for a bounded workload, document the permitted data class/workflow rather than generalizing that approval to all work data.

## Direct API Route

- Use direct API access only when the professional or their organization has a concrete integration/automation requirement and the API account/project, credentials, logging, spend, retention, and provider terms are approved.
- An API endpoint does not reproduce the managed assistant's complete UX, projects, memory, connectors, research interface, or admin workflow automatically.
- Do not place API keys in prompts, documents, chat memory, shared spreadsheets, or source files. Use approved secret management.
- Apply the provider-chain rule when API gateways, routing services, observability proxies, external tools, or third-party agents can receive the work content.

## Local and Offline Route

- Present local inference as an alternative when confidentiality, offline use, provider independence, or an explicit organization requirement justifies local operational burden.
- `Phi-4 Mini Instruct` and `Qwen3 8B` remain current compact text-oriented local candidates for bounded writing/summarization/code-assistance tasks when exact language/task quality and hardware fit are validated.
- `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` remain current compact multimodal candidates when private local image/document/audio understanding is required and the exact runtime supports the modality path.
- Do not equate `runs on my laptop` with `approved private workflow`. Desktop applications, telemetry, model download/update paths, plugins, remote connectors, cloud fallback, synchronization, and storage can still cross the organization boundary.
- Require the complete client → runtime → model → tool/storage path to satisfy the data boundary.
- Exact RAM/VRAM/context/latency fit belongs in sibling hardware selection and must be measured; parameter count, quantized file size, or load success is not enough.

## Agentic and Side-Effecting Work

- Treat tool-using agents as a separate escalation from conversational assistance because they can change external systems.
- Grant least privilege, narrow scopes, explicit destination constraints, and human confirmation for high-impact actions.
- Current workplace connectors can expose both read and write capabilities depending on product/admin settings; inspect the actual tool permissions instead of assuming a connector is read-only.
- Do not automate external commitments, destructive changes, access/permission changes, payments, HR actions, production changes, or broad communications solely from free-form model judgment.
- If multi-system automation becomes a persistent workflow, route to the applicable team/organization automation scenario and agent decision guidance.

## Reliability and Professional Review

- Match verification effort to consequence. Low-stakes brainstorming can use lightweight review; external factual claims, policy interpretation, financial figures, client deliverables, code/configuration, and operational decisions require stronger verification.
- Preserve authoritative originals and deterministic calculations rather than allowing generated prose to become the only record of a professional fact.
- When the assistant cannot access a required source, label the gap instead of inventing the missing information.
- Treat hallucination, stale information, incomplete retrieval, prompt injection in retrieved content, and tool-side effects as workflow risks rather than isolated model defects.

## Cost and Accepted Work Outcome

- Compare routes by **total cost per accepted work outcome**: seat/subscription or API spend, usage credits, correction/review time, context/file handling, admin overhead, connector setup, local hardware/power/maintenance, and the consequence of errors.
- A more expensive managed workspace can be cheaper overall when approved connectors, identity, policy controls, and lower setup/review friction remove repeated manual work.
- A local model can be economically rational for repeated private/offline tasks when existing hardware is sufficient, but include deployment, updates, endpoint security, latency, and quality-review cost.
- Do not maintain multiple paid assistants for nominal model breadth. Add another route only when it repeatedly improves an important workload enough to justify policy, switching, and cost overhead.

## Escalation Triggers

- Move to a role-specific professional scenario when coding, analysis, research, creative production, or another specialized workload becomes the dominant decision.
- Move toward `sensitive-data-professional/` when confidentiality/regulatory/client obligations require materially stronger controls than ordinary approved knowledge work.
- Move from managed assistant to direct API when a repeatable integration/batch/custom-interface need is explicit and approved.
- Move to local/offline when data-egress or connectivity constraints dominate and the complete local path is approved and measured.
- Move to organization-scale knowledge/platform/governance scenarios when shared architecture, identity, policy, budgets, observability, access, or organization-wide deployment becomes the real problem.
- Add an agent/tool route only when repetitive action—not just drafting/reasoning—is the bottleneck and permissions/verification can be bounded safely.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when the professional uses a local route and exact owned hardware constrains model fit.
- Use `../../../hardware/sub/computers/` for ordinary workstation/laptop inference and the applicable vendor/accelerator specialization when known.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link managed assistant examples to `catalog/services/assistant-workspaces/chatgpt`, `catalog/services/assistant-workspaces/claude`, and `catalog/services/assistant-workspaces/gemini` when named.
- Link local text candidates to `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link local multimodal candidates to `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/reference/producers/google/gemma/gemma-4/models/e4b-instruct` when named.
- Link organization-scale and role-specific owners instead of duplicating their detailed governance, platform, or specialist-workload guidance.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI business-data/managed-account documentation, Google Workspace with Gemini enterprise-data and access-control documentation, current Anthropic Team/Enterprise/connector documentation, and canonical AI Lab model/service owners.
- Current evidence establishes meaningful differences between consumer access and managed workplace products: organization data terms, administrator control, identity/access, retention/residency/audit options, connector governance, and permission-aware internal-source access vary by product and configuration.
- Current workplace connectors can expose rapidly changing read/write capabilities; exact actions, scopes, admin controls, retention/indexing behavior, plan eligibility, pricing, model aliases, and regional/residency options are mutable and must be rechecked before rendering current advice.
- Provider commitments establish product/data-handling properties, not independent quality or organization-specific compliance. The employer/client policy and accepted-result testing remain required.

## Validation

- The scenario owns ordinary individual professional knowledge work and does not collapse back into personal/home use.
- Organization-approved managed access is the default hosted route when available and appropriate; consumer access is not treated as automatically acceptable for work data.
- Managed-account administrator visibility/control is explicit and is not confused with teammate chat visibility.
- Connectors preserve source permissions and are treated as part of the data/tool boundary.
- Read-only retrieval and write-capable actions remain distinct risk classes.
- Current research is source-backed and internal knowledge remains provenance/freshness aware.
- Local execution is not presented as sufficient compliance evidence by itself; the complete path must remain within the approved boundary.
- Important calculations and external professional outputs remain reviewable and verifiable.
- Organization-wide platform/governance design stays outside this individual scenario.
- Exact local model identities are canonical and hardware fit is delegated to sibling hardware selection.
- Mutable current claims carry the 2026-08-24 evidence boundary.
