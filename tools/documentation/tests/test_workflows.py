from pathlib import Path
import os
import subprocess
import sys

import yaml


ROOT = Path(__file__).parents[3]
CACHE_WORKFLOW = ROOT / ".github/workflows/documentation-cache.yml"
VALIDATE_WORKFLOW = ROOT / ".github/workflows/documentation-validate.yml"
WORKFLOW_SCRIPTS = ROOT / "scripts/github/workflows"


def load_workflow(path: Path):
    # BaseLoader avoids YAML 1.1 coercing the key `on` to boolean.
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def script_text(step):
    path = step["run"]
    assert "\n" not in path
    script = ROOT / path
    assert script.is_file(), path
    return script.read_text(encoding="utf-8")


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
    assert inputs["source_branch"]["required"] == "false"
    assert inputs["source_branch"]["default"] == ""
    assert inputs["source_branch"]["type"] == "string"
    assert inputs["use_fingerprints"]["type"] == "boolean"
    assert inputs["use_fingerprints"]["default"] == "true"
    assert inputs["reset_cache_branch"]["type"] == "boolean"
    assert inputs["reset_cache_branch"]["required"] == "true"
    assert inputs["reset_cache_branch"]["default"] == "true"


def test_cache_workflow_has_only_required_write_permissions():
    workflow = load_workflow(CACHE_WORKFLOW)
    assert workflow["permissions"] == {
        "contents": "write",
        "pull-requests": "write",
    }


def test_workflow_run_bodies_are_externalized_by_step():
    cases = (
        (CACHE_WORKFLOW, "generate", "documentation-cache"),
        (VALIDATE_WORKFLOW, "validate", "documentation-validate"),
    )
    for workflow_path, job_name, folder in cases:
        workflow = load_workflow(workflow_path)
        for step in workflow["jobs"][job_name]["steps"]:
            if "run" not in step:
                continue
            path = step["run"]
            assert path.startswith(f"scripts/github/workflows/{folder}/")
            assert path.endswith(".sh")
            assert "\n" not in path
            script = ROOT / path
            assert script.is_file(), path
            assert script.read_text(encoding="utf-8").startswith("#!/usr/bin/env bash\n")


def test_cache_workflow_invokes_cli_and_stable_cache_branch():
    workflow = load_workflow(CACHE_WORKFLOW)
    steps = workflow["jobs"]["generate"]["steps"]
    by_name = {step["name"]: step for step in steps}
    text = CACHE_WORKFLOW.read_text(encoding="utf-8")
    generate = script_text(by_name["Generate caches"])
    validate_source = script_text(by_name["Validate source branch"])
    branch = script_text(by_name["Prepare cache branch"])
    inspect = script_text(by_name["Inspect generated changes"])

    assert "tools.documentation.metadata_tooling.cli cache" in generate
    assert 'SOURCE_BRANCH: ${{ inputs.source_branch || github.ref_name }}' in text
    assert 'group: documentation-cache-${{ inputs.source_branch || github.ref_name }}' in text
    assert 'ref: ${{ inputs.source_branch || github.ref_name }}' in text
    assert 'CACHE_BRANCH="cache/${SOURCE_BRANCH}"' in branch
    assert '[[ "$SOURCE_BRANCH" == cache/* ]]' in validate_source
    assert "**/.meta/cache.yml" in inspect


def test_cache_workflow_supports_reset_and_preserve_history_modes():
    workflow = load_workflow(CACHE_WORKFLOW)
    steps = workflow["jobs"]["generate"]["steps"]
    by_name = {step["name"]: step for step in steps}

    assert workflow["jobs"]["generate"]["env"]["RESET_CACHE_BRANCH"] == "${{ inputs.reset_cache_branch }}"
    prepare = by_name["Prepare cache branch"]
    prepare_text = script_text(prepare)
    publish_text = script_text(by_name["Commit generated caches"])
    assert prepare["id"] == "branch"
    assert 'git ls-remote --exit-code --heads origin "refs/heads/${CACHE_BRANCH}"' in prepare_text
    assert 'git checkout -B "$CACHE_BRANCH" "$SOURCE_SHA"' in prepare_text
    assert 'git checkout -B "$CACHE_BRANCH" "origin/${CACHE_BRANCH}"' in prepare_text
    assert 'git merge --no-edit "$SOURCE_SHA"' in prepare_text
    assert "git rebase" not in prepare_text
    assert 'git push origin "HEAD:${CACHE_BRANCH}"' in publish_text
    assert 'git push --force-with-lease origin "HEAD:${CACHE_BRANCH}"' in publish_text

    prepare_index = next(i for i, step in enumerate(steps) if step["name"] == "Prepare cache branch")
    generate_index = next(i for i, step in enumerate(steps) if step["name"] == "Generate caches")
    assert prepare_index < generate_index


def test_validation_workflow_is_manual_only():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    assert set(workflow["on"]) == {"workflow_dispatch"}


def test_validation_workflow_inputs_default_enabled():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["source_branch"]["required"] == "false"
    assert inputs["source_branch"]["default"] == ""
    assert inputs["source_branch"]["type"] == "string"
    for name in ("validate_schemas", "validate_relations", "validate_cache"):
        assert inputs[name]["type"] == "boolean"
        assert inputs[name]["required"] == "true"
        assert inputs[name]["default"] == "true"


def test_validation_workflow_is_read_only():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    assert workflow["permissions"] == {"contents": "read"}


def test_validation_workflow_passes_each_switch_independently():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    steps = workflow["jobs"]["validate"]["steps"]
    by_name = {step["name"]: step for step in steps}
    text = VALIDATE_WORKFLOW.read_text(encoding="utf-8")
    validate = by_name["Validate documentation metadata"]
    validate_text = script_text(validate)

    assert 'group: documentation-validate-${{ inputs.source_branch || github.ref_name }}' in text
    assert 'ref: ${{ inputs.source_branch || github.ref_name }}' in text
    assert validate["env"] == {
        "VALIDATE_SCHEMAS": "${{ inputs.validate_schemas }}",
        "VALIDATE_RELATIONS": "${{ inputs.validate_relations }}",
        "VALIDATE_CACHE": "${{ inputs.validate_cache }}",
    }
    assert "tools.documentation.metadata_tooling.cli validate" in validate_text
    assert '--validate-schemas "$VALIDATE_SCHEMAS"' in validate_text
    assert '--validate-relations "$VALIDATE_RELATIONS"' in validate_text
    assert '--validate-cache "$VALIDATE_CACHE"' in validate_text


def test_validation_workflow_has_no_write_or_pr_commands():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    scripts = "\n".join(
        script_text(step)
        for step in workflow["jobs"]["validate"]["steps"]
        if "run" in step
    )
    text = VALIDATE_WORKFLOW.read_text(encoding="utf-8")
    assert "contents: write" not in text
    assert "pull-requests: write" not in text
    assert "gh pr" not in scripts
    assert "git push" not in scripts


def test_cache_workflow_exposes_agent_summary_contract():
    workflow = load_workflow(CACHE_WORKFLOW)
    steps = workflow["jobs"]["generate"]["steps"]
    by_name = {step["name"]: step for step in steps}

    assert by_name["Capture source revision"]["id"] == "source"
    assert by_name["Generate caches"]["id"] == "generate"
    generate_text = script_text(by_name["Generate caches"])
    assert 'tee "$output_file"' in generate_text
    assert "PIPESTATUS[0]" in generate_text
    for output_name in ("status", "discovered", "processed", "rebuilt", "unchanged", "errors"):
        assert f"{output_name}=" in generate_text

    commit_text = script_text(by_name["Commit generated caches"])
    pr_text = script_text(by_name["Create or reuse cache PR"])
    assert by_name["Commit generated caches"]["id"] == "commit"
    assert 'commit=$(git rev-parse HEAD)' in commit_text
    assert by_name["Create or reuse cache PR"]["id"] == "pr"
    assert 'status=updated' in pr_text
    assert 'status=created' in pr_text

    summary = steps[-1]
    summary_text = script_text(summary)
    assert summary["name"] == "Agent summary"
    assert summary["if"] == "always()"
    assert "jq -cn" in summary_text
    assert "AGENT_SUMMARY_JSON=" in summary_text
    assert "$GITHUB_STEP_SUMMARY" in summary_text
    assert summary_text.count("AGENT_SUMMARY_JSON=") == 1
    assert "actions/upload-artifact" not in CACHE_WORKFLOW.read_text(encoding="utf-8")
    assert 'RESET_CACHE_BRANCH: ${{ inputs.reset_cache_branch }}' in CACHE_WORKFLOW.read_text(encoding="utf-8")
    assert 'reset_branch: ($reset_cache_branch == "true")' in summary_text
    assert "Reset cache branch" in summary_text


def test_validation_workflow_exposes_agent_summary_contract():
    workflow = load_workflow(VALIDATE_WORKFLOW)
    assert workflow["jobs"]["validate"]["env"]["SOURCE_BRANCH"] == "${{ inputs.source_branch || github.ref_name }}"
    steps = workflow["jobs"]["validate"]["steps"]
    by_name = {step["name"]: step for step in steps}

    assert by_name["Capture source revision"]["id"] == "source"
    validate = by_name["Validate documentation metadata"]
    validate_text = script_text(validate)
    assert validate["id"] == "validate"
    assert 'tee "$output_file"' in validate_text
    assert "PIPESTATUS[0]" in validate_text
    assert "relation_statistics<<" in validate_text
    for output_name in ("schemas", "relations", "cache"):
        assert f"{output_name}=" in validate_text

    summary = steps[-1]
    summary_text = script_text(summary)
    assert summary["name"] == "Agent summary"
    assert summary["if"] == "always()"
    assert "jq -cn" in summary_text
    assert "AGENT_SUMMARY_JSON=" in summary_text
    assert "$GITHUB_STEP_SUMMARY" in summary_text
    assert summary_text.count("AGENT_SUMMARY_JSON=") == 1
    assert "actions/upload-artifact" not in VALIDATE_WORKFLOW.read_text(encoding="utf-8")


def test_metadata_workflows_use_node24_compatible_action_majors():
    for workflow_path in (CACHE_WORKFLOW, VALIDATE_WORKFLOW):
        text = workflow_path.read_text(encoding="utf-8")
        assert text.count("actions/checkout@v7") == 1
        assert text.count("actions/setup-python@v7") == 1
        assert "actions/checkout@v4" not in text
        assert "actions/setup-python@v5" not in text


def test_preserve_source_merge_is_published_without_cache_diff():
    workflow = load_workflow(CACHE_WORKFLOW)
    steps = workflow["jobs"]["generate"]["steps"]
    by_name = {step["name"]: step for step in steps}

    prepare_text = script_text(by_name["Prepare cache branch"])
    assert "source_updated=false" in prepare_text
    assert "source_updated=true" in prepare_text

    publish = by_name["Commit generated caches"]
    publish_text = script_text(publish)
    expected = "steps.changes.outputs.changed == 'true' || steps.branch.outputs.source_updated == 'true'"
    assert publish["if"] == expected
    assert publish["env"]["CACHE_CHANGED"] == "${{ steps.changes.outputs.changed }}"
    assert 'if [[ "$CACHE_CHANGED" == "true" ]]; then' in publish_text
    assert 'git push origin "HEAD:${CACHE_BRANCH}"' in publish_text
    assert 'git push --force-with-lease origin "HEAD:${CACHE_BRANCH}"' in publish_text

    pr = by_name["Create or reuse cache PR"]
    assert pr["if"] == expected

    summary = by_name["Agent summary"]
    summary_text = script_text(summary)
    assert summary["env"]["SOURCE_UPDATED"] == "${{ steps.branch.outputs.source_updated }}"
    assert 'source_updated: ($source_updated == "true")' in summary_text
