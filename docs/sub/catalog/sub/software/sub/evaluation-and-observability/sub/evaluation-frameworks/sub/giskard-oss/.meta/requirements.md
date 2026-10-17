# Documentation Requirements

## Requirements

- Identify Giskard OSS as the separately installable Giskard-maintained Python agent evaluation, scenario testing, red-teaming and RAG-quality library from `Giskard-AI/giskard-oss`, distinct from the separately hosted Giskard Hub service and unrelated benchmark datasets.
- Preserve **Giskard umbrella v3.0.1 (2026-10-02)** as a non-prerelease publication, plus **giskard-checks v1.0.6 (2026-10-09)** and **giskard-scan v1.0.1 (2026-10-02)** as independently versioned modules within one canonical framework. The umbrella project's PyPI classifier still says **Beta**; do not translate non-prerelease tags into a blanket mature-GA claim.
- Describe asynchronous scenario checks and LLM-as-judge, agent vulnerability probing and adversarial testing (including prompt injection), and RAG/knowledge-base quality evaluation. These modules are importable components and optional dependencies (`giskard[scan]`), not three duplicate platform products. Legacy Giskard v2 remains available for historical/tabular testing but is no longer actively maintained.
- The umbrella install requires **Python >=3.12**. The repository's root license is **Apache-2.0**; individual workspace package metadata (e.g. `giskard-checks` declared MIT and `giskard-scan` Apache-2.0) must be checked for redistribution and cannot be represented as one uniform subpackage grant.
- **Trust and privacy:** evaluate agents and retrieval data only against approved test environments, isolate potentially state-changing tool calls, review judge/provider traffic and telemetry, and use `GISKARD_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1` before import when collection is not desired. An automated scan is not an assurance of safety, security certification or regulatory compliance.
- Relate the existing source repository and Giskard AI producer through exact `produced-by` / `produces` inverse links. Do not add separate software entries for umbrella extras, individual scanners, hosted Hub dashboards or historical v2 aliases.

## Validation

- Official Giskard OSS README, root/package pyproject manifests, release metadata and repository LICENSE substantiate versions, maturity classification, Python requirement, modular boundaries and licensing notes.
- Exact software relation has the corresponding Giskard AI producer inverse.
