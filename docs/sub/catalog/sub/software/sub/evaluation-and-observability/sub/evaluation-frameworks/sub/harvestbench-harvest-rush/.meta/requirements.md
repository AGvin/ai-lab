# Documentation Requirements

## Requirements

- Identify HarvestBench (the Harvest Rush game and evaluation harness) as an Inspect AI-based **simulation** for assessing agent decisions involving animal welfare, harvest objectives, fuel prices and neighboring crops. It does not itself harm real animals.
- Source-pin the official README, Python package manifest and MIT LICENSE at the referenced commit; the manifest declares Python >=3.10, inspect-ai dependency and the `harvestbench` package.
- Distinguish the model's goal/obstacle-interrupt decisions from deterministic autopilot movement; avoid implying the model directly controls continuous tractor steering.
- Explain that deterministic replay grading separates animal hits, hay bales, rocks, crops and fuel. Controls, valid JSON response rate and output completeness must pass the authors' validation gate before publishing comparative results.
- Distinguish the shipped contact task from older free-navigation engine artifacts. The README explicitly says prior published runs did not use the old free-navigation interface.
- Model training or evaluation contamination can distort the interpretation of results; disclose when training used the environment and avoid extrapolating behavior to real-world safety or animal treatment.
- Model calls use separately configured providers and incur costs; source MIT terms do not cover leaderboard data, private raw logs, third-party models or study rights. Do not claim runs, scientific replication, source dependency audit or whole-catalog clean pass.

## Validation

- Match exact frozen candidate and keep this software identity distinct from benchmark data, operated services and parent frameworks.
- Verify official pinned upstream evidence and one matching category index entry; record unresolved rights or result-validity limits rather than assuming completeness.
