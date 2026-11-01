# IFEval

IFEval is Google's English prompt-and-constraint dataset for evaluating whether language-model responses satisfy verifiable instructions. Examples concern response length, required keywords and output formatting. The [original research](https://arxiv.org/abs/2311.07911) and [Google dataset card](https://huggingface.co/datasets/google/IFEval) describe a published research dataset; the accompanying repository is not an officially supported Google product.

## Dataset boundary

The data pairs prompts with instruction identifiers and constraint arguments. Preserve the exact data revision when comparing runs. Public evaluation prompts should remain separate from training material when measuring held-out performance; a Hub split labeled `train` does not establish an uncontaminated evaluation split.

The original dataset is distinct from checker software, leaderboard views and its use as a workload in [MLPerf Mobile v6.0](../mlperf-mobile-v6-0/). A suite's device results do not replace the source dataset or establish general instruction-following quality.

## Evaluation compatibility

The [original checker](https://github.com/google-research/google-research/blob/master/instruction_following_eval/evaluation_lib.py) distinguishes strict and loose evaluation, and prompt-level and instruction-level results. Loose checks can transform a response before judging constraints. Record the data/checker revisions and exact result label instead of comparing unlabeled accuracy values.

Passing formal constraints does not establish factuality, safety or broad semantic understanding. No model was run or benchmarked for this profile.

## License and provenance

The Google Hub card declares Apache-2.0 for the dataset. Its reviewed file inventory did not list a standalone LICENSE. The [Google Research LICENSE](https://github.com/google-research/google-research/blob/master/LICENSE) and checker headers separately establish Apache-2.0 for code; they are not a complete independent audit of underlying data rights.

Publisher attribution is established; exhaustive beneficial ownership, indirect holdings and sanctions status were not verified.

## Provenance

- Produced by: [Google](../../../producers/sub/g/sub/google/).

## Official resources

- [Google dataset and card](https://huggingface.co/datasets/google/IFEval)
- [Original research source](https://github.com/google-research/google-research/tree/master/instruction_following_eval)
- [Original paper](https://arxiv.org/abs/2311.07911)
- [Original checker](https://github.com/google-research/google-research/blob/master/instruction_following_eval/evaluation_lib.py)
- [Google Research code license](https://github.com/google-research/google-research/blob/master/LICENSE)
