# Documentation Requirements

## Scenario Fit

- Present this scenario for one individual using ordinary phone/tablet/laptop/desktop devices for personal writing, questions, planning, web-backed research, photos, files, light data work, brainstorming, and other everyday assistance with minimal setup and administration burden.
- Keep the scenario explicitly **personal**. Employer/client/internal-data use belongs in `professionals/general-knowledge-worker/` or another applicable professional/organization route when work policy, approved-tool controls, confidentiality, regulated data, or professional-review obligations materially apply.
- Do not absorb other approved scenario identities merely because an everyday user occasionally touches them. Persistent personal knowledge bases, privacy-first/offline operation, travel/multilingual use, family/household orchestration, accessibility-first use, and recurring personal-data analysis become separate decision routes when those concerns dominate the model choice.
- Do not assume a discrete GPU, NPU, Apple Silicon, large RAM pool, or always-on home server. When exact owned hardware becomes a first-order constraint, continue into sibling `../../../hardware/` selection rather than guessing fit here.

## Default Starting Route

- Use **one managed consumer assistant** as the default low-administration starting route when the user's data boundary permits hosted processing. Ordinary personal use normally benefits more from a polished cross-device application, current hosted models, web/file/media tools, and provider-managed updates than from administering local inference.
- Current canonical assistant-workspace examples verified on **2026-08-23** include ChatGPT, Claude, and Gemini. Treat exact default models, free quotas, tool limits, connected-app support, plan pricing, regional availability, and product UI as mutable service facts.
- Do not prescribe permanent provider switching. Run a short evaluation on the user's recurring tasks, choose one primary assistant, and add a second service only when it repeatedly delivers a distinct accepted-result advantage or ecosystem capability worth the extra fragmentation/cost.
- Evaluate the managed candidates with a compact personal workload set such as: explain a current question with sources; rewrite a message; summarize a PDF or image; plan a multi-step personal task; inspect a photo/screenshot; compare options under explicit constraints; and handle a short spreadsheet/table if that is part of normal use.
- Judge the route by accepted-result quality, correction effort, latency, convenience on the user's devices, availability of required modalities/tools, data controls, and monthly cost rather than by provider reputation or one benchmark score.

## Consumer Product and Ecosystem Fit

- Treat current free tiers as the natural first evaluation surface when their limits are adequate. For example, current ChatGPT Free provides web search plus bounded file/image/data-analysis and image-generation tools; current Claude Free uses the current Sonnet-class default and provides a broad consumer assistant surface. These details are verified only for the stated date and must not become permanent ranking criteria.
- Treat device/ecosystem integration as a legitimate convenience dimension when it removes repeated copy/upload/setup steps, but surface the privacy/configuration cost of that integration.
- Gemini is a particularly relevant option for a user already centered on Google/Android/Drive/Photos because current Gemini Apps can work with uploaded documents, images, video/audio, Drive content, and selected connected apps. Do not imply that integration is free of data-governance trade-offs: some connected-app/file workflows depend on the user's Gemini activity settings and account type.
- On current Gemini consumer accounts, `Keep Activity` materially changes both personalization/connected-app availability and data handling. Turning it off limits which connected apps remain available; temporary or activity-off chats have different retention/training behavior. Treat this as a route trade-off to inspect, not a reason to label one provider universally more private.
- For ChatGPT, current consumer Data Controls allow model-improvement opt-out and Temporary Chat has a different history/memory/training boundary; for Claude, current consumer privacy settings and incognito chats provide separate model-improvement/history controls. Link the canonical service owners for exact current policy rather than copying mutable retention text into the rendered scenario.
- A privacy setting changes one provider's processing behavior; it does not automatically make a consumer account appropriate for employer-confidential, regulated, credential, financial-account, or other high-sensitivity data.

## Paid Upgrade Route

- Keep the user on free access when it reliably covers ordinary personal workloads. A paid subscription is justified only when recurring rate/tool limits, superior paid-only capabilities, deadline/availability needs, or correction-time savings produce more value than the subscription cost.
- Prefer **one** paid assistant subscription over accumulating multiple subscriptions by default. Add another paid service only after a repeated task-specific advantage has been measured on the user's real workload.
- Treat current plan prices and feature bundles as mutable. Recheck the canonical service owner at payment time rather than preserving `$20/month` or any current plan name as timeless scenario truth.
- For bursty needs such as tax preparation support, a large personal project, travel planning, or a temporary document-processing period, consider bounded month-to-month use instead of assuming permanent subscription value.
- Do not recommend an API merely because per-token pricing appears cheap. A managed consumer assistant often has lower total cost for an ordinary user once setup, key management, UI, file handling, web tools, memory/project behavior, and troubleshooting are included.

## Direct API and Automation Boundary

- Present direct API access only when the user has a concrete automation, batch, integration, or custom-interface need and enough technical skill to manage credentials, spend limits, error handling, and provider-specific behavior.
- Explain that an API and the provider's consumer assistant subscription are separate products; API billing does not automatically reproduce the managed application's memory, projects, research UI, voice, file flows, or device integrations.
- If the user's goal becomes persistent personal automation with tools and side effects rather than conversational help, require explicit approval boundaries, least privilege, deterministic checks, and recovery behavior. A capable model is not itself a safe automation architecture.
- If a routing intermediary is used for model breadth or cost, evaluate both the intermediary and downstream provider chain under the shared data-boundary rule; an intermediary is not a privacy abstraction by default.

## Local and Offline Route

- Present local inference as an optional route when **privacy, offline availability, provider independence, experimentation, or stable repeated local workloads** materially justify setup and performance trade-offs. Do not present local inference as the default upgrade from a consumer subscription.
- Keep `Phi-4 Mini Instruct` as a compact text-oriented candidate for lightweight offline writing/question/help experiments where its capabilities are sufficient. Keep `Qwen3 8B` as a heavier text/reasoning candidate when usable memory and latency allow it. Link their exact canonical Model Reference identities rather than duplicating complete model cards here.
- Use `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` as current compact multimodal candidates when private local image/document/audio understanding is the deciding workload. The official Gemma 4 family describes E2B and E4B as on-device/mobile/laptop-oriented dense models with text/image/audio input and 128K model context; E2B and E4B differ materially in effective/total parameter scale and must be evaluated separately.
- Treat E2B as the lighter initial multimodal experiment and E4B as a larger alternative only after exact runtime/artifact/memory performance is validated on the target device. Do not claim E4B is automatically the better accepted-result choice solely because it has more parameters.
- Official low-precision/QAT artifacts can reduce storage/weight memory, but a quantized file size is not a complete RAM/VRAM requirement. Include runtime overhead, context/KV allocation, multimodal projection/encoders, OS/application reserve, backend buffers, and any accelerator fallback in fit assessment.
- Remove the old blanket `16–32 GB RAM` planning statement. Instead require **usable memory and measured runtime behavior on the exact device**. A model that loads successfully may still be too slow, thermally constrained, context-limited, or low-quality for the user's actual workflow.
- For CPU-only local inference, require a small acceptance test covering first-token delay, sustained generation rate, device heat/noise, usable context, modality path if applicable, and correction burden. Interactive usability is part of fit.
- If local operation becomes the dominant requirement rather than a fallback, route the reader to the approved `privacy-first-or-offline-user` scenario when materialized and/or the exact hardware-selection subtree; do not grow this page into a local-inference manual.

## Personal Files, Photos, and Connected Data

- Before uploading a personal file, photo, screenshot, message export, calendar item, or connected-account data, classify whether the material is ordinary personal content or meaningfully sensitive.
- Prefer minimizing the submitted scope: crop screenshots, redact identifiers, remove irrelevant pages/columns, or summarize locally before upload when the full source is unnecessary.
- Treat connected-app authorization as data access, not merely a convenience toggle. Review which service/account is connected, what data can be retrieved, whether activity must be enabled, and how to revoke access.
- Do not recommend putting passwords, recovery codes, private keys, full payment-card details, identity-document secrets, or other authentication material into a general consumer assistant. Use dedicated credential/password-management systems instead.
- For highly sensitive personal documents, local/offline processing or a specifically appropriate contracted/private route can be preferable, but local execution still requires endpoint security, backups, access control, and safe deletion; “local” is not synonymous with “secure.”

## Reliability and High-Stakes Boundary

- For ordinary low-stakes drafting, brainstorming, explanations, and planning, conversational verification proportional to the consequence is sufficient.
- For purchases, travel bookings, deadlines, taxes, benefits, contracts, health, legal questions, financial decisions, safety-critical instructions, or other high-consequence actions, require authoritative source verification before acting.
- Use the assistant to organize options, generate questions, summarize supplied material, or identify what to verify; do not present model output as a substitute for a qualified professional, official rule, medical diagnosis, legal advice, financial authorization, or deterministic calculation where the consequence warrants stronger controls.
- For calculations, structured personal data, and forms, validate important values independently and preserve the original source. A fluent explanation does not prove extraction or arithmetic correctness.
- When the assistant uses web/search tools, inspect the cited/linked source and whether it actually supports the claim; generated or mismatched citations do not become reliable merely because the service exposes a search feature.

## Cost and Accepted-Result Method

- Compare managed free, one managed paid subscription, direct API, and local/offline routes only when each is materially plausible for the user's workload.
- Calculate total cost per accepted result: subscription/API spend, retries, correction/source-verification time, setup/maintenance, storage/electricity, device wear/thermal inconvenience, and the value of cross-device/tool integration.
- For ordinary low-volume personal use, operational simplicity can dominate nominal model cost. Self-hosting is not automatically cheaper, private enough, or easier to maintain.
- A second service or local model is justified by a distinct recurring workload, resilience/privacy requirement, or measurable accepted-result advantage—not by collecting models/providers as an end in itself.

## Escalation Triggers

- Escalate from free to a paid managed plan when rate/tool limits or quality/reliability constraints are recurrent rather than occasional.
- Add a second managed assistant only when it repeatedly wins a material workload (for example a required ecosystem integration or specific document/media workflow) enough to offset switching and subscription cost.
- Escalate to direct API when repeatable automation/batch integration is the actual requirement and the user can operate it safely.
- Escalate to local/offline when sensitive personal content, disconnected operation, provider independence, or repeated local workloads outweigh setup/latency/quality penalties.
- Escalate away from local when exact-device tests fail the user's latency, context, modality, thermal, or accepted-quality requirements even if the model fits in memory.
- Escalate to another user-scenario owner when the dominant decision changes to persistent personal knowledge management, accessibility, household/family orchestration, travel/multilingual work, privacy-first offline use, or personal data analysis.
- Escalate to professional/organization scenarios immediately when employer/client data or policy becomes material; do not stretch a consumer account into an unapproved work route.

## Canonical Links

- Link named managed assistants to canonical service owners such as `catalog/services/assistant-workspaces/chatgpt`, `catalog/services/assistant-workspaces/claude`, and `catalog/services/assistant-workspaces/gemini`.
- Link named local models to `catalog/models/microsoft/phi/phi-4/models/phi-4-mini-instruct`, `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b`, `catalog/models/google/gemma/gemma-4/models/e2b-instruct`, and `catalog/models/google/gemma/gemma-4/models/e4b-instruct`.
- Link sibling hardware selection only when the exact device materially constrains the route. Do not duplicate model/service profiles, product policy pages, hardware-fit matrices, or runtime installation instructions here.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current first-party consumer-product/privacy documentation, current official Gemma 4 model documentation, and canonical AI Lab service/model owners.
- Default/free model names, product quotas, plan prices, connected-app availability, activity/privacy controls, retention behavior, and local runtime/artifact support are mutable. Recheck them before rendering a current recommendation.
- Current provider documentation establishes product/model capabilities and data-control behavior, not independent AI Lab quality/performance evidence. Do not infer universal assistant superiority or local-device performance from provider claims.

## Validation

- The scenario remains individual personal/home use and does not reintroduce the old combined `home or office` ambiguity.
- One managed assistant remains the default low-administration route when hosted processing fits the data boundary.
- Consumer ecosystem integration is treated as both convenience and data-access/privacy trade-off.
- Paid subscription, API, and local inference remain separate escalation choices rather than a forced maturity ladder.
- Local candidates have exact canonical identities and no RAM/file-size/load-success shortcut is presented as practical-fit proof.
- High-stakes personal decisions visibly require stronger source/professional/deterministic verification.
- Consumer privacy controls are not presented as approval for confidential work or regulated data.
- Mutable current claims carry the 2026-08-23 evidence boundary.
