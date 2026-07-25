# Choosing Generative Media Models and Workflows

Use this guide to select an exact model, service, deployment, or smallest practical workflow for a defined image, video, music, sound, speech, or voice-generation assignment.

## Translations

- English

## Status

Initial canonical guidance verified on 2026-07-25. Model availability, endpoints, pricing, licenses, provider policies, watermarking, and media-generation behavior change quickly; verify the complete assignment before adoption.

## Define the workload first

Generative media is not one interchangeable capability. Separate the required work into the actual artifact and transformation classes:

- text-to-image generation;
- image-to-image transformation and style adaptation;
- masked editing, inpainting, object replacement, and background replacement;
- outpainting, reframing, and aspect-ratio extension;
- reference-guided subject, product, character, or style preservation;
- typography, logos, diagrams, UI assets, and other text-sensitive visual work;
- text-to-video and image-to-video generation;
- video continuation, remixing, shot creation, or reference-guided motion;
- music generation, continuation, arrangement, or variation;
- sound-effect, ambience, Foley, and general audio generation;
- synthetic speech with a stock or designed voice;
- voice cloning, speaker adaptation, dubbing, and multilingual speech;
- multimodal packages combining image, motion, music, sound, and speech;
- evaluation and approval of generated assets, which should normally be a separate assignment from generation.

Do not select from a single aggregate leaderboard or assume that one model is best across these classes. A model that produces attractive concept images may fail production editing, typography, identity preservation, temporal consistency, audio synchronization, licensing, or deployment requirements.

## Freeze the assignment unit

Treat a recommendation as a claim about one complete generation assignment, not a provider or model family. Record:

- exact downloadable artifact and revision, or exact API service, model ID, endpoint, region, and snapshot when exposed;
- provider, runtime, hardware, weight format, quantization, workflow graph, plug-ins, prompts, parameters, tools, and permissions;
- media class, generation or editing mode, input modalities, and output container;
- source assets, masks, reference images, reference audio, control signals, and their permitted use;
- target dimensions, aspect ratio, duration, frame rate, sample rate, channels, codec, alpha, color space, and file-size limits;
- required subject, identity, character, product, style, layout, text, motion, timing, musical, or speaker constraints;
- allowed variability, number of candidates, seed policy, revision budget, and post-processing policy;
- quality tier and risk classification;
- privacy, confidentiality, retention, residency, copyright, publicity, likeness, voice, trademark, and permitted-use boundaries;
- evaluation suite, reviewers and their independence, evidence, limitations, and verification date.

Create a separate assignment when any material field changes. Do not transfer results between text-to-image and image editing, one aspect ratio and another, one speaker or language and another, short clips and longer sequences, hosted and local deployments, or different quantizations without evidence.

## Set task-specific acceptance gates

Use the repository's five [quality tiers](../combined-workloads/#quality-tiers) rather than inventing a parallel scale.

| Tier | Generative-media gate |
| --- | --- |
| Exploration | Produce labeled candidates quickly; visible defects, loose adherence, and manual selection are acceptable, but the asset is not approved for publication or consequential use |
| Concept draft | Communicate composition, mood, motion, sound, or voice direction well enough for review; preserve critical references sufficiently to guide iteration |
| Working result | Meet declared semantic and technical requirements, pass required file checks, and disclose known visual, temporal, acoustic, identity, or rights limitations |
| Production quality | Pass every pre-registered content, technical, legal, consent, provenance, accessibility, and independent review gate required for release |
| Exceptional quality | Add stricter art direction, continuity, fidelity, mixing, mastering, editorial, accessibility, and specialist review where the additional value justifies the cost |

Define observable gates for the selected medium. An attractive sample, a provider demo, or the generator's self-description is not proof that the assignment passes.

## Select the smallest complete workflow

Start with constraints that can eliminate candidates:

1. Reject artifacts, services, or routes whose license, terms, output rights, consent model, policy, region, or intended use do not cover the workload.
2. Reject routes that violate privacy, confidentiality, residency, offline, likeness, voice, or source-asset restrictions.
3. Separate deterministic preparation and post-processing from model generation where practical.
4. Measure eligible candidates on a frozen representative suite.
5. Compare total cost and latency per accepted asset, including failed generations, candidate selection, editing, review, rendering, storage, and escalation.
6. Choose the least expensive assignment that consistently reaches the tier, then define a separately validated fallback.

The smallest complete system may contain several components:

- a language or multimodal model that converts a brief into prompts, shot lists, masks, or structured controls;
- one or more media generators;
- deterministic image, video, audio, or document tooling;
- an independent perception or evaluation model for triage;
- a human art, editorial, legal, accessibility, or domain reviewer;
- provenance, asset-management, and approval records.

Do not add a planner or critic model when deterministic templates and human selection are cheaper and more reliable. Do not remove independent review merely because the generator can critique its own output.

## Image generation and editing

### Separate generation from editing

Evaluate at least these assignments independently:

- unconstrained text-to-image generation;
- layout- or reference-conditioned generation;
- subject, character, face, product, or brand preservation;
- local masked edits;
- global relighting, restyling, or background changes;
- outpainting and reframing;
- text rendering and graphic-design assets;
- transparent-background or layered production output.

A model can be strong at novel generation but weak at edit locality or repeated identity. A unified generation-and-editing model may reduce service count, but only if it preserves accepted quality across both roles.

### Image acceptance dimensions

Measure, as applicable:

- prompt and negative-constraint adherence;
- composition, count, spatial relationships, perspective, and crop;
- subject, face, character, product, logo, or style preservation;
- edit locality: changed pixels or regions should match the requested scope;
- mask-boundary quality, fill coherence, and outpaint continuity;
- typography, spelling, punctuation, and layout accuracy;
- anatomy, geometry, reflections, shadows, textures, repeated patterns, and small-object integrity;
- background removal, alpha, edge quality, color space, dimensions, and export validity;
- consistency across seeds, revisions, views, and a required asset set;
- evaluator disagreement and human correction effort.

For production asset sets, evaluate the complete set together. Individually acceptable images may still fail continuity, palette, product, character, or layout consistency.

## Video generation and editing

Freeze the required shot grammar before comparing models:

- text-to-video, image-to-video, first-frame, first-and-last-frame, reference-guided, extension, or remix mode;
- duration, aspect ratio, resolution, frame rate, camera movement, and shot count;
- subject, wardrobe, product, environment, and visual-style continuity;
- required motion, timing, causality, interactions, and physical constraints;
- embedded dialogue, ambience, sound effects, music, or synchronization requirements;
- whether several generated shots must edit into one coherent sequence.

Measure:

- prompt, reference, and shot-list adherence;
- temporal coherence and identity drift;
- object permanence, count stability, geometry, physics, and interaction integrity;
- camera-path, framing, lens, and transition behavior;
- first-frame, last-frame, or source-video preservation;
- flicker, warping, morphing, duplicated objects, and frame-level artifacts;
- speech, lip, sound-effect, music, and event synchronization when generated audio is present;
- output duration, dimensions, frame rate, codec, decode, and container validity;
- editability and continuity after trimming, interpolation, compositing, or upscaling;
- queue time, generation time, failure rate, storage, and cost per accepted second or shot.

Do not infer long-form narrative or multi-shot reliability from one short demonstration clip. Test the actual number of shots, identities, revisions, and continuity transitions required by the workload.

## Music, sound, and general audio

Separate:

- instrumental music from songs containing vocals;
- complete tracks from loops, stems, continuations, and variations;
- music from sound effects, ambience, Foley, and general audio;
- reference-conditioned work from text-only generation;
- concept sketches from release-ready audio.

Measure:

- prompt, genre, instrumentation, mood, tempo, meter, key, structure, and duration adherence;
- musical development, repetition, transitions, endings, and long-range coherence;
- melodic, rhythmic, harmonic, vocal, and arrangement defects;
- unwanted speech, identifiable imitation, memorized fragments, or source leakage;
- noise, clipping, distortion, phase, silence, spectral imbalance, and transient artifacts;
- sample rate, bit depth, channels, loudness, peak, codec, loop boundaries, and stem alignment;
- editability, synchronization to picture, and correction or mastering effort;
- source-data, reference-audio, output-rights, distribution, and commercial-use constraints.

A generated waveform that decodes successfully is not a mastered or legally cleared release. Keep composition approval, mix or master approval, rights review, and distribution approval explicit.

## Speech, designed voices, and voice cloning

Evaluate stock or designed voices separately from cloned voices. For each language, accent, voice, and speaking style, measure:

- intelligibility and pronunciation, including names, numbers, abbreviations, and domain terms;
- language, accent, dialect, code-switching, and phoneme coverage;
- speaker similarity and speaker drift when a permitted reference is used;
- pacing, pauses, emphasis, emotion, prosody, and instruction following;
- consistency across sentences, sessions, languages, and expressive styles;
- audio quality, noise, clipping, breath artifacts, discontinuities, and edit points;
- first-byte latency, real-time factor, streaming behavior, and retry rate;
- human detection of misleading identity, context, endorsement, or emotional implication.

Automatic speech recognition, speaker embeddings, similarity metrics, and model judges are diagnostic signals only. Calibrate them against human listeners for the exact language, speaker, recording conditions, and risk. A cloned voice must not approve itself.

## Report measurable outcomes

Pre-register the eligible unit for each medium. Keep failed, rejected, blocked, no-output, and policy-filtered attempts in the denominator when they occur under deployed conditions. Do not silently replace a failed run with a successful rerun.

| Outcome | Numerator / denominator |
| --- | --- |
| Terminal acceptance | Eligible assets passing every declared gate after permitted correction and escalation / all eligible scheduled assets |
| First-pass acceptance | Eligible assets accepted without regeneration, correction, manual editing, or escalation / all eligible assets |
| Candidate efficiency | Accepted terminal assets / all generated candidates, with candidates per accepted asset also reported |
| Prompt and reference adherence | Eligible reviewed assets meeting every required semantic and reference constraint / all eligible reviewed assets |
| Critical-defect rate | Eligible reviewed assets containing at least one pre-defined release-blocking visual, temporal, acoustic, identity, or technical defect / all eligible reviewed assets |
| Edit-locality pass | Eligible edited assets whose requested regions changed and protected regions remained within tolerance / all eligible edited assets |
| Identity or product preservation | Eligible reference-conditioned assets meeting every pre-registered preservation gate / all eligible reference-conditioned assets |
| Technical validity | Eligible assets passing each named decoder, container, dimension, duration, frame, color, alpha, loudness, or schema check / all eligible assets scheduled for that check |
| Continuity pass | Eligible multi-asset sets or sequences meeting the declared cross-asset or cross-shot consistency rule / all eligible sets or sequences |
| Human correction effort | Total measured selection, editing, compositing, cleanup, mixing, mastering, or review time / accepted terminal assets |
| Latency | End-to-end time from assignment start to terminal disposition, including queue, generation, upload, download, review, correction, and escalation |
| Cost per accepted result | Total model, API, GPU, storage, transfer, tooling, correction, and review cost across eligible attempts / accepted terminal assets |

Also report the distribution of rejected reasons. A low acceptance rate caused by one repeated failure signature should trigger rerouting or model replacement, not unlimited sampling.

## Candidate assignments

These candidates are starting points for evaluation, not quality rankings. Product facts below were rechecked against primary sources on 2026-07-25; verify current model IDs, endpoints, access, policies, and terms before deployment.

### OpenAI media APIs

**Candidate role:** Hosted image generation and editing, short video generation, and synthetic speech through separately selected API models.

OpenAI's current [model catalog](https://platform.openai.com/docs/models) lists GPT Image 1 and a smaller image model, Sora 2 and Sora 2 Pro for video, and GPT-4o mini TTS for speech. The [Videos API](https://platform.openai.com/docs/api-reference/videos) uses asynchronous video jobs and supports a prompt with optional reference input. The image-generation tool and API expose generation and editing controls; verify current model-specific support instead of transferring one model's capabilities to another.

Before evaluation:

- record the exact model ID, endpoint, organization or project, region behavior, data controls, retention, moderation, and rate limits;
- test generation, editing, masks, references, output formats, and streaming separately where required;
- test video duration, resolution, reference handling, queue lifecycle, expiration, deletion, and storage behavior;
- evaluate speech voices, pronunciation, instructions, disclosure, and permitted custom-voice behavior independently;
- record current price assumptions and policy restrictions with their verification date.

Do not use ChatGPT product behavior as evidence for an API assignment, and do not infer unrestricted input, identity, or voice use from technical capability.

### Google Vertex AI media models

**Candidate role:** Managed image and video generation for Google Cloud workloads requiring explicit project, region, IAM, storage, quota, and service controls.

Google's current Vertex AI documentation exposes [image generation with Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview) and [video generation with Veo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos). Current release notes should be checked because preview endpoints are retired and replaced over time. The documented Veo interfaces cover text- and image-guided generation, while exact model versions differ in reference, frame, sound, duration, resolution, and quota support.

Before evaluation:

- name the exact publisher model ID, endpoint, location, project, quota mode, and API or SDK version;
- verify text-to-image, editing, reference, watermark, text-to-video, image-to-video, frame, extension, and sound support for that exact model;
- record Cloud Storage, IAM, retention, residency, logging, and data boundary;
- test stated duration, resolution, language, request, and output limitations with representative workloads;
- record current price, availability, deprecation, and replacement assumptions.

Do not collapse Imagen, Gemini image models, Veo versions, preview endpoints, and production endpoints into one unnamed Google candidate.

### Adobe Firefly Services

**Candidate role:** Managed creative API workflow for organizations already using Adobe tooling or requiring a provider-operated image-generation and editing service.

Adobe's [Firefly Services documentation](https://developer.adobe.com/firefly-services/docs/firefly-api/) exposes authenticated image-generation APIs and related creative services. Exact API resources, models, enterprise access, output terms, credentials, quotas, and Content Credentials behavior must be verified for the selected organization and use.

Before evaluation:

- record the exact service, API version, model, operation, credential scope, and organization;
- test generation, fill, expand, composition, style, structure, custom-model, and export requirements separately when used;
- verify source-asset rights, output rights, training or customization terms, retention, and enterprise controls;
- preserve and validate provenance metadata through the complete editing and publishing pipeline where required.

Do not treat Adobe ecosystem integration or provider claims as proof that a specific production brief passes.

### Black Forest Labs FLUX artifacts

**Candidate role:** Local or hosted image-generation and editing evaluation with explicit artifact-level licensing.

The official [FLUX inference repository](https://github.com/black-forest-labs/flux) lists separate artifacts for text-to-image, fill, structural conditioning, variation, and editing. `FLUX.1-schnell` is published under Apache-2.0 through its official [model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell). The `[dev]` artifacts use Black Forest Labs' non-commercial license unless a separate commercial agreement applies; verify the current license text for the exact artifact.

Before evaluation:

- pin the exact repository and model revisions, weight files, encoders, VAE, runtime, scheduler, quantization, and workflow;
- distinguish `schnell`, `[dev]`, hosted `pro`, and later FLUX generations instead of treating FLUX as one model;
- verify whether the assignment requires generation, fill, canny, depth, redux, Kontext, or another separate artifact;
- measure full and quantized memory, load time, throughput, candidate count, and quality loss on the target GPU;
- perform an independent license and permitted-use review before commercial or production use.

### Stability AI image and audio artifacts

**Candidate role:** Self-hosted image or audio baseline where exact artifacts, community-license conditions, hardware, and workflow controls are acceptable.

The official [Stable Diffusion 3.5 Medium model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium) documents a downloadable text-to-image artifact under the Stability AI Community License. The official [Stable Audio Open 1.0 model card](https://huggingface.co/stabilityai/stable-audio-open-1.0) provides a downloadable text-to-audio research artifact under its own community license. Stability's [current license page](https://stability.ai/license) must be checked because covered models and commercial thresholds can change.

Before evaluation:

- bind each test to the exact image or audio artifact and revision;
- record gated-access requirements, model license, dependency licenses, permitted revenue or use conditions, and derivative-model obligations;
- measure target-hardware memory, generation time, output duration, candidate count, and quality under the selected runtime and quantization;
- test image editing or audio continuation only when the exact artifact and workflow support it;
- do not transfer results between image and audio families or between community and hosted services.

### Wan2.1 video models

**Candidate role:** Open local video-generation baseline for controlled hardware and reproducible evaluation.

The official [Wan2.1 repository](https://github.com/Wan-Video/Wan2.1) publishes code and model references for video generation under Apache-2.0. Its accompanying technical report describes multiple sizes and tasks, but repository claims and benchmark results remain starting evidence rather than a production recommendation.

Before evaluation:

- pin the exact model, task variant, revision, dependencies, VAE, text encoder, runtime, precision, and scheduler;
- measure actual VRAM, RAM, storage, load time, generation time, output duration, and failure behavior on the target system;
- evaluate text-to-video and image-to-video separately;
- verify output rights, input rights, safety controls, and downstream distribution requirements independently.

### Meta AudioCraft and MusicGen

**Candidate role:** Local research baseline for text-conditioned music and sound generation.

Meta's official [AudioCraft page](https://ai.meta.com/resources/models-and-libraries/audiocraft/) describes MusicGen for music, AudioGen for sound, and EnCodec for audio representation. Pin the exact repository and model card because code and weights can use different licenses and intended-use constraints.

Before evaluation:

- record the exact MusicGen or AudioGen artifact, size, conditioning mode, revision, code license, weight license, and permitted use;
- separate music, melody-conditioned music, sound effects, and compression tasks;
- measure duration, structure, prompt adherence, acoustic defects, hardware, latency, and acceptance rate;
- perform independent rights and similarity review before publication or commercial distribution.

### ElevenLabs voice cloning

**Candidate role:** Hosted stock, designed, instant-clone, or professionally cloned speech where provider verification and account controls fit the consent model.

ElevenLabs distinguishes [Instant Voice Cloning and Professional Voice Cloning](https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning). Its current Professional Voice Clone documentation requires voice verification and states that users can create a professional clone only of their own voice; a verified owner can share the resulting voice through supported controls. Instant cloning requires the user to confirm that they have the right and consent to clone the supplied voice.

Before evaluation:

- record the exact synthesis and cloning model, voice ID, account, plan, verification state, languages, region, retention, sharing, and deletion controls;
- retain affirmative authorization, allowed purposes, allowed users, expiration, and withdrawal procedure;
- test speaker similarity, pronunciation, language, accent, style, emotional range, drift, latency, and abuse resistance;
- define how access is revoked and how already generated assets are handled after consent withdrawal;
- require disclosure where a reasonable listener could otherwise believe the real person spoke the generated words.

Provider verification reduces some misuse paths but does not replace the deployer's consent, context, security, disclosure, and legal obligations.

## Choose local, hosted, or hybrid deployment

| Dimension | Local | Hosted | Hybrid |
| --- | --- | --- | --- |
| Privacy and source assets | Can keep approved assets offline; still requires local access, logging, cache, and deletion controls | Must satisfy provider processing, retention, region, review, and training-use terms | Classify and route assets explicitly; sanitization does not create permission to upload a protected identity or work |
| License and use | Verify weights, code, dependencies, fine-tunes, adapters, and output terms | Verify service terms, policy, account, region, and output rights | Both routes must be permitted independently |
| Capability | Can compose specialized nodes and controls; quality depends on exact artifacts and workflow | May offer newer unified generation or editing features | Define which capabilities and quality are lost on fallback |
| Operations | Measure VRAM, RAM, storage, loading, batching, workflow compatibility, and maintenance | Measure queue, quota, latency, failure, expiration, and provider version changes | Measure routing, upload, download, storage duplication, and failure of either path |
| Cost | Include GPU occupancy, energy, storage, maintenance, candidate sampling, and review | Include requests, seconds, resolution, storage, transfer, retries, and review | Include both stacks and orchestration overhead |
| Fallback | Validate a smaller artifact, CPU path, queue, or fail-closed state | Validate another endpoint, region, provider, queue, or human production path | Test combined outages and return-to-primary behavior |

Compare total cost per accepted asset or accepted second, not nominal request price or raw samples per second.

## Prefer a hybrid portfolio when it lowers total cost

A bounded hybrid workflow can:

1. keep briefs, private references, masks, storyboards, transcripts, and identity records local;
2. use a local model for exploration, prompt development, rough assets, or low-risk variants;
3. route only approved inputs to a stronger hosted generator for production candidates;
4. run deterministic decoding, metadata, dimension, duration, frame, alpha, loudness, and file checks;
5. use an independent perception or audio model for triage, not final approval;
6. route failed, ambiguous, identity-sensitive, rights-sensitive, or high-value assets to qualified human review;
7. preserve approved masters, prompts, seeds, revisions, consent, provenance, and decisions;
8. delete temporary provider and local artifacts according to the declared retention policy.

A local orchestrator plus on-demand image, video, or audio service can reduce resident VRAM, but startup, readiness, artifact persistence, shutdown, and billing state must be verified independently.

## Reliability, retry, and fallback

Give every production assignment a [reliability profile](../reliability-profiles/) that binds the complete deployment and evidence.

Define:

- a bounded candidate budget and bounded correction budget;
- which defects permit another seed, prompt revision, mask revision, sampler change, or same-model retry;
- repeated-failure signatures that require a different artifact, stronger model, deterministic tool, human editor, or stop;
- whether rejected candidates remain billable and retained in the evidence record;
- provider and local transient-failure backoff, idempotency, and duplicate-job handling;
- independent approval requirements for identity, typography, continuity, audio, rights, and publication;
- a separately tested degraded-operation profile for GPU loss, provider outage, quota exhaustion, network loss, or unavailable reference assets;
- recovery and return-to-primary criteria.

Generative variability is not a justification for unlimited sampling. Stop when the remaining defect is a capability gap, the accepted-result budget is exhausted, or another workflow is economically preferable.

## Safe-use boundaries

- Obtain and retain explicit authorization for real-person likeness, voice, performance, private assets, confidential designs, and restricted source media before use.
- Do not generate or publish deceptive impersonation, fabricated endorsement, fraudulent evidence, or misleading real-world events.
- Treat voice cloning, face replacement, realistic identity editing, and political, financial, medical, legal, journalistic, or public-safety media as high-risk assignments requiring stronger controls and human approval.
- Verify copyright, trademark, publicity, contractual, training-data, reference-asset, output-rights, and distribution constraints for the intended jurisdiction and platform.
- Minimize personal data, secrets, credentials, location data, and unnecessary background information in uploaded references.
- Preserve disclosure and provenance records where the context could mislead. Use current [C2PA specifications](https://spec.c2pa.org/specifications/) or equivalent Content Credentials where supported, but do not treat metadata or watermark presence, absence, or validation as complete proof of truth or authorship.
- Keep original assets, generated candidates, approvals, and edit history separated so a generated or edited asset cannot silently replace an authoritative original.
- Do not claim that an asset is human-made, licensed, consented, professionally reviewed, mastered, accessible, safe, or production-approved unless the required process occurred and evidence is retained.

## Compact decision record

Use this record or equivalent structured data:

```text
Assignment ID:
Media class, generation or editing mode, and intended use:
Inputs, references, masks, controls, and permitted use:
Required content, identity, style, layout, text, motion, music, sound, or voice constraints:
Output dimensions, duration, frame rate, sample rate, channels, codec, alpha, color, and container:
Quality tier and risk:
Model, service, endpoint, region, artifact, and revision:
Runtime, hardware, quantization, workflow, prompts, parameters, seeds, and tools:
Candidate, correction, retry, stop, escalation, and fallback budgets:
Privacy, retention, residency, license, rights, consent, and permitted use:
Evaluation suite, eligible units, exclusions, and failure taxonomy:
Deterministic validators and post-processing:
Reviewers, independence, qualifications, and coverage:
Adherence, defect, preservation, continuity, technical-validity, and acceptance outcomes:
Candidate count, correction effort, latency, and cost per accepted result:
Provenance, disclosure, watermark, approval, and artifact-retention records:
Evidence provenance and limitations:
Verified date and re-evaluation triggers:
```

The selection process, gates, workflow design, and record fields in this page are repository-authored operational guidance. They organize established media-generation, evaluation, production, and safety practices and make no claim of novelty.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Defining Model Reliability Profiles](../reliability-profiles/)
- [Perception and Evaluation](../perception-and-evaluation/)
- [Speech and Conversation](../speech-and-conversation/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [Disclaimer](../../../../../../../disclaimer/)
