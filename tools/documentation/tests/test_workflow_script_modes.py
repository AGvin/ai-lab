from pathlib import Path
import os


ROOT = Path(__file__).parents[3]
WORKFLOW_SCRIPTS = ROOT / "scripts/github/workflows"


def test_workflow_shell_scripts_are_executable():
    scripts = sorted(WORKFLOW_SCRIPTS.rglob("*.sh"))
    assert scripts
    non_executable = [
        script.relative_to(ROOT).as_posix()
        for script in scripts
        if not os.access(script, os.X_OK)
    ]
    assert not non_executable, f"workflow scripts must be executable: {non_executable}"
