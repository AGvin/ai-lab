# Documentation Requirements

## Requirements

- Identify WebArena as the independently published benchmark and reproducible self-hosted environment for evaluating autonomous agents on realistic browser tasks across controlled websites with programmatically assessed execution outcomes, not as a generic browser automation library.
- Preserve the original WebArena task/environment evaluation boundary: 812 example tasks in the first-party published evaluation workflow, with **v0.2.0 annotations released October 24, 2023** after annotation corrections. Do not transfer task counts or scores from related WebArena variants or later browser-evaluation harnesses.
- Explain that the evaluator's functional task-success metric requires controlled and resettable websites (shopping, shopping administration, social forum, software repository management and supporting information tools), task configurations, authenticated sessions and versioned environment state. Public demo sites are useful illustrations but cannot substitute for resettable benchmark instances.
- Distinguish WebArena's browser-interaction tasks from OSWorld's desktop OS environment, BrowseComp's search answers, GAIA's general assistant task suite, VisualWebArena's multimodal/visual tasks, WebArena-Infinity's evolving evaluations and BrowserGym/AgentLab evaluation infrastructure.
- Treat benchmark task JSON/config, environment images, auth state, prompts, browser observation modes, model API versions, success validators and external hosting as version-sensitive reproducibility inputs. Avoid making cross-version leaderboard comparisons without matched evaluator conditions.
- Preserve first-party WebArena-x research team attribution and reciprocal producer relation without conflating the research contributors with a legal commercial vendor.

## Validation

- The official repository and project site independently substantiate original benchmark task scope and annotation release.
- An execution-success score is not represented as simple browser navigation reachability or as a comparable result across incompatible environment and annotation versions.
- The WebArena `produced-by` relation has the exact inverse WebArena-x `produces` link.

## Scoped original-source qualification — 2026-11-08

- **WebArena** is the original published benchmark and resettable self-hosted **web-interaction environment** for autonomous browser agents, with a first-party evaluation workflow of **812 example tasks** across controlled shopping, administrative, forum, repository and information websites. Its original research is documented in the 2023 paper; annotation fixes were released as **v0.2.0 on 2023-10-24**.
- A demonstration instance is not a substitute for a **resettable benchmark installation**; comparison requires matching website containers, task configs, authenticated agent state, action/observation settings, assertions and evaluation harness revision. AgentLab/BrowserGym integrations, leaderboard submissions and related VisualWebArena are separate software/variant boundaries, not interchangeable scored dataset identities.
- Verified original publisher sources: https://github.com/web-arena-x/webarena ; https://webarena.dev/og/ ; https://arxiv.org/abs/2307.13854
- Source acceptance is limited to original benchmark identity and public task/environment/revision boundaries. No controlled website was launched, no credentials used, no benchmark task or comparative score reproduced, no full security/privacy/legal/rights or root-wide schema/cache/CI/render, clean or final gate.
