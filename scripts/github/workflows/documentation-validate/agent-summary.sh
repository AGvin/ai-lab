#!/usr/bin/env bash
set -euo pipefail

validation_status() {
  local requested="$1"
  local reported="$2"
  if [[ "$requested" != "true" ]]; then
    printf 'skipped'
  elif [[ "$reported" == "passed" || "$reported" == "failed" || "$reported" == "skipped" ]]; then
    printf '%s' "$reported"
  else
    printf 'unknown'
  fi
}

schemas_status="$(validation_status "$REQUEST_SCHEMAS" "$SCHEMAS_STATUS")"
relations_status="$(validation_status "$REQUEST_RELATIONS" "$RELATIONS_STATUS")"
cache_status="$(validation_status "$REQUEST_CACHE" "$CACHE_STATUS")"

json="$(jq -cn \
  --arg source_branch "$SOURCE_BRANCH" \
  --arg source_sha "$SOURCE_SHA" \
  --arg request_schemas "$REQUEST_SCHEMAS" \
  --arg request_relations "$REQUEST_RELATIONS" \
  --arg request_cache "$REQUEST_CACHE" \
  --arg schemas_status "$schemas_status" \
  --arg relations_status "$relations_status" \
  --arg cache_status "$cache_status" \
  --arg relation_statistics "$RELATION_STATISTICS" \
  'def nullable: if length > 0 then . else null end;
   {
     workflow: "documentation-validate",
     source_branch: $source_branch,
     source_sha: ($source_sha | nullable),
     requested: {
       schemas: ($request_schemas == "true"),
       relations: ($request_relations == "true"),
       cache: ($request_cache == "true")
     },
     validation: {
       schemas: $schemas_status,
       relations: $relations_status,
       cache: $cache_status
     },
     relation_statistics: ($relation_statistics | split("\n") | map(select(length > 0)))
   }')"

printf 'AGENT_SUMMARY_JSON=%s\n' "$json"

display() {
  if [[ -n "$1" ]]; then printf '%s' "$1"; else printf 'n/a'; fi
}
details_file="${RUNNER_TEMP:-}/documentation-validate-output.txt"
validation_details=""
if [[ -n "${RUNNER_TEMP:-}" && -f "$details_file" ]]; then
  validation_details="$(sed -n '/^VALIDATION_DETAILS_BEGIN$/,/^VALIDATION_DETAILS_END$/p' "$details_file" | sed '1d;$d')"
fi

{
  echo "## Documentation Validate"
  echo
  echo "| Field | Value |"
  echo "| --- | --- |"
  echo "| Source branch | \`$SOURCE_BRANCH\` |"
  echo "| Source SHA | \`$(display "$SOURCE_SHA")\` |"
  echo
  echo "| Validation | Enabled | Result |"
  echo "| --- | --- | --- |"
  echo "| Schemas | \`$REQUEST_SCHEMAS\` | \`$schemas_status\` |"
  echo "| Relations | \`$REQUEST_RELATIONS\` | \`$relations_status\` |"
  echo "| Cache | \`$REQUEST_CACHE\` | \`$cache_status\` |"
  if [[ -n "$validation_details" ]]; then
    echo
    printf '%s\n' "$validation_details"
  fi
  if [[ -n "$RELATION_STATISTICS" ]]; then
    echo
    echo "### Relation statistics"
    echo
    while IFS= read -r line; do
      [[ -n "$line" ]] && echo "- $line"
    done <<< "$RELATION_STATISTICS"
  fi
} >> "$GITHUB_STEP_SUMMARY"
