from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class ToolingError(RuntimeError):
    pass


@dataclass(frozen=True)
class SchemaRef:
    type_name: str
    schema_id: str
    identity: str
    uri: str
    path: str


class Repository:
    def __init__(self, root: Path):
        self.root = Path(root).resolve()
        self.docs_root = self.root / "docs"
        self.meta_root = self.docs_root / ".meta"
        self.schemas_root = self.meta_root / "schemas"

    def repo_path(self, path: Path) -> str:
        return path.resolve().relative_to(self.root).as_posix()

    def load_yaml(self, path: Path) -> dict[str, Any]:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            raise ToolingError(f"cannot load YAML {self.repo_path(path)}: {exc}") from exc
        if data is None:
            return {}
        if not isinstance(data, dict):
            raise ToolingError(f"YAML document must be an object: {self.repo_path(path)}")
        return data

    def _reject_non_root_schema_registries(self) -> None:
        if not self.docs_root.exists():
            raise ToolingError("documentation root does not exist: docs")
        canonical = self.schemas_root.resolve()
        for meta_dir in self.docs_root.rglob(".meta"):
            candidate = meta_dir / "schemas"
            if candidate.is_dir() and candidate.resolve() != canonical:
                raise ToolingError(
                    f"non-root schema registry is not allowed: {self.repo_path(candidate)}"
                )

    @staticmethod
    def _schema_type_and_id(relative: Path) -> tuple[str, str]:
        parts = relative.parts
        filename = parts[-1]
        if not filename.endswith(".schema.json"):
            raise ToolingError(f"invalid schema filename: {relative.as_posix()}")
        stem = filename[: -len(".schema.json")]
        if len(parts) > 1:
            type_name = parts[0]
            id_parts = list(parts[1:-1]) + [stem]
            schema_id = "/".join(id_parts)
        else:
            if "." not in stem:
                raise ToolingError(
                    f"flat schema must use <type>.<id>.schema.json: {relative.as_posix()}"
                )
            type_name, schema_id = stem.split(".", 1)
            schema_id = schema_id.replace(".", "/")
        if not type_name or not schema_id:
            raise ToolingError(f"invalid schema identity: {relative.as_posix()}")
        return type_name, schema_id

    def build_schema_registry(self) -> dict[str, dict[str, str]]:
        self._reject_non_root_schema_registries()
        registry: dict[str, dict[str, str]] = {}
        if not self.schemas_root.is_dir():
            return registry
        for path in sorted(self.schemas_root.rglob("*.schema.json")):
            relative = path.relative_to(self.schemas_root)
            type_name, schema_id = self._schema_type_and_id(relative)
            by_type = registry.setdefault(type_name, {})
            if schema_id in by_type:
                raise ToolingError(f"duplicate schema identity: /:{type_name}:{schema_id}")
            by_type[schema_id] = self.repo_path(path)
        return registry

    def discover_nodes(self) -> list[Path]:
        """Return canonical default-locale documentation nodes in root-to-leaf order."""
        nodes = {self.docs_root.resolve()}
        if not self.docs_root.exists():
            return []
        for path in self.docs_root.rglob("*"):
            if not path.is_dir():
                continue
            rel_parts = path.relative_to(self.docs_root).parts
            if any(part == "l10n" or part.startswith(".") for part in rel_parts):
                continue
            meta = path / ".meta"
            if (
                (path / "README.md").is_file()
                or (meta / "node.yml").is_file()
                or (meta / "entity.yml").is_file()
            ):
                nodes.add(path.resolve())
        return sorted(
            nodes,
            key=lambda item: (
                len(item.relative_to(self.docs_root).parts),
                item.as_posix(),
            ),
        )

    def load_aliases(self) -> dict[str, Any]:
        path = self.meta_root / "aliases.yml"
        if not path.exists():
            return {}
        data = self.load_yaml(path)
        aliases = data.get("aliases")
        if aliases is None:
            return {}
        if not isinstance(aliases, dict):
            raise ToolingError("aliases.yml aliases root must be an object")
        return aliases

    def resolve_schema(self, type_name: str, selector: str) -> SchemaRef:
        if not isinstance(selector, str) or not selector:
            raise ToolingError(f"invalid {type_name} schema selector: {selector!r}")
        registry = self.build_schema_registry()
        schema_id: str
        if selector.startswith("/:"):
            schema_id = selector[2:]
            if not schema_id or ":" in schema_id:
                raise ToolingError(f"invalid explicit root schema selector: {selector}")
        else:
            aliases = self.load_aliases()
            target = (
                aliases.get("schemas", {})
                .get(type_name, {})
                .get(selector)
                if isinstance(aliases.get("schemas", {}), dict)
                else None
            )
            if target is not None:
                if not isinstance(target, str) or not target.startswith("/:"):
                    raise ToolingError(
                        f"schema alias {type_name}.{selector} must target an explicit root selector"
                    )
                schema_id = target[2:]
                if not schema_id or ":" in schema_id:
                    raise ToolingError(
                        f"schema alias {type_name}.{selector} has invalid target {target!r}"
                    )
            else:
                schema_id = selector
        path = registry.get(type_name, {}).get(schema_id)
        if path is None:
            raise ToolingError(f"schema not found: /:{type_name}:{schema_id}")
        identity = f"/:{type_name}:{schema_id}"
        return SchemaRef(
            type_name=type_name,
            schema_id=schema_id,
            identity=identity,
            uri=f"repo:{identity}",
            path=path,
        )
