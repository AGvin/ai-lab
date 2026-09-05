from pathlib import Path
import yaml

from tools.documentation.metadata_tooling.cache import CacheManager
from tools.documentation.metadata_tooling.common import Repository


def load_cache(node: Path):
    return yaml.safe_load((node / ".meta" / "cache.yml").read_text(encoding="utf-8"))["cache"]


def test_root_fingerprint_includes_defaults_aliases_and_schemas(cache_repo):
    manager = CacheManager(Repository(cache_repo))
    fingerprints = manager.current_self_fingerprints(cache_repo / "docs")
    assert "defaults.yml" in fingerprints
    assert "aliases.yml" in fingerprints
    assert "schemas/entity/default.schema.json" in fingerprints
    assert all(value.startswith("gitblob:") for value in fingerprints.values())


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
    assert root["state"]["schemas"]["registry"]["entity"]["default"] == (
        "docs/.meta/schemas/entity/default.schema.json"
    )


def test_alias_values_are_retained_but_relation_paths_are_expanded(cache_repo):
    CacheManager(Repository(cache_repo)).refresh(use_fingerprints=False)
    root = load_cache(cache_repo / "docs")
    child = load_cache(cache_repo / "docs/sub/catalog/sub/item")
    assert root["state"]["aliases"]["effective"]["paths"]["producers"] == (
        "/sub/catalog/sub/producers/sub/"
    )
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
    # Root remains fresh; changed catalog plus both discovered descendants rebuild.
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
