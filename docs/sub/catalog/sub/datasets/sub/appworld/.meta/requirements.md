# Documentation Requirements

## Requirements

- Keep AppWorld's controllable simulated task worlds distinct from a real external service, its MCP server and the agent runtime; preserve dataset/release revision and environment setup.
- Use the pinned original publisher README to identify the dataset and version; distinguish evaluator, harness, source data, and external models.
- Rights and safety: Apache-2.0 covers source within the repository license grant; separately encrypted/released task assets, scenario data and third-party dependencies must follow their own release conditions. Agent-generated programs must run only in isolated authorized environments with no real user accounts.
- This is a metadata-only source acceptance. No benchmark data download, untrusted code execution, model inference, external service access, or full rights audit has been performed.
- Keep one frozen identity, valid parent Datasets navigation, and no duplicate acceptance credit.

## Validation

- Confirm metadata, requirements and reader are consistent with the original source snapshot.
- Do not award unperformed schema-wide CI, cache/render, runtime or whole-catalog clean-pass gates.
