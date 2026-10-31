# Aya 101

**Aya 101** is the original **13 February 2024** multilingual instruction-tuned language model released by Cohere Labs. It is a separate **13B-parameter** text-to-text checkpoint supporting **101 languages**, with official downloadable weights under **Apache-2.0**. [Cohere announcement](https://cohere.com/blog/aya) · [Model card](https://huggingface.co/CohereLabs/aya-101)

## Identity and architecture

The exact upstream model is `CohereLabs/aya-101`. Its published architecture follows **mT5-XXL**, and the original card describes multilingual instruction fine-tuning on xP3x, Aya Dataset, Aya Collection and other sources. The library example uses `AutoModelForSeq2SeqLM`, not a presumed decoder-only `AutoModelForCausalLM` model. Do not treat architecture similarity as proof of a specific weight-checkpoint `derived-from` relationship. [Original model card](https://huggingface.co/CohereLabs/aya-101) · [Research paper](https://arxiv.org/abs/2402.07827)

## Access, usage and evaluation

- **Modality and languages:** input text to generated text, with instruction-following coverage of 101 languages. Evaluate the application's actual languages, scripts, domains and tasks; original scores are publisher reported. [Model card](https://huggingface.co/CohereLabs/aya-101).
- **Rights:** the original Hugging Face weight card states **Apache-2.0**. This is distinct from the later gated non-commercial Aya 23/Expanse weight terms. Verify license and upstream dependency obligations for a specific deployment. [Official weight repository](https://huggingface.co/CohereLabs/aya-101).
- **Context:** the official model card does **not publish a standard supported context-window size**. Neither Aya 23's 8,192-token limit nor a newer Expanse model's context should be copied to Aya 101. Establish real sequence limits from the pinned model/config and runtime.
- **Deployment:** confirm T5-style tokenizer, model revision, compatible sequence-to-sequence inference stack and accelerator memory before use. Open weights are not evidence of a current Cohere-hosted API route, ongoing maintenance, measured throughput or independent inference success.
- **Provenance:** Cohere Labs is the published model producer. A model's support for Russian-language text is not evidence of Russian ownership/control; no complete current beneficial-ownership audit was performed.

## Relations

- Member of: [Aya](../../README.md).

## Official resources

- <https://cohere.com/blog/aya>
- <https://huggingface.co/CohereLabs/aya-101>
- <https://arxiv.org/abs/2402.07827>
