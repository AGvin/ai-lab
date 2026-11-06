# Documentation Requirements

## Requirements

- Identify Tenstorrent as the producer identity for released Tenstorrent hardware products represented in the catalog.
- Keep individual accelerator/system specifications and benchmark conditions with concrete hardware profiles.
- Render the standard `entity-relations` block from validated current-entity relations.
- Preserve this source-backed identity and provenance context: Tenstorrent produces the represented Galaxy Blackhole system and Wormhole n150/n300 accelerator-card family. The company also publishes hardware documentation and software for its platforms; individual cards, systems and software releases remain distinct products.
- Explain the following operating and decision boundary: Select the exact hardware variant and matching software stack. Wormhole installation requirements distinguish chassis clearance, airflow, power and board variants, so one card's installation or performance claims cannot be generalized to Galaxy systems or Blackhole-generation hardware. Verify current ordering availability and supported workloads with Tenstorrent; a product documentation page is not a stock or shipment guarantee.
- Support the producer context with these first-party sources: <https://tenstorrent.com/>, <https://docs.tenstorrent.com/aibs/wormhole/>.

## Validation

- `produces` is the inverse of Tenstorrent Galaxy Blackhole `produced-by`.
