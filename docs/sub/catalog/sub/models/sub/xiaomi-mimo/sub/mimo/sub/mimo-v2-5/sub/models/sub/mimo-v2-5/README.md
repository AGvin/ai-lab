# MiMo-V2.5

**MiMo-V2.5** is Xiaomi MiMo Team's separately published, open **sparse Mixture-of-Experts model** with **310B total / 15B active parameters**, supporting **up to 1 million tokens of context**. It is natively multimodal for understanding **text, images, video, and audio**; these modalities are input capabilities, not a guarantee of image or audio generation.

Xiaomi's release materials describe a hybrid sliding-window/global-attention language backbone with dedicated visual and audio encoders. The [official checkpoint](https://huggingface.co/XiaomiMiMo/MiMo-V2.5) is distributed under **MIT** at this exact model scope.

## Translations

- English

## Relations

- Member of: [MiMo V2.5 series](../../../../)

## Operational and evidence boundary

The publicly published trained model is distinct from the **MiMo-V2.5-Base** training checkpoint, third-party quantizations and hosted API routes. Xiaomi lists the `mimo-v2.5` **API model ID** as deprecated on October 21, 2026; that does not by itself revoke the open checkpoint. Provider benchmark, speed, deployment memory and agent-performance claims are not independent AI Lab test results. The 1M context ceiling is not an assurance of runtime compatibility or quality at that length.

## Official resources

- <https://huggingface.co/XiaomiMiMo/MiMo-V2.5>
- <https://mimo.xiaomi.com/mimo-v2-5>
- <https://mimo.mi.com/docs/en-US/quick-start/model>
