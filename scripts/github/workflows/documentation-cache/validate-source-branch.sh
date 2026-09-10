#!/usr/bin/env bash
set -euo pipefail
if [[ -z "$SOURCE_BRANCH" ]]; then
  echo "source_branch must not be empty" >&2
  exit 2
fi
if [[ "$SOURCE_BRANCH" == cache/* ]]; then
  echo "cache branches cannot be used as source branches" >&2
  exit 2
fi
