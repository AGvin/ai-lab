# Choosing Generative Media Models and Workflows

Select an exact model, service, deployment, or smallest practical workflow for image, video, music, sound, speech, or voice-generation work.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Guidance verified on 2026-07-25. Models, endpoints, prices, licenses, provider policies, watermarking, and generation behavior change quickly; verify the complete assignment before adoption.

## Define the assignment

Separate:

- text-to-image concept generation;
- production image generation;
- image editing, inpainting, outpainting, variation, and background or object changes;
- text-to-video and image-to-video;
- music and sound-effect generation;
- speech synthesis and voice agents;
- authorized voice cloning or identity-conditioned generation;
- candidate evaluation, editing, approval, and publication.

Record exact model or artifact, provider, endpoint, region, runtime, hardware, precision, scheduler, steps, seed, dimensions, duration, frame rate, audio settings, prompts, references, masks, adapters, tools, output format, quality tier, rights, consent, disclosure, and verification date.

Do not transfer results between model versions, fine-tunes, adapters, runtimes, precisions, resolutions, durations, or provider deployments.

## Quality gates

| Tier | Minimum gate |
| --- | --- |
| Exploration | Fast feasibility result; no production or public-use claim |
| Concept draft | Coherent candidate suitable for discussion and direction |
| Working result | Meets primary prompt, format, technical, and defect thresholds |
| Production quality | Independent review, rights checks, provenance, editing, and delivery validation |
| Exceptional quality | Additional creative direction, consistency, polish, and specialist review justified by value |

A technically valid file is not automatically an acceptable artifact.

## Evaluation dimensions

### Images

Measure prompt adherence, composition, anatomy, object count and relations, typography, identity consistency where authorized, style consistency, artifacts, edit locality, mask boundaries, resolution, color, transparency, and delivery format.

For editing, verify both requested changes and protected regions that must remain unchanged.

### Video

Measure prompt and source adherence, temporal consistency, motion, camera behavior, subject identity, scene continuity, frame defects, duration, frame rate, audio synchronization where present, and post-processing effort.

### Music and sound

Measure structure, timing, genre and instrumentation adherence, clipping, noise, transitions, loop quality, stem or channel requirements, duration, loudness, and originality or rights risk.

### Speech and voice

Measure intelligibility, pronunciation, terminology, prosody, emotion, speaker consistency, latency, streaming behavior, audio defects, language variation, and authorized identity match where relevant.

### Workflow outcomes

Report first-pass acceptance, accepted candidates per generation budget, retries, edit effort, reviewer time, latency to terminal artifact, compute or API cost, storage, transfer, and total cost per accepted result.

## Candidate routes

### Local image generation

[FLUX.1-schnell](../../../../../../../software/sub/models/sub/black-forest-labs/sub/flux/sub/flux-1-schnell/) is the current downloadable image candidate for rapid local or temporary generation. Name the exact revision, runtime, precision, offload policy, text encoders, VAE, resolution, and batch. Do not infer 24 GB fit from parameter count or one file size.

### Hosted image and video

Evaluate exact current OpenAI, Adobe Firefly, Google, Azure, or other approved endpoints only after checking region, model identifier, input and output policy, retention, rights terms, watermarking, price units, quotas, and supported editing operations.

### Local and hosted audio

Evaluate exact TTS, music, sound, and voice models by language, speaker inventory, streaming support, license, consent, identity controls, latency, and output rights. A provider product name is not an exact assignment.

### Hybrid workflow

A practical workflow may use a local model for private concepts, a hosted specialist for production candidates, deterministic media validators, and an independent human or calibrated model reviewer.

## Local and on-demand deployment

Record peak VRAM and RAM, load and warm-up time, generation latency, throughput, concurrency, model switching, storage, and failure recovery.

For temporary GPU services:

1. verify task need, rights, consent, quality target, and budget;
2. select exact image, runtime, GPU, storage, and timeout;
3. start with an idempotency key;
4. confirm provider state, endpoint readiness, model identity, and required files;
5. generate a bounded candidate set;
6. persist prompts, parameters, seeds, references, masks, outputs, and provenance outside ephemeral storage;
7. run deterministic validation and independent review;
8. request shutdown and confirm provider and billing state;
9. retry cleanup or escalate when teardown fails.

A worker reporting completion is not proof that a billable service stopped.

## Rights, identity, and provenance

Before generation, record rights or authorization for prompts, references, logos, copyrighted works, faces, voices, personal data, and private material.

Voice cloning, face replacement, impersonation, and identity-conditioned generation require explicit consent and purpose boundaries. Do not use generated identity media to deceive, bypass verification, or imply endorsement.

Preserve available provenance, content credentials, model and version, prompts, parameters, seed, source references, edits, reviewer decisions, and publication disclosure. Do not remove provider marks or provenance contrary to policy or law.

A model's technical capability does not establish a right to create or publish the output.

## Review and fallback

The generator must not be the sole approver of its own output. Use deterministic file checks plus an independent perception model or human review calibrated to the assignment.

Retry transient service or rendering failures. Escalate repeated prompt-adherence, identity, temporal, quality, safety, rights, or capability failures to a different assignment. Bound candidate counts and revision rounds.

## Decision record

```text
Assignment, modality, quality tier, and risk:
Exact model, endpoint or artifact, runtime, hardware, and region:
Prompt, references, masks, adapters, parameters, seed, and format:
Rights, consent, identity, privacy, retention, and permitted use:
Validators, reviewer, rubric, and independence:
Acceptance, defect, latency, effort, and cost outcomes:
Retry, stop, escalation, fallback, lifecycle, and storage rules:
Provenance, disclosure, limitations, verified date, and re-evaluation triggers:
```

## Related pages

- [AI Model Selection and Team Design](../..)
- [Combined Workloads](../combined-workloads/)
- [Perception and Evaluation](../perception-and-evaluation/)
- [Speech and Conversation](../speech-and-conversation/)
- [Resource Lifecycle Orchestration](../orchestration/sub/resource-lifecycle/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
- [C2PA specifications](https://c2pa.org/specifications/specifications/)
- [Adobe Content Credentials](https://contentcredentials.org/)
