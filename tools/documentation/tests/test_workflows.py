from pathlib import Path
import os
import subprocess
import sys

import yaml


ROOT = Path(__file__).parents[3]
CACHE_WORKFLOW = ROOT / ".github/workflows/documentation-cache.yml"


def load_workflow(path: Path):
    # BaseLoader avoids YAML 1.1 coercing the key `on` to boolean.
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def test_cache_cli_reports_stable_summary(cache_repo):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "tools.documentation.metadata_tooling.cli",
            "cache",
            "--no-use-fingerprints",
        ],
        cwd=cache_repo,
        text=True,
        capture_output=True,
        env={**os.environ, "PYTHONPATH": str(ROOT)},
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.startswith("cache: discovered=")
    assert " errors=0" in result.stdout


def test_cache_workflow_is_manual_only():
    workflow = load_workflow(CACHE_WORKFLOW)
    assert set(workflow["on"]) == {"workflow_dispatch"}


def test_cache_workflow_inputs_and_defaults():
    workflow = load_workflow(CACHE_WORKFLOW)
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["source_branch"]["required"] == "true"
    assert inputs["source_branch"]["type"] == "string"
    assert inputs["use_fingerprints"]["type"] == "boolean"
    assert inputs["use_fingerprints"]["default"] == "true"


def test_cache_workflow_has_only_required_write_permissions():
    workflow = load_workflow(CACHE_WORKFLOW)
    assert workflow["permissions"] == {
        "contents": "write",
        "pull-requests": "write",
    }


def test_cache_workflow_invokes_cli_and_stable_cache_branch():
    text = CACHE_WORKFLOW.read_text(encoding="utf-8")
    assert "tools.documentation.metadata_tooling.cli cache" in text
    assert 'CACHE_BRANCH="cache/${SOURCE_BRANCH}"' in text
    assert '[[ "$SOURCE_BRANCH" == cache/* ]]' in text
    assert "**/.meta/cache.yml" in text


VALIDATE_WORKFLOW = ROOT / ".github/workflows/documentation-validate.yml"


def test_validation_workflow_is_manual_only():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    assert set(workflow["on"]) == {"workflow_dispatch"}


def test_validation_workflow_inputs_default_enabled():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["source_branch"]["required"] == "true"
    assert inputs["source_branch"]["type"] == "string"
    for name in ("validate_schemas", "validate_relations", "validate_cache"):
        assert inputs[name]["type"] == "boolean"
        assert inputs[_name]["required"] == "true"
        assert inputs[_name]["default"] == "true"


def test_validation_workflow_is_read_only():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    assert workflow["permissions"] == {"contents": "read"}


def test_validation_workflow_passes_each_switch_independently():
    text = VALIDATE_WORKFLOW.read_text(encoding="utf-8")
    assert "tools.documentation.metadata_tooling.cli validate" in text
    assert '--validate-schemas "${{ inputs.validate_schemas }}"' in text
    assert '--validate-relations "${{ inputs.validate_relations }}"' in text
    assert '--validate-cache "${{ inputs.validate_cache }}"' in text


def test_validation_workflow_has_no_write_or_pr_commands():
    text = VALIDATE_WORKFLOW.read_text(encoding="utf-8")
    assert "contents: write" not in text
    assert "pull-requests: write" not in text
    assert "gh pr" not in text
    assert "git push" not in text
