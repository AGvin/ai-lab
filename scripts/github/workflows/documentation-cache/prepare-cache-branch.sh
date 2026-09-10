#!/usr/bin/env bash
set -euo pipefail
CACHE_BRANCH="cache/${SOURCE_BRANCH}"
echo "source_updated=false" >> "$GITHUB_OUTPUT"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if [[ "$RESET_CACHE_BRANCH" == "true" ]]; then
  echo "mode=reset" >> "$GITHUB_OUTPUT"
  exit 0
fi

if git ls-remote --exit-code --heads origin "refs/heads/${CACHE_BRANCH}" >/dev/null 2>&1; then
  git fetch origin "${CACHE_BRANCH}:refs/remotes/origin/${CACHE_BRANCH}"
  git checkout -B "$CACHE_BRANCH" "origin/${CACHE_BRANCH}"
  if ! git merge-base --is-ancestor "$SOURCE_SHA" HEAD; then
    git merge --no-edit "$SOURCE_SHA"
    echo "source_updated=true" >> "$GITHUB_OUTPUT"
  fi
else
  git checkout -B "$CACHE_BRANCH" "$SOURCE_SHA"
fi
echo "mode=preserve" >> "$GITHUB_OUTPUT"
