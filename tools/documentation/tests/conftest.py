from pathlib import Path
import json
import subprocess
import pytest
import yaml


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def write_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def init_git(path: Path):
    subprocess.run(["git", "init", "-q", str(path)], check=True)


@pytest.fixture
def repo(tmp_path):
    init_git(tmp_path)
    docs = tmp_path / "docs"
    root_policy = (
        "# Ignore files by default while allowing directory traversal.\n"
        "*\n"
        "!*/\n\n"
        "# Fingerprint canonical documentation metadata.\n"
        "!docs/**/.meta/\n"
        "!docs/**/.meta/**\n\n"
        "# Generated / non-cache-relevant metadata.\n"
        "docs/**/.meta/cache.yml\n"
        "/docs/.meta/schemas/**\n"
        "/docs/.meta/templates/**\n"
        "/docs/.meta/requirements_global.md\n"
        "docs/**/.meta/requirements.md\n"
        "docs/**/.meta/requirements/reference-locks/**\n"
    )
    (tmp_path / ".cacheignore").write_text(root_policy, encoding="utf-8")
    (docs / ".meta" / "schemas" / "entity").mkdir(parents=True)
    (docs / ".meta" / "schemas" / "node").mkdir(parents=True)
    write_json(docs / ".meta" / "schemas" / "entity" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "repo:/:entity:default", "type": "object"
    })
    write_json(docs / ".meta" / "schemas" / "entity" / "model.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "repo:/:entity:model", "type": "object"
    })
    write_json(docs / ".meta" / "schemas" / "node" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "repo:/:node:default", "type": "object"
    })
    template = docs / ".meta" / "templates" / "pages" / "example.md"
    template.parent.mkdir(parents=True, exist_ok=True)
    template.write_text("template v1\n", encoding="utf-8")
    return tmp_path


@pytest.fixture
def repo_with_schema_alias(repo):
    write_yaml(repo / "docs" / ".meta" / "aliases.yml", {
        "aliases": {"schema": "default", "schemas": {"entity": {"model": "/:default"}}}
    })
    return repo


@pytest.fixture
def cache_repo(repo):
    docs = repo / "docs"
    write_yaml(docs / ".meta" / "defaults.yml", {
        "node": {
            "schema": "default",
            "requirements": {"path": "requirements.md"},
            "children": {"schema": "default"},
            "localization": {"schema": "localized", "default_locale": "en_US", "locales": []},
        },
        "entity": {"schema": "default"},
    })
    write_json(docs / ".meta" / "schemas" / "node" / "localized.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "repo:/:node:localized", "type": "object"
    })
    write_yaml(docs / ".meta" / "aliases.yml", {
        "aliases": {"schema": "default", "paths": {"producers": "/sub/catalog/sub/producers/sub/"}}
    })
    (docs / "README.md").write_text("# Docs\n", encoding="utf-8")
    parent = docs / "sub" / "catalog"
    child = parent / "sub" / "item"
    write_yaml(parent / ".meta" / "node.yml", {
        "node": {"template": "catalog/landing", "children": {"template": "catalog/item", "children": {"template": "catalog/item/detail"}}}
    })
    (parent / "README.md").write_text("# Catalog\n", encoding="utf-8")
    write_yaml(child / ".meta" / "entity.yml", {
        "entity": {"id": "catalog/item", "name": "Item", "relations": [{"type": "produced-by", "target": {"path": "producers:openai"}}]}
    })
    (child / "README.md").write_text("# Item\n", encoding="utf-8")
    producer = docs / "sub" / "catalog" / "sub" / "producers" / "sub" / "openai"
    write_yaml(producer / ".meta" / "entity.yml", {"entity": {"id": "catalog/producers/openai", "name": "OpenAI"}})
    (producer / "README.md").write_text("# OpenAI\n", encoding="utf-8")
    return repo


@pytest.fixture
def validation_repo(repo):
    docs = repo / "docs"
    write_json(docs / ".meta" / "schemas" / "entity" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "repo:/:entity:default",
        "type": "object",
        "required": ["entity"],
        "properties": {"entity": {"type": "object", "required": ["id", "name"], "properties": {
            "schema": {"type": "string"}, "id": {"type": "string"}, "name": {"type": "string"}, "relations": {"type": "array"}
        }}},
    })
    write_json(docs / ".meta" / "schemas" / "aliases" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "repo:/:aliases:default", "type": "object"
    })
    cache_schema_source = Path(__file__).parents[3] / "docs/.meta/schemas/cache/default.schema.json"
    cache_schema = json.loads(cache_schema_source.read_text(encoding="utf-8"))
    write_json(docs / ".meta" / "schemas" / "cache" / "default.schema.json", cache_schema)
    write_yaml(docs / ".meta" / "defaults.yml", {"node": {"schema": "default", "children": {"schema": "default"}}, "entity": {"schema": "default"}})
    (docs / "README.md").write_text("# Docs\n", encoding="utf-8")
    from tools.documentation.metadata_tooling.cache import CacheManager
    from tools.documentation.metadata_tooling.common import Repository
    CacheManager(Repository(repo)).refresh(use_fingerprints=False)
    return repo
