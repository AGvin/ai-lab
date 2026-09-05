from pathlib import Path
import yaml

from tools.documentation.metadata_tooling.cache import CacheManager
from tools.documentation.metadata_tooling.common import Repository


def load_cache(node: Path):
    return yaml.safe_load((node / ".meta" / "cache.yml").read_text(encoding="utf-8"))["cache"]


def test_cacheignore_policy_is_loaded_from_repository_root(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    assert manager.fingerprint_policy.policy_path == cache_repo / ".cacheignore"


def test_root_templates_are_excluded_and_content_changes_do_not_change_fingerprints(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    root = cache_repo / "docs"
    before = manager.current_self_fingerprints(root)
    assert not any(key.startswith("templates/") for key in before)
    template = root / ".meta/templates/pages/example.md"
    template.write_text("template v2\n", encoding="utf-8")
    after = CacheManager(Repository(cache_repo)).current_self_fingerprints(root)
    assert after == before


def test_root_fingerprint_excludes_schemas_via_cacheignore(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    fingerprints = manager.current_self_fingerprints(cache_repo / "docs")
    assert "defaults.yml" in fingerprints
    assert "aliases.yml" in fingerprints
    assert not any(key.startswith("schemas/") for key in fingerprints)
    assert all(value.startswith("gitblob:") for value in fingerprints.values())


def test_schema_content_change_does_not_change_fingerprints(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    root = cache_repo / "docs"
    before = manager.current_self_fingerprints(root)
    schema = root / ".meta/schemas/entity/default.schema.json"
    schema.write_text(schema.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    after = manager.current_self_fingerprints(root)
    assert after == before


def test_cacheignore_can_reinclude_ignored_schema(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    root = cache_repo / "docs"
    before = manager.current_self_fingerprints(root)
    assert "schemas/entity/default.schema.json" not in before
    policy = cache_repo / ".cacheignore"
    policy.write_text(policy.read_text(encoding="utf-8") + "\n!**/.meta/schemas/entity/default.schema.json\n", encoding="utf-8")
    after = CacheManager(Repository(cache_repo)).current_self_fingerprints(root)
    assert "schemas/entity/default.schema.json" in after


def test_future_meta_file_is_fingerprinted_without_python_allowlist(cache_repo):
    node = cache_repo / "docs/sub/catalog"
    custom = node / ".meta/custom.yml"
    custom.write_text("custom: true\n", encoding="utf-8")
    manager = CacheManager(Repository(cache_repo))
    fingerprints = manager.current_self_fingerprints(node)
    assert "custom.yml" in fingerprints


def test_regular_node_fingerprint_tracks_node_and_entity_only(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    parent = cache_repo / "docs/sub/catalog"
    child = parent / "sub/item"
    assert set(manager.current_self_fingerprints(parent)) == {"node.yml"}
    assert set(manager.current_self_fingerprints(child)) == {"entity.yml"}


def test_full_refresh_writes_root_and_child_parent_snapshot(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    summary = manager.refresh(use_fingerprints=False)
    root = load_cache(cache_repo / "docs")
    parent = load_cache(cache_repo / "docs/sub/catalog")
    child = load_cache(cache_repo / "docs/sub/catalog/sub/item")
    assert "parent" not in root["fingerprints"]
    assert parent["fingerprints"]["parent"] == root["fingerprints"]["self"]
    assert child["fingerprints"]["parent"] == parent["fingerprints"]["self"]
    assert summary.rebuilt == summary.discovered


def test_schema_registry_cache_uses_scalar_paths(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    root = load_cache(cache_repo / "docs")
    assert root["state"]["schemas"]["registry"]["entity"]["default"] == "docs/.meta/schemas/entity/default.schema.json"


def test_alias_values_are_retained_but_relation_paths_are_expanded(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    root = load_cache(cache_repo / "docs")
    child = load_cache(cache_repo / "docs/sub/catalog/sub/item")
    assert root["state"]["aliases"]["effective"]["paths"]["producers"] == "/sub/catalog/sub/producers/sub/"
    relation_path = child["state"]["entity"]["effective"]["relations"][0]["target"]["path"]
    assert relation_path == "/sub/catalog/sub/producers/sub/openai"


def test_nested_children_baseline_propagates(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    parent = load_cache(cache_repo / "docs/sub/catalog")
    child = load_cache(cache_repo / "docs/sub/catalog/sub/item")
    assert parent["state"]["node"]["children"]["outgoing"]["template"] == "catalog/item"
    assert child["state"]["node"]["effective"]["template"] == "catalog/item"
    assert child["state"]["node"]["children"]["outgoing"]["template"] == "catalog/item/detail"


def test_incremental_second_run_skips_fresh_nodes(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    manager.refresh(use_fingerprints=False)
    second = manager.refresh(use_fingerprints=True)
    assert second.rebuilt == 0
    assert second.unchanged == second.discovered


def test_parent_change_rebuilds_parent_and_descendant(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    manager.refresh(use_fingerprints=False)
    parent_meta = cache_repo / "docs/sub/catalog/.meta/node.yml"
    data = yaml.safe_load(parent_meta.read_text(encoding="utf-8"))
    data["node"]["template"] = "catalog/changed"
    parent_meta.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    second = manager.refresh(use_fingerprints=True)
    assert second.rebuilt == 3


def test_forced_full_rebuild_processes_every_node(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    first = manager.refresh(use_fingerprints=False)
    second = manager.refresh(use_fingerprints=False)
    assert second.rebuilt == first.discovered
    assert second.unchanged == 0


def test_repository_cache_schema_has_canonical_identity():
    import json
    schema_path = Path(__file__).parents[3] / "docs/.meta/schemas/cache/default.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == "repo:/:cache:default"
    assert schema["required"] == ["cache"]


def cache_validate(repo):
    from tools.documentation.metadata_tooling.cache_validation import CacheValidator
    return CacheValidator(Repository(repo)).validate()


def test_cache_validation_accepts_fresh_generated_cache(validation_repo):
    result = cache_validate(validation_repo)
    assert result.errors == []
    assert result.checked == result.expected


def test_cache_validation_rejects_missing_cache(validation_repo):
    (validation_repo / "docs/.meta/cache.yml").unlink()
    result = cache_validate(validation_repo)
    assert any("missing cache" in error for error in result.errors)


def test_cache_validation_rejects_malformed_cache(validation_repo):
    (validation_repo / "docs/.meta/cache.yml").write_text("cache: [\n", encoding="utf-8")
    result = cache_validate(validation_repo)
    assert any("malformed cache" in error for error in result.errors)


def test_cache_validation_rejects_stale_self_fingerprint(validation_repo):
    defaults = validation_repo / "docs/.meta/defaults.yml"
    defaults.write_text(defaults.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    result = cache_validate(validation_repo)
    assert any("stale self fingerprints" in error for error in result.errors)


def test_cache_validation_rejects_stale_parent_snapshot(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    manager.refresh(use_fingerprints=False)
    child_path = cache_repo / "docs/sub/catalog/sub/item/.meta/cache.yml"
    data = yaml.safe_load(child_path.read_text(encoding="utf-8"))
    data["cache"]["fingerprints"]["parent"] = {"node.yml": "gitblob:" + "0" * 40}
    child_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = cache_validate(cache_repo)
    assert any("stale parent fingerprints" in error for error in result.errors)


def test_cache_validation_rejects_schema_registry_mismatch(validation_repo):
    cache_path = validation_repo / "docs/.meta/cache.yml"
    data = yaml.safe_load(cache_path.read_text(encoding="utf-8"))
    data["cache"]["state"]["schemas"]["registry"] = {}
    cache_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = cache_validate(validation_repo)
    assert any("schema registry mismatch" in error for error in result.errors)


def test_cache_validation_rejects_alias_state_mismatch(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    cache_path = cache_repo / "docs/.meta/cache.yml"
    data = yaml.safe_load(cache_path.read_text(encoding="utf-8"))
    data["cache"]["state"]["aliases"]["effective"] = {}
    cache_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = cache_validate(cache_repo)
    assert any("alias state mismatch" in error for error in result.errors)


def test_cache_validation_rejects_forbidden_node_controls(validation_repo):
    cache_path = validation_repo / "docs/.meta/cache.yml"
    data = yaml.safe_load(cache_path.read_text(encoding="utf-8"))
    data["cache"]["state"]["node"]["effective"]["notify"] = []
    cache_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = cache_validate(validation_repo)
    assert any("forbidden cached node control" in error for error in result.errors)


def test_cache_validation_rejects_unresolved_known_path_alias(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    child = cache_repo / "docs/sub/catalog/sub/item/.meta/cache.yml"
    data = yaml.safe_load(child.read_text(encoding="utf-8"))
    relation = data["cache"]["state"]["entity"]["effective"]["relations"][0]
    relation["target"]["path"] = "producers:openai"
    child.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = cache_validate(cache_repo)
    assert any("unresolved path alias" in error for error in result.errors)


def test_root_global_requirements_are_excluded_and_content_changes_do_not_change_fingerprints(cache_repo):
    root = cache_repo / "docs"
    requirements = root / ".meta/requirements_global.md"
    requirements.write_text("global requirements v1\n", encoding="utf-8")

    before = CacheManager(Repository(cache_repo)).current_self_fingerprints(root)
    assert "requirements_global.md" not in before

    requirements.write_text("global requirements v2\n", encoding="utf-8")
    after = CacheManager(Repository(cache_repo)).current_self_fingerprints(root)
    assert after == before
