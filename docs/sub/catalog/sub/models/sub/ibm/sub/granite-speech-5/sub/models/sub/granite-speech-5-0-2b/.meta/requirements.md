# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-speech-5.0-2b` and its Apache-2.0 weight license.
- The 20 October 2026 release supports ASR in English, French, German, Spanish, Portuguese and Japanese, with translation to/from English; the card additionally describes English-to-Italian and English-to-Mandarin.
- Keep language-ID, keyword biasing up to 2000 entries, punctuation and capitalization tied to the documented prompts. Segment longer audio; the card recommends chunks up to about two minutes.
- This is distinct from the 470M TurboCTC and NC checkpoints. Its language model uses an intermediate Nano base checkpoint; do not assert identity with the final published base weights.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
