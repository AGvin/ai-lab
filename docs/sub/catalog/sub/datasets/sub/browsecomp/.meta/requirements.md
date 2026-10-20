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
