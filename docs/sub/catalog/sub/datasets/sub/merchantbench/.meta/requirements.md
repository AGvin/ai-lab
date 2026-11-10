# Documentation Requirements

## Requirements

- Present MerchantBench as a released long-horizon benchmark for evaluating LLM-agent coherence in persistent seller-side e-commerce operations.
- Preserve the benchmark's distinguishing 365-day simulated store environment, order-level dynamics, delayed outcomes, supplier changes, cash-flow constraints, and final operational/economic evaluation only at the scope supported by the released repository and paper.
- Keep the simulator, SDK, evaluation harness, baselines, and tests as surfaces of the same benchmark identity unless an independently durable product identity emerges.
- Distinguish MerchantBench from generic e-commerce datasets, memory benchmarks, short-horizon tool-use benchmarks, and production commerce platforms.
- Treat scenario configuration, baselines, evaluator details, benchmark versions, and published results as freshness-sensitive.

## Validation

- The entity remains a benchmark/dataset rather than an e-commerce agent framework or production platform.
- Long-horizon coherence claims remain tied to the released benchmark design and do not become generic claims about agent memory.

## Scoped original-source qualification — 2026-11-08

- **MerchantBench** is the original July 2026 research benchmark for persistent **seller-side e-commerce** decisions across **365 simulated days**, not a production commerce platform. The authors' paper reports a simulation grounded in **98,843 e-commerce product records**, with **26 tools** exposing sourcing, catalog/listing and pricing, cash-flow and order-level decisions with mixed-delay supplier/order feedback.
- The original evaluated eight model configurations under two agent frameworks in 48 runs. Publisher results, including human comparisons and final-net-asset scores, apply only to that simulator and resource/evaluator setup; they do not establish real merchant business outcomes, autonomous payment authority or reliable long-lived customer operations. Reused product-record source rights, personal data and simulation safety must be independently reviewed before redistributing corpora or running with privileged services.
- First-party sources: https://github.com/KhanCold/merchantbench ; https://arxiv.org/abs/2607.28956
- Source acceptance covers the distinct existing 2026 benchmark identity, original task/simulator method and public release scope only. No merchant simulation or agent/tool execution, independent underlying dataset rights/security/legal assessment, published score replication, global schema/cache/CI/render, clean or final gate.
