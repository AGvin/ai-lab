# Retrieval Poisoning

<!--
ai_content:
  managed: true
  l10n: true
-->

Retrieval poisoning manipulates indexed knowledge so a search or RAG system supplies misleading, malicious, or instruction-bearing content.

## Core idea

An attacker may add documents containing false claims, optimized keywords, hidden text, or prompt-injection instructions. Because the system retrieves these documents as evidence, the model may repeat or act on them with apparent grounding.

## Risk factors

- User-controlled ingestion sources.
- Automatic indexing without review.
- Weak provenance and version tracking.
- Ranking based only on similarity.
- Agents with tools that act on retrieved instructions.

## Mitigation

Restrict ingestion, verify source identity, scan content, preserve provenance, use trust-weighted retrieval, and separate factual extraction from instruction execution. Evaluate retrieval against adversarial documents and conflicting sources.

## Common mistakes

- Assuming internal search results are trusted.
- Using citation presence as proof of source quality.
- Allowing retrieved text to control tools.
- Failing to remove compromised documents and derived embeddings.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Indirect Prompt Injection](../indirect-prompt-injection/)
- [Provenance](../provenance/)
- [RAG](../../../retrieval-and-knowledge/sub/rag/)
