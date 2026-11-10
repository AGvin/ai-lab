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

## Scoped original-source qualification — 2026-11-08

- **MMLU-Pro** is the released **TIGER AI Lab / NeurIPS 2024** enhanced knowledge-and-reasoning benchmark, not an alias for original MMLU. The publisher reports **over 12,000 curated questions across 14 subject areas**, typically with **ten** multiple-choice answers rather than the four in original MMLU; its question selection and protocol are distinct.
- The author's `TIGER-AI-Lab/MMLU-Pro` repository supplies evaluator code and the `TIGER-Lab/MMLU-Pro` question distribution. Chain-of-thought versus direct-answer prompting, answer extraction, exact dataset revision and prompt styles materially condition the scores. Historical author-reported model measurements are not independently reproduced here.
- First-party sources: https://github.com/TIGER-AI-Lab/MMLU-Pro ; https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro ; https://arxiv.org/abs/2406.01574
- Original-source credit covers the existing published dataset identity, author provenance, public corpus and evaluation-method boundaries only. No live evaluation, question-by-question or dataset rights audit, contamination guarantee, full repository validation, clean or final gate.
