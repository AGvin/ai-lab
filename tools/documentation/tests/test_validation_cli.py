from pathlib import Path
import os
import subprocess
import sys

import yaml


ROOT = Path(__file__).parents[3]


def run_validate(repo: Path, schemas: bool, relations: bool, cache: bool):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "tools.documentation.metadata_tooling.cli",
            "validate",
            "--validate-schemas", str(schemas).lower(),
            "--validate-relations", str(relations).lower(),
            "--validate-cache", str(cache).lower(),
        ],
        cwd=repo,
        text=True,
        capture_output=True,
        env={**os.environ, "PYTHONPATH": str(ROOT)},
    )


def test_all_validation_categories_pass_on_clean_repo(validation_repo):
    result = run_validate(validation_repo, True, True, True)
    assert result.returncode == 0, result.stderr
    assert "schemas: passed" in result.stdout
    assert "relations: passed" in result.stdout
    assert "cache: passed" in result.stdout


def test_all_false_is_valid_noop(validation_repo):
    result = run_validate(validation_repo, False, False, False)
    assert result.returncode == 0
    assert "schemas: skipped" in result.stdout
    assert "relations: skipped" in result.stdout
    assert "cache: skipped" in result.stdout


def test_schema_switch_is_independent(validation_repo):
    entity = validation_repo / "docs/sub/item/.meta/entity.yml"
    entity.parent.mkdir(parents=True, exist_ok=True)
    entity.write_text(yaml.safe_dump({"entity": {"id": "item"}}, sort_keys=False), encoding="utf-8")
    disabled = run_validate(validation_repo, False, False, False)
    enabled = run_validate(validation_repo, True, False, False)
    assert disabled.returncode == 0
    assert enabled.returncode != 0
    assert "schemas: failed" in enabled.stdout


def test_relation_switch_is_independent(validation_repo):
    source = validation_repo / "docs/sub/a/.meta/entity.yml"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(
        yaml.safe_dump({"entity": {"id": "a", "name": "A", "relations": [{"type": "produces", "target": "missing"}]}}, sort_keys=False),
        encoding="utf-8",
    )
    disabled = run_validate(validation_repo, False, False, False)
    enabled = run_validate(validation_repo, False, True, False)
    assert disabled.returncode == 0
    assert enabled.returncode != 0
    assert "relations: failed" in enabled.stdout


def test_cache_switch_is_independent(validation_repo):
    (validation_repo / "docs/.meta/cache.yml").unlink()
    disabled = run_validate(validation_repo, False, False, False)
    enabled = run_validate(validation_repo, False, False, True)
    assert disabled.returncode == 0
    assert enabled.returncode != 0
    assert "cache: failed" in enabled.stdout
