from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .common import Repository, ToolingError


RELATION_PAIRS: tuple[tuple[str, str], ...] = (
    ("owns", "owned-by"),
    ("parent-of", "child-of"),
    ("has-part", "part-of"),
    ("has-member", "member-of"),
    ("produces", "produced-by"),
    ("maintains", "maintained-by"),
    ("operates", "operated-by"),
    ("has-discovery-resource", "discovery-resource-for"),
    ("has-version", "version-of"),
    ("has-artifact", "artifact-of"),
    ("has-derivative", "derived-from"),
    ("has-learning-resource", "learning-resource-for"),
)

INVERSE = {
    relation: inverse
    for pair in RELATION_PAIRS
    for relation, inverse in (pair, (pair[1], pair[0]))
}


@dataclass(frozen=True)
class EntityRecord:
    entity_id: str
    node: Path
    path: Path
    data: dict[str, Any]


@dataclass(frozen=True)
class Edge:
    source: str
    relation: str
    target: str
    source_path: str


@dataclass
class RelationValidationResult:
    errors: list[str] = field(default_factory=list)
    statistics: dict[str, int] = field(
        default_factory=lambda: {relation: 0 for pair in RELATION_PAIRS for relation in pair}
    )

    @property
    def ok(self) -> bool:
        return not self.errors

    def statistics_lines(self) -> list[str]:
        return [
            f"{left} / {right} — {self.statistics[left]} / {self.statistics[right]}"
            for left, right in RELATION_PAIRS
        ]


class RelationValidator:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.aliases = repo.load_aliases()

    def _logical_id_for_node(self, node: Path) -> str:
        parts = node.resolve().relative_to(self.repo.docs_root).parts
        logical = [part for part in parts if part != "sub"]
        return "/".join(logical)

    def _entity_paths(self) -> list[Path]:
        paths = []
        for path in self.repo.docs_root.rglob(".meta/entity.yml"):
            if "l10n" in path.relative_to(self.repo.docs_root).parts:
                continue
            paths.append(path)
        return sorted(paths)

    def _build_index(self, result: RelationValidationResult) -> dict[str, EntityRecord]:
        index: dict[str, EntityRecord] = {}
        for path in self._entity_paths():
            try:
                root = self.repo.load_yaml(path)
            except ToolingError as exc:
                result.errors.append(str(exc))
                continue
            entity = root.get("entity")
            if not isinstance(entity, dict) or not isinstance(entity.get("id"), str):
                result.errors.append(f"{self.repo.repo_path(path)}: entity.id is required")
                continue
            entity_id = entity["id"]
            node = path.parent.parent
            expected = self._logical_id_for_node(node)
            if entity_id != expected:
                result.errors.append(
                    f"{self.repo.repo_path(path)}: entity id/path mismatch: expected {expected!r}, got {entity_id!r}"
                )
            if entity_id in index:
                result.errors.append(
                    f"duplicate entity id {entity_id!r}: {index[entity_id].path} and {self.repo.repo_path(path)}"
                )
                continue
            index[entity_id] = EntityRecord(entity_id, node, path, entity)
        return index

    def _expand_path_alias(self, raw: str) -> str:
        if ":" not in raw:
            return raw
        alias, suffix = raw.split(":", 1)
        paths = self.aliases.get("paths", {}) if isinstance(self.aliases, dict) else {}
        if not isinstance(paths, dict) or alias not in paths:
            raise ToolingError(f"unresolved path alias: {raw}")
        prefix = paths[alias]
        if not isinstance(prefix, str):
            raise ToolingError(f"path alias {alias!r} must be a string")
        return prefix + suffix

    def _normalize_node_path(self, source_node: Path, raw: str) -> Path:
        expanded = self._expand_path_alias(raw)
        if expanded.startswith("/"):
            candidate = self.repo.docs_root / expanded.lstrip("/")
        else:
            candidate = source_node / expanded
        resolved = candidate.resolve()
        docs = self.repo.docs_root.resolve()
        if resolved != docs and docs not in resolved.parents:
            raise ToolingError(f"relation path escapes documentation root: {raw}")
        return resolved

    def _resolve_target(self, record: EntityRecord, target: Any, index: dict[str, EntityRecord]) -> str:
        if isinstance(target, str):
            target_id = target
        elif isinstance(target, dict) and set(target) == {"id"} and isinstance(target["id"], str):
            target_id = target["id"]
        elif isinstance(target, dict) and set(target) == {"path"} and isinstance(target["path"], str):
            node = self._normalize_node_path(record.node, target["path"])
            entity_path = node / ".meta" / "entity.yml"
            if not entity_path.is_file():
                raise ToolingError(
                    f"unresolvable relation target path {target['path']!r}: no {self.repo.repo_path(entity_path)}"
                )
            root = self.repo.load_yaml(entity_path)
            entity = root.get("entity")
            if not isinstance(entity, dict) or not isinstance(entity.get("id"), str):
                raise ToolingError(
                    f"unresolvable relation target path {target['path']!r}: target entity has no id"
                )
            target_id = entity["id"]
        else:
            raise ToolingError(f"invalid relation target locator: {target!r}")
        if target_id not in index:
            raise ToolingError(f"unresolvable relation target: {target_id!r}")
        return target_id

    def validate(self) -> RelationValidationResult:
        result = RelationValidationResult()
        index = self._build_index(result)
        edges: list[Edge] = []
        seen: set[tuple[str, str, str]] = set()

        for source_id in sorted(index):
            record = index[source_id]
            relations = record.data.get("relations", [])
            if relations is None:
                relations = []
            if not isinstance(relations, list):
                result.errors.append(f"{self.repo.repo_path(record.path)}: entity.relations must be an array")
                continue
            for relation_record in relations:
                if not isinstance(relation_record, dict):
                    result.errors.append(f"{self.repo.repo_path(record.path)}: invalid relation record")
                    continue
                relation = relation_record.get("type")
                if not isinstance(relation, str) or relation not in INVERSE:
                    result.errors.append(f"{self.repo.repo_path(record.path)}: unknown relation type: {relation!r}")
                    continue
                result.statistics[relation] += 1
                try:
                    target_id = self._resolve_target(record, relation_record.get("target"), index)
                except ToolingError as exc:
                    result.errors.append(f"{self.repo.repo_path(record.path)}: {exc}")
                    continue
                key = (source_id, relation, target_id)
                if key in seen:
                    result.errors.append(
                        f"{self.repo.repo_path(record.path)}: duplicate logical edge: {source_id} -[{relation}]-> {target_id}"
                    )
                    continue
                seen.add(key)
                if source_id == target_id:
                    result.errors.append(
                        f"{self.repo.repo_path(record.path)}: self relation is not allowed: {source_id} -[{relation}]-> {target_id}"
                    )
                edges.append(Edge(source_id, relation, target_id, self.repo.repo_path(record.path)))

        edge_set = {(edge.source, edge.relation, edge.target) for edge in edges}
        for edge in edges:
            inverse = INVERSE[edge.relation]
            expected = (edge.target, inverse, edge.source)
            if expected not in edge_set:
                result.errors.append(
                    f"{edge.source_path}: missing inverse: {edge.source} -[{edge.relation}]-> "
                    f"{edge.target}; expected {edge.target} -[{inverse}]-> {edge.source}"
                )
        return result
