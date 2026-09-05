from pathlib import Path

import yaml

from tools.documentation.metadata_tooling.common import Repository


def write_entity(repo: Path, logical_id: str, relations=None):
    node = repo / "docs"
    for segment in logical_id.split("/"):
        node = node / "sub" / segment
    meta = node / ".meta"
    meta.mkdir(parents=True, exist_ok=True)
    data = {"entity": {"id": logical_id, "name": logical_id.rsplit("/", 1)[-1]}}
    if relations is not None:
        data["entity"]["relations"] = relations
    (meta / "entity.yml").write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return node


def validate(repo):
    from tools.documentation.metadata_tooling.relations import RelationValidator
    return RelationValidator(Repository(repo)).validate()


def test_valid_inverse_pair_passes(repo):
    write_entity(repo, "a", [{"type": "produces", "target": "b"}])
    write_entity(repo, "b", [{"type": "produced-by", "target": "a"}])
    result = validate(repo)
    assert result.errors == []
    assert result.statistics["produces"] == 1
    assert result.statistics["produced-by"] == 1


def test_missing_inverse_fails(repo):
    write_entity(repo, "a", [{"type": "produces", "target": "b"}])
    write_entity(repo, "b", [])
    result = validate(repo)
    assert any("missing inverse" in error for error in result.errors)


def test_mismatched_inverse_fails(repo):
    write_entity(repo, "a", [{"type": "produces", "target": "b"}])
    write_entity(repo, "b", [{"type": "produced-by", "target": "c"}])
    write_entity(repo, "c", [])
    result = validate(repo)
    assert any("missing inverse" in error and "a" in error and "b" in error for error in result.errors)


def test_dangling_target_fails(repo):
    write_entity(repo, "a", [{"type": "produces", "target": "missing"}])
    result = validate(repo)
    assert any("unresolvable relation target" in error for error in result.errors)


def test_duplicate_logical_edge_fails(repo):
    write_entity(repo, "a", [{"type": "produces", "target": "b"}, {"type": "produces", "target": {"id": "b"}}])
    write_entity(repo, "b", [{"type": "produced-by", "target": "a"}])
    result = validate(repo)
    assert any("duplicate logical edge" in error for error in result.errors)


def test_self_edge_fails(repo):
    write_entity(repo, "a", [{"type": "has-part", "target": "a"}])
    result = validate(repo)
    assert any("self relation" in error for error in result.errors)


def test_learning_resource_pair_is_registered(repo):
    write_entity(repo, "concept", [{"type": "has-learning-resource", "target": "lesson"}])
    write_entity(repo, "lesson", [{"type": "learning-resource-for", "target": "concept"}])
    result = validate(repo)
    assert result.errors == []
    assert "has-learning-resource / learning-resource-for — 1 / 1" in result.statistics_lines()


def test_statistics_include_every_pair_even_when_zero(repo):
    from tools.documentation.metadata_tooling.relations import RELATION_PAIRS
    result = validate(repo)
    lines = result.statistics_lines()
    assert len(lines) == len(RELATION_PAIRS)
    assert all(line.endswith("— 0 / 0") for line in lines)


def test_path_alias_target_resolves_to_entity_identity(repo):
    aliases = repo / "docs/.meta/aliases.yml"
    aliases.parent.mkdir(parents=True, exist_ok=True)
    aliases.write_text(
        yaml.safe_dump({"aliases": {"schema": "default", "paths": {"targets": "/sub/target/sub/"}}}, sort_keys=False),
        encoding="utf-8",
    )
    write_entity(repo, "source", [{"type": "has-part", "target": {"path": "targets:item"}}])
    write_entity(repo, "target/item", [{"type": "part-of", "target": "source"}])
    result = validate(repo)
    assert result.errors == []


def test_path_inconsistent_entity_id_fails(repo):
    node = write_entity(repo, "correct")
    entity_path = node / ".meta/entity.yml"
    data = yaml.safe_load(entity_path.read_text(encoding="utf-8"))
    data["entity"]["id"] = "wrong"
    entity_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    result = validate(repo)
    assert any("entity id/path mismatch" in error for error in result.errors)


def test_unknown_relation_type_fails(repo):
    write_entity(repo, "a", [{"type": "unknown-relation", "target": "b"}])
    write_entity(repo, "b", [])
    result = validate(repo)
    assert any("unknown relation type" in error for error in result.errors)
