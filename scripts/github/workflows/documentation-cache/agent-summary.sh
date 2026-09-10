#!/usr/bin/env bash
set -euo pipefail

normalize_conclusion() {
  case "$1" in
    success|failure|skipped) printf '%s' "$1" ;;
    *) printf 'unknown' ;;
  esac
}

generation_status="$GENERATE_STATUS"
if [[ -z "$generation_status" ]]; then
  generation_status="$(normalize_conclusion "$GENERATE_CONCLUSION")"
fi
changes_status="$(normalize_conclusion "$CHANGES_CONCLUSION")"

pr_status="$PR_STATUS"
if [[ -z "$pr_status" ]]; then
  if [[ "$CHANGED" == "false" && "$changes_status" == "success" ]]; then
    pr_status="none"
  else
    pr_status="unknown"
  fi
fi

json="$(jq -cn \
  --arg source_branch "$SOURCE_BRANCH" \
  --arg source_sha "$SOURCE_SHA" \
  --arg use_fingerprints "$USE_FINGERPRINTS" \
  --arg reset_cache_branch "$RESET_CACHE_BRANCH" \
  --arg source_updated "$SOURCE_UPDATED" \
  --arg generation_status "$generation_status" \
  --arg discovered "$DISCOVERED" \
  --arg processed "$PROCESSED" \
  --arg rebuilt "$REBUILT" \
  --arg unchanged "$UNCHANGED" \
  --arg errors "$ERRORS" \
  --arg changes_status "$changes_status" \
  --arg changed "$CHANGED" \
  --arg cache_branch "cache/${SOURCE_BRANCH}" \
  --arg cache_commit "$CACHE_COMMIT" \
  --arg pr_status "$pr_status" \
  --arg pr_number "$PR_NUMBER" \
  'def n: if test("^[0-9]+$") then tonumber else null end;
   def nullable: if length > 0 then . else null end;
   {
     workflow: "documentation-cache",
     source_branch: $source_branch,
     source_sha: ($source_sha | nullable),
     use_fingerprints: ($use_fingerprints == "true"),
     generation: {
       status: $generation_status,
       discovered: ($discovered | n),
       processed: ($processed | n),
       rebuilt: ($rebuilt | n),
       unchanged: ($unchanged | n),
       errors: ($errors | n)
     },
     changes: {
       status: $changes_status,
       changed: (if $changed == "true" then true elif $changed == "false" then false else null end)
     },
     cache: {
       branch: $cache_branch,
       commit: ($cache_commit | nullable),
       reset_branch: ($reset_cache_branch == "true"),
       source_updated: ($source_updated == "true")
     },
     pull_request: {
       status: $pr_status,
       number: ($pr_number | n)
     }
   }')"

printf 'AGENT_SUMMARY_JSON=%s\n' "$json"

display() {
  if [[ -n "$1" ]]; then printf '%s' "$1"; else printf 'n/a'; fi
}
{
  echo "## Documentation Cache"
  echo
  echo "| Field | Value |"
  echo "| --- | --- |"
  echo "| Source branch | \`$SOURCE_BRANCH\` |"
  echo "| Source SHA | \`$(display "$SOURCE_SHA")\` |"
  echo "| Fingerprints | \`$USE_FINGERPRINTS\` |"
  echo "| Reset cache branch | \`$RESET_CACHE_BRANCH\` |"
  echo "| Source updated | \`$SOURCE_UPDATED\` |"
  echo "| Generation | \`$generation_status\` |"
  echo "| Discovered | \`$(display "$DISCOVERED")\` |"
  echo "| Processed | \`$(display "$PROCESSED")\` |"
  echo "| Rebuilt | \`$(display "$REBUILT")\` |"
  echo "| Unchanged | \`$(display "$UNCHANGED")\` |"
  echo "| Errors | \`$(display "$ERRORS")\` |"
  echo "| Changes | \`$changes_status / $(display "$CHANGED")\` |"
  echo "| Cache branch | \`cache/${SOURCE_BRANCH}\` |"
  echo "| Cache commit | \`$(display "$CACHE_COMMIT")\` |"
  echo "| Pull request | \`$pr_status / $(display "$PR_NUMBER")\` |"
} >> "$GITHUB_STEP_SUMMARY"
