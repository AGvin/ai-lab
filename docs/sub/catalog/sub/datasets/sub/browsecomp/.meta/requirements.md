# Documentation Requirements

## Requirements

- Present BrowseComp as OpenAI's released benchmark for browsing agents that must persistently locate hard-to-find, entangled information on the web.
- Preserve the benchmark's short-answer verification design and 1,266-problem release scope only with source-backed version context.
- Keep evaluation results, model rankings, browsing stacks, sampling strategies, and contamination/leakage handling run- and version-sensitive.
- Distinguish BrowseComp from general factuality benchmarks, hosted browsing products, and the `simple-evals` software repository that distributes it.

- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [BrowseComp release and methodology](https://openai.com/index/browsecomp/); [OpenAI simple-evals distribution repository](https://github.com/openai/simple-evals).

## Validation

- BrowseComp remains a benchmark/dataset identity rather than a browsing agent or hosted research service.
- Comparative performance claims remain tied to the cited release and evaluation configuration.

## Scoped original-source qualification — 2026-11-08

- **BrowseComp** is OpenAI's **2025-04-10** benchmark of **1,266 difficult web-browsing questions** designed to demand persistent multi-step research to locate obscure facts with concise, comparatively easy-to-check reference answers. This evaluates difficult browsing rather than all factual answering, model safety, or everyday search.
- The first-party release, the `simple-evals` **evaluation software**, the original research methodology and historical model-score tables are separate surfaces. OpenAI asks that question examples and answers **not be republished in plain text or images** to limit leakage; published canaries and benchmark methodology cannot guarantee uncontaminated model training.
- Original publisher sources: https://openai.com/index/browsecomp/ ; https://github.com/openai/simple-evals
- Accepted existing released dataset identity, date and publisher-described scope only. No copying benchmark questions or model result reproduction, browsing test, complete data/privacy/security/legal audit, whole-repository schema/cache/CI/render, clean or final gate.
