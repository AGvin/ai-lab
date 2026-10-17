from __future__ import annotations

from pathlib import Path

from pathspec import GitIgnoreSpec

from .common import Repository, ToolingError


class CacheFingerprintPolicy:
    """Resolve cache fingerprint inputs from repository-root .cacheignore."""

    def __init__(self, repo: Repository):
        self.repo = repo
        self.policy_path = self.repo.root / ".cacheignore"
        self._spec = self._load_spec()
        self._files_by_node = self._index_files()

    def _load_spec(self) -> GitIgnoreSpec:
        try:
            lines = self.policy_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise ToolingError(
                f"cannot load cache ignore policy {self.repo.repo_path(self.policy_path)}: {exc}"
            ) from exc
        try:
            return GitIgnoreSpec.from_lines(lines)
        except (TypeError, ValueError) as exc:
            raise ToolingError(
                f"invalid cache ignore policy {self.repo.repo_path(self.policy_path)}: {exc}"
            ) from exc

    def _owner_for(self, path: Path, node_set: set[Path]) -> Path:
        root = self.repo.docs_root.resolve()
        candidate = path.parent.resolve()
        while candidate == root or root in candidate.parents:
            if candidate in node_set:
                return candidate
            if candidate == root:
                break
            candidate = candidate.parent
        return root

    def _index_files(self) -> dict[Path, list[Path]]:
        nodes = self.repo.discover_nodes()
        node_set = set(nodes)
        indexed: dict[Path, list[Path]] = {node: [] for node in nodes}
        policy = self.policy_path.resolve()

        for path in sorted(self.repo.docs_root.rglob("*")):
            if not path.is_file() or path.resolve() == policy:
                continue
            relative = path.relative_to(self.repo.root).as_posix()
            if self._spec.match_file(relative):
                continue
            owner = self._owner_for(path, node_set)
            indexed.setdefault(owner, []).append(path.resolve())

        return indexed

    def files_for_node(self, node: Path) -> list[Path]:
        return list(self._files_by_node.get(Path(node).resolve(), ()))
