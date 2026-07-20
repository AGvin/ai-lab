# Numerical Precision

Numerical precision defines the number format used to represent model weights, activations, gradients, and caches.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Precision affects memory consumption, numerical range, rounding error, and hardware performance. FP32 provides broad compatibility and precision but uses more memory. FP16, BF16, FP8, and integer formats reduce storage or compute requirements with different range and accuracy characteristics.

## Important distinctions

- **Weight precision:** how model parameters are stored.
- **Compute precision:** the format used during matrix operations.
- **Activation precision:** how intermediate values are represented.
- **Accumulation precision:** the format used when summing many products.
- **KV-cache precision:** the format used for attention cache values.

## Practical use

Check which formats the model, runtime, and hardware support natively. Mixed-precision inference may store weights at low precision while accumulating at a higher precision to preserve stability.

## Trade-offs and limitations

Lower precision can increase speed and reduce memory, but unsupported formats may fall back to slower conversion paths. A format with fewer bits may have a wider numerical range than another format because exponent and mantissa layouts differ.

## Common mistakes

- Treating BF16 and FP16 as interchangeable.
- Assuming stored precision equals compute precision.
- Ignoring accumulation precision in stability-sensitive operations.
- Comparing “8-bit” formats without identifying the actual representation.

## Related concepts

- [Inference and Serving](../../)
- [Quantization](../quantization/)
- [Model Formats](../model-formats/)
- [KV Cache](../kv-cache/)
