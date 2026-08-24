# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person team that repeatedly performs market, competitive, customer, product, policy, technical, or other evidence-based research and turns it into shared insights for decisions.
- Keep the scenario team-scoped. One researcher belongs in `professionals/researcher/`; organization-wide knowledge platforms, enterprise search, formal research infrastructure, or centralized governance belong in organization routes when they dominate.
- Distinguish this scenario from `data-analysis-team/`: structured quantitative analysis can support insights, but here **multi-source discovery, evidence synthesis, citations/provenance, shared review, and reusable research outputs** are the primary model-selection constraints.
- Do not turn the page into market-research methodology or knowledge-management platform design. It owns the AI route for the team's research/insight workflow.

## Shared Research Contract

- Define each research request before model selection: question, audience/decision, scope, source types, time window, languages/regions, confidentiality boundary, required evidence strength, and deadline.
- Keep discovery, evidence extraction, analysis/interpretation, and final synthesis as distinct stages.
- Use a shared evidence structure—source list, evidence matrix, research notebook, or equivalent—so multiple researchers can inspect what supports each important finding.
- Preserve source identity and links/IDs outside chat history; the final insight must remain traceable after a particular assistant conversation disappears.
- Record unresolved gaps/conflicts rather than forcing consensus to produce a clean narrative.

## Default Source-Grounded Managed Route

- Prefer an organization-approved assistant/deep-research surface with uploaded/connected source support, domain/site controls, and citation-linked reports when hosted processing fits the team data boundary.
- Current ChatGPT Deep Research supports public/specified web sources, uploaded files, connected sources, a reviewable research plan, and final reports with citations/source links. Current Gemini Deep Research supports Google Search plus selected/uploaded/connected sources and produces research plans/reports. Treat exact models, limits, source integrations, workspace sharing, and plan access as mutable.
- Evaluate on the team's actual research questions: coverage, authoritative-source rate, citation support, contradictory-evidence handling, time/version awareness, missing-source detection, synthesis quality, and reviewer correction effort.
- Do not use one provider's deep-research report as the evidence corpus itself. Open and verify material sources.
- Add a second research provider only when it repeatedly adds valuable source coverage, languages, specialist-source access, or synthesis quality enough to justify duplication and review complexity.

## External and Internal Sources

- Separate public/external evidence from internal/customer/confidential evidence in the research plan.
- Prefer primary/authoritative external sources for material claims: official product/docs, filings, regulators, standards bodies, original studies/data, government statistics, company releases, or source owners appropriate to the domain.
- Use credible secondary sources for context/discovery and label their interpretive layer.
- For internal sources, preserve source-system permissions and ownership. AI access must not become a shortcut around Drive/SharePoint/Slack/CRM/repository/document permissions.
- Keep internal and external citations distinguishable in the final deliverable so reviewers know which claims are publishable/shareable.
- If the team's central problem becomes permission-aware enterprise knowledge retrieval rather than research synthesis, route to `organizations/business-knowledge-assistant/`.

## Search Coverage and Reproducibility

- Record enough search scope to reproduce material research: sites/databases, key query terms, date range, language/region, filters, and research date.
- When systematic or high-confidence coverage matters, use specialist databases/repositories directly rather than relying on open-web/deep-research coverage.
- Do not interpret `no evidence found` as `evidence does not exist` unless the search design supports that conclusion.
- Track inaccessible/paywalled/missing sources explicitly.
- Re-run time-sensitive searches before a major decision if the output depends on rapidly changing products, prices, laws, competitors, news, or market conditions.

## Evidence Matrix and Claim Traceability

- For non-trivial projects, maintain a team evidence matrix containing source identity, source type, date/version, key claim/evidence, limitations, relevance, confidence/strength, and reviewer status.
- Separate what the source explicitly states from the team's interpretation.
- Require every high-impact final claim to map to one or more verified evidence entries.
- Preserve conflicting evidence and explain why the team weighs sources differently rather than hiding minority/negative findings.
- Do not accept model-generated quotations or statistics unless directly verified in the source.

## Citation and Identity Verification

- Verify titles, authors/organizations, dates, publication/version, URLs/DOIs/stable IDs, and exact supporting passage/table when material.
- Detect duplicate/reposted/syndicated sources so one claim is not falsely counted as multiple independent confirmations.
- Distinguish primary source, vendor claim, independent evidence, news/community report, analyst interpretation, and internal observation.
- Citation presence is not claim support; reviewers must check whether the cited source supports the exact statement.
- Preserve corrections/retractions/version updates when they change evidence.

## Customer and User Insight Work

- Treat interviews, surveys, support tickets, reviews, call transcripts, CRM notes, or product feedback as data with consent/privacy/use boundaries.
- Do not merge identifiable customer data into public web research by default.
- Use AI for coding/tagging, clustering hypotheses, extraction, summarization, and theme comparison only after the team defines a reproducible coding/validation approach.
- Validate automated qualitative coding against a manually reviewed sample and preserve meaningful minority/negative cases.
- Do not turn frequency of mentions into prevalence or causal importance without an appropriate sampling/measurement basis.
- Keep direct customer quotations traceable and verify permission/redaction before external publication.

## Competitive and Market Research

- Verify competitor/product capabilities, prices, availability, terms, release state, geography, and dates from current primary sources where practical.
- Distinguish announced, preview/beta, generally available, discontinued, and region/account-specific capabilities.
- Avoid attributing motives, strategy, market share, or customer sentiment as fact without appropriate evidence.
- Preserve comparable definitions when building competitor matrices; models can produce misleading comparisons when source metrics use different scopes.
- For purchasing/strategic decisions, recheck mutable claims immediately before final recommendation.

## Research Synthesis and Decision Support

- Ask the model to separate evidence, inference, recommendation, uncertainty, and open questions.
- Include strongest counterevidence/alternative explanation for high-impact conclusions.
- Do not compress multiple source disagreements into a single average statement when disagreement is itself decision-relevant.
- Provide confidence/strength qualitatively only when the team defines what the label means; do not invent pseudo-precise probabilities without basis.
- Preserve the decision's source cutoff date so future readers know the freshness boundary.

## Team Review Workflow

- Define roles for material research: requester/owner, researcher(s), evidence reviewer, and final decision/deliverable owner where scale warrants it.
- Require another person to verify high-impact citations/claims rather than allowing the generating model to self-certify its report.
- Keep reviewer comments and accepted corrections in the shared research artifact.
- For fast/low-stakes work, reduce ceremony but preserve source links and factual verification.
- Maintain reusable research templates/query strategies in team-owned storage rather than personal chat memory.

## Shared Knowledge and Research Archive

- Store accepted briefs, evidence tables, source lists, and research notes in a team-owned repository/workspace with ownership and update dates.
- Distinguish archived historical research from current truth; models must not reuse an old brief as current evidence without a freshness check.
- Avoid copying the same source extract into many chats/documents when a canonical evidence note/link can be referenced.
- If an indexed research archive is used, preserve source permissions and provenance and defend against prompt injection/untrusted documents.
- Do not let AI-generated summaries become the only surviving record of primary evidence.

## Quantitative Evidence

- Use deterministic SQL/Python/R/spreadsheet/statistical tools for material calculations.
- Route sustained structured-data work to `data-analysis-team/` while keeping its results linked into the evidence matrix.
- Preserve dataset/source version, filters, code/query, units, denominators, time windows, and uncertainty.
- Do not let the model mix statistically incompatible metrics or claim causation from correlations/observational evidence.

## Confidential Research Boundary

- Classify internal strategy, customer research, interview transcripts, unreleased product plans, vendor proposals, contract terms, employee data, or other confidential sources before hosted use.
- Use organization-approved workspaces/accounts and verify connector/source permissions, retention, model-training defaults, and provider chain.
- Minimize sensitive content sent to models; use redaction, aggregation, local preprocessing, or source restrictions where they preserve the research objective.
- Keep secrets, credentials, private API tokens, and unnecessary direct identifiers out of prompts/corpora.
- If confidentiality/regulatory obligations dominate, route to sensitive/regulated/high-security scenarios.

## Research Agents and Automation

- Use agents for repeatable bounded tasks such as scheduled source checks, structured extraction, source classification, evidence-table updates, or alerting when verification and stopping conditions are explicit.
- Keep broad web/retrieval agents from autonomously publishing final conclusions or contacting external parties without human review.
- Bound source domains, query count, runtime, retries, spend, and result volume to prevent runaway research loops.
- Store source URLs/IDs and retrieval dates with extracted claims.
- Treat untrusted web/internal content as prompt-injection input; retrieved instructions must not override team/system policy.

## Local and Hybrid Route

- Use local processing when confidential corpus analysis, offline research, or provider independence justifies local infrastructure and exact model/hardware quality is sufficient.
- Local models can support extraction, summarization, coding/classification, query expansion, or private synthesis; they do not replace current external search/databases.
- A hybrid route can keep sensitive internal/customer sources local while using hosted deep research for public evidence, combining only sanitized findings under explicit rules.
- Local RAG does not guarantee correctness, freshness, permission, or prompt-injection safety.
- Escalate shared local infrastructure to internal-platform/hardware owners when operation becomes a platform concern.

## Team Evaluation Suite

- Maintain representative research tasks covering current web research, internal-source synthesis, long documents, conflicting evidence, multilingual sources where relevant, customer feedback, and a question with intentionally missing evidence.
- Score source coverage, primary-source proportion, citation correctness, omission, synthesis quality, contradiction handling, latency, reviewer correction time, and cost per accepted brief.
- Include adversarial sources containing misleading claims, duplicated evidence, stale dates, and embedded instructions.
- Compare products/configurations under the same scope/source restrictions where practical.
- Do not use provider research benchmarks as a substitute for team-domain evidence.

## Cost per Accepted Insight

- Compare **total cost per accepted research brief/insight**: seats/API/research credits, specialist database access, document acquisition, agent runs, duplicate searches, verification/review time, internal-source setup, and the consequence of a wrong or missed finding.
- A premium deep-research mode can be economical when it reduces discovery labor without increasing verification burden excessively.
- Smaller/cheaper models can handle extraction/classification if ambiguity is escalated to stronger models/humans.
- Do not optimize for number of sources or pages generated; optimize for relevant verified evidence and decision usefulness.

## Escalation Triggers

- Move from individual researcher use to this scenario when multiple people share evidence, reviews, sources, and deliverables.
- Move to `data-analysis-team/` when structured computation becomes the dominant workflow.
- Move to organization knowledge/platform routes when enterprise-wide source indexing, permissions, shared retrieval infrastructure, or centralized AI governance becomes primary.
- Move to sensitive/regulated routes when source confidentiality or legal/professional obligations require stronger controls.
- Narrow/stop automated research when source verification burden or prompt-injection/data risk exceeds value.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared inference target materially constrains the research route.
- Use `../../../hardware/sub/servers/` for a dedicated team inference/retrieval host and `../../../hardware/sub/computers/` for workstation-led local research where applicable.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link individual research methodology to `catalog/models/selection/user-scenarios/professionals/researcher` where needed.
- Link structured analysis to `catalog/models/selection/user-scenarios/teams/data-analysis-team`.
- Link managed assistant/deep-research services to their canonical service owners when named.
- Link organization knowledge platforms to the applicable organization scenario rather than duplicating them here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT Deep Research and Gemini Deep Research documentation plus current managed-workspace connected-source/permission documentation and canonical AI Lab research owners.
- Current evidence establishes multi-step source-grounded research with user-selectable/restricted sources, uploaded/connected material, research plans, and citation-linked reports. These capabilities do not establish complete scholarly/market coverage or citation correctness.
- Deep-research source access, connected apps, model aliases, limits, workspace sharing, specialist databases, pricing, and current external evidence are mutable; recheck them before rendering current guidance.
- Provider synthesis remains assistance; verified source evidence and team review own final claims.

## Validation

- Shared evidence/review artifacts distinguish the team route from individual research.
- Discovery, extraction/evidence, and synthesis remain separate stages.
- Material claims remain traceable to verified source identity and dates.
- Internal/customer/external evidence preserve separate permissions and publication boundaries.
- Contradictory/missing evidence remains visible rather than being smoothed into consensus.
- Customer qualitative coding is validated and does not convert mention frequency into prevalence without basis.
- Quantitative claims remain reproducible via deterministic tools.
- Automated research is bounded and cannot self-publish high-impact conclusions.
- Organization-wide knowledge/platform concerns are delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
