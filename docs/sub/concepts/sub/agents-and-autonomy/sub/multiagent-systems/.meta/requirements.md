# Documentation Requirements

## Requirements

- Use the reader-facing title `Multi-Agent Systems (MAS)`.
- Define a multi-agent system as a system containing multiple agent entities whose decisions or actions interact directly or indirectly through communication, shared/environment state, task dependencies, resource competition, delegation, review, negotiation, or other coordination mechanisms.
- Distinguish a multi-agent system from merely issuing several model calls, using an ensemble, running parallel samples, routing to non-agent components, or assigning several names to one shared decision process. Multiple components must function as agents under the applicable agent definition and participate in a system-level interaction structure.
- Explain that agents may cooperate, compete, negotiate, review, specialize, delegate, or pursue partially distinct objectives; cooperation is common in LLM applications but is not a universal MAS requirement.
- Present centralized, hierarchical, peer-to-peer, distributed, synchronous, asynchronous, shared-state, message-passing, and environment-mediated coordination as design dimensions/examples rather than one required taxonomy or architecture.
- Make clear that using several agents does not guarantee specialization, independent evidence, diversity, safety, or higher quality. Agents using similar models, prompts, sources, or shared state can produce strongly correlated errors and reinforce one another.
- Explain that system correctness depends on role/authority boundaries, communication and handoff contracts, shared-state ownership, conflict resolution, termination/cycle conditions, resource/side-effect coordination, and verification appropriate to the architecture.
- Distinguish multi-agent coordination from verification: debate, consensus, voting, or agreement among agents is evidence only under an explicitly evaluated aggregation/independence contract and is not automatic proof of correctness.
- Explain that multi-agent systems introduce coordination overhead, extra model/tool calls, state synchronization, latency, communication cost, race/conflict risks, and additional failure modes; more agents are not intrinsically preferable to a single agent or deterministic workflow.
- Preserve the legacy inventory of named multi-agent/orchestration patterns as migration source material only. Do not materialize orchestrator-worker, supervisor-specialist, handoff/swarm, group-chat, graph/DAG, planner-executor, blackboard, event-driven, review-board, or other unselected descendants merely because the legacy page enumerates them.
- Keep concrete multi-agent frameworks, architecture-pattern recommendations, model/team portfolios, benchmark results, organizational simulations, infrastructure/controller designs, and project-specific role graphs with their applicable catalog, engineering, evaluation, learning, or decision owners.
- Use the canonical entity references as research inputs for contemporary multi-agent collaboration dimensions and system-level boundaries when reader-facing rendering is activated.

## Validation

- The page does not classify multiple model calls, ensembles, or parallel generations as a multi-agent system by default.
- Cooperation, hierarchy, shared conversation, or one particular orchestration pattern is not required by the universal definition.
- Agent agreement/majority vote is not treated as independent verification by itself.
- Multi-agent systems are not presented as inherently more capable, reliable, safe, or efficient than simpler alternatives.
- No unselected legacy architecture-pattern descendants are materialized or implied as canonical children.
- Concrete architecture selection and model-team recommendations remain outside this abstract concept owner.
