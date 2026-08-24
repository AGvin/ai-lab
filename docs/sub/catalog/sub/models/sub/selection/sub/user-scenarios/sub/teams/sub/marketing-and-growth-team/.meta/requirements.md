# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person marketing/growth team combining market/customer research, segmentation, campaign planning, copy/media generation, experiments, channel performance, lifecycle messaging, and growth reporting.
- Keep the scenario team-scoped. One creative professional belongs in `professionals/creative-professional/`; a dedicated creative production team belongs in `content-and-creative-team/`; organization-wide sales/revenue automation, customer-service infrastructure, enterprise analytics, or central AI platform belongs in organization routes when those dominate.
- Distinguish this scenario from `research-and-insights-team/`: research is an input, while here campaign execution, growth experiments, customer/prospect data, claims, channel policy, and performance measurement determine the model route.
- Do not turn the page into advertising-platform strategy. It owns AI model/workspace routing and acceptance for the team's workflow.

## Preserve Marketing Sources of Truth

- Identify authoritative sources for product facts, prices, availability, offers, brand guidelines, customer segments, CRM attributes, campaign status, creative approvals, experiment definitions, and performance metrics.
- Use assistants for research, synthesis, drafting, variation, analysis, and workflow proposals; do not let chat memory become the only record of approved claims, audience definitions, spend, or campaign state.
- Keep versioned final creative/copy and the exact campaign/experiment configuration outside the AI tool.
- When source facts conflict, surface the owner/conflict rather than choosing a plausible answer.

## Default Managed Workspace Route

- Prefer an organization-approved managed workspace for research, planning, drafting, document/feedback synthesis, and bounded data analysis when its data boundary fits marketing/customer information.
- Use connected sources only when they materially reduce manual transfer and preserve permission boundaries; exact app/connector catalogs, actions, sync/index behavior, plan limits, and model aliases are mutable.
- Evaluate the workspace on representative tasks: current market/competitor research, brief generation from verified sources, campaign-copy variation, feedback synthesis, a bounded performance table, and a compliance/claim-check case.
- Add specialist media or research models only when a recurring task advantage offsets additional data/provider/integration complexity.

## Market and Audience Research

- Use current source-grounded research for competitors, market changes, platform capabilities, trends, prices, regulations, events, and public customer context.
- Prefer primary/authoritative sources for claims used in campaigns or decisions and record publication/effective dates.
- Route large multi-source research projects to `research-and-insights-team/` while preserving their evidence outputs in the campaign brief.
- Do not treat model-generated personas as market evidence. Personas/hypotheses require validated research or clearly labeled assumptions.
- Do not infer market size, sentiment, adoption, or competitor strategy from generic model memory.

## Segmentation and Customer Data

- Treat CRM/customer/prospect/behavior data as governed data, not convenient personalization context.
- Define segment criteria in deterministic data/CRM systems and preserve the actual query/filters/eligibility logic.
- Use AI to explain, propose, or analyze segments, but do not let the model silently invent demographic, sensitive, intent, or propensity attributes about individuals.
- Verify consent, purpose limitation, channel permissions, suppression/opt-out status, and applicable policy before using customer data for targeting/personalization.
- Avoid uploading broad identifiable datasets when aggregated or minimal fields are sufficient.
- Keep credentials and authentication/payment data out of assistant context.

## Campaign Briefs and Messaging

- Build briefs from verified product/brand/audience/evidence sources.
- Separate factual claims, positioning hypothesis, creative concept, legal-required copy, and channel constraints.
- Use the model to generate variants and critique them, but require final human/brand/legal review proportional to consequence.
- Do not fabricate customer quotes, reviews, awards, certifications, performance claims, comparisons, scarcity, pricing, guarantees, or product capabilities.
- Preserve approved terminology, disclaimers, offer conditions, dates, and regional differences.
- For regulated or high-risk product claims, use authoritative/legal/compliance review rather than model judgment.

## Creative Media Production

- Route exact image/video/audio/speech model selection to `decision-guides/media-creation/` and professional production constraints to `creative-professional/` where applicable.
- Use AI media for ideation/production only after input rights, brand consistency, identity/likeness consent, output-use terms, provenance, and modality-specific quality are evaluated.
- Check generated logos, packaging, text, product geometry, prices, claims, faces/voices, and visual details independently before publication.
- Preserve editable/source assets and final approved outputs outside generation history.
- Do not infer commercial rights from technical generation capability.

## Brand Consistency

- Keep canonical brand guidelines/assets as source of truth.
- Evaluate AI output across a set of campaign assets, channels, languages, aspect ratios, and revisions rather than one sample.
- Check tone, terminology, logo/color/product details, required claims/disclaimers, accessibility, and localization consistency.
- Store reusable approved templates/prompts/guardrails in team-owned systems, not individual chat histories.
- Treat a style-reference feature as a production control only after rights and repeatability are validated.

## Experiments and Growth Measurement

- Use deterministic analytics/experiment systems for conversion, uplift, attribution, revenue, retention, funnel, cohort, and other performance calculations.
- Route sustained analytics to `data-analysis-team/`.
- Preserve experiment population, randomization/exposure, variants, dates, guardrails, sample size, attribution window, channel, and metric definitions.
- Do not let model-generated narratives turn correlation or post-hoc segmentation into causal uplift.
- Check sample-ratio mismatch, tracking changes, missing data, seasonality, novelty, multiple testing, and stopping behavior where material.
- Keep final decisions traceable to executed analysis, not only AI-written campaign summaries.

## Attribution and Cross-Channel Interpretation

- Treat platform-reported attribution as measurement with a defined model/window, not ground truth about causality.
- Preserve differences between click/view/last-touch/multi-touch/incrementality and channel-specific definitions.
- Do not merge incomparable metrics from platforms into one table without normalizing definitions, currencies, timezones, and date windows.
- Use model assistance to explain discrepancies and generate hypotheses, then validate against source analytics.
- Keep organic, paid, lifecycle, referral, and sales-assisted signals separate when the underlying measurement differs.

## Personalization and Lifecycle Messaging

- Use personalization only from allowed data attributes and approved business rules.
- Prefer deterministic eligibility/suppression logic around model-generated copy.
- Do not allow the model to infer or exploit sensitive attributes, vulnerability, health, financial distress, political/religious status, or other restricted categories without a clearly permitted use case and applicable controls.
- Require review for high-impact/customer-sensitive messages such as billing, account status, legal/service changes, or crisis communication.
- Preserve template/version/segment/source data so the team can reproduce what was sent.

## Email, Social, Ads, and Publishing Actions

- Treat publishing, sending, budget/bid changes, audience upload, and campaign activation as side-effecting actions distinct from drafting.
- Start with draft/recommendation workflows; require explicit approval or deterministic policy for external publishing/sending and spend changes.
- Verify account/brand, audience, channel, URL, dates/timezone, budget, offer, tracking parameters, creative version, and required disclaimers before activation.
- Do not let a broad prompt such as `launch this campaign` imply permission to upload audiences, change spend, publish content, or send messages across multiple systems.
- Preserve platform policy/compliance checks outside model judgment where deterministic platform rules exist.

## Localization and Multilingual Marketing

- Evaluate each target language/market independently for meaning, tone, legal copy, product names, cultural context, layout, and brand terminology.
- Use native/qualified review for high-value public campaigns rather than assuming multilingual fluency from model capability labels.
- Preserve approved glossary/terminology and source copy.
- Recheck generated text embedded in images/video separately from translated source copy.
- Route travel/general multilingual personal guidance elsewhere; this route is professional campaign localization.

## Customer Feedback and Social Listening

- Use AI to categorize/summarize reviews, community posts, surveys, and customer messages only with a defined coding/validation approach.
- Preserve sampling/source bias and do not convert mention counts into population prevalence without basis.
- Detect bots/spam/duplicates and platform/source context where material.
- Keep direct quotes traceable and redact personal information as required.
- Route deep insight work to `research-and-insights-team/`.

## Marketing Agents and Automation

- Use agents for bounded workflows such as preparing briefs, classifying feedback, generating controlled variants, assembling reports, or drafting scheduled content when inputs/outputs are reviewable.
- Treat CRM updates, audience creation, publishing, budget changes, emails, lead routing, and external communication as higher-impact actions.
- Apply least privilege, explicit destination/account, approval gates, idempotency, bounded retries/spend, and audit logs.
- Do not allow an agent to autonomously optimize toward a metric by making unlimited spend or messaging changes.
- Treat web/email/CRM content as untrusted prompt-injection input when agents can act on tools.

## Professional and Customer Data Boundary

- Classify customer/prospect data, campaign strategy, unreleased products, pricing plans, contracts, partner data, brand assets, and performance data before hosted use.
- Use approved accounts and preserve source-system permissions.
- Verify provider/intermediary/tool chain for sensitive datasets.
- Minimize uploads and connected-source scope.
- Escalate regulated/high-security/customer-sensitive workflows to the appropriate stronger-control scenario.

## Local and Hybrid Route

- Use local/private models when unreleased creative/strategy/customer context cannot use hosted services or repeated private media/text work justifies local operation.
- Keep local text/media models as bounded candidates subject to exact task/hardware/license/quality validation.
- A hybrid route can keep confidential customer/strategy data local while using hosted models for public research or sanitized creative ideation under explicit routing rules.
- Local generation does not remove rights, consent, endpoint security, model license, or publication review.
- Escalate shared local infrastructure to internal-platform/hardware owners when it becomes a service.

## Team Evaluation Suite

- Maintain representative tasks covering research, brief generation, copy variation, feedback synthesis, media/brand check, experiment interpretation, and a publishing/action scenario.
- Include adversarial cases: stale price/product info, prohibited claim, sensitive customer attribute, wrong audience, conflicting brand source, ambiguous experiment, and content that attempts to trigger tool actions.
- Score factual/brand accuracy, source traceability, accepted creative rate, analytical correctness, compliance/review burden, action safety, latency, and cost.
- Compare configurations using the same campaign/source materials where practical.
- Provider creative/marketing examples are eligibility evidence, not proof of team performance.

## Cost per Accepted Growth Outcome

- Compare **total cost per accepted campaign/experiment/insight**: AI seats/API/media credits, failed variants, research, analytics compute, channel spend affected by errors, correction/review, localization, legal/brand review, and integration/admin.
- Do not optimize on cost per generated asset or token if accepted-result rate is low.
- Specialist media/research models can be worth extra cost when they materially reduce production or review work.
- Keep paid media spend and AI cost distinct but include AI-caused wasted spend/error risk in the decision.

## Escalation Triggers

- Move to this scenario when marketing/growth research, campaign, customer-data, experiment, and publishing workflows become shared team concerns.
- Move to `research-and-insights-team/` when evidence discovery/synthesis dominates.
- Move to `data-analysis-team/` when measurement/experimentation dominates.
- Move to `content-and-creative-team/` when media/content production/brand workflows dominate.
- Move to organization sales/revenue/customer-service routes when high-volume CRM/customer automation becomes organization-scale.
- Move to regulated/high-security routes when customer/data/claim obligations require stronger controls.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared text/media inference target materially constrains the route.
- Use `../../../hardware/sub/computers/` or `../../../hardware/sub/servers/` according to the existing production target.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link media model selection to `catalog/models/selection/decision-guides/media-creation`.
- Link professional creative production to `catalog/models/selection/user-scenarios/professionals/creative-professional`.
- Link research and data work to the applicable team scenario owners.
- Link managed services/local models to canonical owners when named.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current managed-workspace app/permission evidence, current source-grounded deep-research capabilities, current code-backed analytical evidence, current generative-media rights/provenance evidence, and canonical AI Lab research/data/media owners.
- Current evidence supports connected business sources, source-grounded research, code-backed analysis, generative media, and increasingly action-capable integrations; none of these features establish legal claim approval, correct audience eligibility, campaign causality, or publication authorization.
- Product/model aliases, connectors/actions, ad/social platform rules, prices, creative terms, provenance systems, customer-data policies, and channel behavior are mutable; recheck them before rendering current guidance.
- Final claims, customer targeting, campaign activation, and spend remain human/business-system controlled.

## Validation

- Marketing sources of truth remain authoritative for product claims, offers, audience eligibility, campaign state, and metrics.
- Model-generated personas/segments are not treated as market/customer facts without evidence.
- Creative media follows the separate rights/provenance/brand/QC contract.
- Experiments/attribution use deterministic analysis and preserve causal limitations.
- Sensitive customer attributes and consent/opt-out rules are not inferred/overridden by the model.
- Drafting is separated from publishing/sending/spend actions with stronger controls.
- Team-owned templates/approved assets replace personal chat memory as durable campaign state.
- Organization-scale revenue/customer automation is delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
