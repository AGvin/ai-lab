#!/usr/bin/env bash
set -euo pipefail
CACHE_BRANCH="cache/${SOURCE_BRANCH}"
existing="$(gh pr list \
  --head "$CACHE_BRANCH" \
  --base "$SOURCE_BRANCH" \
  --state open \
  --json number \
  --jq '.[0].number // empty')"
if [[ -n "$existing" ]]; then
  echo "status=updated" >> "$GITHUB_OUTPUT"
  echo "number=${existing}" >> "$GITHUB_OUTPUT"
  echo "Updated existing cache PR #${existing}"
  exit 0
fi

gh pr create \
  --head "$CACHE_BRANCH" \
  --base "$SOURCE_BRANCH" \
  --title "Refresh documentation cache for ${SOURCE_BRANCH}" \
  --body "Generated documentation cache refresh. Canonical .meta inputs remain authoritative."
created="$(gh pr list \
  --head "$CACHE_BRANCH" \
  --base "$SOURCE_BRANCH" \
  --state open \
  --json number \
  --jq '.[0].number // empty')"
if [[ -z "$created" ]]; then
  echo "cache PR was created but its number could not be resolved" >&2
  exit 1
fi
echo "status=created" >> "$GITHUB_OUTPUT"
echo "number=${created}" >> "$GITHUB_OUTPUT"
