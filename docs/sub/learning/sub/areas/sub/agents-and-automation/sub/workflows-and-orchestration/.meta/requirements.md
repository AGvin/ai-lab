# Documentation Requirements

## Requirements

- Present Workflows and Orchestration as the Agents and Automation learning group for explicit control-flow patterns used to coordinate one or more agents/workers across stages, decisions, state transitions, delegation, branching, events, review, and human intervention.
- Teach workflow design from the smallest deterministic control structure outward: make state, transitions, ownership, acceptance/failure paths, permissions, side effects, retry/recovery, stopping conditions, and observability explicit before adding model-driven routing or multi-agent topology.
- Keep reusable abstract workflow semantics with `concepts/agents-and-autonomy/workflows-and-orchestration/`; this learning group owns practical design, implementation, evaluation, debugging, and pattern-selection pedagogy.
- Keep generic distributed-system reliability, event infrastructure, resource/capacity management, and production serving concerns with AI Engineering where they are not agent-specific; link those topics rather than duplicating them.
- Use the explicitly selected child topics from learning architecture; materialize only children with source-backed content/navigation value and do not infer unlisted sibling patterns.
- Explain that the current materialized subset begins with `graph-and-dag-workflows/` because its legacy source contains substantial graph-specific executable-state, branching/join, loop, side-effect, recovery, and framework-evidence material ready for migration.
- Preserve pattern-fit guidance: prefer simpler deterministic operations/pipelines when orchestration machinery adds no material value, and introduce graph/event/multi-agent controls only when dependency, state, recovery, ownership, or concurrency needs justify them.

## Validation

- The group is pedagogical and does not duplicate the canonical concept taxonomy.
- Generic AI-engineering concerns are linked rather than re-owned as agent-workflow semantics.
- Current navigation exposes only materialized children and does not imply unmaterialized selected topics are absent from the logical architecture.
- No workflow pattern is recommended solely because a framework supports it.
