# Zyte API

Zyte API is Zyte's hosted web extraction and browser-assisted retrieval service, with REST extraction, proxy transport, managed extraction, browser requests, live CDP access and a documented Search API.

## Access and state boundaries

HTTP extraction, proxy requests, managed browser requests and live CDP connections offer different capabilities. A browser-request session is not a persistent single browser or tab. CDP supplies a live browser with its own IP and cookie jar; separate connections cannot inherit a past CDP session's state.

Current CDP documentation requires a paid subscription or configured pay-as-you-go spending limit and completed business verification. Verify supported outputs, target sites, geo settings, rate limits and billing for the selected mode; proxy transport does not imply every REST capability. Destination permissions, authentication, personal data and retained outputs require their own review.

## Product scope

Zyte API is distinct from the Scrapy framework and Scrapy Cloud spider-job hosting. Its SDKs, coding-agent add-ons and API modes remain access surfaces unless separate lifecycle evidence establishes a new product.

## Relations

- Produced by: [Zyte](../../../../../producers/sub/z/sub/zyte/)

## Official resources

- [Official website](https://www.zyte.com/)
- [Zyte API and access modes](https://docs.zyte.com/zyte-api/get-started.html)
- [CDP browser and session boundary](https://docs.zyte.com/zyte-api/usage/cdp.html)
