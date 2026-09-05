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


def _write_json(path, data):
    import json
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _write_yaml(path, data):
    import yaml
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _entity_schema(uri, require_marker=False):
    properties = {"schema": {"type": "string"}, "id": {"type": "string"}, "name": {"type": "string"}}
    required = ["id", "name"]
    if require_marker:
        properties["marker"] = {"const": "model"}
        required.append("marker")
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": uri,
        "type": "object",
        "required": ["entity"],
        "properties": {"entity": {"type": "object", "required": required, "properties": properties}},
    }


def _aliases_schema():
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "repo:/:aliases:default",
        "type": "object",
        "required": ["aliases"],
        "properties": {
            "aliases": {
                "type": "object",
                "required": ["schema"],
                "properties": {
                    "schema": {"type": "string"},
                    "paths": {"type": "object", "additionalProperties": {"type": "string"}},
                    "schemas": {"type": "object"},
                },
            }
        },
    }


def test_schema_validation_uses_entity_default_from_defaults(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/entity/default.schema.json", _entity_schema("repo:/:entity:default"))
    _write_yaml(repo / "docs/.meta/defaults.yml", {"entity": {"schema": "default"}})
    _write_yaml(repo / "docs/sub/item/.meta/entity.yml", {"entity": {"id": "item", "name": "Item"}})
    result = SchemaValidator(Repository(repo)).validate()
    assert result.errors == []
    assert result.checked == 1


def test_schema_validation_reports_invalid_entity(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/entity/default.schema.json", _entity_schema("repo:/:entity:default"))
    _write_yaml(repo / "docs/.meta/defaults.yml", {"entity": {"schema": "default"}})
    _write_yaml(repo / "docs/sub/item/.meta/entity.yml", {"entity": {"id": "item"}})
    result = SchemaValidator(Repository(repo)).validate()
    assert result.checked == 1
    assert any("'name' is a required property" in error for error in result.errors)


def test_schema_validation_uses_alias_first_short_selector(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/entity/default.schema.json", _entity_schema("repo:/:entity:default"))
    _write_json(repo / "docs/.meta/schemas/entity/model.schema.json", _entity_schema("repo:/:entity:model", require_marker=True))
    _write_json(repo / "docs/.meta/schemas/aliases/default.schema.json", _aliases_schema())
    _write_yaml(repo / "docs/.meta/aliases.yml", {"aliases": {"schema": "default", "schemas": {"entity": {"model": "/:default"}}}})
    _write_yaml(repo / "docs/sub/item/.meta/entity.yml", {"entity": {"schema": "model", "id": "item", "name": "Item"}})
    result = SchemaValidator(Repository(repo)).validate()
    assert result.errors == []
    assert result.checked == 2


def test_schema_validation_explicit_selector_bypasses_alias(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/entity/default.schema.json", _entity_schema("repo:/:entity:default"))
    _write_json(repo / "docs/.meta/schemas/entity/model.schema.json", _entity_schema("repo:/:entity:model", require_marker=True))
    _write_json(repo / "docs/.meta/schemas/aliases/default.schema.json", _aliases_schema())
    _write_yaml(repo / "docs/.meta/aliases.yml", {"aliases": {"schema": "default", "schemas": {"entity": {"model": "/:default"}}}})
    _write_yaml(repo / "docs/sub/item/.meta/entity.yml", {"entity": {"schema": "/:model", "id": "item", "name": "Item"}})
    result = SchemaValidator(Repository(repo)).validate()
    assert any("'marker' is a required property" in error for error in result.errors)


def test_schema_validation_rejects_schema_id_mismatch(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/entity/default.schema.json", _entity_schema("default"))
    _write_yaml(repo / "docs/.meta/defaults.yml", {"entity": {"schema": "default"}})
    _write_yaml(repo / "docs/sub/item/.meta/entity.yml", {"entity": {"id": "item", "name": "Item"}})
    result = SchemaValidator(Repository(repo)).validate()
    assert any("schema $id mismatch" in error for error in result.errors)


def test_aliases_document_uses_direct_root_schema_bootstrap(repo):
    from tools.documentation.metadata_tooling.schemas import SchemaValidator
    _write_json(repo / "docs/.meta/schemas/aliases/default.schema.json", _aliases_schema())
    _write_yaml(repo / "docs/.meta/aliases.yml", {"aliases": {"schema": "default", "paths": {"bad": 123}}})
    result = SchemaValidator(Repository(repo)).validate()
    assert any("123 is not of type 'string'" in error for error in result.errors)


def test_repository_aliases_schema_has_canonical_identity():
    import json
    from pathlib import Path
    schema_path = Path(__file__).parents[3] / "docs/.meta/schemas/aliases/default.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == "repo:/:aliases:default"
