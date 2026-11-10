# AlphaFold 3

AlphaFold 3 is the Google DeepMind and Isomorphic Labs structure-prediction model; academic weights and GA commercial Cloud deployment are access paths to the model, not separate model identities.

## Relations

- Member of: [AlphaFold](../../../../)

## Source-scoped operating boundaries

- The Cloud deployment is GA but allowlisted and requires a commercial subscription; the separately documented downloadable weights are for non-commercial academic research. [Access and license boundary](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/alphafold-3).
- Cloud inference writes structures to Cloud Storage under a serving identity. Deployment, inference, and bucket permissions are separate operational responsibilities; published GPU recipes do not determine access rights. [Deployment identities and storage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/alphafold-3).
- Google identifies AlphaFold 3 as a research tool that is not intended or cleared for clinical diagnostic use. [Use limitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/alphafold-3).

## Official resources

- <https://deepmind.google/science/alphafold/>
- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/alphafold-3>
- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes>
