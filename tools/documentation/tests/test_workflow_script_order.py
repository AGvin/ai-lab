from pathlib import Path

import yaml


ROOT = Path(__file__).parents[3]
CACHE_WORKFLOW = ROOT / ".github/workflows/documentation-cache.yml"


def load_workflow(path: Path):
    # BaseLoader avoids YAML 1.1 coercing the key `on` to boolean.
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def test_cache_workflow_checks_out_before_running_repository_scripts():
    workflow = load_workflow(CACHE_WORKFLOW)
    steps = workflow["jobs"]["generate"]["steps"]
    checkout_index = next(i for i, step in enumerate(steps) if step["name"] == "Check out source branch")
    repository_script_indexes = [
        i
        for i, step in enumerate(steps)
        if isinstance(step.get("run"), str)
        and step["run"].startswith("scripts/github/workflows/")
    ]

    assert repository_script_indexes
    assert checkout_index < min(repository_script_indexes)
