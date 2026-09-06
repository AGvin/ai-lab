#!/usr/bin/env bash
set -euo pipefail
mapfile -t changed < <(git status --porcelain --untracked-files=all | sed -E 's/^.. //')
if (( ${#changed[@]} == 0 )); then
  echo "changed=false" >> "$GITHUB_OUTPUT"
  exit 0
fi
for path in "${changed[@]}"; do
  if [[ "$path" != */.meta/cache.yml ]]; then
    echo "cache workflow produced unauthorized change: $path" >&2
    exit 1
  fi
done
echo "changed=true" >> "$GITHUB_OUTPUT"
# Explicit generated-state pathspec owned by this workflow: **/.meta/cache.yml
