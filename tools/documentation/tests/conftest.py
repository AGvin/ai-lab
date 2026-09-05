from pathlib import Path
import json
import pytest
import yaml


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def write_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


@pytest.fixture
def repo(tmp_path):
    docs = tmp_path / "docs"
    (docs / ".meta" / "schemas" / "entity").mkdir(parents=True)
    (docs / ".meta" / "schemas" / "node").mkdir(parents=True)
    write_json(docs / ".meta" / "schemas" / "entity" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "repo:/:entity:default",
        "type": "object"
    })
    write_json(docs / ".meta" / "schemas" / "entity" / "model.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "repo:/:entity:model",
        "type": "object"
    })
    write_json(docs / ".meta" / "schemas" / "node" / "default.schema.json", {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "repo:/:node:default",
        "type": "object"
    })
    return tmp_path


@pytest.fixture
def repo_with_schema_alias(repo):
    write_yaml(repo / "docs" / ".meta" / "aliases.yml", {
        "aliases": {
            "schema": "default",
            "schemas": {"entity": {"model": "/:default"}}
        }
    })
    return repo
