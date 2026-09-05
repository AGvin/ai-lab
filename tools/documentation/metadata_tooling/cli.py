from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .cache import CacheManager
from .cache_validation import CacheValidator
from .common import Repository, ToolingError
from .relations import RelationValidator
from .schemas import SchemaValidator


def _bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes", "on"}:
        return True
    if normalized in {"false", "0", "no", "off"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="documentation-metadata")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cache = subparsers.add_parser("cache", help="Generate or refresh documentation caches")
    mode = cache.add_mutually_exclusive_group()
    mode.add_argument("--use-fingerprints", dest="use_fingerprints", action="store_true")
    mode.add_argument("--no-use-fingerprints", dest="use_fingerprints", action="store_false")
    cache.set_defaults(use_fingerprints=True)

    validate = subparsers.add_parser("validate", help="Validate documentation metadata")
    validate.add_argument("--validate-schemas", type=_bool, default=True)
    validate.add_argument("--validate-relations", type=_bool, default=True)
    validate.add_argument("--validate-cache", type=_bool, default=True)
    return parser


def _run_cache(use_fingerprints: bool) -> int:
    summary = CacheManager(Repository(Path.cwd())).refresh(use_fingerprints=use_fingerprints)
    print(
        "cache: "
        f"discovered={summary.discovered} "
        f"processed={summary.processed} "
        f"rebuilt={summary.rebuilt} "
        f"unchanged={summary.unchanged} "
        f"errors={summary.errors}"
    )
    return 0 if summary.errors == 0 else 1


def _print_errors(errors: list[str]) -> None:
    for error in errors:
        print(f"error: {error}", file=sys.stderr)


def _run_validate(validate_schemas: bool, validate_relations: bool, validate_cache: bool) -> int:
    repo = Repository(Path.cwd())
    failed = False

    if validate_schemas:
        result = SchemaValidator(repo).validate()
        print(f"schemas: {'passed' if result.ok else 'failed'}")
        if not result.ok:
            failed = True
            _print_errors(result.errors)
    else:
        print("schemas: skipped")

    if validate_relations:
        result = RelationValidator(repo).validate()
        print(f"relations: {'passed' if result.ok else 'failed'}")
        for line in result.statistics_lines():
            print(line)
        if not result.ok:
            failed = True
            _print_errors(result.errors)
    else:
        print("relations: skipped")

    if validate_cache:
        result = CacheValidator(repo).validate()
        print(f"cache: {'passed' if result.ok else 'failed'}")
        if not result.ok:
            failed = True
            _print_errors(result.errors)
    else:
        print("cache: skipped")

    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "cache":
            return _run_cache(args.use_fingerprints)
        if args.command == "validate":
            return _run_validate(args.validate_schemas, args.validate_relations, args.validate_cache)
    except ToolingError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
