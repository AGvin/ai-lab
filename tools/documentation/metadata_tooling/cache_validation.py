from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import yaml

from .cache import CacheManager
from .common import Repository, ToolingError


@dataclass
class CacheValidationResult:
    expected: int = 0
    checked: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


class CacheValidator:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.manager = CacheManager(repo)
        self.aliases = repo.load_aliases()
        self.schemas = repo.build_schema_registry()

    def _load_raw_cache(
        self,
        node: Path,
        result: CacheValidationResult,
    ) -> dict[str, Any] | None:
        path = node / ".meta" / "cache.yml"
        repo_path = self.repo.repo_path(path)
        if not path.is_file():
            result.errors.append(f"{repo_path}: missing cache")
            return None
        result.checked += 1
        try:
            root = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            result.errors.append(f"{repo_path}: malformed cache: {exc}")
            return None
        if not isinstance(root, dict) or not isinstance(root.get("cache"), dict):
            result.errors.append(f"{repo_path}: malformed cache document")
            return None
        return root["cache"]

    def _validate_schema(
        self,
        node: Path,
        cache: dict[str, Any],
        result: CacheValidationResult,
    ) -> None:
        path = node / ".meta" / "cache.yml"
        repo_path = self.repo.repo_path(path)
        selector = cache.get("schema")
        try:
            ref = self.repo.resolve_schema("cache", selector)
            schema = json.loads((self.repo.root / ref.path).read_text(encoding="utf-8"))
            errors = sorted(
                Draft202012Validator(schema).iter_errors({"cache": cache}),
                key=lambda error: list(error.absolute_path),
            )
        except (ToolingError, OSError, json.JSONDecodeError) as exc:
            result.errors.append(f"{repo_path}: cache schema validation setup failed: {exc}")
            return
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            result.errors.append(f"{repo_path}: {location}: {error.message}")

    @staticmethod
    def _contains_forbidden_control(value: Any) -> bool:
        if isinstance(value, dict):
            if "notify" in value or "track" in value:
                return True
            return any(CacheValidator._contains_forbidden_control(item) for item in value.values())
        if isinstance(value, list):
            return any(CacheValidator._contains_forbidden_control(item) for item in value)
        return False

    def _find_unresolved_alias(self, value: Any) -> str | None:
        paths = self.aliases.get("paths", {}) if isinstance(self.aliases, dict) else {}
        known = set(paths) if isinstance(paths, dict) else set()
        if not known:
            return None
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "path" and isinstance(item, str) and ":" in item:
                    prefix = item.split(":", 1)[0]
                    if prefix in known:
                        return item
                found = self._find_unresolved_alias(item)
                if found is not None:
                    return found
        elif isinstance(value, list):
            for item in value:
                found = self._find_unresolved_alias(item)
                if found is not None:
                    return found
        return None

    def validate(self) -> CacheValidationResult:
        nodes = self.repo.discover_nodes()
        parents = self.manager._parent_map(nodes)
        result = CacheValidationResult(expected=len(nodes))
        invalid: set[Path] = set()

        for node in nodes:
            start_errors = len(result.errors)
            parent = parents[node]
            if parent is not None and parent in invalid:
                result.errors.append(
                    f"{self.repo.repo_path(node)}: ancestor cache is invalid: "
                    f"{self.repo.repo_path(parent)}"
                )

            cache = self._load_raw_cache(node, result)
            if cache is None:
                invalid.add(node)
                continue

            self._validate_schema(node, cache, result)
            cache_path = self.repo.repo_path(node / ".meta" / "cache.yml")
            fingerprints = cache.get("fingerprints")
            if not isinstance(fingerprints, dict):
                result.errors.append(f"{cache_path}: missing cache fingerprints")
            else:
                current_self = self.manager.current_self_fingerprints(node)
                if fingerprints.get("self") != current_self:
                    result.errors.append(f"{cache_path}: stale self fingerprints")
                if parent is None:
                    if "parent" in fingerprints:
                        result.errors.append(f"{cache_path}: root cache must not contain parent fingerprints")
                else:
                    current_parent = self.manager.current_self_fingerprints(parent)
                    if fingerprints.get("parent") != current_parent:
                        result.errors.append(f"{cache_path}: stale parent fingerprints")

            state = cache.get("state")
            if not isinstance(state, dict):
                result.errors.append(f"{cache_path}: missing cache state")
            else:
                schema_state = state.get("schemas")
                cached_registry = schema_state.get("registry") if isinstance(schema_state, dict) else None
                if cached_registry != self.schemas:
                    result.errors.append(f"{cache_path}: schema registry mismatch")

                alias_state = state.get("aliases")
                cached_aliases = alias_state.get("effective") if isinstance(alias_state, dict) else None
                if cached_aliases != self.aliases:
                    result.errors.append(f"{cache_path}: alias state mismatch")

                node_state = state.get("node")
                if self._contains_forbidden_control(node_state):
                    result.errors.append(f"{cache_path}: forbidden cached node control notify/track")

                ordinary_state = {
                    key: value
                    for key, value in state.items()
                    if key != "aliases"
                }
                unresolved = self._find_unresolved_alias(ordinary_state)
                if unresolved is not None:
                    result.errors.append(
                        f"{cache_path}: unresolved path alias in cached state: {unresolved}"
                    )

            if len(result.errors) > start_errors:
                invalid.add(node)

        return result
