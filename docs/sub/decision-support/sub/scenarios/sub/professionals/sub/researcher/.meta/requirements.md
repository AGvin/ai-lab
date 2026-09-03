# Documentation Requirements

## Scenario Fit

- Present this scenario for one researcher whose recurring AI-assisted work centers on **source discovery, literature review, evidence synthesis, citation verification, long documents, research notes, data/code interpretation, and reproducible research outputs**.
- Keep the scenario individual-professional in scope. Institution-wide research governance, shared research infrastructure, centralized knowledge systems, and organization-scale controls belong in team/organization routes when they dominate the decision.
- Distinguish this scenario from `general-knowledge-worker/`: evidence coverage, primary-source provenance, scholarly databases, citation identity, methodological interpretation, and research reproducibility materially change the model/tool contract.
- Distinguish it from `data-analyst-or-data-scientist/`: quantitative analysis can be one research workload, but that scenario becomes the owner when structured-data computation/statistics rather than evidence/literature synthesis dominates.
- Do not turn the page into a bibliography-manager, academic-search-engine, or research-methodology product comparison. It owns model-route selection for the research workflow.

## Separate Discovery, Evidence, and Synthesis

- Keep three layers explicit:
  1. **Discovery** — finding candidate papers, reports, datasets, standards, code, patents, documentation, or other relevant sources.
  2. **Evidence inspection** — reading the actual source, extracting methods/results/limitations, and verifying identity/version.
  3. **Synthesis** — comparing evidence, identifying agreement/conflict/gaps, and producing a traceable summary or hypothesis.
- A model-generated search result or citation belongs to discovery until the underlying source has been opened and verified.
- Do not treat a plausible title, DOI, author list, quotation, result, or reference produced from model memory as bibliographic evidence.
- Keep the original source and exact source identity available for every claim important enough to enter a paper, report, review, experiment plan, or decision.

## Default Source-Grounded Managed Route

- Use an organization-approved managed assistant with strong long-document handling and source-grounded web/deep-research capability as the default low-administration route when hosted processing fits the data boundary.
- Current ChatGPT Deep Research can use uploaded files, the public web or restricted sites, and enabled connected sources, with a reviewable research plan and a final report containing citations/source links. Treat exact model, limits, plan access, apps, and source controls as mutable.
- Current Gemini Deep Research can use Google Search plus selected/uploaded/connected sources and produces a research plan/report. Treat current model tiers, source options, limits, and account requirements as mutable.
- Evaluate deep-research products on the user's actual research questions: source coverage, source quality, ability to restrict/prioritize authoritative domains, citation support, handling of contradictory evidence, date/version awareness, omission rate, and human verification effort.
- Do not rank providers globally from one benchmark or vendor demonstration. The useful route depends on field, source access, language, document type, data boundary, and the researcher's acceptance criteria.

## Scholarly and Specialist Source Boundary

- Treat general web search as only one discovery surface. When the field has authoritative specialist databases or repositories, search them directly or include them through supported access rather than assuming open-web coverage is complete.
- Examples can include publisher platforms, Crossref/DOI metadata, PubMed/PMC, arXiv, institutional repositories, standards bodies, patent databases, government/regulatory repositories, domain datasets, or field-specific indexes as applicable.
- Preserve subscription/authentication boundaries. A model or deep-research tool that cannot access a relevant database must not imply that its result is a complete literature search.
- Record search scope where systematic or high-confidence coverage matters: databases/sites, query terms, date window, language, inclusion/exclusion criteria, and search date.
- Distinguish peer-reviewed publication, preprint, technical report, blog/documentation, dataset, code repository, news release, and vendor material. Source type affects what claims the evidence can support.

## Citation and Source Identity

- Verify every material citation against the underlying source before reuse.
- Check title, authors, year/date, publication/venue, DOI or stable identifier, version/revision, and exact page/section/table/figure when the claim depends on a localized passage.
- Detect near-duplicate versions such as preprint versus final paper, conference versus journal extension, repository manuscript versus publisher version, and corrected/retracted versions.
- Do not quote text that the model cannot point to in the actual source. Generated quotations require direct source verification.
- Citation presence is not support. Verify that the cited passage actually substantiates the claim and that the model has not overgeneralized a narrow result.
- Preserve enough source metadata that another researcher can retrieve the same evidence later.

## Literature Review and Evidence Mapping

- Start by defining the research question, scope, population/system, timeframe, and evidence types before broad search.
- Use the model to expand terminology, synonyms, competing theories, related methods, and query formulations, but review those expansions for field-specific errors.
- Build an evidence table/matrix for non-trivial reviews: source identity, question, method/design, sample/data, intervention/system, metrics, key findings, limitations, evidence strength, and relevance to the current question.
- Keep extraction separate from interpretation. The model should identify what the source reports before explaining what it may imply.
- Preserve conflicting findings instead of averaging them into a false consensus.
- Identify missing evidence explicitly: inaccessible source, unclear method, unavailable appendix/data, ambiguous version, or unverified secondary citation.

## Primary Sources and Secondary Synthesis

- Prefer primary/authoritative sources for factual and technical claims when practical.
- Use reviews, meta-analyses, surveys, textbooks, and reputable secondary sources to orient the field and discover primary references, but keep their interpretive layer visible.
- Vendor/provider documentation is appropriate evidence for the vendor's own product/model behavior, not independent validation of quality or comparative superiority.
- News articles, social posts, and community discussion can surface leads or experience reports but should not silently replace the source that owns the technical/scientific claim.
- For standards, laws, regulations, official statistics, protocols, and product specifications, use the current owning body/source and record effective/version dates.

## Long Documents and PDFs

- Use long-context/document tools to accelerate navigation, extraction, comparison, and question answering, but do not treat context-window capacity as proof that every relevant section was considered correctly.
- Preserve page/section/figure/table references for important extracted claims.
- Treat scanned PDFs, multi-column layouts, equations, footnotes, appendices, tables, and figures as possible extraction failure points.
- When exact values matter, verify against selectable source text, tables, supplementary data, or a deterministic extraction path rather than relying on visual OCR-like interpretation alone.
- For multiple papers, prefer structured per-source extraction followed by synthesis over asking a model to summarize a large mixed corpus without source boundaries.

## Current and Time-Sensitive Research

- Treat current scientific/product/policy developments as retrieval tasks rather than training-memory facts.
- Record publication and event/effective dates separately where they differ.
- For fast-moving fields, search for updates, errata, retractions, follow-up work, replication, and current official documentation after identifying an older influential source.
- Do not label the most recently published source as the strongest evidence merely because it is newer.
- Define a recheck boundary for research outputs whose conclusions depend on mutable product capabilities, standards, laws, prices, datasets, or rapidly changing model literature.

## Research Questions and Hypotheses

- Use the model to generate candidate hypotheses, alternative explanations, falsification tests, and missing-variable questions, but label them as generated reasoning rather than observed evidence.
- Ask the model to produce arguments against the current interpretation and to identify what evidence would change the conclusion.
- Do not let the model convert absence of found evidence into evidence of absence unless the search/review design supports that conclusion.
- Keep exploratory hypotheses separate from preregistered/confirmatory analysis where that distinction is methodologically material.

## Quantitative and Computational Research

- Delegate calculations, transformations, statistical tests, simulations, and code execution to deterministic tools and preserve the code/environment needed to reproduce them.
- Use the model for code/query generation, explanation, debugging, methodology review, and result interpretation, but execute and verify the computation independently.
- For published numerical results, trace important values to the source table/dataset or rerunnable analysis.
- When code from a paper/repository is used, verify the exact commit/release/environment and distinguish reproduced behavior from the paper's reported result.
- Route sustained structured-data/statistical work to `data-analyst-or-data-scientist/` where its detailed reproducibility contract applies.

## Coding, Models, and Research Software

- For research code, use coding-model selection from `decision-guides/software-development/` and preserve repository-native tests/validation.
- A model can help interpret unfamiliar research code or implement an experiment, but generated changes must not silently alter methodology, preprocessing, randomization, evaluation metrics, or data splits.
- Keep model-generated code reviewable and version-controlled.
- For computational experiments, record model/service version, prompts/system instructions where material, parameters, seeds, environment, dataset version, and evaluation procedure sufficiently for the intended reproducibility level.

## Research Data and Confidentiality

- Classify unpublished manuscripts, peer-review material, grant proposals, participant data, patient/clinical data, interview transcripts, proprietary datasets, confidential collaborations, embargoed results, and intellectual property before using a hosted model.
- Follow institution/funder/IRB/ethics/client/publisher policy where applicable. A consumer assistant privacy toggle is not equivalent to institutional approval.
- Minimize uploaded content: use public papers, sanitized excerpts, derived statistics, synthetic examples, or local processing when they satisfy the research task.
- Preserve participant consent/data-use restrictions and do not repurpose sensitive data for model prompts or fine-tuning without explicit authorization.
- Keep credentials, repository tokens, private dataset URLs, API keys, reviewer identities, and other secrets outside model-visible context unless explicitly required and safely controlled.

## Peer Review, Authorship, and Integrity

- Use AI to improve clarity, structure, literature navigation, code review, and question generation only within the applicable journal/conference/institution/funder rules.
- Do not fabricate citations, data, experiments, reviewer comments, participant responses, or methodological details.
- The researcher remains responsible for claims, citations, methods, and disclosure requirements in submitted work.
- Do not use AI to impersonate a reviewer/author or bypass confidentiality obligations for peer review or unpublished submissions.
- When policy requires AI-use disclosure, preserve enough workflow detail to disclose accurately.

## Local and Offline Route

- Use local inference when confidential/unpublished material, offline work, provider independence, or repeat private corpus analysis justifies the setup and exact hardware/runtime passes acceptance.
- A local text/reasoning model such as `Qwen3 8B` can support bounded paper summarization, note synthesis, query generation, or code assistance when measured quality is sufficient.
- A compact multimodal model such as `Gemma 4 E2B Instruct` or `Gemma 4 E4B Instruct` can be evaluated for private document/image understanding only when the exact runtime supports the complete modality path.
- Local model memory is not a current literature database. Retrieve current public research through appropriate databases/web tools and then process locally if the data boundary requires it.
- Local retrieval/RAG improves access to the researcher's corpus but does not guarantee source correctness, completeness, citation support, or resistance to poisoned/misleading documents.

## Direct API and Research Automation

- Use direct APIs or custom research agents when the researcher needs reproducible batch extraction, structured evidence tables, repeated classification, custom search/retrieval pipelines, or integration with research software.
- Keep search/retrieval scope, tool permissions, source filters, stopping conditions, retries, and citation/source capture explicit.
- Do not let an autonomous research agent publish, submit, email collaborators, alter datasets, modify repositories, or make external commitments without appropriate confirmation/policy controls.
- For large literature batches, validate extraction against a sampled manually reviewed set before scaling.
- Record model/provider/version and prompt/schema behavior when automated extraction results may be reused as research data.

## Cost per Accepted Research Result

- Compare **total cost per accepted research result**: subscription/API spend, specialist database access, document retrieval, local compute, repeated searches, citation verification, correction time, data cleaning, and the consequence of missed/misrepresented evidence.
- A more capable deep-research mode can be cheaper when it reduces discovery time while preserving traceability, but only if source verification burden remains acceptable.
- A cheap/high-volume model can be useful for first-pass extraction or classification, while a stronger model or human review handles ambiguous/high-impact cases.
- Do not optimize for number of papers summarized. Optimize for relevant evidence correctly identified, verified, and synthesized.

## Escalation Triggers

- Move from ordinary web search/chat to deep research when the question requires multi-source synthesis, broad coverage, source restrictions, or a documented evidence trail.
- Move to specialist scholarly databases/manual search when open-web/deep-research coverage is incomplete or systematic search requirements apply.
- Add a second model/tool only when it materially improves source coverage, long-document handling, extraction accuracy, language support, or synthesis acceptance.
- Move to local/offline processing when unpublished/confidential data cannot use the hosted route and the local stack passes quality/latency requirements.
- Move toward `data-analyst-or-data-scientist/` when quantitative computation becomes the dominant workflow.
- Move to team/organization research routes when shared corpora, institutional permissions, collaborative evidence systems, governance, or research infrastructure become first-order constraints.
- Escalate to a domain expert/methodologist/statistician when the research conclusion requires expertise beyond model-assisted evidence organization.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when local model inference materially constrains the research route.
- Use `../../../hardware/sub/computers/` for personal professional workstations and the applicable accelerator specialization when known.
- Keep research-compute cluster design and hardware purchasing outside this scenario.

## Canonical Links

- Link managed assistant/deep-research products to canonical service owners when named.
- Link `Qwen3 8B` to `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` to their exact canonical Model Reference identities when named.
- Link coding work to `decision-support/selection/models/decision-guides/software-development` and structured-data work to the applicable scenario/decision owner instead of duplicating those contracts.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT Deep Research documentation, current Gemini Deep Research documentation, and canonical AI Lab model/service owners.
- Current deep-research evidence establishes multi-step source-grounded research with user-selectable/restricted sources, uploaded/connected material, research planning, and citation/source-linked reports. These capabilities do not establish complete scholarly coverage or citation correctness.
- Current OpenAI guidance explicitly positions search/deep research as complementary to—not replacements for—specialized databases and instructs users to review linked sources.
- Search indexes, connected-source availability, model aliases, deep-research limits, specialist database access, product data terms, and current literature are mutable; recheck them at research time.
- Provider output is synthesis assistance; the underlying verified source remains the evidence owner.

## Validation

- Discovery, source inspection, and synthesis remain separate stages.
- Generated citations/quotes are never accepted without source verification.
- Specialist scholarly databases remain necessary when general-web coverage is insufficient.
- Source identity/version, publication/effective date, provenance, and contradictory evidence are preserved.
- Long-context capability is not treated as proof of complete/correct document review.
- Quantitative/computational claims retain deterministic reproducibility.
- Confidential/unpublished research follows institution/data-policy boundaries and is not moved to consumer tools by convenience.
- AI-assisted authorship/review follows applicable integrity/disclosure rules.
- Local models/RAG are not treated as current-literature or correctness guarantees.
- Mutable current claims carry the 2026-08-24 evidence boundary.
