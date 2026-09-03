# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual whose model route is primarily constrained by **data egress, offline availability, provider independence, or a requirement to keep processing under local control** rather than by lowest cost, maximum hosted quality, or experimentation breadth.
- Cover three related but distinct operating modes inside one scenario:
  1. **privacy-first connected** — the device may use the Internet, but sensitive prompts/documents should remain local and hosted escalation is allowed only for explicitly permitted data;
  2. **offline-capable** — normal work must continue without Internet access after models/runtimes/corpora are staged locally;
  3. **isolated/air-gapped** — network connectivity is intentionally absent or tightly controlled and updates/models are imported through an explicit transfer process.
- Keep these modes together because they share the same core decision route—local model/runtime/data ownership—but state their different update, tool, and operational constraints rather than claiming all local use is air-gapped.
- Distinguish this scenario from `everyday-home-user/`: a consumer assistant with privacy controls can be acceptable there, while here **local/no-egress behavior is a first-class requirement that can outweigh convenience or frontier quality**.
- Distinguish it from `home-lab-owner/`: persistent multi-client service operation is optional here. A privacy-first user may need only one local desktop app or laptop workflow.
- Distinguish it from `sensitive-data-professional/`: employer/client/regulatory policy and professional accountability move the reader into the professional route even if the technical stack is also local.

## Start With a Data-Path Requirement

- Before choosing a model, identify what must remain local: prompt text, documents, images/screenshots, audio, embeddings, vector indexes, chat history, logs, tool arguments/results, generated files, model-side memory, and any derived metadata.
- Define whether `no egress` means **no prompt/content egress**, **no third-party processing at all**, or **no network connectivity**. These are materially different requirements and must not be collapsed into the word `private`.
- Identify acceptable network operations separately. A privacy-first connected setup may permit model/runtime downloads and update checks while prohibiting prompt/document upload; an air-gapped setup requires staged imports and cannot assume online model discovery or updates.
- Treat every external tool, connector, browser/search function, MCP server, cloud fallback, telemetry/update mechanism, and remote API as a possible separate data path. A local model does not make a workflow offline if its tools still send content elsewhere.
- Minimize sensitive inputs even locally. Local execution reduces provider exposure but does not remove risks from malware, compromised accounts, shared devices, logs, backups, stolen hardware, insecure file permissions, or untrusted tools.

## Default Local Route

- Make a **fully local inference route** the default when the required data boundary cannot be satisfied by ordinary hosted processing.
- Prefer the least operationally complex local runtime that demonstrably keeps the required workflow local on the exact device. A desktop application is often preferable to self-hosting a network service when only one user/device needs access.
- Current LM Studio documentation explicitly supports offline use after required models and runtimes have been obtained: local model chat, local document/RAG processing, and local server requests can operate without Internet connectivity. Treat model search/download, runtime download, and update checks as separate online operations that must be completed before disconnection or staged for isolated systems.
- Current Ollama privacy documentation distinguishes local and cloud execution: locally processed prompts/responses remain on the local machine from Ollama's service perspective, while cloud-hosted models are a different processing route. Preserve that local/cloud distinction instead of calling the product itself uniformly offline/private.
- Do not generalize one software vendor's privacy statement to another runtime. When a product is named as a privacy route, link its canonical software owner and verify the exact version/features used.

## Current Compact Model Ladder

- Use `Phi-4 Mini Instruct` as a compact current text-oriented local baseline when low resource use, multilingual text work, and offline reasoning/writing matter more than multimodal input. Its model-level context/capabilities do not imply that maximum context is practical on every local device.
- Use `Qwen3 8B` as a current stronger general text/reasoning candidate when the exact artifact/runtime/device can support it with acceptable latency and context headroom.
- Use `Qwen3 14B` only when the local machine has enough measured memory/accelerator capacity and the accepted-result improvement over smaller models justifies additional latency, power, and resource use.
- Use `Gemma 4 E2B Instruct` as a compact multimodal candidate for privacy-sensitive local image/document/audio understanding where its exact runtime supports the required modality path.
- Use `Gemma 4 E4B Instruct` as a larger compact multimodal alternative only after measured local fit; do not assume E4B is preferable merely because it is larger.
- Do not make `largest model that fits` the privacy-first goal. The preferred model is the smallest route that meets accepted quality, modality, latency, and context while preserving the required data boundary.
- When current external research identifies a materially better local candidate that is not yet represented in canonical Model Reference, materialize/refresh its canonical identity before adding it as a durable named recommendation.

## Exact Local Fit

- Require exact device, usable RAM/VRAM/unified memory, runtime/backend/version, model artifact/version, quantization/precision, configured context, multimodal auxiliaries, and peak memory before claiming practical fit.
- File size or parameter count is only a planning input. Include KV/context state, runtime buffers, multimodal projectors/encoders, OS/application reserve, display use, and accelerator fallback/offload.
- Measure first-token latency, sustained generation/task latency, usable context, thermals/power where material, and accepted-result quality on the privacy-sensitive workload.
- If a local model fits only with heavy CPU/system-RAM offload, measure whether resulting latency remains usable. Running locally is not valuable if every request becomes impractically slow.
- When the exact hardware becomes the primary question, continue into `../../../hardware/` and the relevant computers/mobile/single-board/server branch rather than embedding a generic local-hardware table here.

## Offline Preparation

- For offline-capable operation, stage **all dependencies required for the real workflow**, not only the main model weights: runtime binaries/libraries, model/tokenizer/template files, multimodal projection/encoder artifacts, embedding/reranker models, local OCR/speech/media dependencies, Python/system packages if used, and the local reference corpus needed by the workload.
- Test the workflow with networking disabled before declaring it offline-ready. Discover hidden downloads, license checks, model lookups, web fonts/assets, telemetry dependencies, tool calls, or package/runtime fetches during this test.
- Keep a reproducible inventory of exact versions and sources. For manually staged model/runtime artifacts, preserve source repository/release, revision/version, file identity, and cryptographic hash when the upstream/distribution provides one or when the operator can calculate and record one.
- Treat community conversions separately from upstream model identity. An offline environment may legitimately use a community GGUF/other conversion, but source provenance and conversion identity must remain traceable.
- Verify licenses/usage conditions before copying model weights or software into an isolated environment; offline transfer does not waive model or software licensing terms.

## Isolated and Air-Gapped Updates

- For an isolated/air-gapped route, define an explicit update path rather than assuming the system will never change.
- Acquire updates on a separate permitted system, verify source/version/integrity, scan/process them according to the user's security model, then transfer through the approved medium/path.
- Preserve rollback copies or a reconstructable previous version when an update can break model format, prompt templates, tool behavior, multimodal support, or accelerator compatibility.
- Do not auto-import arbitrary models merely because they are popular. Each imported artifact increases storage, provenance, and review burden inside the isolated environment.
- If no safe update process exists, surface the resulting **freshness debt**: the local runtime/model/corpus will age, current web knowledge is unavailable, and security/runtime fixes may be delayed.

## Local RAG and Personal Knowledge

- Local document chat/RAG can preserve the no-egress boundary only when **the whole pipeline is local**: document parsing, OCR if needed, chunking, embeddings, vector/index storage, retrieval, reranking, generation, logs, and UI/tool layer.
- Do not call a workflow local if document embeddings or OCR are silently sent to a hosted API while generation is local.
- Treat embeddings/vector indexes as sensitive derived data when they originate from sensitive documents. Local RAG is not a reason to leave indexes/backups broadly accessible.
- Preserve source attribution. Retrieval improves access to local documents but does not guarantee that the model's answer is faithful; important claims still require inspection of the retrieved source.
- When persistent personal knowledge management becomes the dominant need rather than privacy itself, route toward the approved `personal-knowledge-base-user` scenario when materialized.

## Tools, Agents, and Network Egress

- A local LLM with tools is no longer a simple local-text pipeline. Enumerate every tool's permissions and network behavior before calling the workflow offline/private.
- Disable or remove web search, cloud connectors, remote MCP servers, hosted embeddings, analytics, or other network-capable tools when the operating mode requires no egress.
- Prefer read-only/local tools during initial setup. For file writes, shell execution, home automation, messages, or other side effects, use explicit scope/allowlists, sandboxing or isolation where practical, and human approval for high-impact actions.
- Do not put secrets into prompt context merely because the model is local. Prefer OS/keychain/secret-manager boundaries and inject only the minimum credential capability required by a tool.
- Treat local network services as network exposure. Binding an inference server to a LAN interface may expose sensitive prompts/results to other hosts if authentication/access controls are weak.

## Local Storage, History, and Backups

- Verify where the chosen application stores conversation history, imported documents, model metadata, logs, caches, temporary files, and RAG indexes. `Local processing` does not mean `nothing is persisted`.
- Use disk/device encryption and OS account/file permissions appropriate to the sensitivity of stored content; implementation belongs to the device/security owner but is a constraint on whether the local route actually improves privacy.
- Minimize or disable prompt/response logging when it is not required. Logs and crash diagnostics can recreate the same sensitive content the user was trying not to upload.
- Treat backups/sync as a separate egress path. A locally processed private document can still leave the device through cloud backup, photo/file sync, workstation backup, or shared NAS replication.
- Include model weights separately from sensitive state in backup planning: weights are often reconstructable, while private histories/indexes/config/adapters may be unique and should receive deliberate encryption/retention handling.

## Hosted Privacy Controls Are a Different Route

- Explain that consumer hosted privacy controls can reduce some data use but do **not** satisfy strict offline/no-third-party-processing requirements.
- Current ChatGPT consumer controls can disable use of new conversations for model improvement, and Temporary Chat changes history/memory/training behavior; Temporary Chats can still be retained for a bounded safety period, and third-party actions/connectors have their own recipient policies. Therefore `Temporary Chat` is not equivalent to local/no-egress processing.
- Apply the same principle across providers: evaluate current retention, training, human-review, account, region, and connector/provider-chain terms before using a hosted service for a privacy-sensitive task.
- A hosted provider with stronger contractual/zero-retention terms may be a valid **separate controlled-hosted route** for some users, but it remains third-party processing and must match the actual threat/data-boundary requirement.
- Do not weaken a strict local requirement merely because a hosted model is stronger. Instead state the local quality/capability ceiling and provide hosted escalation only for data that is permitted to leave the device.

## Hybrid Privacy Route

- Allow a hybrid route when only part of the user's work is sensitive. Keep sensitive/full-source material local and use hosted models for public, synthetic, or explicitly permitted tasks where their quality/tools offer better accepted-result economics.
- Treat redaction/de-identification as risk reduction, not guaranteed anonymization. Context can re-identify people or confidential material even after obvious names are removed.
- Prefer deriving a minimal non-sensitive question locally rather than sending an entire private source document to hosted infrastructure when the hosted model does not need the source.
- Keep a clear human-visible boundary between local and hosted modes so the user does not accidentally send private context through the wrong model/provider.
- If an application mixes local and cloud models in one UI, require the selected route/provider to be explicit enough that the user can know where a request will run before submission.

## Offline Knowledge and Freshness

- State that an offline model has no live web knowledge unless the user supplies a local current corpus/tool. Model training knowledge and locally cached documents age.
- For changing facts such as software versions, prices, law, medical guidance, schedules, security advisories, or current events, require an approved fresh source before acting. If the system cannot obtain one, mark the answer as potentially stale rather than fabricating currency.
- Build offline reference packs only when the recurring workload justifies update/curation effort. A local snapshot trades freshness for control and availability.
- Keep source timestamps/version metadata with important offline corpora so the user can distinguish `model answer` from `current verified information`.

## High-Stakes and Sensitive Decisions

- Privacy does not improve factual reliability. Local models can hallucinate, miscalculate, misread documents, or produce unsafe instructions just like hosted models.
- For health, legal, financial, safety, identity, security, or other high-consequence decisions, use the model to organize/translate/summarize permitted information while requiring authoritative sources, deterministic checks, or qualified professional review before action.
- For local document extraction, verify material identifiers, dates, amounts, medical values, legal clauses, commands, and other critical fields against the source.
- If stronger hosted quality would materially reduce a high-stakes error but the data cannot leave the device, state that trade-off explicitly rather than silently recommending the weaker local result as sufficient.

## Total Cost and Trade-Offs

- Compare privacy/offline value against setup, storage, update effort, device resource use, electricity, slower inference, limited modalities/tools, and possible quality gap.
- Do not claim local is cheaper merely because weights are free. Include hardware already owned, opportunity cost, operator time, model/runtime update burden, storage/backups, and correction/review time.
- Do not claim hosted is cheaper merely from subscription/API price when the user's core requirement would be violated by third-party processing.
- Use **cost per accepted private outcome**: a route that preserves privacy but is unusably slow or unreliable may need a smaller model/workflow redesign; a stronger local model that requires new hardware may lose to a carefully bounded hybrid route if the data classification permits it.

## Escalation Triggers

- Move from `Phi-4 Mini Instruct` or another compact text baseline to Qwen3 8B/14B only when measured accepted-result quality requires it and exact local resources remain practical.
- Move from Gemma 4 E2B to E4B when multimodal quality improves enough to justify extra resource use; do not upgrade by parameter count alone.
- Move from a desktop-only workflow to `home-lab-owner/` when availability across devices, persistent local APIs, shared storage/RAG, backups, monitoring, or unattended operation become first-class requirements.
- Move toward `personal-knowledge-base-user` when persistent corpus organization/search/retrieval—not just privacy—is the dominant decision.
- Use hosted/hybrid escalation only when the selected input is allowed to leave the device and the provider chain meets the data boundary.
- If exact hardware prevents acceptable local quality/latency/context, continue into `../../../hardware/` to determine realistic local ceilings before considering hardware acquisition or redesign.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` whenever exact device resources determine the local ceiling.
- Use `../../../hardware/sub/computers/` for desktop/laptop CPU/GPU/NPU/Apple-unified-memory routes, `../../../hardware/sub/mobile/` for phone/tablet on-device routes, `../../../hardware/sub/single-board/` for SBC/edge routes, and `../../../hardware/sub/servers/` only when a dedicated local service host exists.
- Do not copy platform runtime/support matrices into this scenario.

## Canonical Links

- Link compact text candidates to `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link the larger text route to `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-14b` when named.
- Link compact multimodal candidates to `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/reference/producers/google/gemma/gemma-4/models/e4b-instruct`.
- Link LM Studio, Ollama, llama.cpp, MLX-LM, MLC-LLM, or another named runtime/application to its canonical software owner rather than duplicating complete privacy/runtime documentation here.
- Link hosted services to canonical service owners when discussing a controlled hosted/hybrid alternative.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current first-party local/offline runtime documentation, current consumer hosted data-control documentation, official current local-model sources, and canonical AI Lab model/hardware owners.
- LM Studio currently documents that downloaded local models, local document/RAG workflows, and its local server can operate offline and keep those inputs local to the application; search/model/runtime download and app-update operations require connectivity. Treat this as a current product-specific statement, not a universal local-runtime property.
- Ollama currently distinguishes local inference from its cloud-hosted model processing in its privacy documentation; recheck the selected mode/version before making product-specific privacy claims.
- Consumer hosted retention/training controls, connector behavior, runtime telemetry/update behavior, model artifacts, and application storage locations are mutable; recheck them before rendering a current privacy recommendation.
- A vendor privacy statement establishes that vendor's documented behavior, not independent proof of endpoint security, OS security, absence of malware, or the user's complete data path.

## Validation

- The scenario has a distinct route because data egress/offline constraints change model, runtime, tool, update, and hosted-fallback choices; it is not a duplicate `everyday-home-user` page.
- `Private`, `local`, `offline`, and `air-gapped` are not used as synonyms.
- A local model does not make cloud tools/connectors/embeddings/backups/logging local automatically; the complete data path is evaluated.
- Offline readiness is tested with connectivity disabled and includes all required runtime/model/auxiliary/corpus dependencies.
- Local RAG is considered private only when the complete parse/embed/index/retrieve/generate pipeline remains within the allowed boundary.
- Consumer privacy controls are not represented as equivalent to strict no-third-party-processing or offline operation.
- Exact model/artifact/runtime/hardware evidence is required; file size, parameter count, or local load success is not practical-fit proof.
- Device/storage/log/backup risks remain visible so `local` is not misrepresented as automatically secure.
- High-stakes reliability remains independent from privacy.
- Hybrid escalation applies the data boundary before any content leaves the local environment.
- Mutable current claims carry the 2026-08-23 evidence boundary.
