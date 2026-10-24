# Snowflake

Snowflake operates the managed Cortex model-inference API and currently maintains the separate TruLens evaluation and tracing framework. TruLens originated at TruEra; the project’s current site explicitly identifies Snowflake stewardship following the TruEra acquisition.

## Producer boundary

Serving external models does not make Snowflake their original trainer. Cortex Inference, AI Functions, Agents, Search and warehousing are distinct services even where they share an account and billing. Check account roles, model lifecycle, regional or cross-region processing and consumption charges for hosted inference. TruLens is independently deployable software whose storage, instrumentation and judge-model choices require their own data controls; using it does not itself require adopting the Cortex Inference API.

## Relations

- Produces: [Snowflake Cortex Inference API](../../../../../services/sub/model-apis/sub/snowflake-cortex-inference-api/)
- Maintains: [TruLens](../../../../../software/sub/evaluation-and-observability/sub/evaluation-frameworks/sub/trulens/)

## Official resources

- [Official source](https://www.snowflake.com/)
- [Cortex REST API](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api)
- [TruLens project and stewardship](https://www.trulens.org/)
- [TruEra acquisition announcement](https://www.snowflake.com/en/blog/snowflake-acquires-truera-to-bring-llm-ml-observability-to-data-cloud/)
- [TruLens evaluation in Snowflake](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-applications-trulens)
