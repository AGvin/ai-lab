# Documentation Requirements

## Requirements

- Use the reader-facing title `Video`.
- Present this node as the canonical modality owner for reusable AI concepts whose primary information domain is temporally ordered visual imagery, while keeping still-image visual concepts under the selected sibling `vision/` domain.
- Define video information through both spatial visual content and temporal organization such as frame order, timing, motion, scene changes, persistence, and temporal relationships; do not reduce video semantics to an unordered set of still images.
- Explain that source video can be represented through decoded frames, clips, spatiotemporal patches/tokens, optical/motion features, learned latents, compressed-domain features, or sampled keyframes. One representation or frame-sampling strategy is not universal.
- Distinguish video modality semantics from video file/container/codec specifications. MP4/MOV/WebM, H.264/HEVC/AV1, frame rates, time bases, color formats, and audio tracks are concrete encodings/container properties with separate specification/runtime ownership.
- Distinguish video from audio. Video assets often include synchronized audio tracks, but acoustic information retains `audio-and-speech/` ownership; multimodal systems can combine the two through context/relations rather than duplicate canonical definitions.
- Keep `video-generation/` as the currently selected materialized descendant. Do not infer unlisted video understanding, captioning, tracking, text-to-video, image-to-video, video-to-video, interpolation, prediction, or editing children merely because they are legitimate video tasks.
- Explain that temporal sampling/compression can hide short events, fine motion, ordering, lip/sound timing, or scene transitions. Accepted video duration or frame count is not proof that every source frame/event is modeled at full fidelity.
- Distinguish modality capability from concrete provider support. A service that accepts or emits a video file can preprocess, sample, transcode, truncate, or split it under model/service-specific rules.
- Make clear that visual realism or temporal smoothness is not factual evidence. Generated or interpreted video requires task-appropriate verification for identities, events, measurements, chronology, and consequential claims.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete codecs/containers, frame/duration/resolution limits, preprocessing/sampling rules, model/service support, benchmark results, prices, and model-selection guidance with their applicable catalog, specification, runtime/service, evidence, or decision owners.

## Validation

- Video is not equated with an unordered image set, one codec/container, or one model architecture.
- Still-image vision and audio remain separate sibling modality owners with explicit cross-modal relationships where needed.
- Unlisted video tasks are not materialized implicitly.
- Duration/frame support is not treated as full-fidelity temporal understanding.
- Concrete format, sampling, model/service, price, and benchmark facts remain outside the abstract video owner.
- Direct-child navigation contains only currently materialized selected descendants.
