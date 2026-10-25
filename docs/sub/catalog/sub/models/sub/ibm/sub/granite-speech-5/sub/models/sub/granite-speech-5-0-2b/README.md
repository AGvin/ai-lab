# Granite Speech 5.0 2B

IBM approximately 2.3B-parameter speech-language checkpoint for multilingual transcription and speech translation. It is distinct from the 470M TurboCTC checkpoints.

## Tasks and constraints

The official card documents ASR in English, French, German, Spanish, Portuguese and Japanese, translation to and from English, and additional English-to-Italian and English-to-Mandarin modes. Prompt-dependent capabilities include language identification, punctuation, capitalization and keyword biasing up to 2000 entries. Segment longer audio; the card recommends chunks of about two minutes or less. Verify prompts, language coverage and quality for the deployment.

Published weights use Apache-2.0; hosted terms are separate. The intermediate Nano base used by the language component is not necessarily identical to final published base weights.

- [Granite Speech 5 family](../../../../)
- [Official IBM model card](https://huggingface.co/ibm-granite/granite-speech-5.0-2b)
