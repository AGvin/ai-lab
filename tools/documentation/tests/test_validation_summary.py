from pathlib import Path
import os
import subprocess


ROOT = Path(__file__).parents[3]
SUMMARY_SCRIPT = ROOT / "scripts/github/workflows/documentation-validate/agent-summary.sh"


def test_validation_summary_separates_enabled_and_result_and_includes_grouped_details(tmp_path):
    output = tmp_path / "documentation-validate-output.txt"
    output.write_text(
        "\n".join(
            [
                "schemas: failed",
                "relations: passed",
                "cache: skipped",
                "VALIDATION_DETAILS_BEGIN",
                "### Schema and reference vocabulary validation issues (2 issue(s) in 2 file(s))",
                "",
                "- **entity.references[].type: unapproved reference type 'whitepaper'**",
                "  - `docs/sub/a/.meta/entity.yml`",
                "  - `docs/sub/b/.meta/entity.yml`",
                "VALIDATION_DETAILS_END",
                "",
            ]
        ),
        encoding="utf-8",
    )
    summary = tmp_path / "summary.md"
    env = {
        **os.environ,
        "RUNNER_TEMP": str(tmp_path),
        "GITHUB_STEP_SUMMARY": str(summary),
        "SOURCE_BRANCH": "batch/example",
        "SOURCE_SHA": "abc123",
        "REQUEST_SCHEMAS": "true",
        "REQUEST_RELATIONS": "true",
        "REQUEST_CACHE": "false",
        "SCHEMAS_STATUS": "failed",
        "RELATIONS_STATUS": "passed",
        "CACHE_STATUS": "skipped",
        "RELATION_STATISTICS": "produces / produced-by — 1 / 1",
    }
    result = subprocess.run(
        ["bash", str(SUMMARY_SCRIPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        env=env,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.count("AGENT_SUMMARY_JSON=") == 1

    text = summary.read_text(encoding="utf-8")
    assert "| Validation | Enabled | Result |" in text
    assert "| Schemas | `true` | `failed` |" in text
    assert "| Relations | `true` | `passed` |" in text
    assert "| Cache | `false` | `skipped` |" in text
    assert "true / failed" not in text
    assert "unapproved reference type 'whitepaper'" in text
    assert "`docs/sub/a/.meta/entity.yml`" in text
    assert "`docs/sub/b/.meta/entity.yml`" in text
