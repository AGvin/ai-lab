import pytest

from tools.documentation.metadata_tooling.common import Repository, ToolingError


def test_grouped_schema_registry_uses_scalar_repo_paths(repo):
    registry = Repository(repo).build_schema_registry()
    assert registry["entity"]["default"] == "docs/.meta/schemas/entity/default.schema.json"
    assert registry["entity"]["model"] == "docs/.meta/schemas/entity/model.schema.json"


def test_absent_alias_registry_is_empty(repo):
    assert Repository(repo).load_aliases() == {}


def test_short_selector_is_alias_first(repo_with_schema_alias):
    resolved = Repository(repo_with_schema_alias).resolve_schema("entity", "model")
    assert resolved.identity == "/:entity:default"
    assert resolved.path == "docs/.meta/schemas/entity/default.schema.json"


def test_explicit_selector_bypasses_alias(repo_with_schema_alias):
    resolved = Repository(repo_with_schema_alias).resolve_schema("entity", "/:model")
    assert resolved.identity == "/:entity:model"
    assert resolved.path == "docs/.meta/schemas/entity/model.schema.json"


def test_non_root_schema_registry_is_rejected(repo):
    local = repo / "docs" / "sub" / "x" / ".meta" / "schemas"
    local.mkdir(parents=True)
    (local / "bad.schema.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(ToolingError, match="non-root schema registry"):
        Repository(repo).build_schema_registry()
