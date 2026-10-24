from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource

from .common import Repository, SchemaRef, ToolingError


@dataclass
class SchemaValidationResult:
    checked: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


class SchemaValidator:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.registry_map = repo.build_schema_registry()
        self.schemas: dict[tuple[str, str], dict[str, Any]] = {}
        self.resource_registry = Registry()
        self.registry_errors: list[str] = []
        self._load_registry_resources()

    def _load_registry_resources(self) -> None:
        for type_name in sorted(self.registry_map):
            for schema_id, repo_path in sorted(self.registry_map[type_name].items()):
                path = self.repo.root / repo_path
                identity = f"/:{type_name}:{schema_id}"
                uri = f"repo:{identity}"
                try:
                    schema = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    self.registry_errors.append(f"{repo_path}: invalid JSON schema: {exc}")
                    continue
                if not isinstance(schema, dict):
                    self.registry_errors.append(f"{repo_path}: schema resource must be an object")
                    continue
                if schema.get("$id") != uri:
                    self.registry_errors.append(
                        f"{repo_path}: schema $id mismatch: expected {uri!r}, got {schema.get('$id')!r}"
                    )
                try:
                    Draft202012Validator.check_schema(schema)
                    resource = Resource.from_contents(schema)
                except Exception as exc:
                    self.registry_errors.append(f"{repo_path}: invalid Draft 2020-12 schema: {exc}")
                    continue
                self.schemas[(type_name, schema_id)] = schema
                self.resource_registry = self.resource_registry.with_resource(uri, resource)

    def _direct_schema(self, type_name: str, selector: str) -> SchemaRef:
        if not isinstance(selector, str) or not selector:
            raise ToolingError(f"invalid {type_name} schema selector: {selector!r}")
        schema_id = selector[2:] if selector.startswith("/:") else selector
        if not schema_id or ":" in schema_id:
            raise ToolingError(f"invalid explicit root schema selector: {selector}")
        path = self.registry_map.get(type_name, {}).get(schema_id)
        if path is None:
            raise ToolingError(f"schema not found: /:{type_name}:{schema_id}")
        identity = f"/:{type_name}:{schema_id}"
        return SchemaRef(type_name, schema_id, identity, f"repo:{identity}", path)

    def _validate_document(
        self,
        result: SchemaValidationResult,
        path: Path,
        type_name: str,
        selector: str | None,
        *,
        direct: bool = False,
    ) -> None:
        result.checked += 1
        repo_path = self.repo.repo_path(path)
        if not selector:
            result.errors.append(f"{repo_path}: missing effective {type_name} schema selector")
            return
        try:
            ref = self._direct_schema(type_name, selector) if direct else self.repo.resolve_schema(type_name, selector)
        except ToolingError as exc:
            result.errors.append(f"{repo_path}: {exc}")
            return
        schema = self.schemas.get((ref.type_name, ref.schema_id))
        if schema is None:
            result.errors.append(
                f"{repo_path}: selected schema unavailable after registry validation: {ref.identity} ({ref.path})"
            )
            return
        try:
            document = self.repo.load_yaml(path)
            validator = Draft202012Validator(schema, registry=self.resource_registry)
            errors = sorted(validator.iter_errors(document), key=lambda error: list(error.absolute_path))
        except (ToolingError, SchemaError) as exc:
            result.errors.append(f"{repo_path}: schema validation setup failed: {exc}")
            return
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            result.errors.append(
                f"{repo_path}: {location}: {error.message} "
                f"[selector={selector!r} schema={ref.identity} path={ref.path}]"
            )

    @staticmethod
    def _deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
        result = deepcopy(base)
        for key, value in overlay.items():
            if isinstance(value, dict) and isinstance(result.get(key), dict):
                result[key] = SchemaValidator._deep_merge(result[key], value)
            else:
                result[key] = deepcopy(value)
        return result

    def _default_config(self) -> dict[str, Any]:
        path = self.repo.meta_root / "defaults.yml"
        return self.repo.load_yaml(path) if path.is_file() else {}

    def _parent_map(self, nodes: list[Path]) -> dict[Path, Path | None]:
        root = self.repo.docs_root.resolve()
        node_set = set(nodes)
        result: dict[Path, Path | None] = {}
        for node in nodes:
            if node == root:
                result[node] = None
                continue
            candidate = node.parent
            parent = None
            while candidate == root or root in candidate.parents:
                if candidate in node_set:
                    parent = candidate
                    break
                if candidate == root:
                    break
                candidate = candidate.parent
            result[node] = parent or root
        return result

    def _validate_aliases(self, result: SchemaValidationResult) -> None:
        path = self.repo.meta_root / "aliases.yml"
        if not path.is_file():
            return
        try:
            data = self.repo.load_yaml(path)
            aliases = data.get("aliases")
            selector = aliases.get("schema") if isinstance(aliases, dict) else None
        except ToolingError as exc:
            result.checked += 1
            result.errors.append(str(exc))
            return
        self._validate_document(result, path, "aliases", selector, direct=True)

    def _validate_entities(self, result: SchemaValidationResult, defaults: dict[str, Any]) -> None:
        entity_default = defaults.get("entity", {})
        default_selector = entity_default.get("schema") if isinstance(entity_default, dict) else None
        for path in sorted(self.repo.docs_root.rglob(".meta/entity.yml")):
            rel_parts = path.relative_to(self.repo.docs_root).parts
            if "l10n" in rel_parts:
                continue
            try:
                data = self.repo.load_yaml(path)
                entity = data.get("entity")
                selector = entity.get("schema", default_selector) if isinstance(entity, dict) else default_selector
            except ToolingError as exc:
                result.checked += 1
                result.errors.append(str(exc))
                continue
            self._validate_document(result, path, "entity", selector)

    def _validate_nodes(self, result: SchemaValidationResult, defaults: dict[str, Any]) -> None:
        default_node = defaults.get("node", {})
        if not isinstance(default_node, dict):
            default_node = {}
        root_selector = default_node.get("schema")
        root_children = deepcopy(default_node.get("children", {}))
        if not isinstance(root_children, dict):
            root_children = {}

        nodes = self.repo.discover_nodes()
        parents = self._parent_map(nodes)
        state: dict[Path, tuple[str | None, dict[str, Any]]] = {}

        for node in nodes:
            parent = parents[node]
            if parent is None:
                incoming_selector = root_selector
                inherited_children = deepcopy(root_children)
            else:
                incoming_selector, inherited_children = state[parent]
                inherited_children = deepcopy(inherited_children)

            path = node / ".meta" / "node.yml"
            raw: dict[str, Any] = {}
            if path.is_file():
                try:
                    data = self.repo.load_yaml(path)
                    value = data.get("node")
                    raw = value if isinstance(value, dict) else {}
                except ToolingError as exc:
                    result.checked += 1
                    result.errors.append(str(exc))
                    raw = {}

            effective_selector = raw.get("schema", incoming_selector)
            child_config = self._deep_merge(
                inherited_children,
                raw.get("children", {}) if isinstance(raw.get("children", {}), dict) else {},
            )
            child_selector = child_config.get("schema", effective_selector)
            nested_children = child_config.get("children", {})
            if not isinstance(nested_children, dict):
                nested_children = {}
            state[node] = (child_selector, nested_children)

            if path.is_file():
                self._validate_document(result, path, "node", effective_selector)

    def validate(self) -> SchemaValidationResult:
        result = SchemaValidationResult(errors=list(self.registry_errors))
        defaults = self._default_config()
        self._validate_aliases(result)
        self._validate_nodes(result, defaults)
        self._validate_entities(result, defaults)
        return result


__all__ = ["SchemaRef", "SchemaValidationResult", "SchemaValidator", "ToolingError"]
