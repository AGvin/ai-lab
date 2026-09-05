from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .cache import CacheManager
from .common import Repository, ToolingError


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="documentation-metadata")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cache = subparsers.add_parser("cache", help="Generate or refresh documentation caches")
    mode = cache.add_mutually_exclusive_group()
    mode.add_argument("--use-fingerprints", dest="use_fingerprints", action="store_true")
    mode.add_argument("--no-use-fingerprints", dest="use_fingerprints", action="store_false")
    cache.set_defaults(use_fingerprints=True)
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


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "cache":
            return _run_cache(args.use_fingerprints)
    except ToolingError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
