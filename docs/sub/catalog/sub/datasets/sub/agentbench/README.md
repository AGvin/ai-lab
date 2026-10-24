# AgentBench

AgentBench is a released benchmark for evaluating language models acting as agents in interactive environments. The original ICLR 2024 benchmark covers eight environments, including operating-system, database, knowledge-graph, game and web/shopping tasks.

The first-party repository announced AgentBench FC on October 10, 2025: a function-calling version integrated with AgentRL and five containerized task types. Original v0.1/v0.2 evaluations and the FC harness have different task and prompting setups; their scores should not be treated as directly comparable.

The benchmark remains distinct from the AgentRL controller, Docker and Redis infrastructure, Freebase data service, live leaderboard, evaluated models and the separately released VisualAgentBench. Reproduce results against a pinned task revision, environment, prompt and token budget, and isolate the executable environments. THUDM provides the represented benchmark provenance; paper contributors and affiliations remain attributable to the corresponding research release.

## Relations

- Produced by: [THUDM](../../../producers/sub/t/sub/thudm/)

## Official resources

- <https://github.com/THUDM/AgentBench>
