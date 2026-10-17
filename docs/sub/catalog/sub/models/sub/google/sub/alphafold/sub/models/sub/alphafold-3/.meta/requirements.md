# Documentation Requirements

## Requirements

- Identify AlphaFold 3 as the deep-learning model co-developed by Google DeepMind and Isomorphic Labs for predicting 3D structures and interactions involving proteins, DNA, RNA, ligands, and ions.
- Preserve its current GA commercial-research deployment boundary and separate academic code/weights access only while supported by first-party sources.
- Keep AlphaFold Server, AlphaFold Protein Structure Database, Google Cloud/Gemini Enterprise Agent Platform hosting, VM/GPU deployment recipes, and downstream drug-discovery workflows separate from the trained-model identity.
- Treat allowlist/commercial-subscription requirements, academic license terms, code/weights revisions, VM/GPU/storage requirements, serving concurrency, pipeline modes, database requirements, inference options, and hosted regions as freshness-sensitive.
- Preserve the first-party limitation that AlphaFold 3 is a research tool and is not intended or cleared for clinical diagnostic use.
- Keep stochastic prediction outputs/confidence metrics scoped to the exact model/runtime/configuration and do not convert structure-prediction confidence into evidence of biological or clinical validity outside the documented scope.

## Validation

- The node represents the concrete AlphaFold 3 model rather than a hosted service or research database.
- Academic and commercial access paths remain distinct.
- Clinical diagnostic approval is never inferred.
