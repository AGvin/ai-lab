from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from .common import Repository, ToolingError


REFERENCE_TYPES: tuple[str, ...] = (
    "official-site",
    "product-page",
    "documentation",
    "repository",
    "specification",
    "registry",
    "distribution",
    "artifact",
    "release-notes",
    "issue-tracker",
    "article",
    "paper",
    "book",
    "terms-of-service",
    "privacy-policy",
    "security",
    "license",
    "other",
)

_REFERENCE_TYPE_SET = frozenset(REFERENCE_TYPES)
_REFERENCE_TYPE_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class ReferenceValidationResult:
    checked: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


class ReferenceValidator:
    """Validate extensible reference vocabularies that are not closed by JSON Schema."""

    def __init__(self, repo: Repository):
        self.repo = repo

    def _entity_paths(self) -> list[Path]:
        paths: list[Path] = []
        for path in self.repo.docs_root.rglob(".meta/entity.yml"):
            if "l10n" in path.relative_to(self.repo.docs_root).parts:
                continue
            paths.append(path)
        return sorted(paths)

    def validate(self) -> ReferenceValidationResult:
        result = ReferenceValidationResult()
        for path in self._entity_paths():
            try:
                root = self.repo.load_yaml(path)
            except ToolingError:
                # Structural/schema validation reports YAML loading failures.
                continue
            entity = root.get("entity")
            if not isinstance(entity, dict):
                continue
            references = entity.get("references", [])
            if not isinstance(references, list):
                continue
            for index, reference in enumerate(references):
                if not isinstance(reference, dict):
                    continue
                reference_type = reference.get("type")
                if not isinstance(reference_type, str):
                    continue
                result.checked += 1
                # Malformed tokens belong to JSON Schema structural validation.
                if not _REFERENCE_TYPE_PATTERN.fullmatch(reference_type):
                    continue
                if reference_type in _REFERENCE_TYPE_SET:
                    continue
                result.errors.append(
                    f"{self.repo.repo_path(path)}: entity.references.{index}.type: "
                    f"unapproved reference type {reference_type!r}; "
                    f"approved values: {', '.join(REFERENCE_TYPES)}"
                )
        return result


__all__ = ["REFERENCE_TYPES", "ReferenceValidationResult", "ReferenceValidator"]
