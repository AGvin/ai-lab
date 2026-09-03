# Documentation Requirements

## Scenario Fit

- Present this scenario for one professional creator—designer, illustrator, photographer, video editor, motion designer, audio creator, copy/creative producer, or adjacent role—whose AI route is constrained by **production quality, editability, brand/style consistency, client/IP boundaries, provenance, iteration speed, and delivery requirements**.
- Keep the scenario individual-professional in scope. Shared brand systems, approval queues, team asset libraries, multi-seat governance, and production operations belong in team/organization routes when they dominate the decision.
- Distinguish this scenario from `general-knowledge-worker/`: creative media generation/editing has modality-specific quality, rights, identity, provenance, file-format, and production-integration constraints that materially change model selection.
- Distinguish it from `mac-developer-or-creator/`: that scenario is hardware/runtime-led by Apple Silicon; this scenario is workflow/creative-deliverable-led regardless of device.
- Keep exact image/video/audio/music/speech model candidate selection in `decision-guides/media-creation/`. This page owns the professional route and how creative-production constraints change which route is acceptable.

## Start From the Deliverable, Not the Model

- Define the actual creative assignment before selecting a model: concept exploration, moodboard, final illustration, product image, ad creative, social asset, UI visual, storyboard, motion/video shot, voiceover, dubbing, sound/music element, editing/inpainting, variation/localization, or another deliverable.
- Record delivery constraints that affect acceptance: dimensions/resolution, duration, frame rate, aspect ratio, color space, alpha/layers, typography/text accuracy, file format, audio sample/codec requirements, editability, deadline, number of variants, and downstream application.
- Separate **ideation quality** from **final-production quality**. A model can be excellent for generating directions/references while being unsuitable for a client-deliverable asset.
- Separate generation from editing. A strong text-to-image/video model may still be a poor production choice if revisions, masking, object continuity, compositing, layer control, or exact brand edits are difficult.
- Preserve the editable/source project and final approved asset outside the generative service history.

## Separate the Creative Workloads

- Classify recurring work before choosing one model/service:
  - text/copy ideation and creative direction;
  - image generation and variation;
  - image editing, inpainting, outpainting, relighting, compositing, or background work;
  - product/marketing imagery;
  - typography/text-in-image work;
  - video generation, extension, editing, or shot ideation;
  - voiceover, speech synthesis, dubbing, or localization;
  - music/sound generation and editing;
  - multimodal reference analysis and feedback;
  - brand/style adaptation;
  - bulk variation/versioning/localization;
  - automation/API-based creative pipelines.
- Do not force all modalities through one provider or model. A professional route can combine a managed creative suite, specialist media models, local open-weight generation, a language/research assistant, and deterministic editing tools.
- Use `decision-guides/media-creation/` for modality-specific candidate evaluation and retain this page as the combined professional workflow owner.

## Default Integrated Creative-Suite Route

- Prefer a managed creative suite with embedded generative features when production integration, editable handoff, established asset workflows, provenance, organization/client acceptance, and reduced file-transfer friction matter more than access to the broadest model catalog.
- Adobe Firefly/Creative Cloud is a current example: Firefly generation is integrated across Adobe creative applications, current non-beta Firefly outputs may be used commercially under Adobe's documented terms, eligible enterprise workflows can have specific IP-indemnification coverage, and Firefly applies Content Credentials to qualifying generated/exported content.
- Treat commercial-use statements and indemnification as **product/contract-specific**. Verify the exact plan, feature, beta status, eligible surface/export event, customer agreement, input rights, and intended use before relying on them.
- Do not present an integrated suite as automatically best quality. Compare its output against specialist models on the exact assignment, while including the cost of re-editing/reimporting external outputs.
- Treat generative credits, premium-feature access, rate limits, and plan allocations as mutable service economics rather than durable model properties.

## Specialist Hosted Generation Route

- Use a specialist hosted model/service when it materially outperforms the integrated suite on an important modality or assignment and the client's data/rights boundary permits the service.
- Evaluate exact model/version and delivery surface. The same provider can expose materially different capabilities, moderation, editing, resolution, provenance, rate limits, or rights terms across consumer app and API surfaces.
- Current OpenAI image-generation surfaces are examples of hosted image generation/editing; current supported OpenAI-generated images include C2PA Content Credentials and SynthID provenance signals. Treat those signals as provenance aids, not proof of copyright ownership, originality, or permission for every use.
- Current Google generative-media products use SynthID watermarking across supported generated image/audio/video/text surfaces. Watermark presence can help establish tool provenance; absence of a detectable watermark is not proof that content is human-created or that no AI was used.
- Prefer a specialist route only when its accepted-result advantage offsets provider switching, asset upload/download, integration, rights review, credit/API spend, and correction effort.

## Rights, Licensing, and Input Authority

- Verify the creator/client has the right to provide every input used for generation or editing: reference images, logos, fonts, stock assets, photographs, video, audio, voice samples, music, characters, likenesses, product imagery, confidential designs, and training/fine-tuning datasets.
- Do not infer permission from technical upload capability. A service accepting an asset does not establish that the user may legally transform or publish it.
- Review provider/service terms for output use, ownership/allocation, indemnification where applicable, prohibited uses, third-party content, beta limitations, and model-specific licenses before commercial delivery.
- Treat open-weight model license, model code license, weights license, training-data claims, and output-use terms as distinct questions when relevant.
- Do not promise that generated output is unique or non-infringing. Current provider terms can explicitly warn that outputs may be similar or non-unique.
- When the consequence is material, use qualified legal/client review rather than model output to decide copyright, trademark, publicity, licensing, or contractual rights.

## Identity, Likeness, and Voice

- Treat a real person's likeness, face, voice, performance, signature style identity, or other identity-conditioned generation as a separate rights/consent boundary.
- Obtain explicit consent and all necessary rights before cloning or reproducing a person's likeness/voice for professional use.
- Do not infer voice/likeness permission from public availability of source media.
- Keep technical voice-cloning or face-generation capability separate from the right to publish, advertise, impersonate, or commercially exploit the result.
- Preserve talent/client approvals and release evidence outside the generative tool when the production process requires them.

## Brand and Style Consistency

- Define what must remain consistent: logo geometry, colors, typography, product packaging, character identity, subject appearance, art direction, camera/look, voice, terminology, or another brand element.
- Use references/style controls only when the provider's terms permit those inputs and the exact model supports the required control mechanism.
- Evaluate consistency across a **set**, not one good output. Run repeated samples, revisions, aspect ratios, languages, scenes, and campaign variants.
- Measure correction burden for common brand failures such as wrong logo/text, product geometry drift, character inconsistency, style drift, color mismatch, hallucinated details, or voice pronunciation changes.
- Preserve canonical brand assets/guidelines as the source of truth. Generated outputs do not redefine a logo, product, palette, or approved style.

## Typography and Structured Visual Content

- For creative work containing exact text, product labels, legal copy, UI text, prices, names, dates, or structured diagrams, require independent verification of every visible token and layout relationship.
- Treat provider claims about text rendering as eligibility evidence only. Evaluate the exact language, font-like appearance, character set, spelling, line breaks, hierarchy, and layout required by the assignment.
- Prefer deterministic typesetting/editing for final critical copy when generated rendering is not reliably editable or exact.
- Do not let an attractive visual hide incorrect product claims, disclaimer text, units, prices, or translated wording.

## Video and Temporal Consistency

- Evaluate video models on shot-level requirements: subject/object persistence, motion plausibility, camera intent, temporal consistency, lip sync, text/logo stability, start/end-frame control, editability, duration, resolution/frame rate, and artifact rate.
- Measure accepted seconds/shots rather than only cost per generation. Failed generations, re-rolls, extensions, upscaling, compositing, and manual repair can dominate economics.
- Preserve continuity references and shot/version IDs so successive generations can be reviewed against the intended sequence.
- Do not treat a visually impressive short clip as evidence of long-form narrative/character consistency.
- Use deterministic NLE/compositing/color/audio tools for final timeline, synchronization, legal copy, and delivery validation where appropriate.

## Speech, Voiceover, Dubbing, and Audio

- Evaluate speech on intelligibility, pronunciation, terminology, language/accent, naturalness, prosody, pacing, style, speaker consistency, long-form continuity, audio defects, delivery format, and editing effort.
- Test every production language/accent independently; do not transfer quality conclusions from English or one speaker to another.
- For dubbing/localization, preserve translation meaning, timing, names/brands, cultural constraints, and client-approved terminology in addition to voice quality.
- Require explicit rights/consent for identity-conditioned voices and preserve the original recording/script when the generated audio is a derivative production asset.
- For music/sound generation, verify provider/model licensing and downstream platform/client requirements before commercial use.

## Provenance and Disclosure

- Preserve available provenance metadata/watermarks through the production pipeline when doing so supports client, platform, newsroom, regulatory, or transparency requirements.
- Current Adobe Firefly applies Content Credentials to qualifying generated/exported media; current OpenAI-supported generated images use C2PA plus SynthID; current Google generative-media products use SynthID on supported media. Treat each implementation according to the exact product/version.
- Provenance signals can be stripped, altered, or unsupported by downstream tools/platforms. Their absence is not proof of non-AI origin.
- Record the model/service and material generative steps separately when the client/organization requires disclosure or auditability.
- Do not describe provenance metadata as a copyright certificate or authenticity proof for the factual content depicted.

## Quality Control and Human Acceptance

- Require independent human/production QC rather than generator self-approval for client-facing work.
- Define modality-specific failure checks before generation. Examples: anatomy/object geometry, logos/text, product details, unwanted artifacts, identity consistency, temporal glitches, audio clipping/noise, pronunciation, unsafe/inaccurate claims, and hidden metadata.
- Compare output to source/reference assets at appropriate zoom/time resolution; thumbnails and first impressions are insufficient for final acceptance.
- Maintain version history for material client revisions and preserve which generated/source assets were used in the final composite.
- For factual/regulated advertising or informational media, verify claims against authoritative sources and legal/client requirements rather than treating visual plausibility as factual evidence.

## Local and Open-Weight Route

- Use local/open-weight media generation when client/IP privacy, offline work, repeat volume, workflow control, model customization, or provider independence justifies hardware/runtime/maintenance burden.
- Consume current open media candidates from `decision-guides/media-creation/`. `Z-Image-Turbo` is a current speed-oriented text-to-image evaluation candidate there; its provider latency/VRAM/quality claims remain eligibility evidence and must be validated on the exact runtime/hardware/assignment.
- Do not infer practical local fit from model size, nominal VRAM claims, image resolution, or successful loading. Verify model artifact, precision/quantization, runtime/backend, peak/steady memory, generation time, resolution/batch settings, and accepted quality.
- Treat checkpoints, LoRAs/adapters, ControlNet/reference components, VAEs/encoders, upscalers, workflow graphs, and custom nodes as part of the reproducibility/security/license surface when used.
- Local generation does not remove input-rights, model-license, endpoint-security, asset-storage, provenance, or consent obligations.

## Hosted/Local Hybrid Production

- Use hybrid routing when some assets must remain private/local while another hosted model materially improves public/sanitized ideation or final quality.
- Define an explicit routing rule for client source assets, unpublished work, faces/voices, product designs, and licensed stock/reference material before using hosted services.
- Do not upload private reference assets to a hosted model merely because the final output will be public.
- Preserve enough metadata/versioning to know which provider/model contributed to each final asset when rights/provenance/client review requires it.

## Direct API and Batch Creative Pipelines

- Use APIs when the professional needs controlled batch variation, templated generation, localization/versioning, integration into DAM/CMS/creative tools, or repeatable production automation.
- Preserve exact model/version, prompt/template, reference assets, parameters, seed where supported/material, post-processing, and output IDs for reproducibility.
- Bound spend, generation count, retries, concurrency, and storage. A creative agent should not endlessly re-roll outputs without explicit acceptance/stopping criteria.
- Separate generation permission from publishing/deployment permission. Automated generation must not auto-publish client media without appropriate review/approval.
- Apply normal secret management to API credentials and limit service permissions to the required project/pipeline.

## Cost per Accepted Creative Asset

- Compare **total cost per accepted creative asset/shot/deliverable**, not cost per generation or token/credit.
- Include subscription/generative-credit/API/compute spend, failed variants, upscale/edit passes, asset transfer/storage, local hardware/power, artist review, retouch/compositing, rights/legal review, and integration friction.
- An integrated suite can win despite higher nominal generation cost when editability and production handoff substantially reduce manual work.
- A specialist model can win despite switching overhead when it materially improves accepted-result rate on a high-value assignment.
- Local generation can be economical at volume on already-owned suitable hardware but include maintenance, model/storage management, power, workflow breakage, and artist correction time.

## Escalation Triggers

- Move from ideation-only use to production generation only after the model/service passes the assignment's rights, quality, editability, and provenance checks.
- Add a specialist provider when the integrated route repeatedly fails a material modality/quality requirement and the new data/rights boundary is acceptable.
- Move to local/open-weight generation when private assets, offline use, customization, or repeated volume justify it and exact hardware/runtime fit is verified.
- Move back to deterministic/manual production when generated text/geometry/identity/continuity or legal/brand constraints cannot be made reliable enough.
- Move toward `mac-developer-or-creator/` when Apple-Silicon hardware/runtime fit becomes the dominant constraint.
- Move toward `sensitive-data-professional/` when confidential client materials, unreleased IP, regulated claims, identity media, or contractual restrictions require materially stronger controls.
- Move to team/organization creative routes when shared brand governance, DAM, approval chains, multi-seat licensing, provenance policy, or production automation become the primary problem.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when local media generation materially constrains the route.
- Use `../../../hardware/sub/computers/` for workstation/laptop local generation and the applicable accelerator specialization when known.
- Use the Apple specialization when Apple-Silicon unified-memory/runtime constraints govern local creative inference.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link modality-specific model selection to `catalog/models/selection/decision-guides/media-creation` rather than duplicating model rankings here.
- Link named managed creative services to their canonical catalog owners when materialized.
- Link exact open media candidates to their canonical Model Reference identities when named in rendered guidance; if an exact candidate owner is not yet materialized, keep the concrete recommendation in `media-creation` until its canonical reference exists.
- Link specialist professional/hardware scenarios instead of duplicating their detailed contracts.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Adobe Firefly commercial-use/IP-indemnification/Content Credentials documentation, current OpenAI generated-image provenance/service terms, current Google SynthID documentation, and canonical AI Lab `media-creation` guidance.
- Current Adobe evidence establishes commercial-use availability for qualifying Firefly outputs, feature/surface-specific indemnification conditions for eligible customers, generative-credit economics, and automatic Content Credentials on qualifying generated/exported media. These do not establish universal ownership/non-infringement or assignment quality.
- Current OpenAI evidence establishes C2PA plus SynthID provenance for supported generated images and product/service rights restrictions that remain input/use specific. Current Google evidence establishes SynthID watermarking across supported generative media and explicitly does not make watermarking a complete detection solution.
- Model versions, provider terms, beta status, indemnification scope, credit/API pricing, provenance implementations, local model artifacts/runtimes, platform disclosure rules, and creative-service capabilities are mutable; recheck them before rendering current guidance.
- Provider quality claims remain eligibility evidence. Professional acceptance requires assignment-specific QC.

## Validation

- The scenario begins from a professional creative deliverable and production constraints, not a universal media-model ranking.
- Ideation and final-production quality remain distinct.
- Exact modality/model candidate ownership stays in `media-creation`.
- Rights to inputs, output-use terms, likeness/voice consent, model license, and commercial-use conditions are explicit and not inferred from technical capability.
- Brand consistency is evaluated across repeated assets/variants, not one successful sample.
- Generated text, factual claims, identity media, and temporal/audio quality have independent QC.
- Provenance signals are treated as transparency evidence, not copyright/factual-authenticity guarantees.
- Local/open-weight execution does not erase rights, privacy, security, provenance, or hardware/runtime validation requirements.
- Cost is measured per accepted production asset/deliverable including correction and rights review.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
