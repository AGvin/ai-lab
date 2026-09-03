# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual who wants AI to work over a **durable personal corpus** of notes, PDFs, bookmarks, articles, transcripts, manuals, project files, or other owned/reference material across many sessions.
- Make the corpus—not chat history—the primary work object. The core decision is how sources are stored, indexed, retrieved, cited, refreshed, and kept under the desired data boundary while one or more models reason over them.
- Distinguish this scenario from `everyday-home-user/`: occasional file upload or one-off document chat does not require a personal knowledge-base architecture.
- Distinguish it from `privacy-first-or-offline-user/`: a knowledge base may be hosted or local. Privacy/offline becomes the primary owner only when no-egress/offline requirements dominate every other choice.
- Distinguish it from `home-lab-owner/`: a personal corpus can live in a managed hosted workspace or local desktop application without persistent self-hosted infrastructure.
- Distinguish it from organization knowledge assistants: shared permissions, enterprise source connectors, organization-wide governance, audit, service ownership, and business knowledge lifecycle move the reader into team/organization scenarios.

## First Decision — What Is the Source of Truth?

- Identify the authoritative corpus before selecting the model or workspace:
  - local Markdown/files/vault;
  - cloud drive/document collection;
  - source-grounded hosted notebook/workspace;
  - self-hosted knowledge workspace;
  - custom indexed corpus whose canonical files remain elsewhere.
- Prefer a source-of-truth format/location that the user can export, back up, inspect, and migrate independently of one model provider when long-term ownership matters.
- Do not treat an assistant's conversational **memory** as a substitute for a knowledge base. Memory can personalize interaction but normally does not provide a complete inspectable, versioned, citation-grounded corpus.
- Do not treat a vector database or embedding index as the source of truth. Derived indexes must be rebuildable from canonical documents and metadata.
- Preserve original source documents and relevant metadata when the exact source matters. Generated summaries, embeddings, extracted text, OCR output, or model-created notes are derived artifacts and can contain errors.

## Route Classes

- Compare four distinct routes when relevant:
  1. **hosted source-grounded knowledge workspace** — lowest administration, provider-managed ingestion/retrieval/generation, but source upload/retention/provider limits are material;
  2. **local-first knowledge workspace with optional AI** — user owns ordinary files/notes and can add local or hosted AI selectively;
  3. **self-hosted AI knowledge workspace** — more control over corpus/model/provider path at the cost of deployment, indexing, updates, backups, and security operations;
  4. **custom RAG/retrieval stack** — maximum control/evaluation flexibility but highest engineering and maintenance burden.
- Do not present these routes as a maturity ladder. A hosted source-grounded product may be the best personal route even for an advanced user; a custom stack is justified only by requirements it materially satisfies.

## Hosted Source-Grounded Workspace

- Use a hosted source-grounded workspace when the user values low administration, convenient source ingestion, citations, cross-device access, and source-derived artifacts more than local custody of every processing step.
- `Gemini Notebook` (formerly NotebookLM) is a current canonical example of this product class. Its persistent notebook/source collection, source-grounded chat, inline citations, notes, and source-derived artifacts make it materially different from a general Gemini assistant conversation.
- Preserve the current product rename boundary: canonical AI Lab identity is `Gemini Notebook`, with `NotebookLM` as the official former name. Do not create separate recommendation identities for the same product.
- Treat supported source types, per-notebook/source limits, model behavior, plans, connected-source synchronization, and product features as mutable. Recheck the canonical service owner before rendering current limits or plan advice.
- Evaluate whether the hosted service stores a copy/snapshot or remains linked/synchronized to the upstream source. Source update semantics determine how quickly answers become stale.
- Keep consumer/account data controls separate from corpus-grounding quality. A service can cite sources well while still being unsuitable for a sensitive corpus under the user's data boundary.

## Local-First Knowledge Workspace

- Use a local-first workspace when durable file ownership, interoperability, offline editing, or existing note practices are primary and AI should be an optional layer rather than the owner of the knowledge.
- `Obsidian` is a current canonical example: its primary identity is a local-first Markdown knowledge workspace whose vault files remain ordinary files on the user's filesystem. AI plugins/agents/sync/publishing are secondary capabilities and must not be confused with the source-of-truth boundary.
- Prefer explicit local files/metadata/links as canonical knowledge when the user wants long-lived portability. The AI index should be rebuildable if a plugin/model/provider changes.
- When adding AI plugins or external services, evaluate each plugin/provider as a new data path. `The notes are local` does not imply that embeddings, prompts, selected passages, or generated answers remain local.
- Do not recommend a plugin solely from popularity. Check maintenance, permissions/data handling, model/provider chain, index location, export/rebuild path, and whether it preserves the user's original vault.

## Self-Hosted Knowledge Workspace

- Use a self-hosted knowledge workspace when the user needs persistent corpus-aware search/chat plus greater control over model/provider/data placement and accepts operational work.
- `Khoj` is the current canonical self-hostable personal knowledge-workspace example. Preserve its current open-source/self-hostable software identity and do not present the historical Khoj Cloud hosted service as currently available; the canonical owner records that hosted Khoj Cloud shut down on **2026-04-15**.
- Evaluate the complete self-hosted pipeline: ingestion/parsing, OCR where needed, embeddings, index/vector store, retrieval/reranking, generation model, user/chat state, backups, upgrades, and network exposure.
- A self-hosted UI does not make the workflow local if it calls hosted embeddings or hosted LLMs. Record every external provider and classify the data sent to it.
- If the user needs high availability/multiple clients/monitoring rather than simply a personal corpus, route operational design into `home-lab-owner/`.

## Model Roles — Do Not Select One Model for the Whole Knowledge System

- Separate at least these model/component roles when they exist:
  - document parsing/OCR/vision;
  - embedding/retrieval representation;
  - keyword or hybrid retrieval;
  - reranking;
  - answer/synthesis generation;
  - optional query rewriting/classification;
  - optional speech/image interfaces.
- A strong generator cannot recover a source that retrieval failed to surface. Improve retrieval/corpus quality before assuming a larger chat model will fix missing evidence.
- An embedding model that retrieves semantically similar text is not sufficient proof of source usefulness. Measure whether the retrieved passages answer the intended personal queries.
- Reranking can improve precision when the initial candidate set is noisy, but it adds latency/compute and should be justified by measured retrieval quality.
- Use a multimodal model only when images/scanned documents/diagrams/screenshots materially require it. For text-heavy corpora, specialized OCR/parsing plus text retrieval can be more reliable and cheaper than sending every page through a VLM.

## Current Local Generator Candidates

- For a local/self-hosted personal corpus, use `Qwen3 8B` as a current compact text/reasoning generator baseline when the hardware/runtime supports it with acceptable context and latency.
- Use `Qwen3 14B` as a larger local synthesis candidate only when measured answer quality/faithfulness over the user's retrieved context improves enough to justify the additional resource burden.
- Use `Phi-4 Mini Instruct` as a lighter text route when local resource limits or low latency matter more than maximum synthesis quality.
- Use `Gemma 4 E2B Instruct` or `Gemma 4 E4B Instruct` when local multimodal document/image understanding is genuinely needed and the exact runtime supports the required modality path.
- Do not rank these models from provider benchmark scores alone. Evaluate them **after the same retrieval context has been supplied** so retrieval and generator differences are not confounded.
- Do not assume the model's maximum advertised context should contain the entire corpus. Retrieval exists to provide a bounded relevant context; larger context can increase latency/memory and still fail to locate the right evidence.

## Ingestion and Corpus Normalization

- Inventory source types and choose an ingestion path that preserves enough structure for later citation: filenames/URLs, titles, headings, page/section anchors, timestamps, authors, source collections, and other useful metadata.
- For PDFs, scans, images, and complex layouts, distinguish embedded-text extraction from OCR and vision-based interpretation. Keep the original document available for verification because extraction can reorder, omit, or misread content.
- Avoid destructive normalization that prevents tracing an answer back to the original source.
- Detect duplicates/version variants when the same document exists in multiple places. Retrieval over conflicting copies can create false consensus or stale answers.
- Define what should **not** be indexed: secrets, credentials, unnecessary sensitive documents, temporary files, generated caches, duplicate exports, or material whose license/terms prohibit the intended processing.
- Treat websites/bookmarks as snapshots unless the system actually refreshes them. A stored page is not automatically current because the source URL still exists.

## Chunking and Context Boundaries

- Treat chunking as a retrieval variable, not a fixed recipe. The useful unit depends on document structure, query type, model/context, and whether relationships span multiple sections.
- Preserve heading/section metadata and reasonable overlap only where it improves retrieval. Excessive overlap increases duplicate evidence and context cost.
- For tables, code, procedures, legal clauses, or structured records, prefer units that preserve the structure needed to interpret the content rather than arbitrary character boundaries.
- When retrieved chunks omit essential surrounding context, fetch neighboring/parent sections or the original source rather than asking the generator to guess.
- Keep source identifiers attached through chunking/retrieval so citations point back to the canonical source, not only to an opaque vector record.

## Retrieval Quality Evaluation

- Build a small personal **gold query set** before tuning models. Include easy lookups, paraphrased questions, multi-source questions, time/version-sensitive questions, and questions whose correct answer is `not in my corpus`.
- Evaluate retrieval separately from generation:
  - whether the needed source appears in the candidate set;
  - ranking position/relevance;
  - stale/conflicting-source behavior;
  - whether unrelated but semantically similar chunks crowd out the answer;
  - latency and corpus-scale behavior.
- Include negative tests where no source supports the answer. The system should abstain or clearly say the corpus does not contain enough evidence rather than allowing the LLM to fill gaps from general knowledge without disclosure.
- When hybrid lexical + semantic retrieval or reranking materially improves the gold-query result, preserve it; otherwise avoid complexity that adds little accepted-result value.

## Answer Grounding and Citations

- Require a clear distinction between **source-grounded statements** and the model's general inference/background knowledge.
- Prefer answers that cite the specific source/section/page/chunk context used. The user should be able to open the cited source and verify the material claim.
- A citation is not proof that the answer is faithful. Test whether the cited passage actually supports the statement and whether conflicting sources were ignored.
- For exact quotations, numbers, dates, identifiers, medical/legal/financial facts, configuration values, or other high-consequence data, verify against the original source instead of trusting a generated paraphrase.
- When sources conflict, surface the conflict and source dates/versions rather than synthesizing one confident answer without provenance.
- RAG does not automatically make a model truthful; it changes the evidence available to the generator.

## Knowledge Freshness and Versioning

- Define source update semantics for every important corpus class: manual re-import, filesystem watcher, sync connector, scheduled crawl, linked source, or immutable snapshot.
- Record source dates/versions where freshness matters. Retrieval cannot distinguish old from current information reliably if the corpus lacks usable metadata.
- Re-index or invalidate derived data after material source changes. Do not assume an old embedding/index automatically reflects edited documents.
- Preserve deleted/superseded material intentionally only when historical retrieval is desired; otherwise stale copies can poison current answers.
- For changing domains such as software, prices, laws, medicine, schedules, product docs, or security guidance, require a current external/authoritative check when the personal corpus may be stale.

## Personal Memory vs Knowledge Retrieval

- Keep three concepts separate:
  - **conversation history** — previous dialogue;
  - **assistant memory/personalization** — compact user facts/preferences retained by a product;
  - **knowledge corpus** — explicit sources the user expects to search/reason/cite.
- Do not represent assistant memory as authoritative factual storage for notes, documents, research, or project history.
- Use memory/personalization only for interaction preferences/context whose exact source citation is unnecessary and whose retention matches the user's privacy expectation.
- When a remembered fact contradicts the corpus, prefer explicit source-grounded evidence and let the user correct/update the memory separately.

## Privacy and Data Boundary

- Classify corpus material before selecting hosted/self-hosted/local routes. A personal knowledge base can contain identity documents, health records, financial data, private correspondence, employer/client material, unpublished work, location history, and other sensitive content accumulated over years.
- Treat embeddings/vector indexes, OCR text, summaries, extracted metadata, query logs, and chat history as potentially sensitive **derived data**. Keeping originals local while sending embeddings or retrieved chunks to a provider can still violate the intended boundary.
- For hosted knowledge workspaces, evaluate current upload retention/training/access/provider-chain policies and account type before ingesting sensitive material.
- For self-hosted/local pipelines, endpoint security, disk encryption, permissions, backups/sync, logs, model/tool downloads, and network exposure remain material; `self-hosted` does not automatically mean secure.
- When strict no-egress/offline operation is primary, apply `privacy-first-or-offline-user/` and require the whole parse/embed/index/retrieve/generate stack to remain inside the allowed boundary.

## Untrusted Sources and Prompt Injection

- Treat corpus documents/web pages/emails/imported notes as **data**, not authority to modify system/tool policy. Retrieved text may contain malicious or accidental instructions aimed at the model.
- Do not allow a source passage to silently authorize tool calls, credential access, file deletion, messaging, payments, or another external side effect.
- For tool-using/agentic knowledge workflows, separate retrieved content from trusted control instructions and require explicit authorization for high-impact actions.
- If the system retrieves Internet content in addition to the personal corpus, mark external/current-web evidence separately from user-owned sources.

## Portability and Lock-In

- Before committing a large corpus to one workspace, verify export/recovery of original sources, notes, and useful metadata. A strong AI feature does not compensate for losing control of long-lived knowledge.
- Prefer rebuildable derived indexes over proprietary state with no export path when the corpus is expected to survive provider/model changes.
- Keep source organization independent enough that moving from hosted to local/self-hosted—or changing the generator/embedding model—does not require reconstructing the user's knowledge from chat transcripts.
- Treat product-generated audio/video/summaries/quizzes or other artifacts as useful derivatives, not replacements for canonical sources.

## Cost and Accepted-Knowledge Outcome

- Compare **cost per trusted retrievable answer**, not only LLM token/subscription price.
- Include workspace subscription/API cost, embedding/index cost, storage, OCR/parsing, re-indexing, local hardware/electricity, backup, setup/maintenance, correction/source-verification time, and the cost of stale/incorrect retrieval.
- Hosted workspaces can win on administration and integrated source UX; self-hosted/local can win on custody/control/offline use; custom RAG can win on evaluation/control only when the user actually needs that flexibility.
- A larger generator can be worse economics if retrieval remains poor. Fix source quality/retrieval before paying for more generation capacity.

## Escalation Triggers

- Move from ordinary assistant file uploads to a knowledge workspace when the same corpus must survive across many sessions and be searched/cited repeatedly.
- Move from hosted source-grounded workspace to local-first/self-hosted when corpus ownership/privacy/offline/provider-control requirements outweigh managed convenience.
- Move from local-first notes to self-hosted AI workspace when semantic retrieval/source-grounded chat becomes recurring enough to justify indexing/operations.
- Move from packaged workspace to custom RAG only when measured retrieval, source-type, model/provider, evaluation, integration, or data-control requirements cannot be satisfied by the simpler route.
- Upgrade the local generator only when the **same retrieved evidence** yields materially better accepted answers; do not use a larger model to mask retrieval defects.
- Add reranking/hybrid search/OCR/vision only after a gold-query/source-type test identifies that layer as the bottleneck.
- Move toward `home-lab-owner/` when the local knowledge service needs persistent remote availability, multiple clients, monitoring, backup operations, and service reliability.
- Move toward professional/team/organization scenarios when the corpus includes employer/client data or becomes a shared governed knowledge base.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when a local generator, embedding model, reranker, OCR/VLM, or persistent knowledge service is constrained by exact device resources.
- Use `../../../hardware/sub/computers/` for desktop/laptop/local-first routes, `../../../hardware/sub/servers/` for persistent self-hosted knowledge services, and `../../../hardware/sub/single-board/` only when an SBC genuinely hosts part of the pipeline.
- Do not duplicate hardware/runtime fit matrices in this scenario.

## Canonical Links

- Link hosted source-grounded service to `catalog/services/knowledge-workspaces/gemini-notebook` when named.
- Link local-first/self-hosted software examples to `catalog/software/interfaces-and-workspaces/knowledge-workspaces/obsidian` and `catalog/software/interfaces-and-workspaces/knowledge-workspaces/khoj` when named.
- Link local generator candidates to canonical Model Reference identities such as `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct`, `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b`, `.../qwen3-14b`, and `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct` / `e4b-instruct` when applicable.
- Link embedding/reranking/OCR/vector/database/runtime products to their canonical owners when materialized; do not invent duplicate identities inside this scenario.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** against current canonical AI Lab knowledge-workspace owners and their current official references: Gemini Notebook as Google's hosted source-grounded notebook/workspace; Obsidian as a local-first Markdown/vault knowledge workspace; and Khoj as continuing open-source/self-hostable personal knowledge software after its hosted Cloud shutdown on 2026-04-15.
- The Gemini Notebook/NotebookLM product rename occurred on **2026-07-16** in the current canonical service evidence; preserve one product identity and recheck current Google feature/source/plan limits before rendering details.
- Source connectors/types/limits, embedding/model choices, product data policies, plugin behavior, OCR support, hosted model aliases, and self-hosted software features are mutable; recheck them before current recommendation claims.
- Vendor source-grounding/citation features establish product capability, not independent proof of retrieval recall, citation faithfulness, or accepted answer quality on the user's corpus. Use the user's gold-query evaluation for that evidence.

## Validation

- The corpus is the primary durable object; chat history and assistant memory are explicitly separate.
- Hosted source-grounded, local-first, self-hosted, and custom RAG routes remain distinct and are not ranked by technical complexity.
- Original sources remain canonical and derived embeddings/indexes/OCR/summaries are rebuildable or treated as derived state.
- Retrieval quality is evaluated separately from generator quality with positive, multi-source, stale/conflicting, and `not in corpus` queries.
- Citations are verified for actual support and do not convert RAG into automatic truthfulness.
- Source freshness/version/update semantics and re-indexing are explicit.
- The whole data path includes derived indexes/logs/retrieved chunks, not only original document storage.
- Retrieved/untrusted source text cannot silently authorize agent/tool side effects.
- Portability/export and long-term corpus ownership are part of model/workspace selection.
- A larger model is not used to mask ingestion/retrieval defects.
- Mutable current claims carry the 2026-08-23 evidence boundary.
