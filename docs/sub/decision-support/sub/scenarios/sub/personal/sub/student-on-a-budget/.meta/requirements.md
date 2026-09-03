# Documentation Requirements

## Scenario Fit

- Present this scenario for a student, learner, or early-career self-learner whose primary constraints are a minimal discretionary AI budget, ordinary/basic personal hardware, mixed study/writing/coding/file tasks, and limited desire or ability to administer AI infrastructure.
- Distinguish this scenario from a generic home user: academic integrity, source verification, coursework policy, institution-provided access, and the value of explanation/learning over answer production materially change the route.
- Do not assume the reader owns a discrete GPU, Apple Silicon system, or other accelerator. When exact owned hardware becomes material, continue into sibling `../../../hardware/` selection rather than guessing local fit here.

## Starting Decision Order

- First check whether the school/university already provides an approved AI assistant, API, lab environment, or institution-managed account at no additional personal cost. Prefer that route when it satisfies the workload and its data/academic-use policy is clear; do not assume consumer-plan privacy or features apply to institution-managed accounts.
- If no adequate institution-provided route exists, start with a short **free hosted evaluation**, not permanent service rotation. Compare two or three materially different assistants on the student's real tasks, then converge on one primary assistant to reduce context fragmentation, repeated setup, and switching cost.
- Current hosted examples verified on **2026-08-23** may include canonical ChatGPT, Claude, and Gemini assistant-workspace services. Treat exact free-tier models, quotas, tools, and regional availability as mutable service facts rather than durable scenario facts.
- As of the verification date, ChatGPT Free exposes broad web/file/image/data-analysis capabilities and a current default model, while Claude Free includes current Sonnet access plus web, code/file creation, and extended-thinking capabilities. Gemini provides consumer access for writing, planning, learning, image/file-oriented work, and Google-service integration. Do not turn these current product details into a permanent rank order.
- Evaluate the candidates with a small representative workload set: explain a difficult concept, improve a draft without replacing the student's authorship, solve and explain a coding/debugging task, summarize a supplied document, and answer one question that requires sources/current information. Record which assistant produces the highest accepted-result value for the student's actual courses.

## Paid Upgrade Route

- Recommend **one paid assistant subscription** only after the selected free route has become a recurring daily tool and free-tier limits, unavailable tools, or repeated quality/retry costs are materially harming study throughput.
- Use current subscription price as a mutable input. On **2026-08-23**, canonical ChatGPT Plus and Claude Pro are both approximately the common `$20/month` monthly-price class (Claude also advertises a lower effective annual-billing rate); recheck before rendering or recommending payment. Google AI plan names, prices, student promotions, quotas, and storage bundles vary by region/account and must be checked at decision time.
- Treat temporary student promotions as opportunistic savings, not as the scenario's durable architecture. Verify eligibility, region, renewal price, cancellation terms, and what happens when the promotion ends.
- Compare the subscription against the student's *accepted-result* workload: avoided retries, better file/research tools, usable limits during deadlines, and time saved. Do not justify a subscription merely because the paid model is nominally stronger.
- If one month contains a deadline-heavy burst but ordinary months do not, prefer month-to-month activation/cancellation or another bounded route over assuming a permanent subscription.

## Direct API Route

- For a technically comfortable student, present direct pay-as-you-go API use as an optional route when occasional scripted or high-volume tasks do not justify a full assistant subscription.
- Explain that API billing and assistant subscriptions are separate products; API access does not automatically reproduce the managed assistant's projects, memory, research UI, file workflows, or other application features.
- Require the reader to estimate monthly token/tool/storage spend and implementation effort before calling the API route cheaper. A low request price can lose to setup/debugging time for a nontechnical or low-volume student.
- Prefer direct provider APIs over an intermediary when privacy, provenance, or support-chain simplicity matters. If a routing intermediary is used for price/model breadth, evaluate both intermediary and downstream provider under the shared provider-chain rule.

## Local and Offline Route

- Present local inference as a **privacy/offline/learning experiment or provider-independence route**, not the default way to save money. On an ordinary laptop, setup effort, CPU latency, limited context, thermal throttling, and lower accepted-result quality can cost more time than a free hosted assistant.
- Keep `Phi-4 Mini Instruct` as the lightest current text-oriented candidate in this scenario. Its official model card identifies a 3.8B-parameter dense text model, 128K maximum context, MIT license, and multilingual coverage including Ukrainian. Treat 128K as model capability rather than a promise that a basic laptop can run that context economically.
- Keep `Qwen3 8B` as the heavier text/reasoning candidate when the laptop has enough usable memory and the student accepts slower CPU inference. Its official card identifies 8.2B parameters, 32K native context with validated YaRN extension to 131K, Apache-2.0 licensing, thinking/non-thinking modes, and broad multilingual support. Do not present it as the low-memory default merely because quantized artifacts exist.
- Keep `Gemma 4 E2B Instruct` as the compact multimodal candidate when local image/document/audio understanding materially matters. The current official Gemma 4 model card describes E2B as a 2.3B-effective / roughly 5.1B-with-embeddings multimodal model family member targeted at mobile/laptop-class deployment, with text/image input and audio support on E2B plus a context window up to the Gemma 4 family limit. Link the exact canonical Model Reference identity rather than abbreviating it to an ambiguous `Gemma E2B` label.
- Where a practical `llama.cpp` demonstration is needed, note that Google publishes an official QAT Q4_0 GGUF route for Gemma 4 E2B Instruct. Treat the model GGUF plus multimodal projection artifact, runtime version, supported modalities, and context as one tested bundle; file size alone is not a RAM or performance guarantee.
- Do not use a blanket `16–32 GB RAM` requirement. Instead classify local fit from **usable** system memory after OS/application reserve, exact quantization/artifact, KV/context allocation, runtime overhead, modality projection, and whether GPU/NPU acceleration is actually available. Eight, sixteen, or thirty-two gigabytes may lead to very different practical outcomes on different platforms.
- On CPU-only machines, explicitly warn that a model fitting into memory may still be too slow for interactive study. Require a small local acceptance test measuring first-token delay, sustained generation speed, thermals, usable context, and answer quality on the student's own tasks before recommending local use beyond experimentation.
- Local inference does not make third-party documents legally or ethically unrestricted. Copyright, course policy, licensed materials, personal data, and institutional rules still apply even when prompts never leave the device.

## Study and Academic-Integrity Boundary

- Frame the assistant as a tutor, reviewer, brainstorming partner, debugger, and research aid rather than an automatic assignment author.
- Require the student to follow the course/institution's AI-use policy. Where AI assistance must be disclosed, the scenario should explicitly recommend keeping enough provenance to disclose what was used.
- For factual/research work, require source inspection rather than trusting generated citations. Verify that cited sources exist, support the stated claim, and are acceptable under the course's citation rules.
- For mathematics, code, data analysis, and other verifiable outputs, require independent checking: recompute important results, run tests, inspect generated code, and compare against primary course material or authoritative sources.
- Do not recommend uploading unpublished research, another person's work, restricted exam material, institution-confidential data, employer data, or sensitive personal information to a consumer assistant merely because it is free.

## Data Boundary and Consumer Controls

- Apply the shared scenario data-boundary rules before product preference. Public/non-sensitive coursework can use the best cost/quality route; institution-confidential or regulated data needs an explicitly approved route.
- Consumer privacy controls reduce some risks but do not convert a personal account into an institution-approved confidential-data environment. Link canonical service owners for current training/retention/activity controls rather than duplicating mutable policies here.
- If the student must use a consumer service for personal non-confidential material, encourage review of current training/activity controls and temporary-chat options where offered; recheck service-specific retention and human-review boundaries before giving privacy-sensitive advice.

## Cost and Evaluation Method

- Compare four distinct route classes where relevant: institution-provided/approved access, free consumer assistant, one paid subscription or bounded API spend, and local/offline inference.
- Calculate total cost per accepted result, not zero-dollar request cost. Include subscription/API spend, retries, manual correction, source verification, setup/maintenance time, local electricity/thermal cost, and the opportunity cost of waiting for slow inference during study sessions.
- A free route wins when it meets quality, quota, and policy needs with tolerable correction time. A paid route wins when its additional usable capability or availability reliably saves more time/value than it costs. A local route wins when offline/privacy/control benefits outweigh setup and performance penalties.

## Escalation Triggers

- Escalate from free to paid hosted access when recurring rate limits, unavailable tools, deadline-time availability, or repeated quality corrections materially block real coursework.
- Escalate from one assistant to a second specialized assistant only when the second route demonstrates a distinct accepted-result advantage on a recurring workload; do not maintain multiple paid subscriptions by default.
- Escalate from consumer assistant to direct API when automation/batch integration is the actual need and the student can manage keys, spend controls, and implementation safely.
- Escalate from hosted to local/offline when privacy, disconnected operation, reproducibility, or hands-on model learning becomes a first-class requirement rather than an abstract preference.
- Escalate away from local inference when the chosen model cannot meet required latency, modality, context, or quality on the actual laptop; fitting into RAM is not sufficient evidence.
- When a fixed GPU, Apple Silicon machine, NPU laptop, or other accelerator materially changes the choice, continue into the matching hardware-constrained selection route instead of expanding this scenario into a hardware guide.

## Canonical Links

- Link hosted examples to canonical service owners: `catalog/services/assistant-workspaces/chatgpt`, `catalog/services/assistant-workspaces/claude`, and `catalog/services/assistant-workspaces/gemini` when they are named.
- Link local candidates to canonical Model Reference identities, including `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct`, `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b`, and `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct`.
- Do not duplicate the complete model/service profiles, mutable pricing tables, or hardware-fit matrices in this scenario.

## Evidence and Freshness

- This scenario's route logic and named current examples were re-evaluated on **2026-08-23** using current first-party product/model sources plus canonical AI Lab owners.
- Free-tier model names, quotas, assistant features, subscription/API prices, student promotions, region eligibility, consumer data controls, and runtime/artifact support remain mutable; recheck them before rendering a current recommendation.
- Provider model cards establish official capabilities/limits, not independent AI Lab quality or performance measurements. Do not infer laptop speed, accepted-result quality, or superiority from parameter count, context window, or provider benchmark claims alone.

## Validation

- The scenario remains learner/budget-specific and does not collapse into generic consumer guidance.
- Institution-provided access is evaluated before personal spending.
- Free hosted evaluation converges toward a primary assistant instead of recommending permanent multi-service rotation as a virtue by itself.
- A paid subscription, API, and local inference are separate escalation routes with explicit triggers and trade-offs.
- Academic integrity, source verification, and data-boundary requirements are visible in the final page.
- Exact local model identities and their materially different text/multimodal/resource roles are preserved.
- No RAM number, model size, context length, quantization file size, or successful load is presented as a guarantee of practical local fit.
- Mutable current-service claims carry the 2026-08-23 verification boundary and canonical owner links.
