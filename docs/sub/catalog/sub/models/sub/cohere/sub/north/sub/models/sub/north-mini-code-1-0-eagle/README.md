# North Mini Code 1.0 Eagle draft

This is a small learned EAGLE speculative-decoding draft model published separately for use alongside the full North Mini Code 1.0 coding model.

## Identity and provenance

The original `CohereLabs/North-Mini-Code-1.0-eagle` repository lists BF16 safetensors (~79.2M reported parameters), three dense sliding-window transformer draft layers and Apache-2.0 licensing. It is neither the 30B total/3B active target generator nor an FP8/W4A16 precision package. Publisher naming establishes compatibility, not independently proven weight derivation or all developers' identities. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle) [Official repository README](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle/blob/main/README.md) [Target card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).

## Decision and operating boundaries

- The draft proposes speculative decoding candidates; the compatible North Mini Code target verifies them. Do not use the draft alone as a full coding/chat model or count a served target plus draft as one identical model checkpoint. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- The official card demonstrates vLLM EAGLE with `num_speculative_tokens=3` and a separate `model` identifier; supported target FP8/W4A16 formats are publisher-reported, not AI Lab compatibility tests. The example's `--max-model-len 320000` is a server flag and does not prove the draft has a standalone 320K native context. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- Published weights carry Apache-2.0 metadata; verify model/target contracts, selected hardware, runtime release, access, memory, performance and any price/data residency separately. Speculative decoding can add overhead; no unqualified latency or output quality benefit is established here. [Target model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- No local weight download, inference, accuracy or speed measurement, independently confirmed full corporate ownership review or Russian-control classification was conducted.

## Catalog relations

- [North](../../../../) — family.

## Related target

- [North Mini Code 1.0](../north-mini-code-1-0/) — compatible full target model (compatibility only, not a trained-from assertion).

## Official resources

- [North Mini Code Eagle draft](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- [Official Eagle draft README](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle/blob/main/README.md).
- [North Mini Code target](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).
