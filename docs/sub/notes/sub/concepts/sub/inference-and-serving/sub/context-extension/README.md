# Context Extension

Context extension groups techniques used to increase a model's usable context length beyond its native or default configuration.

This category includes methods that adapt positional encoding or related context handling for longer sequences.

## Methods

- [`yarn/`](./sub/yarn/) — YaRN extends the usable context window of RoPE-based transformer models.
- [`ntk-aware-scaling/`](./sub/ntk-aware-scaling/) — NTK-aware scaling extends RoPE context by rescaling the rotary frequency base.
- [`longrope/`](./sub/longrope/) — LongRoPE uses non-uniform positional interpolation and searched rescaling factors for longer contexts.
- [`position-interpolation/`](./sub/position-interpolation/) — Position Interpolation rescales position indices so longer sequences fit within the original positional range.
