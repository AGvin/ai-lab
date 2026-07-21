# Metadata Filtering

Metadata filtering restricts retrieval using structured attributes such as source, date, language, tenant, product, document version, or access policy.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Semantic or lexical similarity alone cannot express every retrieval requirement. Filters reduce the candidate space before or during search and help ensure that results belong to the correct user, project, time range, or document class.

## Practical use

- Enforce tenant and repository boundaries.
- Retrieve only current document versions.
- Restrict results by product, locale, or content type.
- Exclude archived or unapproved sources.
- Search within a user-selected collection.

## Design considerations

Distinguish search convenience filters from security authorization. Security-sensitive filters must be enforced by the data layer and must not depend on model-generated metadata. Normalize metadata values and define update behavior when source documents change.

## Trade-offs and limitations

Strict filters can reduce recall when metadata is missing or incorrect. Complex filter expressions may also limit index performance or behave differently across vector databases.

## Common mistakes

- Letting the model choose an unrestricted tenant ID.
- Storing inconsistent dates or category labels.
- Applying filters after unauthorized content has already been returned.
- Forgetting to update metadata when documents are replaced.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Vector Databases](../vector-databases/)
- [Trust Boundaries](../../../safety-privacy-and-reliability/sub/trust-boundaries/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)