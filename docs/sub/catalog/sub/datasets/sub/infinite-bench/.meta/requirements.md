# Documentation Requirements

## Requirements

- Identify InfiniteBench as one multi-task long-context evaluation benchmark, not an inference API, universal memory guarantee, independent catalog identity for each task or a copy of another LongBench release.
- The pinned README describes 12 distinct tasks with 100k+ token contexts and a mixture of synthetic and real-world scenarios. Task lengths, language and exact examples are task-specific.
- Record the dataset revision, task IDs, context length, tokenizer, truncation, prompt construction, output parsing and scoring script. Do not assert that a model supports a benchmark length merely because an API accepts a nominal 100k-token context.
- Root LICENSE is MIT for covered source. Original documents, books or third-party texts and their derived substitutions can carry separate dataset and reproduction constraints.
- Long-context evaluation has latency, memory and inference cost implications. Context retrieval, task scoring and output quality should be independently checked, rather than assuming token-length alone establishes reasoning skill.
- No benchmark data download, model evaluation, context-window compatibility test, rights audit or whole-catalog clean pass was performed.

## Validation

- Match one frozen dataset candidate with a canonical indexed entity and pinned first-party evidence.
- Do not count benchmark data as proof of legal rights, runtime evaluation or repository-wide clean validation.
