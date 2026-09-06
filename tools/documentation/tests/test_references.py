import yaml

from tools.documentation.metadata_tooling.common import Repository
from tools.documentation.metadata_tooling.references import REFERENCE_TYPES, ReferenceValidator


def _write_entity(repo, name: str, reference_type: str):
    path = repo / f"docs/sub/{name}/.meta/entity.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "entity": {
                    "id": name,
                    "name": name,
                    "references": [
                        {
                            "type": reference_type,
                            "source": {"url": "https://example.com/reference"},
                            "purposes": ["research"],
                            "authority": "independent",
                        }
                    ],
                }
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )


def test_reference_semantic_validator_accepts_registered_types(repo):
    for index, reference_type in enumerate(REFERENCE_TYPES):
        _write_entity(repo, f"item-{index}", reference_type)
    result = ReferenceValidator(Repository(repo)).validate()
    assert result.errors == []
    assert result.checked == len(REFERENCE_TYPES)


def test_reference_semantic_validator_rejects_unapproved_well_formed_type(repo):
    _write_entity(repo, "item", "whitepaper")
    result = ReferenceValidator(Repository(repo)).validate()
    assert result.checked == 1
    assert len(result.errors) == 1
    assert "unapproved reference type 'whitepaper'" in result.errors[0]


def test_reference_semantic_validator_leaves_malformed_tokens_to_json_schema(repo):
    _write_entity(repo, "item", "Privacy Policy")
    result = ReferenceValidator(Repository(repo)).validate()
    assert result.checked == 1
    assert result.errors == []
