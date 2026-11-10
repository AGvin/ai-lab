# Documentation Requirements

## Identity and official release

- Seedance 2.5 is ByteDance Seed's **newly announced video model dated 2026-07-31**, separate from Seedance 2.0 and from the Seedream image-generation family. The current first-party model catalog independently names Seedance 2.5. [Official announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) [ByteDance Seed models](https://seed.bytedance.com/en/models).
- The publisher attributes single-pass audiovisual generation up to **30 seconds**, followed by iterative extensions; it describes up to **30 reference images, 10 reference video clips and 10 reference audio clips**, plus timestamp-level targeted editing and professional green-screen and camera controls. These are published model claims, not AI Lab runtime tests. [Announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) [Product](https://seed.bytedance.com/en/seedance2_5).
- Keep exact release date distinct from provider route IDs: BytePlus ModelArk has described the `dreamina-seedance-2-5-260628` video-generation endpoint in its 202606 provider release bulletin. This is a service/route/version identifier, **not another trained-model identity** or proof that every region/account has access. [BytePlus release bulletin](https://docs.byteplus.com/en/docs/modelark/model-release-announcement).
- ByteDance's launch describes a joint audiovisual generation approach built on the Seedance 2.0 architecture; do not infer one identical checkpoint, published parameter count, exact open weights or a blanket global license.

## Operating and safety boundaries

- Published entry points include Dreamina/Jimeng and Doubao experiences and BytePlus ModelArk routes. Check authentication, release tier, regional availability, request modes, quotas, pricing, data processing and retention with the selected provider. Do not claim a live authenticated API request was performed.
- Input reference assets may contain personal likeness, voice, copyrighted material or sensitive scenes; use only authorized inputs and obtain output distribution rights and consent where applicable. Publisher benchmark and quality claims are not independent accuracy or safety validation.
- Treat 30-second and reference-count limits as publisher-described launch capabilities, not universal guarantees for every serving route or future release.

## Validation

- The canonical metadata has one `member-of` relation to Seedance and the family has an exact reciprocal `has-member` relation.
- Parent publication namespace and existing producer use supplemental navigation without frozen acceptance credit. Only the distinct Seedance 2.5 model earns one metadata and one original-source evidence gate if independently verified.
- No licensed weights obtained, hosted requests run, legal/privacy/security certification, whole-catalog renderer/schema/cache/CI or clean/final gate claimed.
