# Documentation Requirements

## Requirements

- Present GAIA as the benchmark for General AI Assistants built around real-world questions requiring combinations of reasoning, multimodal understanding, browsing, and tool use.
- Preserve dataset splits, access conditions, task composition, evaluation protocol, and current leaderboard state only with source/version context.
- Keep benchmark results and submission state freshness-sensitive.
- Distinguish GAIA from generic assistant concepts, hosted leaderboards, and evaluation software.

## Validation

- GAIA remains a benchmark/dataset identity.
- Claims about capability coverage and performance remain tied to current first-party benchmark material.

## Scoped original-source qualification — 2026-11-08

- **GAIA** is the released **2023 GAIA benchmark for General AI Assistants**, evaluating challenging real-world multi-step questions requiring combinations of reasoning, browsing/tool use and multimodal materials. The upstream GAIA benchmark team owns the original research and dataset; it is separate from the hosted leaderboard, scored submissions, agent implementations and other similarly named products.
- The official `gaia-benchmark/GAIA` Hugging Face distribution is **gated**; its publisher asks researchers not to republish validation/test questions in a publicly crawlable form. Gated distribution and 450+ published-task scope do not imply access to hidden test answers, universal dataset reuse rights or verified agent performance.
- Verified publisher sources: https://huggingface.co/gaia-benchmark ; https://huggingface.co/datasets/gaia-benchmark/GAIA ; https://arxiv.org/abs/2311.12983
- Source gate covers the existing original dataset identity, published purpose, access restrictions and protocol boundary only. No gated content downloaded, leaderboard scores recreated, complete item rights/legal/security/privacy audit, whole-repo schema/cache/CI/render, clean or final acceptance.
