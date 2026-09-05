#!/usr/bin/env bash
set -euo pipefail
CACHE_BRANCH="cache/${SOURCE_BRANCH}"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if [[ "$RESET_CACHE_BRANCH" == "true" ]]; then
  git checkout -B "$CACHE_BRANCH" "$SOURCE_SHA"
fi

if [[ "$CACHE_CHANGED" == "true" ]]; then
  git add -- ':(glob)**/.meta/cache.yml'
  git commit -m "Refresh documentation cache for ${SOURCE_BRANCH}"
fi

commit=$(git rev-parse HEAD)
echo "commit=${commit}" >> "$GITHUB_OUTPUT"

if [[ "$RESET_CACHE_BRANCH" == "true" ]]; then
  git push --force-with-lease origin "HEAD:${CACHE_BRANCH}"
else
  git push origin "HEAD:${CACHE_BRANCH}"
fi
