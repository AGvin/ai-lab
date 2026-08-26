# Documentation Requirements

## Requirements

- Use the reader-facing title `Diffusion Models`.
- Define diffusion models as generative/probabilistic model families built around a forward process that progressively corrupts data toward a simpler reference distribution and a learned reverse/denoising or score-based process that reconstructs or samples data by reversing that corruption dynamics.
- Present discrete-time denoising diffusion probabilistic models and continuous-time score/SDE formulations as closely related major families. Do not define the entire concept around one discrete scheduler, one denoising parameterization, or image-only DDPM implementations.
- Explain that the learned model can predict noise, clean data, velocity/other reparameterized targets, score functions, or related quantities depending on the formulation; one prediction target is not part of the universal definition.
- Distinguish the forward corruption/noising process used during training or mathematical construction from the reverse generative process used for sampling. Concrete parameterizations can use different variance/noise schedules or continuous dynamics.
- Distinguish diffusion models from latent diffusion. Diffusion can operate directly in data space or in a learned latent/representation space; using a VAE/autoencoder-compressed latent space is an important architecture pattern, not a requirement of diffusion itself.
- Distinguish diffusion models from text-to-image or image-generation concepts. Diffusion is a model/generative-process family that can be applied to images, audio, video, 3D, scientific data, actions/trajectories, or other domains; text conditioning and visual output are application/conditioning choices.
- Explain that conditioning can use labels, text/language representations, images, masks, structural signals, control inputs, or other context, but conditioning mechanism and classifier/classifier-free guidance are not universal diffusion requirements.
- Distinguish the learned diffusion model from the sampling/solver algorithm used to execute the reverse process. DDPM/DDIM-style samplers, numerical SDE/ODE solvers, predictor-corrector methods, accelerated/distilled samplers, and scheduler choices can change step count and behavior without changing the underlying concept boundary.
- Make clear that the number of sampling steps is not a direct quality measure. Fewer or more steps can interact with the trained model, solver/scheduler, guidance, numerical error, and task; compare concrete methods empirically rather than universalizing step counts.
- Explain that random seeds control only one source of stochasticity and do not by themselves guarantee reproducibility across model versions, schedulers, numerical precision, kernels, runtimes, hardware, preprocessing, or conditioning pipelines.
- Distinguish diffusion from autoregressive generation, GANs, normalizing flows, and masked/iterative generation while acknowledging hybrid architectures and formulations can combine mechanisms.
- Make clear that diffusion does not inherently solve compositionality, exact text rendering, spatial constraints, identity consistency, temporal consistency, factuality, or safety. These properties depend on model/data/conditioning/evaluation rather than the diffusion mechanism alone.
- Keep concrete checkpoints, latent autoencoders, conditioning encoders, schedulers/samplers, guidance scales, step counts, seeds, runtime implementations, benchmark results, and workflow/model-selection recommendations with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for discrete diffusion and continuous score-based generative modeling boundaries when reader-facing rendering is activated.

## Validation

- Diffusion models are not defined only as image generators or text-to-image systems.
- Latent-space operation, a VAE, classifier-free guidance, and one noise/sampling schedule are not stated as universal requirements.
- Discrete DDPM-style and continuous score/SDE formulations are represented without collapsing every detail into one implementation.
- Sampling step count, guidance strength, or seed is not presented as a universal quality/reproducibility guarantee.
- Diffusion is distinguished from the concrete sampler/solver and from other generative-model families.
- Concrete models, samplers, control systems, benchmark outcomes, and deployment recipes remain outside the abstract architecture owner.
