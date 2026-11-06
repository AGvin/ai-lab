# Documentation Requirements

## Requirements

- Identify Wan as Alibaba Cloud's large-scale generative-model family for video and related creative-media generation.
- Preserve the family boundary separately from Alibaba Cloud Model Studio hosting, Wan web experiences, Qwen/Qwen-Image, generated assets, and downstream runtime integrations.
- Materialize released Wan model series when their versioned product identity materially changes generation modes or reader decisions; avoid one canonical node per snapshot or API endpoint.
- Treat available generation/editing modes, modalities, output resolution/duration, regional availability, prices, quotas, prompt controls, safety/product policies, and serving aliases as freshness-sensitive.
- Preserve Wan Team production provenance.
- Attribute quality, realism, consistency, and performance claims to Wan/Alibaba or the cited evaluator.

## Decision and Operational Boundaries

- Wan is the creative-media model family associated with the official Wan-Video organization and Wan Team.
- Distinguish released open-weight Wan models from hosted Wan model IDs; open-repository licensing does not license hosted services or all later generations.
- For Model Studio calls, verify retention and region separately: enabling workspace ZDR does not block calls to unsupported models, and asynchronous or stateful features can fall outside ZDR.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Wan remains a trained-model family rather than a hosted creative service.
- Version snapshots and API routes do not become duplicate trained-model identities by default.
- Producer provenance resolves bidirectionally.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
