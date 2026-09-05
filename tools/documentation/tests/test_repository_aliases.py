from pathlib import Path

import yaml


def test_repository_root_alias_registry_has_base_catalog_paths():
    root = Path(__file__).parents[3]
    aliases_path = root / "docs/.meta/aliases.yml"
    aliases = yaml.safe_load(aliases_path.read_text(encoding="utf-8"))["aliases"]
    assert aliases == {
        "schema": "default",
        "paths": {
            "producers": "/sub/catalog/sub/producers/sub/",
            "software": "/sub/catalog/sub/software/sub/",
            "models": "/sub/catalog/sub/models/sub/",
            "skills": "/sub/catalog/sub/agent-skills/sub/",
        },
    }


def test_repository_aliases_are_loaded_and_fingerprinted():
    from tools.documentation.metadata_tooling.cache import CacheManager
    from tools.documentation.metadata_tooling.common import Repository

    root = Path(__file__).parents[3]
    repo = Repository(root)
    assert repo.load_aliases()["paths"] == {
        "producers": "/sub/catalog/sub/producers/sub/",
        "software": "/sub/catalog/sub/software/sub/",
        "models": "/sub/catalog/sub/models/sub/",
        "skills": "/sub/catalog/sub/agent-skills/sub/",
    }
    fingerprints = CacheManager(repo).current_self_fingerprints(root / "docs")
    assert set(fingerprints) == {"aliases.yml", "defaults.yml"}
