# Documentation Requirements

## Requirements

- Present this scenario for several or tens of developers sharing coding assistants/agents, repositories, review practices, budgets, and acceptance responsibilities rather than for one engineer choosing a personal tool.
- Preserve a managed coding-agent pilot with products such as Cursor, Codex, or Claude Code as the low-infrastructure team route; evaluate representative repositories/users, usage distribution, code-data path, correction rate, review burden, and cost attribution rather than seat price alone.
- Preserve shared bounded local/self-hosted workers such as Qwen2.5-Coder 7B Instruct for lower-risk coding and Gemma 4 E4B Instruct for bounded multimodal developer tasks when task routing, logging, and acceptance tests demonstrate value.
- Preserve a shared coding-agent specialist such as Qwen3-Coder-Next only as an evaluation candidate on appropriately measured infrastructure; exact artifact, context, concurrency, runtime, accepted-result quality, and operational burden must be validated.
- Require coding agents that execute commands or modify files to run with appropriate sandboxing/VM/container isolation, least privilege, approval gates, bounded retries, and independent verification of completion.
- State that a local/self-hosted model endpoint does not prove the complete coding-client path is local; review the exact IDE/agent/provider chain before sending proprietary or confidential source code.
- Keep coding-task candidate/ranking evidence in `catalog/models/selection/decision-guides/software-development/` and agent-loop safeguards in `catalog/models/selection/decision-guides/agents-and-automation/`; this scenario owns team-level adoption/routing/review economics.
- Split centralized gateway, organization-wide identity, budgets, logging, provider contracts, and shared-platform ownership into `organizations/internal-ai-platform/` rather than duplicating full platform concerns here.
- Evaluate sustained team usage, uneven included quotas, shared-worker utilization, retries, engineer review, incident/risk burden, and total cost per accepted change when deciding whether to move beyond managed pilots.
- Escalate from a team-level route when centralized organization policy/platform ownership or cross-team shared access becomes the primary constraint.

## Validation

- The scenario remains a bounded software-development team workflow rather than organization-wide AI platform design.
- Agent execution includes isolation, least privilege, approval, and verification requirements.
- Local model access is not treated as proof that the complete coding client/data path is local.
- Central gateway/identity/budget/contract concerns are delegated to the organization platform scenario.
