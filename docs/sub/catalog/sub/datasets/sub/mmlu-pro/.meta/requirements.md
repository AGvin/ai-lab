# Documentation Requirements

## Requirements

- Identify MMLU-Pro as a released more difficult multi-task language-understanding and reasoning benchmark derived from MMLU, introduced by the original research group and maintained in the TIGER AI Lab repository.
- Preserve MMLU-Pro's original curated multiple-choice questions with a larger answer set, 14 major tested disciplines, and evaluation protocol; keep it separate from MMLU, GPQA, MMMU, and other benchmarks measuring different workloads.
- Scope question counts, revisions, task splits, licenses, known data contamination, answer-extraction methods, prompt sensitivity, languages and current evaluated model coverage to first-party revisions.
- Distinguish the fixed benchmark dataset and reference evaluation scripts from live leaderboard state and third-party model submissions.
- Do not present a raw percent correct from MMLU-Pro as equivalent to accuracy on the original MMLU, across prompt/CoT policies, or across unreconciled dataset revisions.
- Preserve the canonical first-party producer relation and matching inverse.

## Validation

- The released dataset/benchmark identity remains distinct from evaluation software/harnesses, leaderboards and model submissions.
- Revision, scoring and methodology boundaries are explicit when numerical claims are made.
- Source links and reciprocal producer provenance resolve correctly.
