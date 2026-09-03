# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person content/creative team repeatedly producing text, image, audio, video, scripts, campaign assets, social content, editorial material, or mixed-media deliverables under shared brand, rights, review, and publication responsibilities.
- Keep the scenario team-scoped. One creator belongs in `professionals/creative-professional/`; campaign/growth measurement belongs in `marketing-and-growth-team/`; organization-wide DAM, brand governance, enterprise creative operations, or central AI platform belongs in organization routes when those dominate.
- Distinguish this scenario from `small-business-team/`: here **production volume, shared brand/source assets, modality-specific QC, approval/versioning, provenance, rights, and publication workflow** determine the route.
- Keep exact modality/model candidate selection in `decision-guides/media-creation/`. This page owns team workflow and acceptance, not a permanent image/video/audio model ranking.

## Start From the Production Pipeline

- Map the actual team stages before selecting AI tools: brief → research/source gathering → ideation → draft/generation → edit/composite → factual/brand/rights/QC review → approval → localization/versioning → publication/delivery → archive/reuse.
- Define which stages AI may accelerate and which remain deterministic or human-owned.
- Preserve source assets, editable project files, approved outputs, usage rights, and final publication versions outside chat/generation history.
- Treat one-off ideation and production-at-scale as different operating modes. The latter requires stronger reproducibility, asset tracking, review, and cost controls.
- Avoid adding automated publication merely because generation becomes fast; generation permission and publication permission remain separate.

## Shared Brand and Asset Sources

- Identify canonical brand guidelines, logos, palettes, typography, product imagery, templates, voice/tone rules, terminology, disclaimers, licensed stock, reference libraries, and client-specific assets.
- Keep these assets in team-owned systems with clear ownership/versioning rather than individual assistant memories.
- Use AI references/style controls only when the team has the rights to provide those inputs and the selected product/model supports the required control.
- Evaluate consistency across a set of outputs, channels, languages, formats, and revisions—not one attractive sample.
- Do not allow generated variants to silently redefine brand colors, logo geometry, product design, character identity, legal copy, or approved terminology.

## Default Integrated Creative Workspace Route

- Prefer an organization-approved integrated creative suite when editability, shared assets, review/handoff, identity management, provenance, and production-tool integration materially reduce team friction.
- Adobe Creative Cloud/Firefly is a current example of a production-integrated route. Adobe documents commercial-use positioning for qualifying Firefly outputs, Content Credentials/provenance support, and offer/workflow-specific IP-indemnification opportunities for eligible customers. Treat every commercial/indemnification claim as exact-plan/feature/contract specific rather than universal.
- Evaluate integrated tools on real team assignments and revision loops, not only first-generation quality.
- Include import/export fidelity, layered/editable workflow, typography, asset-library integration, version control, review comments, batch/localization support, and downstream delivery in acceptance.
- Do not assume an integrated suite must be the highest-quality generator; compare specialist models when the accepted-result advantage is material.

## Specialist Hosted Media Route

- Add a specialist image/video/audio/speech model/service when the integrated route repeatedly fails an important creative requirement and the additional provider/data/rights boundary is acceptable.
- Consume exact candidates and modality-specific criteria from `decision-guides/media-creation/` rather than copying dated model rankings into this scenario.
- Evaluate exact service/model/version and surface because consumer app, enterprise app, and API can differ in resolution, controls, moderation, provenance, rate limits, rights terms, and editing features.
- Include asset upload/download/reformatting, review, rights checks, and re-entry into the production suite in total workflow cost.
- Maintain a fallback/replacement strategy because hosted model availability, aliases, quotas, pricing, and features can change quickly.

## Provenance and Content Credentials

- Preserve available provenance signals when they materially support client, platform, editorial, regulatory, or internal transparency requirements.
- Current OpenAI-generated supported images use C2PA Content Credentials plus SynthID, and supported OpenAI-generated audio uses SynthID; OpenAI explicitly states that provenance signals do not establish factual accuracy, ownership, or correct context.
- Current Adobe Firefly workflows use Content Credentials on qualifying generated/exported content; current Google generative-media surfaces use SynthID on supported media. Treat coverage as product/export/version specific.
- Downstream editing, transcoding, screenshots, platform uploads, or metadata stripping can alter or remove provenance information. Absence of a signal is not proof that content is human-created.
- Store the model/service and material generative steps in the team's production record when disclosure/audit requires more than embedded metadata.

## Rights, Licenses, and Input Authority

- Verify rights for every input: photographs, stock, logos, fonts, product assets, music, video, scripts, voices, likenesses, characters, reference art, client materials, and training/customization datasets.
- Technical upload capability does not prove permission to transform or publish the asset.
- Review provider terms for commercial output use, input rights, third-party content, model-specific/open-weight licenses, indemnification where applicable, beta/preview exclusions, and prohibited uses.
- Do not promise uniqueness or non-infringement from generated output; provider terms and provenance signals cannot make that guarantee.
- Preserve license/source evidence for third-party assets incorporated into final deliverables.
- Escalate material copyright/trademark/publicity/contract questions to qualified legal/client review rather than model judgment.

## Likeness, Voice, and Identity Media

- Treat real-person face, likeness, voice, performance, or identity-conditioned generation as a separate consent/rights boundary.
- Require explicit authorization and production records for talent/voice/likeness use where appropriate.
- Do not infer consent from public availability of photos/audio/video.
- Keep identity consistency, pronunciation, lip sync, and likeness accuracy in the modality-specific QC plan.
- Do not allow generated identity media to auto-publish without the required review/disclosure/approval.

## Text and Editorial Production

- Use assistants for briefs, outlines, drafts, rewrites, scripts, headlines, summaries, variants, localization drafts, and critique from verified source material.
- Preserve factual sources, product/service claims, names, dates, prices, quotations, statistics, legal copy, and client commitments outside generated prose.
- Require editorial review for factual correctness, tone, audience, originality/reuse concerns, citations where needed, and unsupported claims.
- Detect duplicated or near-duplicated generated copy across campaigns/channels when originality matters.
- Keep approved copy/version in the CMS/document/DAM workflow rather than conversational memory.

## Image Production and Editing

- Evaluate text-to-image separately from editing/inpainting/outpainting/compositing/relighting/background replacement because production usefulness can differ substantially.
- Check subject/object geometry, product details, logo/text accuracy, brand style, artifacts, masks/edges, resolution, color, and editability.
- For exact typography, labels, prices, UI text, or disclaimers, prefer deterministic typesetting when model rendering cannot be verified reliably.
- Preserve source/reference images and final composites so generated elements can be audited and revised.
- Do not treat a good thumbnail preview as final-quality acceptance.

## Video and Motion Production

- Evaluate shot-level temporal consistency, subject/product identity, motion, camera behavior, text/logo stability, start/end-frame control, lip sync, editability, duration, resolution/frame rate, and artifact frequency.
- Measure cost per accepted shot/second rather than generation request because rerolls, extensions, upscaling, interpolation, compositing, audio work, and manual correction can dominate.
- Preserve shot/version IDs and reference assets so continuity can be reviewed across a sequence.
- Use deterministic NLE/compositing/color/audio tools for final timeline, synchronization, captions/legal copy, and delivery validation where appropriate.

## Audio, Voiceover, and Dubbing

- Evaluate intelligibility, pronunciation, names/brands, terminology, language/accent, naturalness, prosody, pacing, style, speaker consistency, long-form continuity, clipping/noise/artifacts, delivery format, and edit burden.
- Test every production language/accent/speaker independently.
- Preserve approved scripts/translations and the original recording where a generated derivative is produced.
- Verify voice/identity consent and service/model output rights before publication.
- Keep music/sound generation licensing and platform/client delivery requirements explicit.

## Team Review and Approval

- Define review roles appropriate to scale: creator/operator, factual/editorial reviewer, brand/creative reviewer, rights/legal reviewer where required, and final publisher/approver.
- Do not allow the generating model to self-certify final acceptance.
- Use checklists for recurring failure classes that are easy to miss at volume: wrong names/text/prices, brand drift, hidden artifacts, unsafe claims, licensing gaps, identity problems, provenance loss, localization errors, wrong output specs.
- Keep approval comments and final status in a shared production system.
- For low-risk/high-volume content, simplify review only after sampled evidence demonstrates the route meets agreed acceptance.

## Versioning and Reproducibility

- Preserve exact model/service/version when exposed, source/reference assets, prompt/template, parameters/seed when material, custom model/LoRA/adapter/workflow version, editing/post-processing steps, and output IDs for reusable workflows.
- Do not rely on reproducibility from prompt text alone when hosted models can change behind aliases.
- Store approved reusable templates/workflows in team-owned versioned storage.
- Distinguish draft generations from final approved assets so later automation cannot accidentally publish an unreviewed variant.
- Keep localization/format variants linked to the same canonical source campaign/content version.

## Local and Open-Weight Production Route

- Use local/open-weight generation when confidential/client assets, offline work, customization, high repeated volume, provider independence, or workflow control justifies model/runtime/hardware operations.
- Consume concrete media candidates from `decision-guides/media-creation/`; do not preserve legacy FLUX/Z-Image/other picks here unless the canonical media guide currently retains them for the exact modality.
- Verify exact artifact, runtime/backend, precision/quantization, resolution/duration, batch/concurrency, peak memory, generation time, and accepted quality.
- Treat checkpoints, adapters/LoRAs, ControlNet/reference components, custom nodes, VAEs/encoders, upscalers, and workflow graphs as part of provenance/license/security/reproducibility.
- Do not infer local fit from nominal VRAM, model size, provider performance claims, or successful loading.
- Shared local workers need authentication, user/project isolation, queueing, storage cleanup, monitoring, updates, and concurrency testing.

## Hosted/Local Hybrid Route

- Use hybrid routing when sensitive source assets must remain local but public/sanitized ideation or specialist generation benefits from hosted models.
- Define per-asset routing rules before generation: client-confidential, unreleased product, talent/identity, licensed stock/reference, public source, and approved derivative.
- Do not upload a protected source merely because only the final output will be public.
- Preserve provider/model provenance across local and hosted stages where rights/audit/client review require it.

## API and Batch Content Pipelines

- Use APIs when repeated production justifies templated generation, batch localization/versioning, DAM/CMS integration, programmatic resizing/variant production, or structured workflow orchestration.
- Bound generation count, retries, concurrency, spend, storage, and job duration.
- Require deterministic validation of filenames/metadata/destinations and human/automated QC appropriate to content risk before publication.
- Separate generation, review approval, and publication as distinct state transitions.
- Protect API credentials and restrict service permissions to the intended project/workflow.
- An agent should not endlessly regenerate until a subjective metric improves; define stopping/acceptance rules.

## Moderation, Safety, and Publication Policy

- Apply content policy/moderation requirements appropriate to the channel, audience, client, region, and content type.
- Model safety filters do not replace editorial policy, advertising/platform rules, legal review, age/audience controls, or brand standards.
- Verify factual and regulated claims independently, especially health, finance, safety, politics, legal, product performance, and endorsements.
- Keep publication destination/account explicit; approval to generate an asset does not authorize posting it to public/client channels.
- Preserve incident/removal/correction workflow for published content that later proves inaccurate, infringing, unsafe, or off-brand.

## Collaboration and Asset Isolation

- Keep client/brand/project assets separated enough to prevent accidental cross-project reference or generation.
- Verify workspace/library/folder permissions and offboarding so former members lose access appropriately while team-owned source assets remain available.
- Do not combine client reference libraries or fine-tuning/customization data without explicit authorization.
- Keep internal unreleased assets out of broad public/shared generation spaces when a scoped project surface is available.
- Treat external collaborators/contractors as separate access boundaries.

## Team Evaluation Suite

- Maintain representative assignments across the team's actual modality mix: one text/editorial item, image generation/editing task, video/audio task if used, brand-consistency set, localization variant, and a rights/provenance/publishing edge case.
- Include adversarial cases: wrong product/logo/text, unsupported factual claim, protected input, likeness without permission, provenance stripped in export, conflicting brand guideline, and content that should not publish.
- Score accepted-result rate, factual/brand correctness, modality QC, revision count, rights/provenance completeness, editability, publication safety, latency, and reviewer time.
- Compare products/model versions using the same source assets/brief where legally permitted.
- Provider demos/benchmarks are candidate evidence, not production acceptance.

## Cost per Accepted Creative Deliverable

- Compare **total cost per accepted deliverable**, including seats, generative credits/API/compute, failed variants, local hardware/power, storage, asset transfer, editing/compositing, review, localization, rights/legal work, moderation, and publication correction risk.
- Integrated tools can beat a lower per-generation specialist when editability/handoff saves significant production time.
- Specialist models can beat integrated tools on high-value assignments when accepted-result rate materially improves.
- Local generation can win at sustained volume only after operations and human correction are included.
- Track accepted assets/shots/minutes/deliverables rather than raw generations.

## Escalation Triggers

- Move from individual creator to this scenario when brand/assets/review/publication become shared team responsibilities.
- Move to `marketing-and-growth-team/` when campaign targeting, experiments, attribution, customer data, or paid-channel operations dominate.
- Move to `research-and-insights-team/` when source research/evidence synthesis dominates.
- Move to organization creative/platform routes when DAM/brand governance, centralized asset provenance, multi-team production, enterprise licensing, or shared media infrastructure dominates.
- Move to sensitive/high-security routes when unreleased/client/identity/regulated data requires stronger controls.
- Move back to deterministic/manual production where AI quality/editability/rights constraints cannot meet the deliverable acceptance threshold.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when a fixed local/shared media worker materially constrains model selection.
- Use `../../../hardware/sub/computers/` for creator workstations and `../../../hardware/sub/servers/` for dedicated shared media/inference workers.
- Hardware purchasing remains outside this scenario; hosted/API/hybrid routes remain valid alternatives.

## Canonical Links

- Link modality-specific model selection to `catalog/models/selection/decision-guides/media-creation`.
- Link individual production constraints to `catalog/models/selection/user-scenarios/professionals/creative-professional` where useful.
- Link campaign/growth concerns to `catalog/models/selection/user-scenarios/teams/marketing-and-growth-team`.
- Link named services/models to their canonical catalog owners only when materialized/current.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Adobe Firefly commercial-use/IP-indemnification/Content Credentials evidence, current OpenAI C2PA/SynthID generated-content provenance documentation, current Google SynthID evidence, and canonical AI Lab `media-creation`/creative scenario owners.
- Current evidence establishes useful provenance mechanisms and commercial/enterprise creative-product terms, but provenance does not prove factual accuracy, ownership, or correct context, and commercial/indemnification coverage remains feature/offer/contract specific.
- Media model versions, credits/pricing, rights/terms, provenance coverage, export behavior, API limits, moderation/platform policies, and local runtime/artifact support are mutable; recheck them before rendering current guidance.
- Team production acceptance requires assignment-specific QC and rights review rather than provider positioning alone.

## Validation

- The scenario is a shared production workflow, not a generic small-business route or single-creator route.
- Concrete media model ranking remains in `media-creation`, avoiding stale legacy model picks here.
- Shared brand/source assets and final approved outputs remain authoritative outside assistant memory.
- Rights to inputs, model/service terms, likeness/voice consent, provenance, and publication authorization remain separate controls.
- Provenance metadata/watermarks are not treated as ownership or factual-authenticity guarantees.
- Modality-specific QC and human/team acceptance occur before publication.
- API/agent pipelines separate generation, review, and publication states.
- Local/open-weight production includes runtime/hardware/license/security/concurrency rather than nominal VRAM shortcuts.
- Cost is measured per accepted deliverable including correction/review/rights work.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
