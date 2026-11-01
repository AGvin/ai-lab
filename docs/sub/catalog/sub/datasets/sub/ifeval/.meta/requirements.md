# Documentation Requirements

## Requirements

- Identify IFEval as Google's released concrete English prompt-and-constraint dataset, not a generic instruction-following concept, leaderboard, hosted evaluation service or separately packaged checker. Preserve its canonical identity across Hub/source distributions.
- Explain verifiable response constraints at a factual orientation level; dataset examples include length, keyword and formatting requirements. Keep a scoring tutorial or model-comparison results with their separate owners.
- Preserve prompt text, instruction identifiers and constraint arguments as the data contract. Pin the exact data revision and checker version for reproducible use. A Hub split named train does not establish that training on public evaluation prompts is appropriate.
- Distinguish strict versus loose and prompt-level versus instruction-level result labels only to prevent incompatible score comparisons. Loose checker transformations and all model results are evaluator/run behavior, not separate datasets.
- Keep the existing MLPerf Mobile v6.0 workload reference distinct from this original source dataset; its suite/device scores do not replace IFEval's dataset identity.
- The official Google Hub card declares Apache-2.0 for data; no standalone LICENSE was listed there in the source review. The actual Google Research root LICENSE and checker headers establish Apache-2.0 code licensing. Do not misrepresent code-license retrieval as an independent complete data-rights audit.
- Preserve Google Research attribution through the existing Google producer; do not invent a new corporate producer or imply this research repository is an officially supported Google product.
- Formal-constraint performance does not certify factuality, safety or broad semantic instruction understanding. Public prompt exposure creates contamination concerns; no model execution, score, backend compatibility or production suitability was tested here.
- Provenance review establishes publisher attribution, not exhaustive ultimate ownership, current indirect holdings or sanctions status. Do not infer nationality or control from names.
- Render the complete visible current-entity relation projection through the standard entity-relations component. Include explicit official resources: Google Hub dataset, original Google Research source, original paper, checker source, and actual Google Research LICENSE.

## Validation

- Preserve exactly one source-dataset identity; do not accept MLPerf integration, strict/loose scores or checker packages as duplicate datasets.
- Google produced-by / produces resolves bidirectionally and all new reader links resolve.
- Full page agrees with this contract and applicable global documentation requirements; separate scoped YAML/reference/relation/link checks from whole-repository schema/cache/CI and final publication acceptance.
