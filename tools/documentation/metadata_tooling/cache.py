from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
import os
import subprocess
from typing import Any

import yaml

from .cache_fingerprints import CacheFingerprintPolicy
from .common import Repository, ToolingError


CONTROL_KEYS = {"children", "local", "reset", "notify", "track"}


@dataclass
class CacheSummary:
    discovered: int = 0
    processed: int = 0
    rebuilt: int = 0
    unchanged: int = 0
    errors: int = 0


class CacheManager:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.fingerprint_policy = CacheFingerprintPolicy(repo)

    def _git_blob(self, path: Path) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", str(self.repo.root), "hash-object", "--no-filters", str(path)],
                check=True,
                text=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as exc:
            raise ToolingError(
                f"cannot fingerprint {self.repo.repo_path(path)}: {exc.stderr.strip()}"
            ) from exc
        return f"gitblob:{result.stdout.strip()}"

    def current_self_fingerprints(self, node: Path) -> dict[str, str]:
        node = Path(node).resolve()
        meta = node / ".meta"
        fingerprints: dict[str, str] = {}
        for path in self.fingerprint_policy.files_for_node(node):
            try:
                key = path.relative_to(meta).as_posix()
            except ValueError:
                key = path.relative_to(node).as_posix()
            if key in fingerprints:
                raise ToolingError(
                    f"duplicate cache fingerprint key at {self.repo.repo_path(node)}: {key}"
                )
            fingerprints[key] = self._git_blob(path)
        return fingerprints

    @staticmethod
    def _deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
        result = deepcopy(base)
        for key, value in overlay.items():
            if isinstance(value, dict) and isinstance(result.get(key), dict):
                result[key] = CacheManager._deep_merge(result[key], value)
            else:
                result[key] = deepcopy(value)
        return result

    @staticmethod
    def _ordinary(node_config: dict[str, Any]) -> dict[str, Any]:
        return {
            key: deepcopy(value)
            for key, value in node_config.items()
            if key not in CONTROL_KEYS
        }

    def _load_defaults(self) -> dict[str, Any]:
        path = self.repo.meta_root / "defaults.yml"
        return self.repo.load_yaml(path) if path.is_file() else {}

    def _load_node_config(self, node: Path) -> dict[str, Any]:
        path = node / ".meta" / "node.yml"
        if not path.is_file():
            return {}
        root = self.repo.load_yaml(path)
        value = root.get("node", {})
        if not isinstance(value, dict):
            raise ToolingError(f"node root must be an object: {self.repo.repo_path(path)}")
        unsupported = [key for key in ("reset", "notify", "track") if key in value]
        if unsupported:
            raise ToolingError(
                f"unsupported cache operation in {self.repo.repo_path(path)}: {', '.join(unsupported)}"
            )
        return value

    def _expand_path_alias(self, value: str, aliases: dict[str, Any]) -> str:
        if ":" not in value:
            return value
        alias, suffix = value.split(":", 1)
        paths = aliases.get("paths", {}) if isinstance(aliases, dict) else {}
        if alias not in paths:
            raise ToolingError(f"unresolved path alias: {value}")
        prefix = paths[alias]
        if not isinstance(prefix, str):
            raise ToolingError(f"path alias {alias} must be a string")
        expanded = f"{prefix}{suffix}"
        if not expanded.startswith("/"):
            raise ToolingError(f"path alias {alias} must expand from documentation root")
        parts: list[str] = []
        for part in expanded.split("/"):
            if part in ("", "."):
                continue
            if part == "..":
                if not parts:
                    raise ToolingError(f"path alias escapes documentation root: {value}")
                parts.pop()
            else:
                parts.append(part)
        return "/" + "/".join(parts)

    def _load_entity(self, node: Path, aliases: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
        path = node / ".meta" / "entity.yml"
        if not path.is_file():
            return {}
        root = self.repo.load_yaml(path)
        entity = root.get("entity")
        if not isinstance(entity, dict):
            raise ToolingError(f"entity root must be an object: {self.repo.repo_path(path)}")
        effective = self._deep_merge(defaults.get("entity", {}), entity)
        relations = effective.get("relations")
        if isinstance(relations, list):
            normalized = []
            for relation in relations:
                item = deepcopy(relation)
                target = item.get("target") if isinstance(item, dict) else None
                if isinstance(target, dict) and isinstance(target.get("path"), str):
                    target["path"] = self._expand_path_alias(target["path"], aliases)
                normalized.append(item)
            effective["relations"] = normalized
        return effective

    def _build_node_state(
        self,
        node: Path,
        parent_cache: dict[str, Any] | None,
        aliases: dict[str, Any],
        schemas: dict[str, dict[str, str]],
        defaults: dict[str, Any],
    ) -> dict[str, Any]:
        raw = self._load_node_config(node)
        if parent_cache is None:
            default_node = defaults.get("node", {})
            if not isinstance(default_node, dict):
                raise ToolingError("defaults.yml node root must be an object")
            incoming_ordinary = self._ordinary(default_node)
            inherited_children = deepcopy(default_node.get("children", {}))
            parent_local: dict[str, Any] = {}
        else:
            parent_node = parent_cache["state"]["node"]
            baseline = deepcopy(parent_node["children"]["outgoing"])
            inherited_children = deepcopy(baseline.pop("children", {}))
            incoming_ordinary = baseline
            parent_local = deepcopy(parent_node["children"].get("local", {}))

        outgoing = self._deep_merge(incoming_ordinary, self._ordinary(raw))
        effective = deepcopy(outgoing)
        if parent_local:
            effective.update(parent_local)
        current_local = raw.get("local", {})
        if current_local:
            if not isinstance(current_local, dict):
                raise ToolingError(
                    f"node.local must be an object: {self.repo.repo_path(node / '.meta/node.yml')}"
                )
            effective.update(deepcopy(current_local))

        current_children = raw.get("children", {})
        if current_children and not isinstance(current_children, dict):
            raise ToolingError(
                f"node.children must be an object: {self.repo.repo_path(node / '.meta/node.yml')}"
            )
        child_config = self._deep_merge(inherited_children, current_children or {})
        unsupported_children = [key for key in ("reset", "notify", "track") if key in child_config]
        if unsupported_children:
            raise ToolingError(
                f"unsupported child cache operation at {self.repo.repo_path(node)}: "
                + ", ".join(unsupported_children)
            )
        child_outgoing = self._deep_merge(outgoing, self._ordinary(child_config))
        if isinstance(child_config.get("children"), dict) and child_config["children"]:
            child_outgoing["children"] = deepcopy(child_config["children"])
        child_local = deepcopy(child_config.get("local", {}))

        entity = self._load_entity(node, aliases, defaults)
        return {
            "node": {
                "effective": effective,
                "outgoing": outgoing,
                "children": {"outgoing": child_outgoing, "local": child_local},
            },
            "entity": {"effective": entity},
            "aliases": {"effective": deepcopy(aliases)},
            "schemas": {"registry": deepcopy(schemas)},
        }

    def _cache_path(self, node: Path) -> Path:
        return node / ".meta" / "cache.yml"

    def _load_cache(self, node: Path) -> dict[str, Any] | None:
        path = self._cache_path(node)
        if not path.is_file():
            return None
        try:
            root = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            return None
        if not isinstance(root, dict) or not isinstance(root.get("cache"), dict):
            return None
        cache = root["cache"]
        fingerprints = cache.get("fingerprints")
        state = cache.get("state")
        if cache.get("schema") != "default" or not isinstance(fingerprints, dict) or not isinstance(state, dict):
            return None
        required_state = {"node", "entity", "aliases", "schemas"}
        if not required_state.issubset(state):
            return None
        return cache

    def _write_cache(self, node: Path, cache: dict[str, Any]) -> None:
        meta = node / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        destination = meta / "cache.yml"
        temporary = meta / ".cache.yml.tmp"
        payload = yaml.safe_dump({"cache": cache}, sort_keys=False, allow_unicode=True)
        temporary.write_text(payload, encoding="utf-8")
        os.replace(temporary, destination)

    def _parent_map(self, nodes: list[Path]) -> dict[Path, Path | None]:
        node_set = set(nodes)
        result: dict[Path, Path | None] = {}
        root = self.repo.docs_root.resolve()
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

    def refresh(self, use_fingerprints: bool = True) -> CacheSummary:
        self.fingerprint_policy = CacheFingerprintPolicy(self.repo)
        nodes = self.repo.discover_nodes()
        parents = self._parent_map(nodes)
        defaults = self._load_defaults()
        aliases = self.repo.load_aliases()
        schemas = self.repo.build_schema_registry()
        summary = CacheSummary(discovered=len(nodes))
        caches: dict[Path, dict[str, Any]] = {}
        rebuilt_nodes: set[Path] = set()

        for node in nodes:
            summary.processed += 1
            parent = parents[node]
            current_self = self.current_self_fingerprints(node)
            expected_parent = self.current_self_fingerprints(parent) if parent is not None else None
            existing = self._load_cache(node) if use_fingerprints else None
            parent_rebuilt = parent in rebuilt_nodes if parent is not None else False
            fresh = False
            if existing is not None and not parent_rebuilt:
                fingerprints = existing.get("fingerprints", {})
                fresh = fingerprints.get("self") == current_self
                if parent is None:
                    fresh = fresh and "parent" not in fingerprints
                else:
                    fresh = fresh and fingerprints.get("parent") == expected_parent
            if fresh:
                caches[node] = existing
                summary.unchanged += 1
                continue

            parent_cache = caches[parent] if parent is not None else None
            state = self._build_node_state(node, parent_cache, aliases, schemas, defaults)
            fingerprints: dict[str, Any] = {"self": current_self}
            if parent is not None:
                fingerprints["parent"] = expected_parent
            cache = {
                "schema": "default",
                "fingerprints": fingerprints,
                "state": state,
            }
            self._write_cache(node, cache)
            caches[node] = cache
            rebuilt_nodes.add(node)
            summary.rebuilt += 1

        return summary
