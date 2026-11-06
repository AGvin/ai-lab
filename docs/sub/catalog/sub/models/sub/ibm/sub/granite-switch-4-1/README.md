# Granite Switch 4.1

Granite Switch 4.1 is IBM's composed language-model family with stable 8B and 30B checkpoints. Each integrates chat, decision and Guardian adapters and a speech encoder, enabling multiple documented modes through its chat-template and control-token contract.

## Family boundaries

The catalog represents two stable checkpoints. Preview releases and separately published adapter libraries have different lifecycle and ownership boundaries. A combined checkpoint does not imply that all deployment backends support every mode. Treat its embedded speech component as the bundled revision rather than automatically adopting later standalone TurboCTC updates.

IBM's 27 October 2026 **4.1.1** is an in-place release revision, not a new family or separate model node. It keeps the original 8B/30B language bases and the existing `decision` + `guardian-core` adapter design but updates `decision` weights and the embedded multilingual TurboCTC encoder. Both versions require revision pinning; the original 4.1 revision used English-only speech. [IBM release note](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) [8B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) [30B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b).

The 4.1.1 model cards list **seven** supported audio languages (English, French, German, Spanish, Portuguese, Italian and Japanese), with punctuated, capitalized output. The announcement says ten; the discrepancy is unresolved, so deployment guidance uses the narrower checkpoint-card list. The encoder is not jointly trained with the LLM, and transcription errors can change model responses or decisions. [8B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) [30B model card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) [Announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1).

The published weights use Apache-2.0; hosted terms differ. Consult the pinned model revision, supported runtime and audio/adapter compatibility before deployment.

## Models

- [Granite Switch 4.1 8B](./sub/models/sub/granite-switch-4-1-8b/)
- [Granite Switch 4.1 30B](./sub/models/sub/granite-switch-4-1-30b/)

## Official resources

- [IBM 8B checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-8b)
- [IBM 30B checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-30b)
- [IBM Granite Switch 4.1.1 patch release](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1)
