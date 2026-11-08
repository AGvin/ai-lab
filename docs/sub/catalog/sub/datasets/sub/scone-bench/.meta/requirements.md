# Documentation Requirements

## Requirements

- Identify SCONE-bench as the released smart-contract exploitation benchmark developed by Anthropic with research collaborators to evaluate agents on exploiting real-world-vulnerability contracts in local simulation.
- Preserve the benchmark boundary around sandboxed exploit generation and simulated value extraction; do not turn benchmark tasks into instructions for exploiting live systems.
- Treat contract/exploit inventory, source datasets, chain coverage, sandbox/tooling, time budget, MCP exposure, scoring/value conversion, contamination cutoff, model roster, and current benchmark revision as freshness-sensitive.
- Keep SCONE-bench distinct from DefiHackLabs as source data, ExploitBench/ExploitGym as external benchmarks, general cybersecurity evaluations, and real-world offensive operations.
- Attribute model comparisons to the exact benchmark revision and sandbox configuration.
- Preserve Anthropic provenance while acknowledging collaboration where described by source material.

## Validation

- The node remains a defensive/research benchmark identity rather than a live exploitation tool.
- Performance claims remain scoped to simulated benchmark environments.

## Scoped original-source qualification — 2026-11-08

- **SCONE-bench** is Anthropic and collaborators' original **2025** defensive research benchmark for investigating AI-agent capabilities on **405 historically exploited smart contracts from 2020–2025** on Ethereum, Binance Smart Chain and Base. The contracts originate in DefiHackLabs but that upstream repository is a source of target cases rather than Anthropic-owned original inventions or a second SCONE-bench identity.
- The original evaluation isolates each case in a **locally simulated blockchain sandbox** and gives an agent an approximately **60-minute** budget to identify a bug and execute a test case under constrained tool access, measuring *simulated* extracted native tokens/funds. Publisher aggregate value results depend on contract snapshots, prices, chain-specific simulation, hidden verifier, model version, context and tools; they cannot authorize attacks on active systems or establish a forecast of actual financial loss.
- Original publisher sources: https://www.anthropic.com/research/smart-contracts ; https://www.anthropic.com/research/exploit-evals .
- Source credit is for one existing research benchmark and permitted isolated historical task/evaluator definition, not operational exploits, live chain execution or model test runs. Full contract/data rights, vulnerabilities/security/legal, reader repair (currently absent), repository CI/render, clean and final acceptance remain unverified.
