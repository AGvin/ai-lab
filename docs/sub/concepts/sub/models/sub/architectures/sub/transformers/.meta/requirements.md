# Documentation Requirements

## Requirements

- Use the reader-facing title `Transformers`.
- Define the Transformer as a neural-network architecture family built around attention-based processing of token or element representations, combined with learned position-wise transformations and residual/normalization structure.
- Explain the original Transformer as an encoder-decoder architecture that replaced recurrent and convolutional sequence processing with attention mechanisms, while making clear that modern Transformer families include encoder-only, decoder-only, encoder-decoder, multimodal, sparse/MoE, and hybrid variants.
- Treat self-attention as a central Transformer mechanism but keep the detailed attention and self-attention definitions with their selected child concepts rather than duplicating them here.
- Explain that sequence/position information must be represented because attention alone does not inherently encode input order; implementations may use learned or fixed positional representations, relative position methods, rotary methods, or other mechanisms rather than one universal scheme.
- Distinguish Transformer architecture from language-model identity and scale. A Transformer need not be an LLM or language model, and an LLM classification does not by itself specify every architectural detail.
- Distinguish Transformer architecture from training objective and post-training. Autoregressive next-token prediction, masked modeling, instruction tuning, preference optimization, and other objectives/procedures are not part of the universal architecture definition.
- Qualify complexity claims: standard full self-attention forms pairwise interactions whose compute/memory cost grows quadratically with sequence length, while efficient, sparse, local, linearized, recurrent-memory, and hybrid variants can change this behavior.
- Do not treat parallel training/prefill, KV-cache behavior, long-context quality, factuality, interpretability, or persistent memory as intrinsic guaranteed properties of every Transformer; those depend on architecture variant, objective, runtime, and system design.
- Keep concrete model dimensions, context limits, runtime compatibility, benchmark results, serving/resource measurements, and model-selection guidance with their applicable catalog, evidence, inference, or decision owners.
- Use the canonical entity references as research inputs for original and current Transformer terminology when reader-facing rendering is activated.

## Validation

- The page does not equate `Transformer` with `LLM`, `decoder-only model`, or `generative AI`.
- Encoder-only, decoder-only, and encoder-decoder forms are treated as architecture variants rather than separate definitions of Transformer itself.
- Positional information is not tied to one fixed encoding method.
- Quadratic-cost claims are explicitly scoped to standard full attention rather than all Transformer variants.
- The page does not imply attention weights alone are a complete explanation of model reasoning or that longer context guarantees better recall/use.
- Legacy runtime/model-selection consequences are not duplicated into this canonical architecture node.
