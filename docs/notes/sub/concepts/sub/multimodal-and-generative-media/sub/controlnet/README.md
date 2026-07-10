# ControlNet

ControlNet conditions diffusion generation with structural information such as edges, depth, pose, segmentation, line art, or surface normals.

## Core idea

A control model processes a structural map and injects its guidance into the diffusion network. This lets the prompt determine appearance while the control signal constrains layout or geometry. Different ControlNet models are trained for different map types and base-model families.

## Practical use

- Preserve pose or composition from a reference.
- Convert sketches or line art into rendered images.
- Maintain room geometry using depth maps.
- Follow edge structure while changing style.
- Generate consistent layouts from segmentation maps.

## Trade-offs and limitations

Strong control can reduce creativity or conflict with the prompt. Weak control may not preserve structure. Preprocessor errors become generation constraints, and mismatched model families can produce poor results.

## Common mistakes

- Using a control model built for another base model.
- Applying excessive control strength throughout all denoising steps.
- Treating a noisy depth or pose map as accurate geometry.
- Combining several controls without balancing their influence.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Diffusion Models](../diffusion-models/)
- [Image-to-Image](../image-to-image/)
- [Latent Space](../latent-space/)
