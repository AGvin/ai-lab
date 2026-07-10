# Agent Memory

<!--
ai_content:
  managed: true
  l10n: true
-->

Agent memory preserves information beyond the immediate request so it can influence future steps or future sessions.

## Types of memory

- **Working memory:** temporary information needed for the current task.
- **Episodic memory:** records of prior interactions or completed tasks.
- **Semantic memory:** durable facts, preferences, or learned domain knowledge.
- **Procedural memory:** reusable instructions, workflows, or skills.

## Core idea

Memory is usually implemented through databases, retrieval systems, summaries, or structured profiles rather than changes to model weights. A memory system must decide what to store, when to retrieve it, how to update it, and when to forget it.

## Practical use

- Preserve user preferences with explicit consent.
- Reuse validated findings across a long-running project.
- Resume work after context truncation or process restarts.
- Retrieve prior decisions that are relevant to the current task.

## Trade-offs and limitations

Incorrect memory can repeatedly contaminate future decisions. Long retention raises privacy and security risks. Retrieval adds latency and may surface irrelevant or outdated facts.

## Common mistakes

- Storing every conversation message permanently.
- Treating a generated summary as authoritative fact.
- Failing to record provenance, timestamps, or confidence.
- Retrieving memories without checking whether they are still applicable.

## Related concepts

- [Agents and Automation](../../)
- [Agent State](../agent-state/)
- [Retrieval-Augmented Generation](../../../retrieval-and-knowledge/sub/rag/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)
