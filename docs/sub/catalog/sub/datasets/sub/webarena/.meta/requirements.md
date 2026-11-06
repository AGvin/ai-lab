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
