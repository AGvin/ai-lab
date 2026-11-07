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

## Scoped original-source qualification — 2026-11-08

- **IFEval** is Google's released research **instruction-following prompt-and-checkable-constraint dataset** originally described in **2023**. The first-party `google-research/google-research/instruction_following_eval` repository contains the original task prompts and evaluator and explicitly says the project is **not an officially supported Google product**.
- Its prompt records and constraint parameters are dataset content; formal strict/loose and prompt-level/instruction-level checks are distinct **evaluator protocols**, not separate benchmark source identities. Passing formatting/length/keyword checks cannot establish answer factuality, real-world safety or semantically correct instruction compliance. Google's official Hub data page declares Apache-2.0 while the research code license and third-party rights retain separate boundaries.
- Verified first-party sources: https://github.com/google-research/google-research/tree/master/instruction_following_eval ; https://huggingface.co/datasets/google/IFEval ; https://arxiv.org/abs/2311.07911
- Gate covers existing original dataset identity, public source, research support boundary and scoring-contract distinction only. No grader run, current leaderboard assessment, full item-level rights/privacy/security audit, global schema/cache/CI/render, clean or final credit.
