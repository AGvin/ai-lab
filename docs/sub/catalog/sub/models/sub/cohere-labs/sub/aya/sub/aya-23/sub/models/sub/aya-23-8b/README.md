# Aya 23 8B

**Aya 23 8B** is Cohere Labs and Cohere's separately published **8B** multilingual text-generation model from the **23 May 2024 Aya 23** research release. The official `CohereLabs/aya-23-8B` card specifies **8,192 tokens** of context and **23 languages**. [Model card](https://huggingface.co/CohereLabs/aya-23-8B) · [Cohere announcement](https://cohere.com/blog/aya23)

## Identity and training scope

This is an instruction-tuned research-weight checkpoint, not Aya Expanse 8B, Aya Vision, a vector embedding service, a quantized duplicate or a hosted endpoint entitlement. The card documents a pretrained Command-family foundation plus Aya-related multilingual data, **without identifying one exact concrete Command checkpoint** as its training parent. Claimed multilingual evaluation is publisher-reported and must be reproduced on target languages and tasks. [Publisher card](https://huggingface.co/CohereLabs/aya-23-8B).

## Usage and deployment boundaries

- Use text input to generate text. Budget prompt and output within the **8,192-token** context; no image understanding or newer Expanse 128K context is established. [Model configuration/usage](https://huggingface.co/CohereLabs/aya-23-8B).
- Model download is **gated**: accept the published conditions before using weights. License is **CC-BY-NC-4.0** with the Cohere Labs acceptable-use policy and license addendum; do not assume unrestricted commercial rights. [Repository terms](https://huggingface.co/CohereLabs/aya-23-8B).
- The 8B parameters require lower inference memory relative to Aya 23 35B; actual VRAM, quantized variants, hardware compatibility and output quality depend on implementation and testing. Pin the official model revision, matching tokenizer, chat template and Transformers/runtime versions. [Usage instructions](https://huggingface.co/CohereLabs/aya-23-8B).
- Current Hugging Face page does not itself prove current Cohere API availability, benchmark advantage, independent inference success, or Russian beneficial ownership/control. No such independent assessment was performed.

## Relations

- Member of: [Aya 23](../../../../README.md).

## Official resources

- <https://huggingface.co/CohereLabs/aya-23-8B>
- <https://cohere.com/blog/aya23>
