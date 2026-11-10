# HarvestBench / Harvest Rush

**HarvestBench**, implemented as the **Harvest Rush** simulated farm game, measures how AI agents trade off task progress and fuel against harms to simulated animals and property in an Inspect AI evaluation. The source software and experiment task are not the same entity as a hosted leaderboard, model scores or the paper.

## Experiment and scoring

According to the [first-party README](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/README.md), two model-directed tractors run through a farm game. An autopilot manages movement, while an LLM chooses objectives and responds when animals, hay bales or rocks block travel. The scenarios compare free/harmless hay obstacles, costly rocks and animals that can be hit without immediate fuel cost; neighboring crops introduce a second incentive conflict.

The task's **deterministic scorer** reads recorded episodes, separating animal harm, hay damage, rock impacts, crops, fuel and related events. The authors describe a separate validation gate checking sufficiently complete, well-formed model responses and sane controls before reporting comparable cells. Older free-navigation interfaces retained in the repository are not the interface used for the published runs.

The [package manifest](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/pyproject.toml) declares Python >=3.10, `inspect-ai` and game-engine dependencies. Running actual evaluations requires separate model-provider access and reproducible model, seed, protocol and judge-free grading settings.

## Interpretation and rights

The described animal harms occur in a **simulation**, not in real farming. A resulting score is specific to the experimental protocol and training history, not general proof of ethics or safety. The [MIT license](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/LICENSE) concerns project code; raw private logs, leaderboard data, model provider services and paper/data rights remain separate.

No game, model evaluation, score verification, dependency audit or whole-catalog clean pass was executed.

## Official source snapshot

- [Repository](https://github.com/CompassionML/harvestbench)
- [README.md](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/README.md)
- [pyproject.toml](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/pyproject.toml)
- [LICENSE](https://github.com/CompassionML/harvestbench/blob/62c4382579c1b44375610f900387da4a630d475c/LICENSE)
