# Documentation Requirements

## Scenario Fit

- Present this scenario for a household in which AI assists recurring shared work such as planning, shopping, recipes, calendars, reminders, school/home documents, family travel preparation, household questions, photos/files, and voice-driven coordination.
- Keep the decision centered on the **household context**, not merely one person's general assistant use. Multiple people, shared devices, shared artifacts, age differences, permissions, and family privacy must materially affect the model/service route.
- Distinguish this scenario from `everyday-home-user/`: that scenario assumes one individual and primarily personal state; this scenario must explicitly handle identity separation and shared household state.
- Distinguish it from `personal-knowledge-base-user/`: durable document retrieval can be one household workload, but that scenario becomes the owner when the main problem is building/querying a persistent corpus rather than coordinating a household.
- Distinguish it from `home-lab-owner/`: an always-on local household assistant may use home-lab infrastructure, but the home-lab scenario owns server operation, remote access, backups, monitoring, and infrastructure maintenance when those become first-order constraints.
- Distinguish it from `accessibility-first-user/`: voice and reduced typing can be useful household modalities, but accessibility becomes the owner when assistive-technology compatibility or disability-related access determines the route.

## Separate Household Workloads

- Classify the recurring household work before choosing one assistant or model:
  - shared calendars, appointments, reminders, and household task lists;
  - shopping/grocery planning and recurring lists;
  - recipes, meal planning, pantry-based ideas, and substitutions;
  - school letters, schedules, forms, notices, and family documents;
  - household travel/event planning;
  - explanation, drafting, summarization, and research for adults;
  - age-appropriate learning/help for children or teens;
  - photos, screenshots, receipts, labels, appliance instructions, and other multimodal inputs;
  - shared household reference information such as routines, maintenance notes, warranties, and instructions;
  - optional smart-home or other tool actions.
- Do not force every workload into one general LLM. Calendar/task systems, deterministic reminders, shared lists, document stores, parental controls, a managed assistant, and a local model can each own a different part of the solution.
- Treat the model as an interface/reasoning component rather than the sole system of record for dates, tasks, shopping lists, medical instructions, passwords, or other household state that must remain reliably shared.

## Default Managed Route

- Use a current managed multimodal assistant as the default low-administration starting route for adult household members when hosted processing fits the family's data boundary.
- Current canonical examples include ChatGPT and Gemini. Evaluate them on the household's real devices, languages, voice/image/file needs, connected-service fit, family age requirements, correction burden, and data controls rather than ranking providers globally.
- Prefer **individual accounts for individual people** instead of one shared adult login. Current OpenAI policy states that an OpenAI account is intended for the individual who created it and should not be made available to other people.
- Keep private conversation history, memory, and personal connected data separated by account unless a product explicitly provides a supported shared surface. Do not infer a shared family memory from account linking, account switching, or use on the same device.
- Use a shared calendar/list/document system as the household source of truth when several people must see or edit the same state. The assistant may read, summarize, or update that state through supported connections, but the underlying shared service remains authoritative.

## Household Ecosystem and Connected Apps

- Treat ecosystem integration as a first-order route dimension because household value often comes from reducing manual transfers between conversation, calendars, tasks, notes, documents, and shopping/planning tools.
- Gemini is a current relevant example for households already centered on Google services: its Google Workspace connection can work with Gmail, Drive/Docs, Calendar, Keep, and Tasks, including supported create/edit actions for calendar events, notes/lists, tasks, and reminders.
- Current Gemini connected-app availability and behavior depend on account, platform, region, app support, and settings such as `Keep Activity`. Recheck those dependencies before presenting an integration as available.
- ChatGPT can connect to Google services such as Gmail, Calendar, and Drive on supported surfaces/accounts. Treat exact actions, indexing/sync behavior, scopes, account eligibility, and retention/data-control behavior as mutable service facts owned by the canonical ChatGPT service page.
- Before connecting a family account, inspect what data the assistant can access, what actions it can perform, whether data is indexed/synced, what account owns the connection, and how access is revoked.
- Do not enable broad connected-app access merely because the integration exists. Connect only the household data sources required by the accepted workloads.

## Children, Teens, and Account Boundaries

- Treat children and teens as a separate product/safety boundary rather than additional users of an adult's account.
- Current ChatGPT guidance states that ChatGPT is not intended for children under 13 and requires parental consent for users from 13 to 18; for educational interaction with children under 13, the direct interaction must be conducted by an adult.
- Current ChatGPT parental controls allow a parent/guardian and teen to link separate accounts and manage selected settings. The linked parent does **not** receive access to the teen's conversations; do not misrepresent parental controls as conversation monitoring or shared family history.
- Current ChatGPT teen protections, parental-control options, safety notifications, eligible features, and rollout state are mutable; recheck them for the exact account and region before recommending a child/teen route.
- Current Gemini supports parent-managed access through Family Link for eligible supervised child accounts in supported regions. Availability is regional and staged, and some features have age restrictions; do not assume that a supervised Gemini route is available everywhere.
- For a child below a product's supported age or outside a supervised-product region, use adult-mediated interaction rather than bypassing account/age requirements.
- Do not treat an AI safety filter or parental-control setting as a substitute for age-appropriate supervision, family rules, or authoritative educational/health/safety sources.

## Shared Device and Voice Identity

- A kitchen tablet, family computer, smart display, speaker, or other shared surface creates an identity problem: the assistant must not silently expose one person's conversation history, connected mail/calendar, photos, or personalized memory to another household member.
- Verify which account/profile is active before showing personal results or performing account-specific actions. Prefer explicit account/profile selection when the device cannot reliably distinguish users.
- Treat voice recognition as convenience evidence, not authorization evidence. A voice command alone should not authorize purchases, security changes, deletion of data, disclosure of sensitive personal information, or other high-impact actions.
- If a device supports lock-screen or hands-free assistant access, inspect what content/actions remain available while locked and disable unnecessary access for sensitive household data.
- Do not store secrets, recovery codes, payment credentials, alarm/security codes, or other authentication material in conversational memory merely to make shared voice access convenient.

## Shared Household State

- Keep household state in explicit shared artifacts where possible: shared calendars, lists, notes, documents, task systems, or purpose-built home systems.
- Use assistant memory/personalization for low-risk individual preferences only when the user understands the scope and can review/delete it. Do not rely on implicit memory as the only copy of appointments, medication schedules, school deadlines, maintenance intervals, or other important facts.
- When the household wants durable AI-grounded reference over manuals, warranties, recipes, household notes, school documents, or archives, evaluate a bounded shared knowledge route and route deeper retrieval design to the applicable knowledge-base scenario/content.
- Separate factual source data from generated summaries. Preserve the original document, calendar event, note, receipt, instruction manual, or official message so a generated interpretation can be checked later.
- Define an owner for shared data. Avoid a configuration where every family member can silently overwrite authoritative household instructions through conversational prompts.

## Household Planning and Current Information

- For groceries, recipes, chores, packing lists, event ideas, and low-stakes planning, optimize for convenience and accepted-result quality rather than maximum model capability.
- For opening hours, prices, product availability, transport, school schedules, local rules, weather, appointments, and other changing facts, require a current source rather than model memory.
- For meal planning, ask for relevant constraints such as allergies, dietary restrictions, age, available ingredients, equipment, time, and budget. Treat generated substitutions as suggestions until safety-sensitive constraints are verified.
- For family travel or multilingual needs that become recurrent and dominant, continue into `traveler-or-multilingual-user/` rather than expanding this page into a travel guide.

## Documents, Photos, and Family Privacy

- Family data can combine information about multiple people in one artifact: names, addresses, school details, children, health information, schedules, locations, financial details, photos, and relationship information.
- Minimize uploads: crop screenshots, redact unrelated people/identifiers, remove unnecessary pages, and submit only the fields needed for the task.
- Treat school reports, medical documents, identity documents, insurance, tax/finance files, legal documents, custody information, location history, family photos, and private messages as higher-sensitivity content requiring a deliberate data boundary.
- A household member's presence in a photo, message, or document does not automatically mean another household member should upload it to an external assistant. Respect the privacy of every person represented in shared data.
- Do not upload passwords, private keys, recovery codes, full payment-card details, or one-time authentication codes to a general assistant.

## Smart-Home and Side-Effecting Actions

- Keep conversational advice separate from actions that change the physical/digital household environment.
- For low-risk actions such as creating a reminder or adding a grocery-list item, supported tool execution can be useful when the active account and destination are clear.
- Require stronger confirmation and least-privilege tool access for actions affecting locks, alarms, cameras, heating/cooling safety limits, purchases, account permissions, deletion, vehicles, appliances with safety consequences, or other high-impact state.
- Do not let a general household agent infer authorization from conversational context alone when multiple household members can reach the same interface.
- Preserve an audit/review path for recurring automations. If autonomous tool use becomes the primary goal, route to the applicable agents/automation decision guidance instead of treating model capability as the complete solution.

## Local and Offline Household Route

- Present local inference as an alternative when family privacy, offline availability, provider independence, or reuse of owned hardware materially outweigh managed-service convenience.
- For a compact local text helper, `Phi-4 Mini Instruct` remains a current candidate for memory/compute-constrained multilingual text workloads; validate the exact household languages and tasks rather than assuming model-card language support proves accepted quality.
- For local multimodal household tasks such as reading appliance labels/manual screenshots, interpreting images, or processing audio where exact runtime support exists, evaluate `Gemma 4 E2B Instruct` first as a compact candidate and `Gemma 4 E4B Instruct` as a larger alternative. The current official Gemma 4 model card positions E2B/E4B for mobile/laptop/on-device deployment and supports text/image/audio inputs with 128K context.
- Do not infer practical fit from parameter count, quantized file size, or successful loading. Measure usable memory, runtime/backend support, latency, context/KV headroom, sustained thermals/power, modality path, and accepted-result quality on the exact device.
- A local model does not solve household identity/permission problems by itself. A shared local endpoint still needs user separation, access control, storage/backup policy, and protection from one user exposing another user's private data.
- If operating a persistent local server becomes the dominant burden, continue into `home-lab-owner/` and sibling hardware selection rather than duplicating server guidance here.

## High-Stakes Family Boundary

- Use AI to organize questions, summarize supplied material, prepare checklists, or explain terminology, but not as the sole authority for medication doses, allergy safety, poisoning, emergency response, child health, legal/custody issues, tax/benefit eligibility, financial authorization, or other high-consequence household decisions.
- Verify medical instructions against the prescribing clinician/pharmacist/official label and emergency guidance against authoritative services. A family assistant must not replace professional or emergency channels.
- Verify school/administrative deadlines, payments, forms, travel documents, and official requirements against the original institution or document before acting.
- For calculations involving bills, budgets, doses, dates, or quantities, preserve source values and use deterministic calculation/validation where an error would matter.

## Cost and Accepted Household Outcome

- Compare routes by **cost per accepted household outcome**, including subscriptions for multiple eligible users, API usage, connected-service costs, local hardware/storage/power, setup/admin time, correction effort, and the value of shared-state integration.
- Do not buy several assistant subscriptions merely so every family member has the same provider. Start with free/eligible managed access where adequate and pay only when recurring limits or capabilities justify it for the people who need them.
- A single adult paid account is not a substitute for supported individual accounts when other household members need independent use.
- Local hosting is justified by privacy/offline/control or repeated shared workloads, not by assuming it is automatically cheaper than managed consumer services once maintenance and endpoint security are included.

## Escalation Triggers

- Move from an individual `everyday-home-user` route to this scenario when multiple household members or shared state materially affect account, privacy, or workflow design.
- Add connected calendar/task/note/document access when repeated manual transfer is the bottleneck and the family accepts the resulting data-access boundary.
- Move from conversational memory to an explicit shared system of record when dates, tasks, lists, or instructions must be dependable across people and devices.
- Move to local/offline processing when sensitive family data or disconnected use is recurrent and the exact hardware/runtime route passes acceptance tests.
- Move toward `personal-knowledge-base-user/` when durable household document retrieval becomes the dominant workload.
- Move toward `home-lab-owner/` when operating the local service becomes a persistent infrastructure responsibility.
- Move toward `traveler-or-multilingual-user/` or `accessibility-first-user/` when those dimensions become the dominant decision constraint.
- Move to a stronger professional/official/human route immediately for high-stakes medical, legal, financial, educational, or safety decisions that exceed ordinary household assistance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` whenever the household chooses a local model and exact owned hardware constrains fit.
- Use `../../../hardware/sub/computers/` for a shared household PC/laptop route, `../../../hardware/sub/single-board/` when an SBC hosts a small always-on service, and `../../../hardware/sub/servers/` when a dedicated inference host is actually present.
- Do not recommend buying hardware from this scenario. The hardware journey owns fit for a fixed target; hardware purchasing remains outside this model-selection route.

## Canonical Links

- Link managed assistant examples to `catalog/services/assistant-workspaces/chatgpt` and `catalog/services/assistant-workspaces/gemini` when named.
- Link local text candidates to `catalog/models/microsoft/phi/phi-4/models/phi-4-mini-instruct` when named.
- Link local multimodal candidates to `catalog/models/google/gemma/gemma-4/models/e2b-instruct` and `catalog/models/google/gemma/gemma-4/models/e4b-instruct` when named.
- Link sibling scenario/hardware owners rather than reproducing their detailed model, infrastructure, or device-fit guidance.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current OpenAI account-sharing, age, teen, and parental-control documentation; current Google Gemini supervised-account/Family Link and Connected Apps documentation; current official Gemma 4 and Phi-4 Mini model evidence; and canonical AI Lab model/service owners.
- Current evidence confirms that ChatGPT account sharing is not the supported household identity model, teen parental controls link separate accounts without exposing teen conversations, Gemini child/supervised availability is region- and feature-dependent, and Gemini connected apps can currently integrate supported Calendar/Tasks/Keep/Workspace household workflows.
- Product age rules, supervised-account availability, parental-control features, connected-app permissions/actions, account plans, model aliases, pricing, retention/data controls, and regional availability are mutable; recheck them before rendering current advice.
- Provider capability/model-card claims establish eligibility and product behavior, not independent accepted-result quality or exact-device performance. Household acceptance tests remain required for important workloads.

## Validation

- The scenario is distinct from one-person everyday use because it explicitly models multiple people, shared state, children/teens, shared devices, and household permissions.
- One shared adult account is not presented as the solution for multiple family members.
- Child/teen use follows supported age/account/supervision boundaries rather than bypassing them.
- Household calendars, tasks, lists, and important instructions retain an explicit source of truth outside conversational memory.
- Connected-app convenience is paired with account ownership, permission, data-access, and revocation checks.
- Voice identity is not treated as sufficient authorization for high-impact actions.
- Local inference preserves user-separation and endpoint-security requirements and does not become `local = private = safe` shorthand.
- High-stakes medical, legal, financial, educational, and safety decisions require authoritative/professional verification.
- Exact local-model identities are canonical and practical fit is measured on the real device.
- Mutable product and policy claims carry the 2026-08-24 evidence boundary.
