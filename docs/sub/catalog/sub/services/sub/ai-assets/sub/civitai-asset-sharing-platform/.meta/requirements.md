# Documentation Requirements

## Requirements

- Catalog Civitai as a vendor-operated **AI asset sharing and discovery platform** rather than treating hosted model files, individual user creators, image assets or its self-hostable source application as the same identity.
- Pin first-party `civitai/civitai@e33d090034326331d5a250e38357bed0c3dec004` README and root Apache-2.0 LICENSE, and separately identify `civitai.com` as the operated platform.
- The pinned repository describes model browsing, uploads, collaboration, commenting, a Next.js/tRPC/Prisma stack and local development dependencies. These are source implementation details, not guaranteed hosted product features or supported deployment SLAs.
- Do **not** infer that model uploads, images, LoRAs, user data and third-party checkpoints inherit the Apache-2.0 repository code license. Check each asset's actual license, creator permissions, commercial-use restrictions and derivative-content rules.
- Describe moderation, unsafe and unauthorized uploads, malicious or untrusted model artifacts, rights/publicity/privacy risk, and hosting/community terms as service-boundary concerns. Do not provide unsafe asset download/workflow instructions.
- Hosted service plans, capabilities, content policies, identity controls, access restrictions and pricing are mutable. No production deployment, uploaded asset inspection, secure-model-file verification, licensing audit or whole-catalog clean pass is claimed.

## Validation

- One canonical service reader under the selected category and one relative index link; distinct source software, model, content and operator boundaries remain explicit.
- First-party evidence supports the scoped profile only. Do not infer runtime tests, full rights/contract audits or repository-wide clean status.
