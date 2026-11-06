# Documentation Requirements

## Requirements

- Identify AgentIF as THU-KEG's original 707-instruction research dataset across 50 real-world agentic applications. Instructions average 1,723 words and 11.9 constraints; do not present these as per-row limits or universal model capabilities.
- Preserve data and benchmark methodology boundaries: original annotated prompts/constraints, coded or LLM-based judging, evaluation runner, leaderboard, judge-model configurations and trained or evaluated models are separate things. AgentIF does not duplicate Google's IFEval or THUDM's interactive AgentBench.
- Preserve the exact original GitHub repository `data/` scope and its explicit `data/LICENSE` (CC BY 4.0) separate from code `LICENSE` (Apache-2.0). The Hugging Face mirror currently exposes `cc-by-nc-4.0` metadata. This is a **material first-party distribution-license conflict**: document both precisely, do not silently choose a globally applicable license or promise unrestricted commercial reuse of the mirror. Obtain permissions/clarification for uses requiring certainty.
- Pin dataset, constraint checker, judging model and harness revision for repeatability. The 2026-10 project release changes evaluation to thinking/non-thinking modes, vendor-selected decoding, three independent runs and `gpt-5.6-luna` as a judge, whereas original single-run results used `gpt-4o-2024-11-20`. The two leaderboard eras are **not comparable**.
- Annotated `evaluation` items can contain executable code and external-model judging logic; do not execute unreviewed dataset-provided code snippets, tools or instructions in a privileged environment. Sandbox checkers, safeguard credentials and prevent model-output/prompt injection from becoming trusted instructions. Untrusted supplied prompts may contain sensitive or unsafe instructions; review data rights separately.
- Treat judge variance, vendor-recommended model decoding and model selection as evaluation methodology rather than universally calibrated success rates. No fresh original benchmark execution, independent validation of the annotated constraints or exhaustive beneficial-owner/sanctions review was performed for this catalog profile.
- Attribute original dataset publishing identity to THU-KEG / Tsinghua University's Knowledge Engineering Group, not the separately registered `THUDM` GitHub publisher or Tsinghua University as an implicitly sponsoring legal entity. Preserve author names and lab relationship without inventing incorporation, legal ownership, nationality-based risk or sanctions clearance.
- Record original producer↔dataset reciprocal relations and complete first-party references in reader-facing materials.

## Validation

- Exactly one new `catalog/datasets/agentif` identity; no separate evaluator, score version, generic IFEval extension or hosted service is materialized as part of this intake.
- Reciprocal `catalog/producers/t/thu-keg` links and reader navigation resolve.
- Both conflicting official distribution licenses are visible, without claiming commercial freedom for the Hub distribution.
- Evaluation revisions are explicitly non-comparable; no claim of runtime execution or whole-catalog render/schema/cache/CI validation.
